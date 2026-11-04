# Validation Reference

Use this before handing off a Ren'Py VN project.

## Static Checks

Run:

```sh
rg -n "^label |^default |^image |scene cg|show screen|call screen" game
find game/images -type f | sort
```

Confirm:

- every required label exists
- all menu branches jump/return correctly
- variables are initialized with `default`
- image declarations match files
- old placeholders do not shadow final assets accidentally

## Ren'Py Lint

Run:

```sh
<renpy-bin> <project-path> lint
```

Report if lint was unavailable. Do not claim engine validation if only static checks ran.

## Visual QA

Check these manually or with screenshots when possible:

- choice text wraps and stays above the dialogue box
- speaker namebox does not overlap dialogue
- status button stays top-right
- sprites are bust-sized and do not cover UI
- CGs are 16:9 and not collages/triptychs unless explicitly intended
- Chinese text renders with real glyphs, not boxes

## Asset QA

Prefer the bundled checker:

```sh
python <skill-dir>/scripts/check_vn_assets.py --project <project-path>
```

If the checker is unavailable, inspect dimensions with Pillow, ImageMagick, OS-native tools, or a short script. Use `1280x720` for backgrounds and CGs unless the project uses a different resolution.

## Documentation Checklist

README should include:

- title and description
- content rating note
- how to run in Ren'Py
- language support
- project structure
- route overview
- asset status
- known limitations
- next polish suggestions
