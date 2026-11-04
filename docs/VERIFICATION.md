# Production verification — 4 November2026

Current signedAPK:80,009,790bytes, SHA-256 `2e5c03f925a188249a1aed87992241be00c7fc1447f88cb667b3fba0dc8f0253`.

| Check | Recorded result |
|---|---|
| Story contracts | PASS:12scenes,7540 narrative/menu words, five binary choices; source beats retained. |
| Native functional suite | PASS:12executed cases,79assertions,185.281seconds; one optional software-GL autosave diagnostic skipped. |
| Complete story paths | PASS:`00000` and`11111`; every option and all five later callbacks verified. All32combined paths were not executed. |
| Native persistence/UI | PASS:manualsave/load, rollback, phone history/no duplication, automaticreading, skip, settings, menus, confirmationcancel and authored actor poses. |
| Motion-enabled acting | PASS:one focusedcase,6assertions;42.873seconds; actual desktop screen recording retained. This is not physical Android frame-rate evidence. |
| Final menu/heading check | PASS:five focusedcases,6assertions;19.716seconds. |
| Visual review | Actual1280×720 captures inspected for title, dialogue, gestures, pairedactors, choices, phone, save/load, backlog, settings, gift, casualcostume andending. Twelve compressed own-game captures are in docs/screenshots/final. |
| Production artwork | PASS:exact33image inventory, source/outputhashes, dimensions and alpha. No earlier character/background pack is included in this selection. |
| SignedAPK | PASS:signature, exact33image/10audio/4font/59GUI hashes, API21–36 metadata, threeABIs,16KB64bitELF alignment and no INTERNET permission. |
| Android install/render | PASS:current APK installed; canonicaltitle/newphone rendered on preserved API21x86_64 softwaredevice. Product AudioTrack selector worked without externalwrapper ordebug-app setting. |
| Android lifecycle/autosave | BLOCKED: later Android API21 software-emulator ANR during chat; final save/load, resume and fresh autosave remain unverified. Baseline results do not substitute. See ANDROID_VERIFICATION.md. |
| Desktop bundle | PASS:71,001,940bytes; ZIPCRC and all33nativeRPA image hashes match sources; projecttests/tools excluded. |
| Graphify | Real0.9.102build/cluster/export/query, citedpath traversal, freshness guard and browserviewer exercised. Ren’Py uses the documented projectadapter; this is not upstreamnative.rpy support. |

Exact logs and routes: tests/artifacts/native-production.log, native-motion.log, native-heading-check.log and native-paths.json. APK audit: tests/artifacts/android-build.json. Desktop audit: tests/artifacts/desktop-build.json. Source verification commands are in tests/README.md and docs/BUILD.md.

The optional headless autosave test is affected by Ren’Py’s one-second background screenshot deadline under software rendering. Selecting a suite explicitly also enables its disabled children; normal regression uses the global suite so the optional diagnostic remains separate. Final Android autosave must be reported from actual ordinary play.

The Android environment has noKVM and usesTCG/softwareGL. First native interface startup took47.6seconds after installation on that environment. This does not establish startup time, smoothness, audio quality or compatibility on physical phones. No physical-device test is claimed.

Earlier baseline commits/reports predate the canonical cast, haowjy prose polish, final jeans and azure interface. Their results are historical evidence rather than proof of this revision.
