# Build MADOROMI

The game uses Ren'Py **8.5.3.26051504** and matching RAPT. The build helper pins the SDK and RAPT archives by SHA-256. It targets Android API 36, with minimum Android API 21 and OpenGL ES 3.0, and packages ARMv7, ARM64 and x86-64 runtimes. Linux/Windows distributions use Ren'Py's native `pc` package.

## Linux prerequisites

Use a 64-bit Linux machine with Bash, Python 3, `curl`, `tar`, `bzip2`, `unzip`, `sha256sum`, OpenGL/Mesa and normal Ren'Py SDL dependencies. On a headless machine use Xvfb for runtime tests. The cloud workspace uses `/workspace/toolchains`; elsewhere the default is `$XDG_CACHE_HOME/madoromi/toolchains` or `$HOME/.cache/madoromi/toolchains`. All SDKs, downloaded archives, Gradle caches and signing files stay outside the repository.

```bash
tools/build.sh bootstrap
python3 -m pip install Pillow
python3 tests/check_assets.py
tools/build.sh lint
tools/build.sh run
tools/build.sh test
tools/build.sh desktop
```

The production runtime illustrations are committed under `game/images/originals/`. They extend the user's canonical character concepts and use a coherent generated 2D environment family. A clean checkout does not need the earlier itch.io acquisition step or an image-generation service. `tests/check_assets.py` verifies the selected production files against their manifest and also runs before lint. Pillow is therefore required for development lint/packaging, not for playing the game. See `docs/licenses/visual-art.md` and `docs/licenses/production-art.json` for provenance and transformations. `tools/prepare_art.py` is the production-only full-canvas resize/conversion tool; ordinary builds use the committed WebPs.

`tools/acquire_visuals.py`, `visual-assets.json` and the creator-page evidence remain the historical baseline acquisition audit. They are not required for the current production selection; do not repopulate the old character/background directories into a final build.

Desktop distributions bundle game images in Ren'Py's visual archive, created with the pinned SDK's own `Archive` class. Android uses RAPT's native packaging: game images are assets inside the signed APK. RAPT disables RPA creation and its asset loader reads those images directly. Preserve this native packaging rather than adding a second extraction layer.

On a headless Linux host:

```bash
xvfb-run -a tools/build.sh test
```

The `test` command uses isolated saved data and requires the final native testcase report to say `Status: PASSED`. This check matters because Ren'Py teardown can otherwise return exit code zero after a failed testcase. Lint uses `--error-code`.

## Android APK

```bash
tools/build.sh bootstrap-android
tools/build.sh android
```

`bootstrap-android` downloads Temurin **21.0.13+9**, Android command-line tools **12.0 / 11076708**, SDK platform **36**, build tools **35.0.0** and platform tools. Running that command accepts the Android SDK licenses for the local build. RAPT pins Gradle **9.1.0** and Android Gradle Plugin **8.13.0**. The first Android build downloads their Maven dependencies.

The final APK is `dist/Madoromi-1.0.0-android.apk`. Each build uses an empty staging directory so a failed result copy cannot reuse an older APK. The build verifies its cryptographic signature and native image-asset packaging, writes `android-signature.txt`, records package/version/SDK/ABI/permission metadata in `android-metadata.txt`, and writes a SHA-256 sidecar. Ren'Py also leaves its original timestamped APK name in `dist/`. The helper sets `MADOROMI_NATIVE_ANDROID=1` during this build so desktop RPA files are excluded.

Install on a device with USB debugging enabled:

```bash
adb install -r dist/Madoromi-1.0.0-android.apk
adb shell am start -n id.wynndev.madoromi/org.renpy.android.PythonSDLActivity
```

Alternatively, copy the APK to the phone, open it and allow the file manager to install apps when Android prompts. The application plays offline without Android's `INTERNET` permission. Ren'Py's Android runtime also declares permissions including wake-lock, network-state access and legacy external storage; the complete list is in `android-metadata.txt`. Portrait phones rotate to landscape.

## Signing and environment overrides

The first Android build generates a release signing key under the external toolchain's `signing/` directory, with a randomly generated password file and restrictive permissions. **Back up that directory privately.** Rebuilding with the same key allows Android to update an existing installation; a different key requires uninstalling the old app. Keys and password files must never enter Git or a public release.

For an existing key, provide `MADOROMI_KEYSTORE`, `MADOROMI_KEY_PASSWORD_FILE` and optionally `MADOROMI_KEY_ALIAS` (default `madoromi`). The keystore and key must use the same password. The script never prints the password and writes signing properties only inside the external RAPT project.

Other supported overrides are `MADOROMI_TOOLCHAINS`, `RENPY_SDK`, `MADOROMI_JAVA_HOME`, `ANDROID_SDK_ROOT`, `GRADLE_USER_HOME`, `MADOROMI_DIST`, and `MADOROMI_SIGNING_DIR`. The helper sets `JAVA_HOME` to its pinned JDK unless `MADOROMI_JAVA_HOME` is supplied. Java downloads inherit the environment's HTTPS proxy route. On a managed host the helper uses `/etc/ssl/certs/java/cacerts` when available; override `MADOROMI_JAVA_TRUSTSTORE` if needed. TLS verification stays enabled.

The GitHub Actions workflow checks lint, runs native testcases and builds the desktop archive. Its manual Android option builds an APK using an ephemeral CI key; release updates should be built with the retained private release key above.

## Engine proof and limits

Both engines compiled and ran the same small Indonesian dialogue/choice probe. Godot **4.6.3.stable.official.7d41c59c4** imported its scene and ran both choice callbacks. Ren'Py **8.5.3.26051504** passed lint and a real GUI testcase through history, save slot 1, a choice and loading slot 1. Its GL2 runtime uses Mesa llvmpipe under Xvfb in this workspace.

Ren'Py's SDK GUI already connects rollback, history, skip, auto, save/load and preferences to native engine actions. The Godot base scene needed custom controls/callbacks and did not provide those VN systems. Both are viable; Ren'Py fits this project with less custom game logic and no dialogue add-on. Probe logs are retained outside Git at `/workspace/toolchains/probes/` in the development workspace.

API/signature validation does not establish device runtime compatibility. See the verification report for the final game's actual testcase, screenshot and Android launch results. The cloud machine has no `/dev/kvm`; Android emulation, if used, runs through software CPU emulation.

## Final artifact and development graph checks

`python3 tests/check_apk.py` verifies the built release APK against exact current source asset hashes, native ABIs, signature,16KB alignment and API/permission metadata. It uses Android build-tools35.0.0 from `--sdk` or `ANDROID_SDK_ROOT`; see `tests/README.md` for native coverage.

Android selects SDL’s native `android` (Java AudioTrack) audio driver in `game/android_audio.rpy` before audio initialization. This avoids the OpenSLES mutex stall observed on the API21 software emulator without disabling music, ambience or SFX. Final testing must clear diagnostic `wrap.id.wynndev.madoromi` and debug-app overrides before launch.

Graphify is development-only. On a new machine, use `tools/knowledge_graph.sh setup`; after changing graph inputs use `tools/knowledge_graph.sh build` and `python3 tests/check_knowledge_graph.py`. CLI query/path/explain commands reject stale graph inputs. See [KNOWLEDGE_GRAPH.md](KNOWLEDGE_GRAPH.md).

## User target device

The user confirmed POCO F6 running Android16. The current APK targets API36 and includes arm64-v8a with16KB-aligned ELF load segments. These checks establish package requirements, not a physical POCO F6 gameplay test. API21 TCG ANR diagnostics must be distinguished from this modern ARM64 target.

## Automatic choice checkpoints

Five authored choice boundaries use the documented native `renpy.force_autosave(take_screenshot=True, block=True)` API. `config.autosave_on_choice=False` prevents a duplicate asynchronous request. The engine continues to own save format, slot rotation, rollback guards and restore behavior; no custom persistence format is used. This avoids the native background screenshot’s one-second deadline on slow software rendering. The required `choice_autosave` testcase proves a fresh slot restores the decision after a different answer was selected.
