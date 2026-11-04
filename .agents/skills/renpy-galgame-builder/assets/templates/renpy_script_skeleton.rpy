# Starter Ren'Py visual novel skeleton.
# Replace labels, characters, variables, and image declarations for the target project.

define narrator = Character(None)
define p = Character("PLAYER")
define h = Character("HEROINE")

default heroine_trust = 0
default truth_score = 0
default route_lock = None

image bg_room = Solid("#17233f")
image heroine neutral = Solid("#88ddff")

label start:
    jump prologue

label prologue:
    scene bg_room with dissolve
    show heroine neutral
    h "You woke up before the system finished deciding what you were."

    menu:
        "Trust her voice, even if it knows too much.":
            $ heroine_trust += 1
        "Ask what she is hiding from you.":
            $ truth_score += 1

    jump final_choice

label final_choice:
    if heroine_trust >= truth_score:
        jump ending_heroine
    jump ending_truth

label ending_heroine:
    h "Then stay. Not because I asked. Because you chose."
    return

label ending_truth:
    narrator "The truth does not forgive you. It only opens the door."
    return
