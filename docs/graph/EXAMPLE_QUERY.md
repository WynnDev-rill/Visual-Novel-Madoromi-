# Query verification

Actual Graphify CLI results for the generated graph. Wrapper freshness checks run before traversal; later source changes require regeneration.

```text
$ tools/knowledge_graph.sh path "label:start" "label:act_3"
PASS: graph freshness, source citations, endpoints, five choices/state callbacks and known narrative/UI/art relations (273 nodes).
Shortest path (3 hops):
  start --jump [EXTRACTED]--> act_1 --jump [EXTRACTED]--> act_2 --jump [EXTRACTED]--> act_3
Path confidence: EXTRACTED (weakest hop 1: jump)

$ tools/knowledge_graph.sh query "story_color" --budget 650
PASS: graph freshness, source citations, endpoints, five choices/state callbacks and known narrative/UI/art relations (273 nodes).
Graph: docs/graph/graph.json (273 nodes) | Traversal: BFS depth=2 | Start: ['story_color', 'story_reply'] | 67 nodes found

[!] TRUNCATED: showing 21 of 67 nodes (~650-token budget). The answer may be among the 46 cut nodes — raise the token budget to 2175 to get all 67 (CLI: --budget 2175, MCP: token_budget=2175) or narrow the query (e.g. context_filter=['call'], or get_node for a specific symbol).

NODE story_color [src=game/story.rpy loc=L6 community=Project documentation]
NODE story_reply [src=game/story.rpy loc=L4 community=Project documentation]
NODE story_company [src=game/story.rpy loc=L5 community=Project documentation]
NODE story_courage [src=game/story.rpy loc=L7 community=Project documentation]
NODE story_promise [src=game/story.rpy loc=L8 community=Project documentation]
NODE game/story.rpy [src=game/story.rpy loc=L1 community=Art and sound resources]
NODE act_3 [src=game/story.rpy loc=L614 community=Art and sound resources]
NODE act_2 [src=game/story.rpy loc=L315 community=Art and sound resources]
NODE Kuning, seperti lampu toko menjelang tutup. [src=game/story.rpy loc=L258 community=Project documentation]
NODE Ajukan pertanyaan yang sungguh ingin kutahu. [src=game/story.rpy loc=L45 community=Project documentation]
NODE Biru, seperti air ketika angin sudah reda. [src=game/story.rpy loc=L253 community=Project documentation]
NODE Dengarkan apa yang membuatnya penasaran. [src=game/story.rpy loc=L41 community=Project documentation]
NODE act_1 [src=game/story.rpy loc=L13 community=Art and sound resources]
NODE Choice in act_1 (L251) [src=game/story.rpy loc=L251 community=Project documentation]
NODE Choice in act_1 (L39) [src=game/story.rpy loc=L39 community=Project documentation]
NODE Choice in act_2 (L591) [src=game/story.rpy loc=L591 community=Project documentation]
NODE story_color: blue / gold [src=docs/STORY.md loc=L73 community=Project documentation]
NODE story_reply: listen / questions [src=docs/STORY.md loc=L71 community=Project documentation]
NODE MADOROMI complete romance story [src=docs/STORY.md loc=L3 community=Project documentation]
NODE Mutual confession and relationship acceptance [src=docs/STORY.md loc=L23 community=Project documentation]
NODE Painted jeans given after acceptance [src=docs/STORY.md loc=L29 community=Project documentation]
... (truncated — 46 more nodes cut by ~650-token budget. Narrow with context_filter=['call'] or use get_node for a specific symbol)
```
