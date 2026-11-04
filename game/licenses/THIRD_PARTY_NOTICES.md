# MADOROMI — third-party notices

Project production: WynnDev. Story adapted under the user's instruction from the supplied short story **Sepuluh Detik**. The supplied original is preserved in `docs/source/cerita-asli.docx`; its rights are not replaced by any engine or asset license.

## Character and environment art

Canonical character designs: the user's supplied `aoi_base_bust_v1.png`, `mio_base_bust_v1.png`, `sora_base_bust_v1.png` and `ren_base_bust_v1.png` from Google Drive. The user authorizes their use and the development of consistent expressions, costumes and body language for MADOROMI. The source folder identifies these as cropped/upscaled upper-body AI design concepts; they are not pre-existing full-body sprites or Live2D rigs.

Production character expansions/variations, coherent environments and the painted-jeans prop are developed through OpenAI image generation. They are disclosed as AI-generated project artwork, with no claim of exclusive copyright or independent commercial clearance of underlying source references. Private original-reference JPGs are not distributed or used as generation inputs. Benchmark-game art, screenshots, fonts and music are not production assets. See `docs/licenses/visual-art.md`, `docs/licenses/original-environments.md` and `docs/licenses/production-art.json` for lineage and preparation.

The earlier baseline used **Potat0Master** Character Sets A01/A02 and environment packs (https://potat0master.itch.io/), under terms permitting game use/editing and prohibiting standalone redistribution. Its archive hashes and creator-page evidence remain a historical curation record in `docs/licenses/visual-assets.json` and `evidence/`. Those images are superseded by the canonical production-art selection and are not included as a second visual style in the revised runtime. No Potat0Master illustration was submitted for image generation.

App icon: **Madoromi_App_Icon_Master_1536.png**, supplied and selected by the user through Google Drive. Used as explicitly instructed. Original artist/independent commercial publication rights were not documented in the supplied material; no third-party ownership claim is made. See `docs/licenses/icon.md`.

## Music

"Dream Culture", "Easy Lemon", "Touching Moments Five - Circle", "Touching Moments Four - Melody"

Kevin MacLeod (incompetech.com)

Licensed under Creative Commons: By Attribution 4.0

http://creativecommons.org/licenses/by/4.0/

Converted to Ogg Vorbis and level adjusted for MADOROMI.

## Sound and ambience

"Inventory Sound Effects" (`turn_page.wav`) by **artisticdude**, submitted by Ogrebane.
https://opengameart.org/content/inventory-sound-effects
Licensed under CC BY 3.0: https://creativecommons.org/licenses/by/3.0/
Converted to Ogg Vorbis and level adjusted for MADOROMI.

**Interface Sounds** — Kenney (kenney.nl), CC0 1.0.

**Crickets Ambient Noise (Loopable)** — Ted Kerr / Wolfgang_, CC0 1.0.
https://opengameart.org/content/crickets-ambient-noise-loopable

**Ambient Bird Sounds** — isaiah658, CC0 1.0.
https://opengameart.org/content/ambient-bird-sounds

**Pleasing Bell Sound Effect** — Julie Damsgaard / Spring Spring / Spring Enterprises, CC0 1.0.
https://opengameart.org/content/pleasing-bell-sound-effect

CC0: https://creativecommons.org/publicdomain/zero/1.0/

Selected runtime files are converted/level adjusted; birds have a wrap crossfade. No character voice acting or generated music is included. Exact source hashes and transformations are documented in `docs/licenses/audio.md` and `audio-files.json`. License/credit copies are bundled under `game/licenses/`.

## Fonts

Noto Sans, Noto Serif, Noto Serif CJK JP — Google/Adobe/Noto contributors, SIL Open Font License 1.1. Full copyright and OFL notices are bundled in `game/licenses/`. `MadoromiTitleJP.otf` is a renamed subset for the Japanese title only. Font rights and reserved names remain with their owners.

## Engine and development references

Ren'Py 8.5.3: https://www.renpy.org/ . The engine includes MIT/LGPL and other components; its distribution contains the corresponding license notices and source availability information. https://www.renpy.org/doc/html/license.html

Ren'Py default GUI code/assets are adapted under the SDK's MIT license. Madoromi uses native engine persistence, rollback, history, auto and skip.

Locally installed development skills `visual-novel` and `game-ui-ux` come from gamedev-skills/awesome-gamedev-agent-skills under Apache 2.0; upstream LICENSE/NOTICE and pinned provenance are kept in `.agents/skills/`. They are excluded from the game runtime. Other read-only workflow references and decisions are in `docs/SKILLS.md`.

Editorial tooling: `writing-principles`, `creative-writing-craft`, `story-review` and `story-memory` from **haowjy/creative-writing-skills**, commit `1cb520f9c61e79ce2b1c56dba18601b2d6873433`, Apache License 2.0. Source: https://github.com/haowjy/creative-writing-skills . Unmodified upstream skill/resources, full LICENSE copies and SHA-256 provenance are retained in their `.agents/skills/` directories. No upstream root NOTICE file was present at this commit. These skills are development references, excluded from game runtime; their license does not replace the user's story or character-source rights. Actual editorial use is documented in `docs/STORY_AUDIT.md` and `docs/licenses/creative-writing-skills.md`.

Graphify 0.9.102 (`graphifyy`), © 2026 Safi Shamsi and contributors, Apache-2.0 with historical MIT portions. Its licenses, NOTICE and pinned upstream manifest are in `.agents/skills/graphify/`. The isolated CLI and Ren'Py adapter are development tools, excluded from the runtime. See `docs/KNOWLEDGE_GRAPH.md` for regeneration and verified query usage.
