---
name: renpy-galgame-builder
description: Build, polish, localize, and validate Ren'Py galgame / visual novel prototypes. Use when Codex is asked to create a Ren'Py project, implement VN story flow, route logic, choices, status screens, cyber/anime galgame UI, placeholder or generated asset integration, CG/background/sprite declarations, Traditional Chinese localization, CJK font fixes, Ren'Py lint cleanup, README/docs, or packaging-ready visual novel examples.
---

# Ren'Py Galgame Builder

## Core Workflow

1. Inspect the project first: `rg --files`, then read `game/script.rpy`, `game/screens.rpy`, `game/options.rpy`, `game/gui.rpy`, and README/docs if present.
2. Preserve story variables, labels, route logic, and image ids unless the user explicitly asks for structural changes.
3. Implement the smallest complete VN slice that runs from `start` to at least one ending, then expand prose/UI/assets in focused passes.
4. Prefer stable Ren'Py declarations and screens over clever Python. Keep assets under `game/images/{backgrounds,characters,cg,ui}/`.
5. Always run Ren'Py lint when the SDK is available. If not, do static checks for labels, image paths, variables, and translation syntax.

## Task Map

- **New prototype or story expansion**: read [story-structure.md](references/story-structure.md).
- **UI/layout/assets**: read [ui-and-assets.md](references/ui-and-assets.md).
- **Image generation prompts or art direction passes**: read [image-generation.md](references/image-generation.md).
- **English/Traditional Chinese localization or乱码 fixes**: read [localization.md](references/localization.md).
- **Validation and release readiness**: read [validation.md](references/validation.md).

## Ren'Py Project Defaults

Use a normal VN resolution unless the repo says otherwise:

```renpy
define config.screen_width = 1280
define config.screen_height = 720
```

Use safe visual layout defaults:

- Dialogue box: bottom, about `1160x170`, padded.
- Choices: centered near `y=300`, max width `850-950`, wrapping text.
- Sprites: bust-sized, centered behind the dialogue box, not huge full PNGs unless intended.
- Status/settings buttons: top-right, small, not over content.

## Implementation Rules

- Keep R17 romance sensual, intimate, and character-revealing, not explicit.
- Do not rely on nudity, minors in romance, or sexual violence.
- Every romantic scene should reveal a secret; every secret should change how the romance feels.
- For placeholders, prefer Ren'Py `Solid`, scaled `Transform`, or clean generated PNGs. Avoid giant text placeholders over the dialogue UI.
- Do not bake UI text into images. Render text with Ren'Py so localization works.
- When adding Chinese, bundle or reference a CJK-capable font and set Ren'Py styles to use it.

## Common Commands

Install helper script dependencies when needed:

```sh
python -m pip install -r <skill-dir>/scripts/requirements.txt
```

Use the Ren'Py launcher or an SDK path discovered on the user's machine:

```sh
<renpy-bin> <project-path> lint
<renpy-bin> <project-path> translate tchinese
```

For cropping generated UI sheets or normalizing VN images:

```sh
python <skill-dir>/scripts/slice_vn_assets.py --help
```

For asset path, size, and alpha checks:

```sh
python <skill-dir>/scripts/check_vn_assets.py --project <project-path>
```

For reusable starter files, inspect `<skill-dir>/assets/templates/`.

## Completion Checklist

- Required labels exist and are reachable.
- Default variables are initialized.
- Menus update the intended variables.
- All referenced PNG paths exist, or safe `Solid` fallbacks remain.
- CGs return to the appropriate background before sprite/dialogue continuation.
- UI text wraps at 1280x720 and does not overlap the dialogue box.
- English remains the source language if adding localization.
- Ren'Py lint passes, or limitations are clearly reported.
