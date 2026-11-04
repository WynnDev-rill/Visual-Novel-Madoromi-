# Visual art provenance and production selection

Revised 4 November 2026. The current visual production pass follows the user's four canonical character designs and a single fine-line painted 2D environment family. It replaces the earlier Potat0Master character/background selection. The earlier creator-page evidence and [visual-assets.json](visual-assets.json) remain a historical acquisition audit; they are not the current runtime manifest.

## User-supplied character designs

The user supplied `aoi_base_bust_v1.png`, `mio_base_bust_v1.png`, `sora_base_bust_v1.png` and `ren_base_bust_v1.png` through `MADOROMI — Visual Novel / 02 - Aset & Lisensi / Karakter — MADOROMI`. Their current instruction expressly authorizes using these designs and developing consistent expressions, costumes and body language for this game.

The folder's manifest describes the PNGs as 1200×1600 RGBA upper-body concepts, cropped and upscaled from one AI-generated lineup. They are not native full-body portraits, ready-made expression sets, or Live2D models. Production extends the supplied PNG concepts into standing sprites with complete arms/hands, expression changes and scene-specific poses. Ren remains the first-person viewpoint; his concept can be used for a cast/profile portrait without placing him opposite the reader in every scene.

| Character | Canonical design anchors |
| --- | --- |
| Aoi | Blonde low side bun, two narrow dark hairpins as shown in the supplied image, thin round glasses, amber eyes, ivory vest, navy/gold blazer and bow |
| Mio | Blue-black medium-length hair, round glasses, blue eyes, gray vest, navy/gold uniform |
| Sora | Messy dark hair, round glasses, headphones at the neck, navy/gold uniform; drummer |
| Ren | Ash-brown parted hair, calm expression, dark scarf and navy uniform; first-person protagonist |

The supplied original-reference JPGs remain private source references and are not distributed in this repository or used as generation inputs. The supplied concept PNGs are the design inputs. User authorization and provenance are recorded here; no independently verified commercial clearance of the underlying references or exclusive copyright in generated work is asserted. This record does not replace rights in the user's source material.

## Production transformations and runtime files

OpenAI image generation is used to develop the supplied concepts into consistent expressions, body poses and the afterstory costume. The user's current instruction permits creating coherent backgrounds with AI. The same character finish and palette guide all new environments; no benchmark-game illustration, screenshot or music is submitted as a production asset.

Approved derived runtime WebPs are stored under `game/images/originals/`. Production metadata belongs in `production-art.json`: source/output identifiers and hashes, native/runtime dimensions, preparation, generation prompts where retained, and reference lineage. Original tool outputs and private reference downloads remain outside the repository. Mechanical preparation may resize or convert images while preserving a common sprite canvas; it does not invent facial features or repaint anatomy with a separate image-processing pipeline.

Body language is part of the current integration pass: Aoi's shy clasp, open laugh and tender hand-at-heart poses; Mio's thoughtful glasses gesture; and Sora's relaxed headphone/pocket posture. These require actual scene integration and screenshot checks before they count as verified acting. Expression and pose changes must preserve identity, anatomy, costume and apparent scale. Native Ren'Py dissolves connect changes, with reduced motion available.

The committed production selection supports a clean checkout without downloading the historical illustration packs. Run:

```bash
python3 -m pip install Pillow
python3 tests/check_assets.py
```

Desktop builds use the native Ren'Py visual archive. Android builds use RAPT's native image assets inside the signed APK. Final runtime evidence is reported separately in [VERIFICATION.md](../VERIFICATION.md); a successful earlier-art build does not verify replacement illustrations.

## Historical asset-first curation

The baseline used Potat0Master Character Sets A01/A02 and environment packs from the creator's [itch.io pages](https://potat0master.itch.io/). Their audited custom terms permitted personal/commercial game use and editing, and prohibited standalone redistribution. Those raw third-party images remain outside Git. Exact archive hashes, members, adaptation and page quotations are retained in [visual-assets.json](visual-assets.json) and [evidence](evidence/); `tools/acquire_visuals.py` is retained for historical reproducibility, not as a current build prerequisite.

No Potat0Master illustration was submitted for image generation. Kyuririn was evaluated but not integrated; NoranekoGames was excluded because its AI-use restriction did not fit this workflow. The replacement decision follows the user's supplied canonical designs and requirement for a coherent visual family, while keeping mature licensed audio, fonts and native engine systems.
