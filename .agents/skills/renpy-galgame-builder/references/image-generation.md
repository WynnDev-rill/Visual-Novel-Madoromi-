# Image Generation Reference

Use this when creating art manifests, writing prompts, generating placeholders, revising art direction, or postprocessing generated sheets for a Ren'Py galgame.

## Core Rules

- Generate only the requested asset type for the current pass: backgrounds, sprites, CGs, or UI. Do not mix passes unless the user asks.
- Keep final VN assets text-free. Prompts must include `no text`, `no UI`, `no logo`, `no watermark`, and usually `no captions`.
- Keep characters adult when romance is involved: `adult woman, age 20+`.
- Prefer clean, readable visual novel composition over cinematic clutter. Dialogue and sprites need visual space.
- If a generated result is too dark, gritty, horror-like, or realistic, retry with stronger style anchors: `cute anime visual novel`, `anime galgame background`, `soft lighting`, `pastel neon`, `clean futuristic interior`, `romantic sci-fi`.
- Do not bake translations, labels, status text, title text, or button text into images. Ren'Py should render all player-facing text.
- For transparent sprites, request `transparent background`, then verify actual alpha. If the image shows checkerboard pixels, remove or regenerate.

## Soft Cyber Romance VN Prompt Pattern

Use this pattern for the Neon Firewall style and similar cyber romance VNs:

```text
16:9 visual novel background, cute anime visual novel style, soft cyberpunk,
pastel cyan, pink, purple, and white lighting, clean futuristic interior,
romantic sci-fi mystery atmosphere, cozy but slightly suspenseful,
polished anime galgame background, elegant and readable composition,
no characters, no UI, no text, no logo, no watermark,
not horror, not gritty, not industrial decay, no heavy black shadows
```

For heroine sprites:

```text
adult woman age 20+, cute anime visual novel heroine, expressive eyes,
soft cel-shaded anime style, romantic sci-fi outfit, appealing silhouette,
clean transparent sprite, full body or three-quarter bust, no background,
no text, no logo, no watermark, not realistic, not horror, not grotesque
```

## Asset Pass Order

1. Backgrounds: six to eight 1280x720 16:9 PNGs, no characters.
2. Character sprites: one heroine at a time, transparent PNG, consistent scale and pose family.
3. Expression variants: reuse outfit/silhouette; change face and small body language only.
4. CGs: 1280x720 16:9, scene-specific, no captions, no collage/triptych unless requested.
5. UI assets: text-free transparent PNGs; crop or recreate clean panels from generated sheets.

## Retry Heuristics

- Too dark: add `bright pastel`, `soft white fill light`, `clean anime galgame`, `no heavy shadows`.
- Too scary: add `romantic`, `cozy`, `gentle`, `charming heroine-focused VN style`, `not horror`.
- Too busy: add `simple readable composition`, `clear center stage`, `visual novel dialogue-safe lower area`.
- Wrong aspect: explicitly require `1280x720, 16:9`.
- Text artifacts: regenerate with `no text, no letters, no symbols, no signage, no labels`; crop only if artifacts are outside the useful area.

## Integration Notes

- Save backgrounds under `game/images/backgrounds/`.
- Save sprites under `game/images/characters/`.
- Save CGs under `game/images/cg/`.
- Save UI under `game/images/ui/`.
- Update `script.rpy` image declarations after assets exist.
- Keep Solid fallback declarations commented nearby when useful for future portability.
- Run `python <skill-dir>/scripts/check_vn_assets.py --project <project-path>` and Ren'Py lint after integration.
