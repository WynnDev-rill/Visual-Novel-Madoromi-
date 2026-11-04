# Verification — baseline checked 2026-11-04

This report distinguishes native desktop play, static source checks, and Android
verification. This is the working baseline before the user's new character
replacement and haowjy full-script polish. It does not claim those new revisions
are finished.

## Recorded evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Story preservation | PASS | `python3 tests/check_story.py`: 12 scenes, 7,601 narrative/dialogue words; required source beats and sequence intact. |
| Native desktop baseline | PASS | Final revised UI: Ren'Py 8.5.3.26051504; 11 executed cases, 71 assertions, 95.988 seconds; one optional autosave diagnostic skipped. |
| Both contrasting complete paths | PASS | `00000` and `11111`, each with all five later callbacks, completed ending and chapter 3 unlocked. |
| Manual save/load and phone backlog | PASS | Native tests restored a selected story branch and the fourth phone message; speaker/text history and no duplicate next message were asserted. |
| Automatic reading, skip and preferences | PASS | Native AFM reached phone presentation, skip stopped at a choice; text/motion and separate audio mixer settings responded. |
| Native menu destinations | PASS | Help, credits, load, chapters and engine information screens opened and returned. |
| Branch rollback | PASS | Fresh native save/load and rollback assertions passed. Ordinary Android autosave remains a separate device check. |
| Revised UI verification | PASS | 23 real 1280×720 captures inspected; offscreen window anchor, active-tab contrast, history columns, face occlusion and target size were corrected. |
| Android package | PASS | 79,200,445 bytes; source inventory/signature/16KB alignment verified in tests/artifacts/android-build.json. |
| Android device runtime | Pending | Recovering existing emulator installation/launch evidence; no physical-device result claimed. |
| New story/art pass | In progress | User requested higher-quality replacement character, coherent art and installed haowjy audit on 2026-11-04. Rebuild/regression required afterward. |

Baseline report and screenshots are at
`/workspace/downloads/madoromi-tests/touch/`. Representative captures are in
`docs/screenshots/baseline/`. Validation command:

```sh
python3 tests/check_story.py \
  --coverage /workspace/downloads/madoromi-tests/touch/native-paths.json \
  --coverage-mode choices \
  --report /workspace/downloads/madoromi-tests/touch/native.log
```

The contrasting paths exercise every choice option and callback. The optional
32-combination matrix has not been run and is not claimed as covered.

## Baseline screenshot review

Actual engine captures were inspected for cafeteria, beanbag lounge, courtyard
confession, painted-jeans keepsake, history, save and ending. The expected scene
art and Indonesian text rendered; the ending displayed `TAMAT`. Choice buttons
covered the heroine's face in this baseline, which the final UI revision moves
lower. Desktop captures were 1739×978 pixels on a 1920×1080 virtual canvas and
are not Android readability evidence.

## Harness correction

Ren'Py 8.5.3 queues a test `click` before processing its input. Immediately using
`skip fast until screen "choice"` could therefore match the choice that had
just been clicked. Waiting for that choice screen to close fixes the harness
race. The old 60-second testcase limit also interrupted complete-route tests;
the suite now allows 420 seconds per case and bounded waits for interactions.

The test harness now excludes `game/saves`, which Ren'Py normally includes even
when `--savedir` is given. A fresh-slot check diagnosed Ren'Py's one-second
background screenshot timeout under software GL. This remains an optional
diagnostic, not an accepted ordinary-device autosave result. No custom product
save system is introduced.

Earlier failed reports in `/workspace/downloads/madoromi-tests/native.log`
precede those corrections and do not describe the recorded passing baseline.
The native report's final `Status: PASSED` is required; a process exit of zero
alone is not accepted as test evidence.

See [tests/README.md](../tests/README.md) for reproduction and coverage scope.
