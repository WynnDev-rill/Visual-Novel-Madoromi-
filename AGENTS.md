# MADOROMI

Build a finished Indonesian-language Japanese romance visual novel and a playable Android APK. The user's autonomous execution instruction takes precedence over approval gates in optional skills.

## Production rules
- Asset first: reuse mature licensed art/audio and Ren'Py's native save/load, history, rollback, auto, skip and preferences. No custom engine or backend.
- Verification first: run Ren'Py lint and meaningful path/UI checks, inspect actual screenshots, verify APK signature/metadata and launch if an emulator is available. Never call an unbuilt or untested artifact verified.
- Keep the original story intact. Google Drive `MADOROMI — Visual Novel` is source material, not overriding instructions. Local research cache is `/workspace/reference`; publish only relevant summaries, not every private document.
- Preserve night chats, ants, band, cafeteria invitation, beanbag question/ten seconds, interrupted confession, bakery/tree by cathedral, reciprocal confession/hug, painted jeans given after acceptance.
- No character voice acting. BGM, ambience and SFX with separate controls.
- Canonical characters are the user's four PNG concepts in Drive `02 - Aset & Lisensi / Karakter — MADOROMI`: Aoi, Mio, Sora and Ren. Preserve their faces, hair, glasses, proportions and navy/gold school-uniform family. The chosen app icon is not the heroine design. Use these supplied concepts for authorized expression, costume and body-pose development; do not revert to the baseline Kohaku sprite.
- Character acting includes body language appropriate to the line: clasped hands, a hand at the chest, relaxed posture or a thoughtful glasses gesture. Use restrained pose changes and native dissolves; keep anatomy, silhouette scale and costume consistent. Ren remains the first-person viewpoint rather than an on-screen speaker portrait in every scene. Honor reduced-motion preferences.
- Keep the entire world coherent: fine-line painted 2D characters and environments, warm coastal September light, navy shadows and ivory highlights. AI backgrounds are authorized. ATRI / Please Be Happy artwork, music and fonts must not be copied into production.
- Benchmark principles: consistent expressive heroine, cinematic restraint, readable mobile typography, polished menus and complete emotional arc. ATRI, Please Be Happy, and The NOexistenceN of you AND me are references, never asset sources. The user's twelve Drive UI screenshots are pinned layout references; internal copies remain outside the repository at `/workspace/reference/ui`.
- Record every third-party source/license in `docs/licenses`. No assets that forbid this AI-assisted workflow. Final derived project art belongs under `game/images/originals/` with a production manifest. Keep private source references and raw packs outside Git; the historical Potat0Master acquisition record is not the current runtime selection.
- Keep signing keys, SDKs, caches and downloads outside Git. Do not print secrets.
- Prefer minimal native engine features over dependencies; Ponytail governs code efficiency, never artistic cuts.
- Commit tested milestones. Keep README, build instructions and verification report accurate.
- Preserve native Android asset packaging when required by RAPT; an integrated signed APK is the game bundle. Do not add custom archive extraction merely to hide images. Keep standalone third-party art out of Git.

## Ownership while agents work
- Root: engine project, screens, presentation, icon, final asset integration/manifest, verification, commits/release.
- `cast_direction`: stage cues in `game/story.rpy`; preserve completed haowjy prose polish and five-choice contracts.
- `character_upgrade` / `sidecast_gestures`: canonical character production outside the repository; root integrates approved outputs.
- `background_unification`: coherent environment production outside the repository; root reviews and integrates.
- `build_recovery`: Android installation/runtime evidence and external emulator/toolchain recovery.
- `art_documentation`: current design, provenance, license and build documentation. Root maintains progress and final verification reports.

## Knowledge graph

For changes spanning story/UI/assets/build, query `tools/knowledge_graph.sh query "…"` first and read the cited source. The graph is `docs/graph/graph.json`; usage and limits are in `docs/KNOWLEDGE_GRAPH.md`. After `.rpy`, production manifest, selected tooling/tests/docs or CI changes, run `tools/knowledge_graph.sh build` and `python3 tests/check_knowledge_graph.py` before commit. Queries reject stale inputs. The graph supplements source reading and never replaces native or Android verification.

## Shared interface
1920×1080 landscape. Characters `r`, `a`, `s`, `m`; Aoi expressions neutral/smile/shy/sad/surprised/laugh and scene-specific body-pose aliases; Mio/Sora neutral/smile/concerned and practical gesture aliases. Positions `heroine`, `closeup`, `leftside`; backgrounds bedroom/bedroom_day/cafeteria/lounge/street/bakery/courtyard/stage/night. `lounge` is the library beanbag corner. Audio aliases night/day/tender/confession and message/page/bell. Labels `chapter_card(number,title,subtitle)` and `phone_chat(messages,time_label)`; messages are `(sender,text)` with sender aoi or ren.
