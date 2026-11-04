# Native Ren'Py story state and display aliases.
define r = Character("Ren", color="#285d79")
define a = Character("Aoi", color="#963f4b")
define s = Character("Sora", color="#596c35")
define m = Character("Mio", color="#73518a")
default persistent.completed = False
default persistent.chapter_unlocked = 1
default persistent.text_size = 36
default persistent.reduce_motion = False
default aoi_outfit = "school"
default quick_menu = True

define audio.night = "audio/bgm/night.ogg"
define audio.day = "audio/bgm/day.ogg"
define audio.tender = "audio/bgm/tender.ogg"
define audio.confession = "audio/bgm/confession.ogg"
define audio.message = "audio/sfx/message.ogg"
define audio.ui = "audio/sfx/ui.ogg"
define audio.page = "audio/sfx/page.ogg"
define audio.bell = "audio/sfx/bell.ogg"

init python:
    config.overlay_screens.append("quick_menu")
    renpy.music.register_channel("ambience", mixer="ambience", loop=True)
    for _bg in ("bedroom", "bedroom_day", "cafeteria", "artroom", "artroom_evening", "cafe", "cafe_evening", "school", "school_evening", "street", "street_evening", "stage", "night", "nature", "courtyard", "bakery", "lounge"):
        renpy.image("bg " + _bg, "images/" + ("originals/" if _bg in ("courtyard", "bakery", "lounge") else "backgrounds/") + _bg + ".webp")
    for _expression in ("neutral", "smile", "shy", "sad", "surprised", "laugh", "angry", "tears"):
        renpy.image("aoi " + _expression, DynamicDisplayable(lambda st, at, exp=_expression: (Image("images/characters/aoi/" + aoi_outfit + "_" + exp + ".webp"), None)))

transform heroine:
    xalign .62
    yalign 1.0
    zoom 1.0
    on show:
        alpha 0.0
        xoffset 20
        ease (0.0 if persistent.reduce_motion else .35) alpha 1.0 xoffset 0
    on replace:
        alpha 1.0
        xoffset 0

transform closeup:
    xalign .62
    yalign 1.0
    zoom 1.26
    yoffset 170

transform leftside:
    xalign .28
    yalign 1.0

transform title_character:
    xalign .84
    yalign 1.0
    zoom .9
    yoffset 36

transform scene_drift:
    subpixel True
    xalign .5
    yalign .5
    zoom 1.035
    # Motion stays restrained and can be disabled in Preferences.
    linear (0.0 if persistent.reduce_motion else 26.0) zoom (1.035 if persistent.reduce_motion else 1.075)

transform card_in:
    alpha 0.0
    yoffset 18
    ease .45 alpha 1.0 yoffset 0

label chapter_card(number, title, subtitle):
    window hide
    $ _chapter_quick = quick_menu
    $ quick_menu = False
    scene expression Solid("#101b2a")
    call screen chapter_title(number, title, subtitle)
    $ quick_menu = _chapter_quick
    return

label phone_chat(messages, time_label):
    window hide
    $ _phone_index = 0
    while _phone_index < len(messages):
        $ _phone_index += 1
        play sound audio.message
        $ _phone_sender, _phone_text = messages[_phone_index - 1]
        $ (a if _phone_sender == "aoi" else r).add_history("adv", "Aoi · pesan" if _phone_sender == "aoi" else "Ren · pesan", _phone_text)
        call screen phone_messages(messages[:_phone_index], time_label)
    return
