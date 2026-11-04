# MADOROMI integration

The unmodified upstream Codex skill is `SKILL.md`. This project stores the
existing graph in `docs/graph/`, not the upstream default `graphify-out/`.
Read `docs/KNOWLEDGE_GRAPH.md` and use `tools/knowledge_graph.sh` so the pinned
external environment, source freshness gate and Ren’Py adapter are selected.

Do not run an unrestricted semantic scan over the repository: it contains
upstream skills and audit material that are not the game dependency graph.
The adapter feeds real Graphify build/cluster/export/query APIs and is explicit
about upstream's lack of `.rpy` classification. Rebuild after source changes;
read returned source citations before modifying the game. Native testing
remains authoritative for gameplay and Android behavior.
