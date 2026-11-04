# Localization And Font Reference

Use this for Traditional Chinese support, language menus, or Chinese乱码/font issues.

## Translation Workflow

Keep English as source. Generate translation skeletons:

```sh
<renpy-bin> <project-path> translate tchinese
```

Use `game/tl/tchinese/` for Traditional Chinese.

Translate:

- dialogue and narration
- menu choices
- custom UI strings
- status screens
- ending titles
- README language notes

Do not overwrite `game/script.rpy` with Chinese unless explicitly requested.

## Language Menu

Simple safe pattern:

```renpy
screen language_menu():
    tag menu
    frame:
        vbox:
            text _("Language")
            textbutton "English" action Language(None)
            textbutton "繁體中文" action Language("tchinese")
            textbutton _("Return") action Return()
```

Add a title-screen button and, if useful, a status/preference-screen button.

## CJK Font Fix

If Chinese becomes乱码, square boxes, or missing glyphs, the active font lacks CJK glyphs.

Bundle a CJK font under:

```text
game/fonts/SourceHanSansLite.ttf
```

Set GUI and custom styles:

```renpy
define nfap_ui_font = "fonts/SourceHanSansLite.ttf"
define gui.text_font = nfap_ui_font
define gui.name_text_font = nfap_ui_font
define gui.interface_text_font = nfap_ui_font
define gui.button_text_font = nfap_ui_font

style default:
    font "fonts/SourceHanSansLite.ttf"
    language "eastasian"

style say_dialogue:
    font "fonts/SourceHanSansLite.ttf"
    language "eastasian"
```

Ren'Py SDK often includes `sdk-fonts/SourceHanSansLite.ttf`. Copy it into the project so packaged builds work on other machines.

## Style Guidance

Translate naturally, not literally.

- NOVA: calm, elegant, possessive, precise.
- MAYA: warm, guilty, wounded, restrained.
- HYDRA: seductive, playful, poetic, dangerous.
- System narration: clinical, ritualistic, coldly poetic.

Keep glossary terms consistent:

- Eden Relay: 伊甸中繼站
- AFTER PROTOCOL: AFTER PROTOCOL / 終末協議
- Corruption: 腐化
- Truth: 真相
- Intimacy: 親密度
