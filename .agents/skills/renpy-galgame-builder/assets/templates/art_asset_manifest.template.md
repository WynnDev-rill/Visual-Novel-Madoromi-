# Art Asset Manifest

## Backgrounds

| Asset ID | Filename | Folder | Scene Usage | Priority | Size | Visual Description | Image Generation Prompt | Ren'Py Notes |
|---|---|---|---|---|---|---|---|---|
| bg_example | example_background.png | game/images/backgrounds/ | Opening scene | required | 1280x720 | Clean readable VN background. | 16:9 visual novel background, cute anime VN style, no characters, no UI, no text, no watermark. | `image bg_example = "images/backgrounds/example_background.png"` |

## Character Sprites

| Character | Expression | Filename | Folder | Priority | Target Size | Visual Description | Prompt | Ren'Py Notes |
|---|---|---|---|---|---|---|---|---|
| HEROINE | neutral | heroine_neutral.png | game/images/characters/ | required | transparent PNG, bust-safe | Adult anime VN heroine, clear silhouette. | adult woman age 20+, cute anime visual novel heroine, transparent background, no text. | `image heroine neutral = Transform("images/characters/heroine_neutral.png", zoom=0.42)` |

## CG Key Moments

| Asset ID | Filename | Folder | Scene Usage | Priority | Size | Visual Description | Prompt | Ren'Py Notes |
|---|---|---|---|---|---|---|---|---|
| cg_example | cg_example.png | game/images/cg/ | Route intimacy scene | important | 1280x720 | Romantic suspense CG, non-explicit. | 16:9 anime visual novel CG, adult characters, intimate but non-explicit, no text, no UI. | `image cg example = "images/cg/cg_example.png"` |

## UI Assets

| Asset ID | Filename | Folder | Priority | Size | Visual Description | Notes |
|---|---|---|---|---|---|---|
| dialogue_box | dialogue_box.png | game/images/ui/ | required | 1160x170 | Transparent dialogue panel, no text. | Text must be rendered by Ren'Py. |

## Audio Suggestions

- Title theme:
- Suspense ambience:
- Romance motif:
- Choice confirm:

## Implementation Checklist

- [ ] All final PNGs exist.
- [ ] Backgrounds and CGs are 1280x720.
- [ ] Sprites have real transparency.
- [ ] UI assets contain no baked text.
- [ ] `script.rpy` image declarations match filenames.
- [ ] Ren'Py lint passes.
