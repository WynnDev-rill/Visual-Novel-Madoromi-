# Visual art acquisition and rights

Audited on 3 November 2026. All reused runtime artwork is by **Potat0Master**, acquired from the creator's own itch.io pages. Aoi uses the same Kohaku character across all expressions and outfits. The creator's character name is an asset identifier; the game character and story are original to MADOROMI.

Suggested in-game credit: **Character and background art: Potat0Master — https://potat0master.itch.io/**. Credit is appreciated rather than required under the audited terms.

## Permitted use and distribution boundary

The creator expressly permits personal and commercial games and modification of the artwork. The creator prohibits resale or distribution of the images as standalone assets, including modified versions. The pages specifically clarify that making and selling a visual novel with the art is permitted.

Therefore the selected images are used only inside MADOROMI and are excluded from the source repository. Distributions include them in the integrated game: a Ren'Py visual archive on desktop, or native image assets inside the signed Android APK. Do not publish the downloaded ZIPs, raw artwork directories, sprite contact sheets, or an asset-only archive. Raw downloads are retained outside the project at `/workspace/downloads/visuals`.

The checked pages contain no restriction on this AI-assisted development workflow or ordinary visual inspection/resizing. “No generative AI was used” describes the creator's production method; it does not forbid AI-assisted game development. No creator art was used to train a model or submitted for image generation. Preparation uses Pillow for a fixed transparent crop and Lanczos resizing; it adds no painted or generated detail.

The downloaded archives contain no separate EULA or README. Relevant page quotations, retrieval dates, and page digests are preserved in [evidence](evidence/). Exact archive hashes, individual members, adaptation, dimensions, output hashes, and runtime paths are recorded in [visual-assets.json](visual-assets.json).

## Reproduce the approved selection

```sh
python -m pip install Pillow
python tools/acquire_visuals.py --cache /path/outside/source/visual-cache
```

The script uses the creator's public free download flow, selects the audited download by published filename, verifies the archive SHA-256, and derives the chosen game images. It requires no account or payment. A changed archive fails closed for another license/content review; it does not silently accept new material. Pillow is a development dependency, not a game dependency. The default project destination is the script's parent project directory; `--project` can override it.

The source repository alone intentionally does not contain these third-party images. Run acquisition before linting, rendering, desktop packaging, or Android packaging. A game build must include the images as part of the integrated game bundle; Android uses RAPT's native APK assets rather than RPA files. The creator's download pages remain the source of truth for future releases.

## Selected packs

| Pack | Scene or character use | Source |
| --- | --- | --- |
| Character Set A01, 2160p WebP free tier | Kohaku, summer/winter school uniforms; 17 consistent expressions | [Creator page](https://potat0master.itch.io/free-characters-for-visual-novels-set-a01) |
| Character Set A02, 2160p WebP free tier | Same Kohaku, white T-shirt and blue blouse; 17 expressions each | [Creator page](https://potat0master.itch.io/characters-set-a02) |
| Personal Rooms Pack 1 | Same bedroom by day and lamplit night | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-personal-rooms-pack-1) |
| School Mini Pack 1 | School exterior, classroom, hallway; day/evening variants | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-school-mini-pack-1) |
| School Mini Pack 2 | Art room, afternoon/evening | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-school-mini-pack-2) |
| Mini Pack 1 | Coffee shop, afternoon/evening | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-mini-pack-1) |
| Mini Pack 2 | Canteen | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-mini-pack-2) |
| Starter Pack 2 | Street, night city and auditorium | [Creator page](https://potat0master.itch.io/free-visual-novel-backgrounds-starter-pack-2) |
| Stylized Random Pack A | River/forest and stone rail arch establishing shots | [Creator page](https://potat0master.itch.io/free-stylized-backgrounds-for-visual-novels-random-pack-a) |

## Art direction and known gaps

The chosen family combines soft anime portraits with restrained Blender-rendered scenery, warm afternoon light, blue-grey school clothing, and golden-brown hair. The heroine's face, eyes, silhouette and shading stay identical between outfits. The source portraits are 1440×2160; every portrait uses the same crop `(80, 420, 1320, 2160)` and becomes a 770×1080 transparent WebP. All expression changes align without moving her head. Backgrounds become 1920×1080 WebP, generally downsampled from 3840×2160; the older Starter Pack 2 backgrounds are already 1920×1080.

The approved reused packs do **not** supply a cathedral/tree courtyard, a bakery with visible bread, or a beanbag lounge. A classroom was not relabeled as a lounge, and a park playground was not relabeled as a cathedral. Those locations require original environment illustrations; their provenance is separate from this register. A coffee shop can support secondary café scenes but does not visually establish the source story's favorite bakery.

Kyuririn's current download was inspected as a candidate but not integrated: its selection mixes sketches, unrelated locations, and only a small number of finished interiors. NoranekoGames was excluded because its broad prohibition on AI use is incompatible with this workflow. No benchmark game artwork or screenshots are included in the build.

## Expression interface

Files are `game/images/characters/aoi/{outfit}_{expression}.webp`. Outfits: `school`, `summer`, `casual`, `blouse`.

| Game expression | Creator expression |
| --- | --- |
| neutral | normal |
| smile | normalblush |
| shy | blush |
| sad | upset |
| surprised | huh |
| laugh | happy |
| talk, tears, pout, frown, angry, angrytalk, disgusted, poutangry | Same creator label |
| smirk | evilsmirk |
| dread | purp |
| sadtalk | upsettalk |

Portraits deliberately retain the original artist's designs. No new character art, expression interpolation, face swaps, or generative retouching was used.
