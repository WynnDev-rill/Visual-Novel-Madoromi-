# Production verification — 4 November2026

Current signedAPK:80,646,930 bytes, SHA-256 `3b8795e5e47def3ffaa2870f3a3791011b2a97c1f29e21699c34f773b8ad09b4`.

| Check | Recorded result |
|---|---|
| Story contracts | PASS:12scenes,7540 narrative/menu words, five binary choices; source beats retained. |
| Native functional suite | PASS:13 executed cases,85 assertions,301.024 seconds; zero skipped. |
| Complete story paths | PASS:`00000` and`11111`; every option and all five later callbacks verified. All32combined paths were not executed. |
| Native persistence/UI | PASS:manualsave/load, rollback, phone history/no duplication, automaticreading, skip, settings, menus, confirmationcancel and authored actor poses. |
| Motion-enabled acting | PASS:one focusedcase,6assertions;42.873seconds; actual desktop screen recording retained. This is not physical Android frame-rate evidence. |
| Final menu/heading check | PASS:five focusedcases,6assertions;19.716seconds. |
| Visual review | Actual1280×720 captures inspected for title, dialogue, gestures, pairedactors, choices, phone, save/load, backlog, settings, gift, casualcostume andending. Twelve compressed own-game captures are in docs/screenshots/final. |
| Production artwork | PASS:exact33image inventory, source/outputhashes, dimensions and alpha. No earlier character/background pack is included in this selection. |
| SignedAPK | PASS:signature, exact33image/10audio/4font/59GUI hashes, API21–36 metadata, threeABIs,16KB64bitELF alignment and no INTERNET permission. |
| Android install/render | PASS:current APK installed; canonicaltitle/newphone rendered on preserved API21x86_64 softwaredevice. Product AudioTrack selector worked without externalwrapper ordebug-app setting. |
| Android lifecycle/autosave | Fresh native Android choice autosave, restoration and background/resume PASS: advanced with the second answer, then loaded the earlier choice. Standard touch replay reached the choice without ANR. Earlier injected-input ANR and reduced-resolution diagnostics remain separately recorded. See ANDROID_VERIFICATION.md. |
| Desktop bundle | PASS:71,002,834bytes; ZIPCRC and all33nativeRPA image hashes match sources; projecttests/tools excluded. |
| Graphify | Real0.9.102build/cluster/export/query, citedpath traversal, freshness guard and browserviewer exercised. Ren’Py uses the documented projectadapter; this is not upstreamnative.rpy support. |

Exact logs and routes: tests/artifacts/native-production.log, native-motion.log, native-heading-check.log and native-paths.json. APK audit: tests/artifacts/android-build.json. Desktop audit: tests/artifacts/desktop-build.json. Source verification commands are in tests/README.md and docs/BUILD.md.

Choice autosave is now required regression coverage. A new native slot was created, another answer was selected, and loading restored the earlier decision. The game uses the documented blocking native save mode at five choice boundaries, avoiding the one-second background screenshot deadline. The Android build also created a fresh173,842-byte auto-1-LT1.save at the first choice; CRC validation passed. Detailed Android restore checks are recorded separately.

The Android environment has noKVM and usesTCG/softwareGL. First native interface startup took47.6seconds after installation on that environment. This does not establish startup time, smoothness, audio quality or compatibility on physical phones. No physical-device test is claimed.

Earlier baseline commits/reports predate the canonical cast, haowjy prose polish, final jeans and azure interface. Their results are historical evidence rather than proof of this revision.

The latest APK and SHA256SUMS were uploaded in place to the user's Drive. Returned Drive metadata confirms the expected filename and80,646,930-byte size. GitHub's binary-upload endpoint returned HTTP401; the empty draft release was not published. Source pushes remain available.
