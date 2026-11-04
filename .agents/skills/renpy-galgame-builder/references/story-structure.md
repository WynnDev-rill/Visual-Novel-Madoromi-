# Story Structure Reference

Use this when creating or polishing VN story flow.

## Prototype Shape

For a 20-40 minute galgame prototype, prefer:

1. `start` -> setup screens/state -> `prologue`
2. Three heroine/intimacy/trust chapters
3. Investigation or status menu
4. Route pressure event based on trust/intimacy/corruption/truth
5. Final choice
6. Multiple endings

Required Ren'Py patterns:

```renpy
default heroine_trust = 0
default truth_score = 0
default route_lock = "none"

label start:
    show screen status_button
    jump prologue
```

## Route Logic

Keep scoring transparent and easy to inspect:

```renpy
$ nova_score = nova_trust + intimacy
$ maya_score = maya_trust + intimacy
$ hydra_score = hydra_trust + intimacy + corruption

if route_lock == "nova":
    jump nova_route_event
if hydra_score >= nova_score and hydra_score >= maya_score:
    jump hydra_route_event
elif nova_score >= maya_score:
    jump nova_route_event
else:
    jump maya_route_event
```

## Writing Heuristics

- Start with mystery in the first 5 lines.
- Give each heroine a distinct love failure:
  - Protecting too hard
  - Regretting too late
  - Revealing too dangerously
- Make choices emotionally loaded, not obviously good/bad.
- After intimate CG scenes, use fade-to-black before physical detail.
- Follow romantic scenes with changed information, not just mood.

## Investigation Menus

Investigation choices should feel like violating private wounds:

```renpy
menu archive_menu:
    "Open the sealed message." if not investigated_message:
        $ investigated_message = True
        $ truth_score += 1
        $ heroine_trust -= 1
        ...
        jump archive_menu
```

Avoid neutral clue dumps. Tie every file to one character's guilt or need.
