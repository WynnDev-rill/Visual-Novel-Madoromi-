# Native verification

`check_story.py` checks source-story preservation and validates evidence from
Ren'Py. It does not simulate play or establish runtime coverage by itself.

Run native UI tests on a real display or under Xvfb, with a fresh save directory:

```sh
evidence=/tmp/madoromi-verification
mkdir -p "$evidence/screenshots" "$evidence/saves"
MADOROMI_TEST_COVERAGE="$evidence/native-paths.json" \
MADOROMI_TEST_SCREENSHOTS="$evidence/screenshots" \
renpy.sh /path/to/madoromi test madoromi \
  --savedir "$evidence/saves" --overwrite-screenshots \
  > "$evidence/native.log" 2>&1
python3 tests/check_story.py --coverage "$evidence/native-paths.json" \
  --coverage-mode choices --report "$evidence/native.log"
```

The normal suite completes the contrasting `00000` and `11111` routes. Those
paths exercise every decision option and every later callback. They do not
establish all 32 combinations. To run the entire combination matrix, set
`MADOROMI_TEST_FULL_MATRIX=1` and validate with `--coverage-mode matrix`.

The suite also checks phone history, manual save/load, rollback to an earlier
choice, automatic reading, skip stopping at choices,
settings and native menu destinations. Screenshots include cafeteria, lounge,
courtyard, history, save and ending screens. Save data and screenshots remain
outside the source tree by using the environment variables above.

For device screenshot QA, `MADOROMI_TEST_SCENE_SAVES=1` retains page 8 slots
1–4 at cafeteria, lounge, courtyard confession and the ending. Transfer only
to a QA installation built from the same source version; these slots and test
code are not included in release distributions.

`MADOROMI_TEST_SIZE=1280x720` renders smaller native captures for mobile-scale
layout review. This does not turn a desktop test into an Android runtime test.
`MADOROMI_TEST_AUTOSAVE_DEBUG=/tmp/autosave-debug.log` records otherwise swallowed
native background screenshot/save exceptions without changing their behavior.

The separate `choice_autosave` diagnostic is enabled with
`MADOROMI_TEST_REQUIRE_AUTOSAVE=1`. It deletes `auto-1` and requires a newly
created choice autosave. Ren'Py's one-second background screenshot deadline can
fail under software GL during automated skipping; that test is optional in the
headless suite and an ordinary-device autosave check is reported separately.

Check the report's final `Status: PASSED` and actual assertion counts. Ren'Py can
exit zero after a failed test when a teardown calls `exit`; process status alone
is insufficient. `tools/build.sh test` enforces the report status automatically.

The harness waits for a clicked choice to disappear before skipping to the next
one. In Ren'Py 8.5.3, `click` queues input and a following `until screen "choice"`
can otherwise match the previous interaction before that input is handled.

Desktop tests verify the native game logic and UI. APK signature/API checks and
Android launch/touch/readability verification are separate evidence.
