# MADOROMI — third-party notices

Project production: WynnDev. Story adapted under the user's instruction from the supplied short story **Sepuluh Detik**. The supplied original is preserved in `docs/source/cerita-asli.docx`; its rights are not replaced by any engine or asset license.

## Character and environment art

**Potat0Master** — Character Sets A01/A02 and selected environment packs. https://potat0master.itch.io/

The creator permits personal/commercial game use and modification, and forbids reselling or redistributing sprites/backgrounds as standalone assets. Selected art is resized, then distributed only inside the integrated game: a Ren'Py visual archive on desktop, or native assets inside the signed Android APK. The public source repository contains acquisition code and source/license evidence rather than those standalone images. Art rights remain with the creator. See `docs/licenses/visual-art.md` and `visual-assets.json` for exact works, files and terms.

Three environment gaps and the painted-jeans prop were generated specifically for MADOROMI using OpenAI image generation. These are disclosed as AI-generated project images, with no exclusive-copyright claim. No benchmark game art or licensed character was submitted to generation.

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
