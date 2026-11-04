# MADOROMI knowledge graph

Built with Graphify0.9.102 plus the project Ren’Py adapter. Upstream `.rpy` classification: None. The adapter is line-oriented structural extraction, not a full Ren’Py parser or runtime proof. Python tools use Graphify’s genuine tree-sitter AST extractor. Three source documents have a preserved independent host-agent semantic extraction with checked anchors. Binary art is indexed through the approved manifest, never sent to a model.

The JSON/extraction preserve 1086 typed, cited evidence edges. The clustered HTML and generated analysis below aggregate these to 565 unique endpoint connections. 15 Python import/call symbols have no audited implementation; they are explicitly tagged unresolved external symbols, rather than guessed definitions.

Token accounting: no separate model/API calls run on regeneration. Host-agent semantic-extraction token usage is unavailable; upstream zero fields below are placeholders and do not assert zero total workflow cost. The graph does not cover external SDK internals, private Drive documents, every dynamic expression or every possible route.

# Graph Report - madoromi  (2026-11-04)

## Corpus Check
- 25 files · ~34,857 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 274 nodes · 565 edges · 20 communities (9 shown, 11 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Project documentation
- Development and verification tools
- Project documentation
- Art and sound resources
- Art and sound resources
- Art and sound resources
- Art and sound resources
- Build and release pipeline
- Art and sound resources
- Project documentation
- Art and sound resources
- Story and preference state
- Story and preference state

## God Nodes (most connected - your core abstractions)
1. `act_2` - 38 edges
2. `act_1` - 37 edges
3. `act_3` - 36 edges
4. `game_menu` - 20 edges
5. `epilogue` - 18 edges
6. `main_menu` - 17 edges
7. `MADOROMI complete romance story` - 13 edges
8. `preferences` - 12 edges
9. `complete_routes` - 12 edges
10. `quick_menu` - 11 edges

## Surprising Connections (you probably didn't know these)
- `story_reply: listen / questions` --documents_state--> `story_reply`  [EXTRACTED]
  docs/STORY.md → game/story.rpy
- `act_2` --speaks_as--> `Mio`  [EXTRACTED]
  game/story.rpy → game/definitions.rpy
- `preferences` --uses_native_action--> `SetScreenVariable`  [EXTRACTED]
  game/system_ui.rpy → game/screens.rpy
- `story_company: quiet / help` --documents_state--> `story_company`  [EXTRACTED]
  docs/STORY.md → game/story.rpy
- `story_color: blue / gold` --documents_state--> `story_color`  [EXTRACTED]
  docs/STORY.md → game/story.rpy

## Import Cycles
- None detected.

## Communities (20 total, 11 thin omitted)

### Community 0 - "Project documentation"
Cohesion: 0.06
Nodes (54): Choice in act_1 (L39), Continue, FileAction, FileDelete, FileLoad, FilePage, FileSave, Hide (+46 more)

### Community 1 - "Development and verification tools"
Cohesion: 0.09
Nodes (8): main(), require(), main(), sha(), convert(), describe(), loop_birds(), run()

### Community 2 - "Project documentation"
Cohesion: 0.08
Nodes (35): Choice in act_1 (L111), Choice in act_1 (L251), Choice in act_2 (L591), Choice in epilogue (L944), Beanbag question and ten seconds, Completed afterstory and healthier goodnight routine, haowjy creative-writing-craft, story_color: blue / gold (+27 more)

### Community 3 - "Art and sound resources"
Cohesion: 0.08
Nodes (15): SetScreenVariable, bubble, choice, confirm, help, input, keyboard_help, mouse_help (+7 more)

### Community 4 - "Art and sound resources"
Cohesion: 0.14
Nodes (11): audio.bell, audio.confession, audio.day, audio.message, audio.night, audio.page, audio.tender, chapter_card (+3 more)

### Community 6 - "Art and sound resources"
Cohesion: 0.17
Nodes (6): Aoi, Mio, Ren, act_1, epilogue, start

### Community 7 - "Build and release pipeline"
Cohesion: 0.31
Nodes (11): build android, build archive_visuals, build bootstrap, build bootstrap_android, build desktop, build download, build java_network, build lint (+3 more)

### Community 8 - "Art and sound resources"
Cohesion: 0.22
Nodes (6): Sora, act_3, persistent.reduce_motion, heroine, leftside, scene_drift

### Community 9 - "Project documentation"
Cohesion: 0.40
Nodes (6): tools/build.sh pinned build helper, Desktop RenPy visual archive, Native RAPT Android image assets, Native engine testcase evidence, RenPy native VN engine systems, Reproducible build workflow

## Knowledge Gaps
- **23 isolated node(s):** `input`, `preferences.text_cps`, `preferences.afm_time`, `Rollback`, `Skip` (+18 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 70 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `game_menu` connect `Project documentation` to `Art and sound resources`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **What connects `input`, `preferences.text_cps`, `preferences.afm_time` to the rest of the system?**
  _23 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Project documentation` be split into smaller, more focused modules?**
  _Cohesion score 0.06490384615384616 - nodes in this community are weakly interconnected._
- **Why does `act_2` connect `Art and sound resources` to `Project documentation`, `Project documentation`, `Art and sound resources`, `Art and sound resources`, `Art and sound resources`?**
  _High betweenness centrality (0.003) - this node is a cross-community bridge._
- **Should `Development and verification tools` be split into smaller, more focused modules?**
  _Cohesion score 0.08974358974358974 - nodes in this community are weakly interconnected._
- **Should `Project documentation` be split into smaller, more focused modules?**
  _Cohesion score 0.0773109243697479 - nodes in this community are weakly interconnected._
- **Should `Art and sound resources` be split into smaller, more focused modules?**
  _Cohesion score 0.08045977011494253 - nodes in this community are weakly interconnected._