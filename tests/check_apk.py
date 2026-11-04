#!/usr/bin/env python3
"""Check the newly built APK against actual source assets and native ABIs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess
from zipfile import ZipFile, ZIP_STORED, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("apk", nargs="?", type=Path, default=ROOT / "dist/Madoromi-1.0.0-android.apk")
p.add_argument("--sdk", type=Path, default=Path(os.environ.get("ANDROID_SDK_ROOT", "/workspace/toolchains/android-sdk")))
p.add_argument("--report", type=Path, default=ROOT / "tests/artifacts/android-build.json")
args = p.parse_args()
signer = args.sdk / "build-tools/35.0.0/apksigner"
signature = subprocess.check_output([str(signer), "verify", "--verbose", "--print-certs", str(args.apk)], text=True)
assert "Verified using v2 scheme (APK Signature Scheme v2): true" in signature
cert = re.search(r"Signer #1 certificate SHA-256 digest: (\w+)", signature).group(1)
subprocess.run([str(args.sdk / "build-tools/35.0.0/zipalign"), "-c", "-P", "16", "4", str(args.apk)], check=True, stdout=subprocess.DEVNULL)
manifest_xml = subprocess.check_output([str(args.sdk / "build-tools/35.0.0/aapt"), "dump", "xmltree", str(args.apk), "AndroidManifest.xml"], text=True)
extracts_native = bool(re.search(r"android:extractNativeLibs.*0xffffffff", manifest_xml))
counts, missing, mismatches, unwanted, native = {}, [], [], [], {}
alignments = []
compressed_native = False
script_digests = []
with ZipFile(args.apk) as z:
    names = set(z.namelist())
    splash = ROOT / "android-presplash.jpg"
    if splash.exists():
        assert z.read("assets/android-presplash.jpg") == splash.read_bytes(), "Startup branding mismatch"
    # Ren'Py's compiled distribution may be normalized, so full RPYC bytes
    # differ from development copies. The engine stores its source digest in
    # the last16bytes (script.py: write_rpyc_md5), using this pinned SDK magic.
    for source in sorted((ROOT / "game").glob("*.rpy")):
        if source.name.startswith("test"):
            continue
        internal = "assets/x-game/x-" + source.with_suffix(".rpyc").name
        expected_digest = hashlib.md5(source.read_bytes() + b"_2025-07-06").digest()
        assert z.read(internal)[-16:] == expected_digest, "Stale compiled script: " + source.name
        script_digests.append(source.relative_to(ROOT).as_posix())
    for category in ("images", "audio", "fonts", "gui"):
        sources = sorted(f for f in (ROOT / "game" / category).rglob("*") if f.is_file())
        counts[category] = len(sources)
        expected = set()
        for path in sources:
            internal = "assets/" + "/".join("x-" + part for part in path.relative_to(ROOT).parts)
            expected.add(internal)
            if internal not in names:
                missing.append(path.relative_to(ROOT).as_posix())
            elif hashlib.sha256(z.read(internal)).digest() != hashlib.sha256(path.read_bytes()).digest():
                mismatches.append(path.relative_to(ROOT).as_posix())
        actual = {n for n in names if n.startswith("assets/x-game/x-" + category + "/") and not n.endswith("/")}
        unwanted.extend(sorted(actual - expected))
    for name in names:
        if any(token in name for token in ("x-testcases", "x-tests/", "x-tools/", "x-docs/", "x-.agents/", "x-visuals.rpa", ".keystore", ".jks")):
            unwanted.append(name)
        if name.startswith("lib/") and name.endswith(".so"):
            abi = name.split("/")[1]
            native[abi] = native.get(abi, 0) + 1
            data = z.read(name)
            assert data[:4] == b"\x7fELF", name
            if data[4] == 2:
                assert data[5] == 1, "Expected little-endian ELF"
                offset = struct.unpack_from("<Q", data, 32)[0]
                entry_size, count = struct.unpack_from("<HH", data, 54)
                for i in range(count):
                    entry = offset + i * entry_size
                    if struct.unpack_from("<I", data, entry)[0] == 1:
                        alignments.append(struct.unpack_from("<Q", data, entry + 48)[0])
                compression = z.getinfo(name).compress_type
                assert compression in (ZIP_STORED, ZIP_DEFLATED), name
                if compression == ZIP_DEFLATED:
                    # RAPT uses Android's native extraction for its legacy
                    # minimum API. ZIP offsets do not govern extracted ELF
                    # loads; their program-header alignment still must be16KB.
                    assert extracts_native, "Compressed native libraries require extraction"
                    compressed_native = True
    assert native == {"arm64-v8a": 1, "armeabi-v7a": 1, "x86_64": 1}, native
    assert min(alignments) >= 16384, alignments
metadata = subprocess.check_output([str(args.sdk / "build-tools/35.0.0/aapt"), "dump", "badging", str(args.apk)], text=True)
assert "package: name='id.wynndev.madoromi'" in metadata
assert "sdkVersion:'21'" in metadata and "targetSdkVersion:'36'" in metadata
network = "android.permission.INTERNET" in metadata
assert not network
assert counts["images"] == 33 and counts["audio"] == 10 and counts["fonts"] == 4, counts
assert not (missing or mismatches or unwanted), (missing, mismatches, unwanted)
report = {"apk": "dist/" + args.apk.name, "bytes": args.apk.stat().st_size, "sha256": hashlib.sha256(args.apk.read_bytes()).hexdigest(), "verified_source_asset_counts": counts, "asset_hash_mismatches": mismatches, "missing_assets": missing, "unwanted_build_or_test_files": unwanted, "native_library_counts": native, "native_libraries_compressed": compressed_native, "extract_native_libraries": extracts_native, "zip_alignment_verified": True, "minimum_64bit_ELF_load_alignment": min(alignments), "certificate_sha256": cert, "network_permission": network, "signature_verified": True}
args.report.parent.mkdir(parents=True, exist_ok=True)
report["compiled_script_source_digests_verified"] = script_digests
args.report.write_text(json.dumps(report, indent=2) + "\n")
print("PASS: APK signature, exact asset hashes/inventory, ABIs, 16KB alignment, API21–36 and offline permission profile.")
print("SHA-256:", report["sha256"])
