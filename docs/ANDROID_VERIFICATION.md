# Android verification

## Earlier production candidate — 2026-11-04

The revised APK contains the 33 production images, the new system interface,
and the Android AudioTrack selector. Its identity is:

- APK: `dist/Madoromi-1.0.0-android.apk`; 80,009,790 bytes
- SHA-256: `2e5c03f925a188249a1aed87992241be00c7fc1447f88cb667b3fba0dc8f0253`
- Package: `id.wynndev.madoromi`; version name `1.0.0`; version code `1793774665`
- Runtime asset audit: 33 images, 10 audio files, 4 fonts and 59 GUI files;
  no missing files or source hash mismatches
- Signature and ZIP alignment verified; 16,384-byte minimum 64-bit ELF load
  alignment; compressed native libraries use Android's declared extraction
- No network permission; no test harness or build files packaged

The static audit for this earlier candidate is [`tests/artifacts/android-build-candidate1.json`](../tests/artifacts/android-build-candidate1.json).
Final runtime evidence is in [`tests/artifacts/android-final/`](../tests/artifacts/android-final/).

Installation initially exceeded the preserved 512 MiB guest data partition's
update staging space. Removing only the old application code with
`pm uninstall -k` and reinstalling succeeded while retaining saves and
preferences. No userdata was wiped. The external SDL wrapper property and
Android debug-app setting were cleared before launch. The packaged selector
opened SDL Java AudioTrack at 48 kHz, stereo float, with 2,229-frame buffers.

`am start -W` reached its wait timeout after 18.4 seconds; the software-emulated
app subsequently initialized its native interface at 47.6 seconds and rendered
the title. The launch timeout is retained in the evidence rather than counted
as a successful Android wait response. Actual screenshots establish rendering.
The installed-package snapshot was taken before this launch.

This earlier candidate reached chat 01.47; a later input-injection/relaunch session produced an Android ANR. Screenshot `09-anr-during-chat.png` and `anr-summary.txt` retain it. The trace places the main thread in Android InputConsumer and SDLThread within ART CheckJNI. The cause was not isolated, and no claim is made that AudioTrack alone fixed it. Subsequent standard-touch replay reached the choice without that ANR. Reduced-resolution save/resume diagnostics are historical evidence, separate from the current build below.

## Baseline build — 2026-11-04

This section describes the APK built on 2026-11-03, before the subsequent art
and narrative revision. It is baseline evidence, not verification of a later
release. Rebuild and repeat the runtime checks after the revision is frozen.

- Original APK filename: `Madoromi-1.0.0-android.apk` (the normalized `dist/`
  path is replaced by later builds; identify this baseline by the hash below)
- Size: 79,200,445 bytes
- SHA-256: `55f805e5ca6c3d344af0cba1acdee928be7f4b6857e41c2799b7031e45440490`
- Package: `id.wynndev.madoromi`; version name `1.0.0`; version code `1793730293`
- Minimum/target SDK: 21/36; landscape; ARMv7, ARM64 and x86-64 runtimes
- v1 and v2 signatures: verified; no `INTERNET` permission
- Runtime assets: 90 images, 10 audio files, 4 fonts and 59 GUI files; native
  Android packaging; no missing assets or hash mismatches in the build audit
- Minimum 64-bit ELF load alignment: 16,384 bytes

The machine-readable static audit is
[`tests/artifacts/android-baseline/build.json`](../tests/artifacts/android-baseline/build.json).
Static package checks do not establish runtime compatibility.

Runtime checks use the preserved API 21 x86-64 AVD at
1280×720, 240 dpi, OpenGL ES 3.0 with SwiftShader. This host lacks KVM, so
Android runs under software CPU emulation.

| Runtime check | Result | Evidence |
| --- | --- | --- |
| APK installation | PASS | Android package manager returned `Success`; installed version code/name match the APK. |
| Activity launch | PASS | `am start -W` returned `Status: ok`; game title screen rendered. |
| Title and first chapter | PASS | Actual 1280×720 captures `01-title.png`, `02-chapter.png`, `03-opening.png`. |
| Native audio output | PASS | Enabled WAV backend captured nonzero 44.1 kHz stereo PCM with game audio features unmuted; `audio.json`. |
| Phone presentation | PASS | First through fifth messages rendered; `05-phone-four.png`, `07-phone-five.png`. |
| Manual save/load | PASS with driver override | Native slot 1 created at message four, advanced to message five, then Muat → slot 1 → Ya restored exactly four messages; `manual-save.json`, `09-manual-restored-phone-four.png`. |
| Background/resume | PASS with driver override | Android Home and activity resume retained PID 2483 and exactly four phone messages; `background-resume.json`, `10-background-home.png`, `11-resumed-phone-four.png`. |
| Fresh choice autosave | NOT VERIFIED | Earlier QA autosaves were backed up and deleted through native Hapus controls. The first choice was reached, but no new automatic file appeared in this run. No stale slot is accepted as evidence. |

Captures and Android install/launch metadata are in
[`tests/artifacts/android-baseline/`](../tests/artifacts/android-baseline/).

The original default OpenSLES path stalled on this software-emulated API 21
device after partial play, including with enabled host audio. Later baseline
flow checks use the unchanged APK with the external launch environment
`SDL_AUDIODRIVER=android`, selecting SDL's bundled Java AudioTrack driver.
The test process environment confirmed the override; SDL opened two-channel
float output at 48 kHz with 2,229 frames. This does not establish a complete
default-configuration pass for the original APK. The final rebuilt APK must
be checked separately after removing the external wrapper/debug-app setting.

## Emulator recovery

The earlier emulator process was gone. Only its stale AVD lock files were
removed; signing material, Android userdata and the SD card were preserved.
The emulator's free-space check required reclaiming reproducible external RAPT
build intermediates and a hash-identical external APK copy. No source assets,
Maven downloads, APKs in `dist/` or save data were removed. A later Gradle build
regenerates those intermediates.

The API 21 guest's OpenSLES audio buffers timed out with `-no-audio`, eventually
stalling the app's input queue. Android also showed a system-process timeout
during one software-emulated boot. Enabled WAV output restored host audio flow,
but OpenSLES still stalled during later play. The AudioTrack diagnostic above
then completed manual restoration and Home/resume without that input stall.
Both changes preserve the game's normal audio channels; no mute or audio
feature removal was used.
The retained 12-second sample contains 154,949 nonzero PCM samples, RMS 393.628
and peak 6,926 on the signed 16-bit scale. This proves native audio output;
it does not establish physical-device speaker quality.

Use a persistent execution session for the emulator process:

```sh
QEMU_AUDIO_DRV=wav \
QEMU_WAV_PATH=/workspace/toolchains/android-baseline-emulator.wav \
ANDROID_AVD_HOME=/workspace/toolchains/avd \
ANDROID_SDK_ROOT=/workspace/toolchains/android-sdk \
/workspace/toolchains/android-sdk/emulator/emulator \
  -avd Madoromi_API21 -accel off -no-window -audio wav -no-boot-anim \
  -no-snapshot -gpu swiftshader_indirect -memory 1024 -partition-size 512 \
  -sdcard /workspace/toolchains/avd/Madoromi_API21.avd/sdcard.img
```

Never remove locks belonging to a live emulator or wipe userdata to resolve a
stale lock. The SDK, AVD and signing directory stay outside the repository.
The external WAV grows by about 10 MiB per minute while audio plays; its RIFF
lengths finalize when the emulator exits. Keep the emulator alive between
baseline and final-build checks, and stop it through `adb emu kill` when done.

For long-running QA in this workspace,
`python3 /workspace/toolchains/start-madoromi-emulator.py` starts the same AVD
in a detached session, checks the lock owner, and leaves active emulators
untouched. It uses the enabled WAV backend with `/dev/null` as output after
the bounded audio sample above was retained. An external silence WAV satisfies
the emulator's microphone input. This prevents recording growth while the
emulator waits for later builds; it changes no game files or mixer settings.

## Current native checkpoint revision

The build with SHA-256 `3b8795e5e47def3ffaa2870f3a3791011b2a97c1f29e21699c34f773b8ad09b4` is80,646,930bytes. It includes project-specific startup art and five native blocking choice checkpoints. After a fresh start, ordinary in-game preferences/Skip reached the first choice and created `auto-1-LT1.save` (173,842bytes); the archive CRC passed. No previous save was loaded before that checkpoint. The earlier ANR was recorded in an older build/input-injection session; its cause is not claimed isolated. Repeated standard touch reached the choice on1280×720 without that ANR. The user target is POCO F6/Android16, which has not been physically tested in this workspace.

The current APK then advanced with the second answer to phone 01.49, opened Muat → Otomatis, and loaded the original checkpoint through native confirmation. Screenshot `22-choice-restored.png` shows the first decision restored. The original checkpoint had rotated to slot2 after the native quit-autosave triggered during a cancelled title-exit prompt; this is recorded rather than misidentifying slot1. The desktop required regression separately asserts that the earlier story variable is restored.

Home/background/resume also returned to the same first choice. Both background and foreground native events came from PID6785 (`checkpoint-lifecycle.log`). The first15-second resumed capture was black while this software renderer recovered; `25-resumed-choice-settled.png` records the settled screen. This verifies retained state, not fast physical-device resume. The API21 guest lacks `pidof`; process identity is established by the native lifecycle log instead.
