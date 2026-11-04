#!/usr/bin/env python3
"""Convert approved MADOROMI paintings to runtime WebP; never generate/edit art.

Production inputs stay outside Git. Final WebPs and their hash register are
committed, so normal builds do not need Drive, image generation or this script.
"""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BACKGROUNDS = ("bedroom", "bedroom_day", "cafeteria", "street", "stage", "night", "courtyard", "bakery", "lounge")
AOI = tuple("school_" + e for e in ("neutral", "smile", "shy", "sad", "surprised", "laugh", "shy_clasp", "laugh_open", "tender_heart")) + ("casual_smile",)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--production", type=Path, default=Path("/workspace/downloads"))
    p.add_argument("--concept-index", type=Path, default=Path("/workspace/reference/characters-base-sources.json"))
    p.add_argument("--partial", action="store_true", help="Stage available paintings while production is active")
    args = p.parse_args()
    sources = [(args.production / "environment-production" / (name + ".png"), name + ".webp", (1920, 1080), False) for name in BACKGROUNDS]
    sources.append((args.production / "environment-production/jeans.png", "jeans.webp", (1920, 1080), False))
    sources.append((args.production / "musicroom-production/musicroom.png", "musicroom.webp", (1920, 1080), False))
    for person, names in (("aoi", AOI), ("mio", ("neutral", "smile", "concerned", "thoughtful")), ("sora", ("neutral", "smile", "concerned", "easy"))):
        sources.extend((args.production / "character-production" / person / (name + ".png"), "characters/" + person + "/" + name + ".webp", (720, 1080), True) for name in names)
    concepts = json.loads(args.concept_index.read_text())
    for person in ("aoi", "ren", "mio", "sora"):
        concept = next(c for c in concepts if c["title"] == person + "_base_bust_v1.png")
        sources.append((Path(concept["path"]), "cast/" + person + ".webp", (210, 280), True))
    missing = [str(s) for s, *_ in sources if not s.exists()]
    if missing and not args.partial:
        raise SystemExit("Missing approved production inputs:\n" + "\n".join(missing))
    manifest_path = ROOT / "docs/licenses/production-art.json"
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    previous_assets = {item["runtime_path"]: item for item in previous.get("assets", [])}
    records = []
    for source, relative, size, transparent in sources:
        if not source.exists():
            continue
        output = ROOT / "game/images/originals" / relative
        old = previous_assets.get(str(output.relative_to(ROOT)), {})
        source_hash = sha(source)
        if (previous.get("conversion_recipe", 1) == 1 and output.exists()
                and old.get("source_sha256") == source_hash
                and old.get("runtime_size") == list(size)
                and old.get("runtime_sha256") == sha(output)):
            records.append(old)
            continue
        with Image.open(source) as raw:
            original_size = list(raw.size)
            im = raw.convert("RGBA" if transparent else "RGB")
            # A single full canvas for every expression/pose preserves alignment.
            # No per-image bounding-box crops, face edits or background removal.
            im = im.resize(size, Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        if transparent:
            im.save(output, "WEBP", lossless=True, method=6)
        else:
            im.save(output, "WEBP", quality=94, method=6)
        records.append({"runtime_path": str(output.relative_to(ROOT)), "runtime_size": list(size), "runtime_sha256": sha(output), "source_file": source.name, "source_sha256": sha(source), "source_size": original_size, "alpha_required": transparent, "adaptation": "Full-canvas Lanczos resize and WebP conversion only", "origin": "user-provided canonical concept" if relative.startswith("cast/") else "OpenAI image generation for MADOROMI; user canonical designs anchor character identity and finish"})
    manifest = {"schema_version": 1, "conversion_recipe": 1, "production_date": "2026-11-04", "complete": not missing, "expected_count": len(sources), "notes": "Project-specific artwork used under the user's explicit instruction. AI-generated expansions, poses, outfits, environments and prop are disclosed; no exclusive copyright or independent clearance of supplied source concepts is asserted. Original JPG research references and private Drive files are not redistributed.", "assets": records}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Prepared {len(records)}/{len(sources)} approved runtime images. Missing: {len(missing)}.")


if __name__ == "__main__":
    main()
