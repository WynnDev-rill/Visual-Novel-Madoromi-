#!/usr/bin/env bash
# Pinned Ren'Py builds. Toolchains, downloads and signing material stay outside Git.
set -euo pipefail
ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
if [[ -d /workspace/toolchains ]]; then
    DEFAULT_TOOLCHAINS=/workspace/toolchains
else
    DEFAULT_TOOLCHAINS="${XDG_CACHE_HOME:-$HOME/.cache}/madoromi/toolchains"
fi
TOOLCHAINS=${MADOROMI_TOOLCHAINS:-$DEFAULT_TOOLCHAINS}
VERSION=8.5.3
RENPY_SDK=${RENPY_SDK:-$TOOLCHAINS/renpy-$VERSION-sdk}
ANDROID_SDK_ROOT=${ANDROID_SDK_ROOT:-$TOOLCHAINS/android-sdk}
JAVA_HOME=${MADOROMI_JAVA_HOME:-$TOOLCHAINS/jdk-21}
GRADLE_USER_HOME=${GRADLE_USER_HOME:-$TOOLCHAINS/gradle-cache}
OUT=${MADOROMI_DIST:-$ROOT/dist}
export JAVA_HOME ANDROID_SDK_ROOT GRADLE_USER_HOME
export SDL_AUDIODRIVER=${SDL_AUDIODRIVER:-dummy}

download() {
    local url=$1 file=$2 checksum=$3
    mkdir -p -- "$(dirname -- "$file")"
    if [[ ! -f $file ]]; then
        curl --fail --location --retry 3 --output "$file.part" "$url"
        mv -- "$file.part" "$file"
    fi
    printf '%s  %s\n' "$checksum" "$file" | sha256sum --check --status || {
        echo "Checksum mismatch: $file" >&2; exit 1;
    }
}

bootstrap() {
    local downloads=$TOOLCHAINS/downloads
    download "https://www.renpy.org/dl/$VERSION/renpy-$VERSION-sdk.tar.bz2" \
        "$downloads/renpy-$VERSION-sdk.tar.bz2" \
        eb0a9be7f0fb13632fe25ceade9a8bed5a1b4d6b6e83bd19eeeb29e1a1bb4a45
    [[ -x $RENPY_SDK/renpy.sh ]] || tar -xjf "$downloads/renpy-$VERSION-sdk.tar.bz2" -C "$TOOLCHAINS"
    download "https://www.renpy.org/dl/$VERSION/renpy-$VERSION-rapt.zip" \
        "$downloads/renpy-$VERSION-rapt.zip" \
        8a12be34a2f5238d125ff6dd76a56772fd8e44838af864f81bca82c1059b00e6
    [[ -d $RENPY_SDK/rapt ]] || unzip -q "$downloads/renpy-$VERSION-rapt.zip" -d "$RENPY_SDK"
    "$RENPY_SDK/renpy.sh" --version
}

java_network() {
    # Java does not read HTTPS_PROXY itself. Preserve the environment's proxy route.
    local truststore=${MADOROMI_JAVA_TRUSTSTORE:-/etc/ssl/certs/java/cacerts}
    if [[ -f $truststore ]]; then
        export JAVA_TOOL_OPTIONS="${JAVA_TOOL_OPTIONS:-} -Djavax.net.ssl.trustStore=$truststore"
    fi
    local proxy_options
    proxy_options=$(python3 - <<'PY'
import os
from urllib.parse import urlsplit
p = urlsplit(os.environ.get('HTTPS_PROXY', os.environ.get('https_proxy', '')))
if p.hostname:
    port = p.port or 8080
    print(f'-Dhttps.proxyHost={p.hostname} -Dhttps.proxyPort={port} '
          f'-Dhttp.proxyHost={p.hostname} -Dhttp.proxyPort={port} '
          '-Dhttp.nonProxyHosts=localhost|127.*|[::1]')
PY
)
    export JAVA_TOOL_OPTIONS="${JAVA_TOOL_OPTIONS:-} $proxy_options"
}

bootstrap_android() {
    bootstrap
    local downloads=$TOOLCHAINS/downloads
    download 'https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.13%2B9/OpenJDK21U-jdk_x64_linux_hotspot_21.0.13_9.tar.gz' \
        "$downloads/jdk21.tar.gz" \
        d7f5d5cf865a2902b70ff549b97586a7d3f234e016f041ab447ea740c7d66d1c
    if [[ ! -x $JAVA_HOME/bin/javac ]]; then
        mkdir -p "$JAVA_HOME"
        tar -xzf "$downloads/jdk21.tar.gz" -C "$JAVA_HOME" --strip-components=1
    fi
    download 'https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip' \
        "$downloads/android-commandlinetools-11076708.zip" \
        2d2d50857e4eb553af5a6dc3ad507a17adf43d115264b1afc116f95c92e5e258
    if [[ ! -d $ANDROID_SDK_ROOT/cmdline-tools/12.0 ]]; then
        mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools"
        unzip -q "$downloads/android-commandlinetools-11076708.zip" -d "$ANDROID_SDK_ROOT/cmdline-tools"
        mv "$ANDROID_SDK_ROOT/cmdline-tools/cmdline-tools" "$ANDROID_SDK_ROOT/cmdline-tools/12.0"
    fi
    ln -sfn 12.0 "$ANDROID_SDK_ROOT/cmdline-tools/latest"
    java_network
    # Invoking bootstrap-android accepts Google's SDK licenses for this local build.
    local sdk_status
    set +o pipefail
    yes | "$ANDROID_SDK_ROOT/cmdline-tools/12.0/bin/sdkmanager" \
        --sdk_root="$ANDROID_SDK_ROOT" 'platform-tools' 'platforms;android-36' 'build-tools;35.0.0'
    sdk_status=${PIPESTATUS[1]}
    set -o pipefail
    return "$sdk_status"
}

require_engine() {
    [[ -x $RENPY_SDK/renpy.sh ]] || { echo 'Run tools/build.sh bootstrap first.' >&2; exit 1; }
    mkdir -p "$OUT"
}

lint() {
    require_engine
    python3 "$ROOT/tests/check_assets.py"
    "$RENPY_SDK/renpy.sh" "$ROOT" lint --error-code
}

signing() {
    local signing_dir=${MADOROMI_SIGNING_DIR:-$TOOLCHAINS/signing}
    export MADOROMI_KEYSTORE=${MADOROMI_KEYSTORE:-$signing_dir/madoromi-release.jks}
    export MADOROMI_KEY_PASSWORD_FILE=${MADOROMI_KEY_PASSWORD_FILE:-$signing_dir/password}
    export MADOROMI_KEY_ALIAS=${MADOROMI_KEY_ALIAS:-madoromi}
    mkdir -p "$signing_dir"
    chmod 700 "$signing_dir"
    if [[ ! -f $MADOROMI_KEYSTORE ]]; then
        umask 077
        python3 - <<'PY'
import os, secrets
from pathlib import Path
p = Path(os.environ['MADOROMI_KEY_PASSWORD_FILE'])
if not p.exists():
    p.write_text(secrets.token_urlsafe(36) + '\n')
PY
        "$JAVA_HOME/bin/keytool" -genkeypair -noprompt -alias "$MADOROMI_KEY_ALIAS" \
            -keyalg RSA -keysize 3072 -validity 14600 \
            -dname 'CN=WynnDev Madoromi, O=WynnDev' \
            -keystore "$MADOROMI_KEYSTORE" -storepass:file "$MADOROMI_KEY_PASSWORD_FILE"
    fi
    [[ -f $MADOROMI_KEY_PASSWORD_FILE ]] || { echo 'Missing signing password file.' >&2; exit 1; }
    # RAPT normally copies keys from the project. android.json disables that;
    # configure its external Gradle project instead.
    [[ -d $RENPY_SDK/rapt/project ]] || cp -a "$RENPY_SDK/rapt/prototype" "$RENPY_SDK/rapt/project"
    export RENPY_SDK ANDROID_SDK_ROOT
    python3 - <<'PY'
import os
from pathlib import Path
rapt = Path(os.environ['RENPY_SDK']) / 'rapt'
key = Path(os.environ['MADOROMI_KEYSTORE']).resolve()
password = Path(os.environ['MADOROMI_KEY_PASSWORD_FILE']).read_text().strip()
def prop(value):
    return str(value).replace('\\', '\\\\').replace(':', '\\:').replace('=', '\\=')
properties = {
    'sdk.dir': os.environ['ANDROID_SDK_ROOT'], 'key.store': key,
    'key.alias': os.environ['MADOROMI_KEY_ALIAS'],
    'key.store.password': password, 'key.alias.password': password,
}
(rapt / 'sdk.txt').write_text(os.environ['ANDROID_SDK_ROOT'] + '\n')
for name in ('local.properties', 'bundle.properties'):
    p = rapt / 'project' / name
    p.write_text(''.join(f'{k}={prop(v)}\n' for k, v in properties.items()))
    p.chmod(0o600)
p = rapt / 'project' / 'gradle.properties'
text = p.read_text()
if 'org.gradle.workers.max=' not in text:
    p.write_text(text + '\norg.gradle.workers.max=2\n')
PY
}

archive_visuals() {
    # Use Ren'Py's own Archive class for desktop distributions. Android uses
    # RAPT's native image assets inside the signed APK instead.
    python3 - "$RENPY_SDK" "$ROOT" <<'PY'
import sys, textwrap
from pathlib import Path
sdk, root = map(Path, sys.argv[1:])
source = (sdk / 'launcher/game/archiver.rpy').read_text(encoding='utf-8-sig')
body = source.split('init python in archiver:', 1)[1]
namespace = {'_dict': dict, '_list': list}
exec(compile(textwrap.dedent(body), str(sdk / 'launcher/game/archiver.rpy'), 'exec'), namespace)
target = root / 'game/visuals.rpa'
temporary = target.with_suffix('.rpa.part')
archive = namespace['Archive'](str(temporary))
images = root / 'game/images'
files = sorted(p for p in images.rglob('*') if p.is_file())
if not files:
    raise SystemExit('No runtime visuals: restore the committed game/images/originals assets.')
for path in files:
    archive.add(path.relative_to(root / 'game').as_posix(), str(path))
archive.close()
temporary.replace(target)
print(f'Archived {len(files)} runtime visual files with the native Ren\'Py archiver.')
PY
    export MADOROMI_PREARCHIVED=1
}

desktop() {
    lint
    archive_visuals
    "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" distribute "$ROOT" \
        --package pc --destination "$OUT" --no-update
}

android() {
    # RAPT's native asset loader reads images directly from the signed APK.
    # Desktop RPA archives are intentionally excluded on Android.
    export MADOROMI_NATIVE_ANDROID=1
    lint
    [[ -x $JAVA_HOME/bin/javac && -x $ANDROID_SDK_ROOT/build-tools/35.0.0/apksigner ]] || {
        echo 'Run tools/build.sh bootstrap-android first.' >&2; exit 1;
    }
    java_network
    signing
    # Ren'Py can suppress an exception while copying its build result. Use an
    # empty destination so a failed copy cannot silently reuse an older APK.
    local staging
    staging=$(mktemp -d "$OUT/.android-build.XXXXXX")
    "$RENPY_SDK/renpy.sh" "$RENPY_SDK/launcher" android_build "$ROOT" --destination "$staging"
    python3 - "$staging" "$OUT" <<'PY'
import shutil, sys
from pathlib import Path
from zipfile import ZipFile
staging, out = map(Path, sys.argv[1:])
apks = list(staging.glob('id.wynndev.madoromi-*-release.apk'))
if not apks:
    raise SystemExit('Android build did not produce a new release APK.')
apk = max(apks, key=lambda p: p.stat().st_mtime)
target = out / 'Madoromi-1.0.0-android.apk'
with ZipFile(apk) as z:
    names = z.namelist()
    if 'assets/x-game/x-visuals.rpa' in names:
        raise SystemExit('Android assets unexpectedly contain a desktop RPA archive.')
    if not any(n.startswith('assets/x-game/x-images/') and n.endswith('.webp') for n in names):
        raise SystemExit('APK is missing the native Android game images.')
shutil.copy2(apk, out / apk.name)
shutil.copy2(apk, target)
shutil.rmtree(staging)
PY
    "$ANDROID_SDK_ROOT/build-tools/35.0.0/apksigner" verify --verbose --print-certs \
        "$OUT/Madoromi-1.0.0-android.apk" > "$OUT/android-signature.txt"
    "$ANDROID_SDK_ROOT/build-tools/35.0.0/aapt" dump badging \
        "$OUT/Madoromi-1.0.0-android.apk" > "$OUT/android-metadata.txt"
    (cd "$OUT" && sha256sum Madoromi-1.0.0-android.apk > Madoromi-1.0.0-android.apk.sha256)
    echo "Verified signed APK: $OUT/Madoromi-1.0.0-android.apk"
}

test_game() {
    require_engine
    local savedir
    savedir=$(mktemp -d "$TOOLCHAINS/test-saves.XXXXXX")
    "$RENPY_SDK/renpy.sh" --savedir "$savedir" "$ROOT" test "$@" 2>&1 | tee "$OUT/test-report.log"
    # Ren'Py teardown can mask a failed testcase with exit code zero.
    python3 - "$OUT/test-report.log" <<'PY'
import re, sys
from pathlib import Path
text = Path(sys.argv[1]).read_text(errors='replace')
text = re.sub(r'\x1b\[[0-9;]*m', '', text)
statuses = re.findall(r'\[rpytest\]\s+Status:\s+(\w+)', text)
if not statuses or statuses[-1] != 'PASSED':
    raise SystemExit('Ren\'Py test report did not finish with Status: PASSED.')
PY
}

case ${1:-lint} in
    bootstrap) bootstrap ;;
    bootstrap-android) bootstrap_android ;;
    lint) lint ;;
    desktop) desktop ;;
    android) android ;;
    archive) require_engine; archive_visuals ;;
    all) desktop; android ;;
    run) require_engine; exec "$RENPY_SDK/renpy.sh" "$ROOT" ;;
    test) shift; test_game "$@" ;;
    *) echo 'Usage: tools/build.sh {bootstrap|bootstrap-android|lint|desktop|android|archive|all|run|test}' >&2; exit 2 ;;
esac
