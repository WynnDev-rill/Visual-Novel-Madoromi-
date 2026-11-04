# Android runtime evidence by revision

Files01–09 and initial launch/audio metadata belong to the earlier candidate identified by `../android-build-candidate1.json`. They retain the input-injection ANR; do not treat them as proof that the latest revision passed every check.

Files10–12 and low-resolution diagnostic metadata record800×450 save and Home/resume checks. Files13–15 record the later standard-touch replay/save UI before the blocking-checkpoint rebuild. Their associated save listings retain native file evidence.

Files17 onward belong to APK SHA-256 `3b8795e5e47def3ffaa2870f3a3791011b2a97c1f29e21699c34f773b8ad09b4` at1280×720 on API21 x86_64 TCG:

- 17: fresh first choice; native-choice-autosave.json records a new CRC-valid173,842-byte save.
- 18: progressed with the second answer to phone01.49.
- 19: transient cancelled title-exit confirmation while opening the menu; native quit-autosave rotated the choice checkpoint.
- 20–22: automatic slot selection, load confirmation, restored first choice. The original checkpoint is slot2 on the captured automatic page.
- 23–25: Home, early black resumed surface, then settled first-choice render. checkpoint-lifecycle.log establishes same-process background/foreground events. checkpoint-background-resume.json records scope and timing limitations.

No physical POCO F6/Android16 result is claimed. Device performance and sound quality cannot be inferred from this CPU/software-rendered AVD.
