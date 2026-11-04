# Native Ren'Py story state and display aliases.
define r = Character("Ren", color="#c6eaff")
define a = Character("Aoi", color="#f7f9ff")
define s = Character("Sora", color="#d9f3dc")
define m = Character("Mio", color="#e2e6ff")
define portrait_dissolve = Dissolve(.22)
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
    for _bg in ("bedroom", "bedroom_day", "cafeteria", "street", "stage", "musicroom", "night", "courtyard", "bakery", "lounge"):
        renpy.image("bg " + _bg, "images/originals/" + _bg + ".webp")

    def madoromi_aoi(st, at, expression):
        # The epilogue has one authored casual pose. Earlier saves retain the
        # native outfit variable, so resolve it without inventing missing files.
        name = "casual_smile" if aoi_outfit == "blouse" else "school_" + expression
        return Image("images/originals/characters/aoi/" + name + ".webp"), None

    for _expression in ("neutral", "smile", "shy", "sad", "surprised", "laugh", "shy_clasp", "laugh_open", "tender_heart"):
        renpy.image("aoi " + _expression, DynamicDisplayable(madoromi_aoi, expression=_expression))
    for _person, _expressions in (("mio", ("neutral", "smile", "concerned", "thoughtful")), ("sora", ("neutral", "smile", "concerned", "easy"))):
        for _expression in _expressions:
            renpy.image(_person + " " + _expression, "images/originals/characters/" + _person + "/" + _expression + ".webp")

transform heroine:
    xalign .62
    yalign 1.0
    zoom 1.0
    on show:
        alpha 0.0
        xoffset 20
        easein (0.0 if persistent.reduce_motion else .32) alpha 1.0 xoffset 0
    on replace:
        alpha 1.0
        xoffset 0
    on hide:
        easeout (0.0 if persistent.reduce_motion else .20) alpha 0.0 xoffset -12

transform closeup:
    xalign .62
    yalign 1.0
    zoom 1.26
    yoffset 170

transform leftside:
    xalign .12
    yalign 1.0
    on show:
        alpha 0.0
        xoffset -18
        easein (0.0 if persistent.reduce_motion else .32) alpha 1.0 xoffset 0
    on replace:
        alpha 1.0
        xoffset 0
    on hide:
        easeout (0.0 if persistent.reduce_motion else .20) alpha 0.0 xoffset -12

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
