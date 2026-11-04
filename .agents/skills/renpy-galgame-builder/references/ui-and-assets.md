# UI And Asset Integration Reference

Use this when fixing VN layout, integrating sprites/backgrounds/CGs, or preparing art passes.

## Image Declarations

Prefer clear names that match filenames:

```renpy
image bg_server_core = "images/backgrounds/server_temple_core.png"
image cg nova_neural_repair = "images/cg/cg_nova_neural_repair.png"

define sprite_zoom = 0.42
image nova neutral = Transform("images/characters/nova_neutral.png", zoom=sprite_zoom)
```

Keep legacy placeholder declarations if older script scenes still use them.

## Sprite Safety

Common failure: full-height transparent sprite files appear huge and cover UI.

Fix with:

```renpy
transform centerish:
    xalign 0.5
    yalign 0.98

define sprite_zoom = 0.42
image heroine neutral = Transform("images/characters/heroine_neutral.png", zoom=sprite_zoom)
```

If PNGs contain checkerboard instead of alpha, clean transparency before declaring.

## CG Integration

CGs should be 16:9 and usually `1280x720`.

```renpy
scene cg nova_neural_repair with dissolve
...
scene bg_firewall_control with dissolve
show nova vulnerable at centerish
```

Do not show character sprites on top of a CG unless intentionally compositing. After a CG section, return to the correct background before continuing normal sprite dialogue.

## UI Layout

Use 1280x720-safe defaults:

```renpy
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        ypos 300
        yanchor 0.5
        spacing 8
        for i in items:
            textbutton i.caption action i.action

style choice_button:
    xsize 900
    yminimum 58
    padding (22, 12)

style choice_button_text:
    size 20
    xmaximum 840
    text_align 0.5
    layout "subtitle"
```

Do not bake labels into UI PNGs. Use `text _("STATUS")` or `textbutton _("Language")`.

## Asset Manifests

For production art lists, include:

- asset id
- filename
- folder
- scene usage
- priority
- target size/aspect ratio
- visual description
- image prompt
- Ren'Py integration notes

For cute anime galgame style, prompts should say: `cute anime visual novel`, `soft cyberpunk`, `pastel neon`, `clean futuristic interior`, `no text`, `no UI`, `no watermark`.
