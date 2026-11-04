# Production progress

## 2026-11-04 — approximately95%

This is a milestone estimate, not elapsed time or a measured quality score.
The complete12-scene story has received a haowjy full-script audit and targeted polish. The latest production uses all four canonical user character designs, six Aoi facial states, three body poses, a matching women's-jeans epilogue costume, Mio/Sora expressions and gestures, ten coherent 2D backgrounds and a story-specific gift insert.

The azure/white ATRI-inspired UI has passed actual screenshot review. Native regression passed12 executed cases/79 assertions with both contrasting complete paths and all later callbacks; one optional software-GL autosave diagnostic was skipped. Separate motion-enabled acting and final menu captures passed. Graphify0.9.102 is installed; its real build/query/export pipeline, Ren'Py adapter, stale-input guard and browser viewer have been exercised.

The current signedAPK is80,009,790bytes, SHA-256 `2e5c03f925a188249a1aed87992241be00c7fc1447f88cb667b3fba0dc8f0253`. Signature, exact33image/10audio/4font/59GUI hashes, ABIs,16KBELF alignment, SDK metadata and offline permissions pass. It is installed on the software Android device; ordinary final-game play/state checks are still underway without the diagnostic audio wrapper. Desktop packaging and final tested commit/release publication remain. Progress reaches100% only when those stated deliverables are complete.

## Resume checkpoint

Implementation/asset/UI milestone committed as `ab483c2`; clean GitHub Actions passed. Android ANR evidence committed as `f398044`. Release remains a draft with no uploaded assets: GitHub asset upload host returned HTTP401 even though source pushes/API identity requests succeeded. The verified local APK and PC ZIP remain in `dist/` with SHA256SUMS.txt. Do not describe this as a fully verified final Android release.

Next: isolate the final APK chat ANR on Android API21 TCG; verify ordinary final-build save/load, resume and fresh autosave. Existing desktop source/visual tests must not be repeated unnecessarily. Diagnostic AVD currently uses800×450 override and debug.checkjni=0; both are environment diagnostics, not product changes. Restore1280×720 for target-profile screenshot checks. Raw ANR trace: `/workspace/downloads/madoromi-final-anr.txt`. User was asked for target phone model/Android version. Repair GitHub release-upload authorization before publishing assets; do not publish the empty draft as final.
