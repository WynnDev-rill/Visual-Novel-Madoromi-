# Font licenses

Checked 2026-11-03. Fonts are embedded under **SIL Open Font License 1.1**, permitting commercial game bundling. Include the supplied copyright/license files in distributions. No font may be sold by itself.

| Runtime font (`game/fonts/`) | Provenance and purpose | Edits |
|---|---|---|
| `NotoSans-Regular.ttf` | Installed `/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf`; readable Latin/Indonesian dialogue and controls | Unmodified |
| `NotoSerif-Regular.ttf` | Installed Noto Serif; title and section typography | Unmodified |
| `NotoSerif-Italic.ttf` | Installed Noto Serif Italic; optional written-note styling | Unmodified |
| `MadoromiTitleJP.otf` | Face 0, **Noto Serif CJK JP Regular**, from installed `/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc` | FontTools subset; renamed internally to **Madoromi Title JP** |

The 10KB Japanese subset supports the title **まどろみ**, **マドロミ**, **MADOROMI**, digits and a few separators only. It is not a general Japanese text font. Latin fonts cover Indonesian diacritics; no claim is made that they cover Japanese dialogue.

Upstreams: [Noto fonts](https://github.com/notofonts/noto-fonts), [Noto CJK](https://github.com/notofonts/noto-cjk). Installed package provenance, copyright notices and the complete OFL are preserved in [`noto-core-copyright.txt`](noto-core-copyright.txt) and [`noto-cjk-copyright.txt`](noto-cjk-copyright.txt). Those Debian manifests also describe packaging files not shipped as fonts; the embedded fonts themselves use OFL, not the Debian packaging license.

Subset creation: FontTools `TTCollection(...).fonts[0]`, subset text `まどろみマドロミMADOROMI ·—　0123456789`, preserve source copyright fields, rename name IDs 1/2/3/4/6/16/17, save as OTF. The complete fonts remain available in the source package; no derivative uses a reserved original family name.
