# Production progress

## 2026-11-04 — approximately 99%

This is a milestone estimate, not a measured quality score. The complete game and signed Android package are delivered; direct validation on the user's POCO F6/Android 16 remains outstanding. No physical-phone result is claimed.

The three-act, twelve-scene romance and epilogue are complete. The haowjy script audit preserves the original story and all five choices. Production uses the user's canonical cast with facial expressions, body gestures and a coordinated jeans costume, ten coherent backgrounds, an ATRI-inspired azure/white interface, licensed instrumental music, ambience and SFX without character voice acting. The supplied Drive icon is integrated. Graphify 0.9.102 is installed and connected to the development workflow.

Native regression: 13 executed cases, 85 assertions, zero skipped; both contrasting complete routes and all later callbacks pass. Required choice autosave creates a fresh checkpoint and restores the earlier decision. Independent motion-enabled acting and menu captures are retained. The latest build uses native blocking saves at five choices and project-specific Android loading art.

Final APK: 80,646,930 bytes, SHA-256 `3b8795e5e47def3ffaa2870f3a3791011b2a97c1f29e21699c34f773b8ad09b4`. Signature, source asset hashes, nine compiled-script source digests, API21–36 metadata, three ABIs, ARM64 16KB ELF alignment and offline permissions pass. On the API21 software-emulated Android device, ordinary touch reached the first choice, created a fresh native autosave, restored it after a different answer, and retained the choice across Home/resume. This is not a performance or compatibility guarantee for physical Android16 hardware. Earlier input-injection ANR evidence remains documented separately.

PC bundle: 71,002,834 bytes; ZIP CRC and all33 archived production image hashes pass. SDKs, signing keys and test harnesses are excluded from runtime packages.

## Delivered files and repository

The final APK replaced the earlier candidate at [the stable Drive link](https://drive.google.com/file/d/1DGm4kIdWkhHl9EjGE5-9FhVljB09Mq0i/view). [SHA256SUMS](https://drive.google.com/file/d/18TOzAYADdj1vZ2cgxE0luHXXwCa4-1Pu/view) was also updated. Both local packages remain in `dist/`.

GitHub release v1.0.0 is now published with the exact tested APK and its checksum as downloadable assets. Direct uploads from the workspace returned HTTP401; repository GitHub Actions successfully verified and uploaded the existing signed bytes, then published the draft (run41841323746). No rebuild or signing-key transfer was needed. The temporary delivery branch is removed after publication. Signing material remains private outside Git.

Remaining acceptance check: install the latest Drive APK on POCO F6/Android16 and confirm readable full-screen presentation, music, first-choice progression, native save/load and Home/resume. The task environment cannot perform this physical check remotely.
