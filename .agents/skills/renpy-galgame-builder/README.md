# Ren'Py Galgame Builder

A Codex skill for building, polishing, localizing, and validating Ren'Py galgame / visual novel prototypes.

It captures a practical workflow for:

- Ren'Py project structure and route logic
- VN UI layout fixes
- Background, sprite, CG, and UI asset integration
- Image generation prompt rules for cute anime / soft cyber romance styles
- UI sheet slicing and clean text-free UI fallback generation
- Traditional Chinese localization and CJK font fixes
- Ren'Py lint and asset validation

## Demo

Actual screenshots from a Ren'Py soft cyber romance VN prototype built with this workflow:

![Traditional Chinese title screen](docs/demo/demo-title-tchinese.jpg)

![Traditional Chinese dialogue scene](docs/demo/demo-dialogue-tchinese.jpg)

![Traditional Chinese choice menu](docs/demo/demo-choice-tchinese.jpg)

![NOVA CG scene with dialogue UI](docs/demo/demo-cg-nova-tchinese.jpg)

These screenshots show real Ren'Py runtime output: title menu, localized dialogue, choice UI, CG integration, custom UI assets, and CJK font rendering. Replace them with screenshots from your own project when publishing your game.

## Install

Copy this folder into your Codex skills directory:

```sh
~/.codex/skills/renpy-galgame-builder
```

Install helper script dependencies when needed:

```sh
python -m pip install -r scripts/requirements.txt
```

Ren'Py itself is only required when you want to launch, lint, or build a game. The skill can still draft scripts, screens, manifests, and localization files without the Ren'Py SDK installed.

## Use

Invoke the skill explicitly:

```text
Use $renpy-galgame-builder to create a 30-minute Ren'Py romance mystery prototype.
```

Useful prompts:

```text
Use $renpy-galgame-builder to fix my Ren'Py VN UI layout, sprite scaling, and choice menu wrapping.
```

```text
Use $renpy-galgame-builder to add Traditional Chinese localization and fix CJK font rendering.
```

```text
Use $renpy-galgame-builder to create an art asset manifest and integrate generated backgrounds, sprites, CGs, and UI.
```

## Tools

```sh
python scripts/slice_vn_assets.py --help
python scripts/check_vn_assets.py --project /path/to/renpy-project
```

## Ren'Py Workflow

1. Install the Ren'Py SDK from the official Ren'Py website.
2. Create or open a Ren'Py project folder. A typical project contains `game/script.rpy`, `game/screens.rpy`, `game/options.rpy`, and `game/images/`.
3. Ask Codex to use this skill to scaffold or polish the VN:

```text
Use $renpy-galgame-builder to create a playable Ren'Py visual novel prototype in this repository.
```

4. Launch the project from the Ren'Py launcher, or run it with your local Ren'Py executable.
5. Run lint before sharing:

```sh
<renpy-bin> /path/to/project lint
```

6. Check generated/copied assets:

```sh
python scripts/check_vn_assets.py --project /path/to/project
```

7. Use the Ren'Py launcher to build distributions for Windows, macOS, Linux, or web, depending on your project needs.

## Demo Screenshot Tips

For public game repos, include 2-5 screenshots:

- Title screen
- Dialogue scene with one heroine sprite
- Choice menu
- Status/investigation screen
- Localization example, if the game is bilingual

Use a consistent screenshot size. Pure in-game captures should usually be 1280x720 or another 16:9 size; windowed runtime screenshots with title bars are also fine for showing that the project really launches. Avoid major spoilers, explicit imagery, debug overlays, and screenshots with broken placeholder art.

## License

MIT. See [LICENSE](LICENSE).
