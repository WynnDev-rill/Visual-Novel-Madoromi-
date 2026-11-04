#!/usr/bin/env python3
"""Ren'Py adapter feeding real Graphify; source graph is evidence, not a CFG.

Graphify 0.9.102 does not classify .rpy. This deliberately small line-oriented
adapter covers declarations, calls, actions, choices, state and asset cues.
Python tooling still uses Graphify's own tree-sitter extractor. Unsupported
dynamic expressions are not guessed, and no model/API is used during rebuilds.
"""
from collections import Counter
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/graph"
SEMANTIC = OUT / "semantic.json"
MANIFEST = ROOT / "docs/licenses/production-art.json"
NATIVE_ACTIONS = r"\b(ShowMenu|Start|Return|FileSave|FileLoad|FileDelete|FileAction|FilePage|Preference|Rollback|RollbackToIdentifier|MainMenu|Continue|Skip|ToggleField|SetField|SetScreenVariable|Hide|Show|Notify|OpenURL|Quit)\s*\("


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sources():
    return sorted(set(ROOT.glob("game/*.rpy")) | set(ROOT.glob("tests/*.py")) | {ROOT / ("tools/" + n) for n in ("build.sh", "prepare_art.py", "prepare_audio.py", "knowledge_graph.py", "knowledge_graph.sh")} | {ROOT / ("docs/" + n) for n in ("STORY.md", "BUILD.md", "STORY_AUDIT.md")} | {ROOT / ".github/workflows/build.yml", MANIFEST, SEMANTIC})


def source_hashes():
    return {p.relative_to(ROOT).as_posix(): digest(p) for p in sources()}


def extract_project():
    nodes, edges = {}, []

    def node(key, label, kind, path, line=None, **extra):
        path = str(path.relative_to(ROOT)) if isinstance(path, Path) and path.is_absolute() else str(path)
        file_type = ("image" if Path(path).suffix in (".webp", ".png", ".jpg") else "concept") if kind == "asset" else "code"
        nodes.setdefault(key, {"id": key, "label": label, "kind": kind, "file_type": file_type, "source_file": path, "source_location": f"L{line}" if line else None, "_origin": "ast", **extra})
        return key

    def edge(a, b, relation, path, line, confidence="EXTRACTED", **extra):
        edges.append({"source": a, "target": b, "relation": relation, "confidence": confidence, "confidence_score": 1.0 if confidence == "EXTRACTED" else .8, "weight": 1.0, "source_file": str(path.relative_to(ROOT)), "source_location": f"L{line}", "_origin": "ast", **extra})

    files = sources()
    for path in files:
        node("file:" + str(path.relative_to(ROOT)), path.relative_to(ROOT).as_posix(), "file", path, 1)
    # All selected production images are registered, including dynamically
    # resolved expressions; binary pixels are never sent through graph extraction.
    for item in json.loads(MANIFEST.read_text())["assets"]:
        rel = item["runtime_path"]
        node("asset:" + rel, rel.removeprefix("game/"), "asset", rel, runtime_sha256=item["runtime_sha256"])
        line = next(i for i, value in enumerate(MANIFEST.read_text().splitlines(), 1) if rel in value)
        edge("file:docs/licenses/production-art.json", "asset:" + rel, "registers_asset", MANIFEST, line)
    declarations = {}
    variables = {}
    for path in ROOT.glob("game/*.rpy"):
        for line, text in enumerate(path.read_text().splitlines(), 1):
            match = re.match(r"(label|screen|transform)\s+([\w.]+)", text)
            if match:
                kind, name = match.groups(); key = node(kind + ":" + name, name, kind, path, line)
                declarations[(kind, name)] = key
                edge("file:" + str(path.relative_to(ROOT)), key, "declares", path, line)
            match = re.match(r"default\s+([\w.]+)\s*=", text)
            if match:
                name = match[1]; variables[name] = node("state:" + name, name, "state", path, line)
            match = re.match(r'define\s+(\w+)\s*=\s*Character\("([^"]+)"', text)
            if match:
                node("character:" + match[1], match[2], "character", path, line)
            match = re.match(r'define\s+audio\.(\w+)\s*=\s*"([^"]+)"', text)
            if match:
                key = node("audio:" + match[1], "audio." + match[1], "audio_alias", path, line)
                asset = node("asset:game/" + match[2], match[2], "asset", "game/" + match[2])
                edge(key, asset, "resolves_to", path, line)
    for path in ROOT.glob("game/*.rpy"):
        rel = path.relative_to(ROOT).as_posix(); owner = "file:" + rel
        outfit, menu, branch = "school", None, None
        for line, text in enumerate(path.read_text().splitlines(), 1):
            stripped = text.strip(); indent = len(text) - len(text.lstrip())
            match = re.match(r"(label|screen|transform)\s+([\w.]+)", text)
            if match:
                owner = declarations[match[1], match[2]]; menu = branch = None
            match = re.match(r"\s*testcase\s+(\w+)", text)
            if match:
                owner = node("test:" + match[1], match[1], "testcase", path, line)
                edge("file:" + rel, owner, "declares_test", path, line)
            match = re.search(r'aoi_outfit\s*=\s*"(\w+)"', text)
            if match: outfit = match[1]
            if stripped.startswith("#"): continue
            if branch and indent <= branch[1]: branch = None
            if re.match(r"menu(?:\s+\w+)?\s*:", stripped):
                menu = node(f"choice:{rel}:{line}", f"Choice in {owner.split(':', 1)[-1]} (L{line})", "choice", path, line)
                edge(owner, menu, "offers_choice", path, line)
            match = re.match(r'"(.+)"\s*:', stripped)
            if match and menu:
                key = node("option:" + hashlib.sha256(match[1].encode()).hexdigest()[:12], match[1], "option", path, line)
                edge(menu, key, "has_option", path, line); branch = (key, indent)
            for name, key in variables.items():
                if re.search(r"(?<![\w.])" + re.escape(name) + r"(?![\w.])", text) and not stripped.startswith("default "):
                    writes = bool(re.match(r"\$\s*" + re.escape(name) + r"\s*=", stripped))
                    edge(branch[0] if branch and writes else owner, key, "writes_state" if writes else "reads_state", path, line)
            match = re.match(r"(jump|call)\s+(?:(screen)\s+)?([\w.]+)", stripped)
            if match:
                kind = "screen" if match[2] else "label"; key = declarations.get((kind, match[3]))
                if key: edge(owner, key, "shows_screen" if kind == "screen" else match[1], path, line)
            match = re.match(r"use\s+(\w+)", stripped)
            if match and ("screen", match[1]) in declarations:
                edge(owner, declarations["screen", match[1]], "uses_screen", path, line)
            for action in re.finditer(NATIVE_ACTIONS, text):
                key = node("native:" + action[1], action[1], "native_action", path, line, external_definition="Ren'Py native action")
                edge(owner, key, "uses_native_action", path, line)
            for action, name in re.findall(r'(ShowMenu|Show|Hide|Start)\("([^"\n]+)"', text):
                kind = "label" if action == "Start" else "screen"
                if (kind, name) in declarations: edge(owner, declarations[kind, name], action.lower(), path, line)
            match = re.match(r"(scene|show|hide)\s+(bg|aoi|mio|sora)\s*(\w+)?", stripped)
            if match:
                operation, person, expression = match.groups()
                if expression:
                    if person == "bg": asset_path = "game/images/originals/" + expression + ".webp"
                    else:
                        name = ("casual_smile" if outfit == "blouse" else "school_" + expression) if person == "aoi" else expression
                        asset_path = "game/images/originals/characters/" + person + "/" + name + ".webp"
                    key = "asset:" + asset_path
                    if key in nodes: edge(owner, key, operation + "_image", path, line)
            for name in re.findall(r"\bat\s+(\w+)", text):
                if ("transform", name) in declarations: edge(owner, declarations["transform", name], "stages_with", path, line)
            for name in re.findall(r"\baudio\.(\w+)", text):
                if "audio:" + name in nodes: edge(owner, "audio:" + name, "uses_audio", path, line)
            for asset in re.findall(r'["\']((?:images|audio|fonts|gui)/[^"\'\n]+\.(?:webp|png|ogg|ttf|otf))["\']', text):
                if (ROOT / "game" / asset).is_file():
                    key = node("asset:game/" + asset, asset, "asset", "game/" + asset)
                    edge(owner, key, "references_asset", path, line)
            match = re.match(r'([rasm])\s+"', stripped)
            if match: edge(owner, "character:" + match[1], "speaks_as", path, line)
    # Build tasks are shell functions, not invented engine subsystems.
    path = ROOT / "tools/build.sh"; owner = "file:tools/build.sh"
    task_names = re.findall(r"^(\w+)\(\)\s*\{", path.read_text(), re.M)
    for line, text in enumerate(path.read_text().splitlines(), 1):
        match = re.match(r"(\w+)\(\)\s*\{", text)
        if match:
            owner = node("build:" + match[1], "build " + match[1], "build_task", path, line)
            edge("file:tools/build.sh", owner, "declares_task", path, line)
        for name in task_names:
            if re.match(r"\s+" + re.escape(name) + r"(?:\s|$)", text):
                edge(owner, "build:" + name, "calls_task", path, line)
        for file in files:
            if file.name in text and not text.lstrip().startswith("#"):
                edge(owner, "file:" + file.relative_to(ROOT).as_posix(), "references_file", path, line)
    for path in [p for p in files if p.suffix == ".py" and p.name != "knowledge_graph.py"] + [ROOT / ".github/workflows/build.yml"]:
        owner = "file:" + path.relative_to(ROOT).as_posix()
        for line, text in enumerate(path.read_text().splitlines(), 1):
            if text.lstrip().startswith("#"): continue
            for target in files:
                if target != path and target.name in text:
                    edge(owner, "file:" + target.relative_to(ROOT).as_posix(), "references_file", path, line)
            for name in re.findall(r"tools/build\.sh\s+([\w-]+)", text):
                name = {"test": "test_game", "bootstrap-android": "bootstrap_android"}.get(name, name)
                if name in task_names: edge(owner, "build:" + name, "runs_build_task", path, line)
    # Curated semantic extraction is preserved with source anchors. Moving a
    # paragraph rebases its line; editing it requires an honest focused review.
    fragment = json.loads(SEMANTIC.read_text())
    for section in ("nodes", "edges"):
        for item in fragment[section]:
            item = dict(item); lines = (ROOT / item["source_file"]).read_text().splitlines()
            anchor = item.pop("source_anchor")
            old = int(item["source_location"][1:]) - 1
            if old >= len(lines) or lines[old] != anchor:
                positions = [i for i, value in enumerate(lines) if value == anchor]
                if len(positions) != 1: raise ValueError("Semantic anchor changed; review " + item["source_file"] + ": " + anchor)
                item["source_location"] = "L" + str(positions[0] + 1)
            if section == "nodes": nodes[item["id"]] = item
            else: edges.append(item)
    # Explicit same-identifier doc-to-code links preserve the ledger's value.
    for item in list(nodes.values()):
        if item.get("_origin") == "semantic":
            for name, key in variables.items():
                if name in item["label"]:
                    edges.append({"source": item["id"], "target": key, "relation": "documents_state", "confidence": "EXTRACTED", "confidence_score": 1.0, "weight": 1.0, "source_file": item["source_file"], "source_location": item["source_location"], "_origin": "semantic"})
    unique = {}
    for item in edges:
        if item["source"] == item["target"]: continue
        unique[(item["source"], item["target"], item["relation"], item["source_file"], item["source_location"])] = item
    return {"nodes": list(nodes.values()), "edges": list(unique.values()), "input_tokens": 0, "output_tokens": 0}


def build():
    from importlib.metadata import version
    from graphify.extract import extract
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.export import to_json, to_html
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.detect import classify_file

    if version("graphifyy") != "0.9.102": raise RuntimeError("Use pinned Graphify0.9.102 environment")
    extraction = extract_project()
    python_files = [p for p in sources() if p.suffix == ".py" and p.name != "knowledge_graph.py"]
    ast = extract(python_files, root=ROOT, cache_root=Path(sys.prefix) / "madoromi-graph-cache", max_workers=2)
    for item in ast.get("nodes", []):
        item.setdefault("kind", "python_symbol")
        if item.get("label") == Path(item.get("source_file", "")).name:
            extraction["edges"].append({"source": "file:" + item["source_file"], "target": item["id"], "relation": "ast_module", "confidence": "EXTRACTED", "confidence_score": 1.0, "weight": 1.0, "source_file": item["source_file"], "source_location": "L1", "_origin": "ast"})
    extraction["nodes"].extend(ast.get("nodes", [])); extraction["edges"].extend(ast.get("edges", []))
    # The upstream AST pass reports external imports and unresolved call names
    # without definitions. Keep these explicit as unknown symbol references,
    # never as audited external implementations or missing graph endpoints.
    known = {item["id"] for item in extraction["nodes"]}
    unresolved = set()
    for item in extraction["edges"]:
        for endpoint in ("source", "target"):
            key = item[endpoint]
            if key not in known:
                extraction["nodes"].append({"id": key, "label": key, "kind": "unresolved_symbol", "file_type": "concept", "source_file": "", "source_location": None, "external": True, "definition_status": "Unresolved upstream AST symbol; implementation not audited", "_origin": "ast"})
                known.add(key); unresolved.add(key)
    (OUT / "extraction.json").write_text(json.dumps(extraction, ensure_ascii=False, indent=2) + "\n")
    graph = build_from_json(extraction, directed=True, root=ROOT, dedup=False)
    assert graph.number_of_nodes() > 0
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    labels = {}
    names = {"label": "Narrative and scene direction", "screen": "Reading and system interface", "state": "Story and preference state", "asset": "Art and sound resources", "build_task": "Build and release pipeline", "testcase": "Native functional verification", "python_symbol": "Development and verification tools"}
    for cid, members in communities.items():
        kinds = Counter(graph.nodes[n].get("kind", "document") for n in members)
        labels[cid] = names.get(kinds.most_common(1)[0][0], "Project documentation")
    detection = {"total_files": len(sources()), "total_words": sum(len(p.read_text().split()) for p in sources()), "files": {"code": [p.relative_to(ROOT).as_posix() for p in sources() if p.suffix in (".py", ".rpy", ".sh")], "document": ["docs/STORY.md", "docs/BUILD.md", "docs/STORY_AUDIT.md"]}, "skipped_sensitive": []}
    # Graphify's clustered graph is a DiGraph. Its supported original_links
    # export retains all typed, cited evidence in a MultiDiGraph JSON instead
    # of silently replacing repeated read/speech/action edges at one endpoint.
    assert to_json(graph, communities, str(OUT / "graph.json"), force=True, community_labels=labels, original_links=extraction["edges"])
    assert to_html(graph, communities, str(OUT / "graph.html"), community_labels=labels)
    report = generate(graph, communities, cohesion, labels, god_nodes(graph), surprising_connections(graph, communities), detection, {"input": 0, "output": 0}, ".", suggested_questions=suggest_questions(graph, communities, labels))
    note = "# MADOROMI knowledge graph\n\nBuilt with Graphify0.9.102 plus the project Ren’Py adapter. Upstream `.rpy` classification: " + str(classify_file(ROOT / "game/story.rpy")) + ". The adapter is line-oriented structural extraction, not a full Ren’Py parser or runtime proof. Python tools use Graphify’s genuine tree-sitter AST extractor. Three source documents have a preserved independent host-agent semantic extraction with checked anchors. Binary art is indexed through the approved manifest, never sent to a model.\n\nThe JSON/extraction preserve " + str(len(extraction["edges"])) + " typed, cited evidence edges. The clustered HTML and generated analysis below aggregate these to " + str(graph.number_of_edges()) + " unique endpoint connections. " + str(len(unresolved)) + " Python import/call symbols have no audited implementation; they are explicitly tagged unresolved external symbols, rather than guessed definitions.\n\nToken accounting: no separate model/API calls run on regeneration. Host-agent semantic-extraction token usage is unavailable; upstream zero fields below are placeholders and do not assert zero total workflow cost. The graph does not cover external SDK internals, private Drive documents, every dynamic expression or every possible route.\n\n"
    (OUT / "GRAPH_REPORT.md").write_text(note + report)
    summary = {"graphify_version": version("graphifyy"), "nodes": graph.number_of_nodes(), "evidence_edges": len(extraction["edges"]), "clustered_connections": graph.number_of_edges(), "communities": len(communities), "unresolved_symbols": len(unresolved), "source_hashes": source_hashes(), "graph_sha256": digest(OUT / "graph.json"), "extraction_sha256": digest(OUT / "extraction.json"), "renpy_adapter": "line-oriented; .rpy unsupported upstream", "semantic_tokens": "host-agent usage unavailable"}
    (OUT / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"Graphify built {summary['nodes']} nodes, {summary['evidence_edges']} evidence edges, {summary['communities']} communities.")


def check():
    manifest = json.loads((OUT / "manifest.json").read_text())
    assert source_hashes() == manifest["source_hashes"], "Knowledge graph is stale; run tools/knowledge_graph.sh build"
    for name in ("graph", "extraction"):
        assert digest(OUT / (name + ".json")) == manifest[name + "_sha256"], "Graph artifact changed: " + name
    data = json.loads((OUT / "extraction.json").read_text())
    ids = {n["id"] for n in data["nodes"]}
    assert len(ids) == len(data["nodes"]), "Duplicate graph IDs"
    for edge in data["edges"]:
        assert edge["source"] in ids and edge["target"] in ids, edge
        assert edge.get("confidence") in ("EXTRACTED", "INFERRED", "AMBIGUOUS"), edge
        if edge.get("confidence") == "EXTRACTED": assert edge.get("confidence_score", 1) == 1
        if str(edge.get("source_location", "")).startswith("L"):
            path = ROOT / edge["source_file"]
            assert path.is_file() and 1 <= int(edge["source_location"][1:]) <= len(path.read_text().splitlines()), edge
    triples = {(e["source"], e["target"], e["relation"]) for e in data["edges"]}
    for triple in [("label:start", "label:act_1", "jump"), ("label:act_3", "asset:game/images/originals/courtyard.webp", "scene_image"), ("screen:quick_menu", "screen:save", "showmenu")]:
        assert triple in triples, "Missing known relation: " + str(triple)
    for name in ("story_reply", "story_company", "story_color", "story_courage", "story_promise"):
        assert any(e["relation"] == "writes_state" and e["source"].startswith("option:") and e["target"] == "state:" + name for e in data["edges"]), name
        assert any(e["relation"] == "reads_state" and e["target"] == "state:" + name for e in data["edges"]), name
    assert sum(n.get("kind") == "choice" for n in data["nodes"]) == 5
    for asset in json.loads(MANIFEST.read_text())["assets"]:
        assert digest(ROOT / asset["runtime_path"]) == asset["runtime_sha256"], "Art manifest is stale: " + asset["runtime_path"]
    graph = json.loads((OUT / "graph.json").read_text())
    assert len(graph.get("links", graph.get("edges", []))) == len(data["edges"]), "Graph lost evidence edges"
    assert all("/workspace/" not in json.dumps(item) for item in data["nodes"] + data["edges"]), "Nonportable source path"
    print(f"PASS: graph freshness, source citations, endpoints, five choices/state callbacks and known narrative/UI/art relations ({len(ids)} nodes).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    arguments = parser.parse_args()
    build() if arguments.command == "build" else check()
