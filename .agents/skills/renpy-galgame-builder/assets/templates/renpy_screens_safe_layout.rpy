# 1280x720-safe Ren'Py UI layout starter.

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1160
        ysize 170
        bottom_margin 24

        if who is not None:
            text who id "who"

        text what id "what"

screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        ypos 300
        yanchor 0.5
        spacing 8

        for i in items:
            textbutton i.caption action i.action

style say_window:
    background Frame("images/ui/dialogue_box.png", 24, 24)
    padding (34, 26, 34, 24)

style say_label:
    xpos 24
    ypos 10

style say_dialogue:
    xpos 24
    ypos 48
    xmaximum 1060
    size 26
    line_spacing 4

style choice_button:
    background Frame("images/ui/choice_button_idle.png", 18, 18)
    hover_background Frame("images/ui/choice_button_hover.png", 18, 18)
    xsize 900
    yminimum 58
    padding (24, 12)

style choice_button_text:
    size 22
    xmaximum 840
    text_align 0.5
    layout "subtitle"
