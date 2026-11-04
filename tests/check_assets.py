#!/usr/bin/env python3
"""Validate the actual committed art inventory before lint/packaging."""
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/licenses/production-art.json").read_text())
assert manifest["complete"], "Production art is still incomplete"
assets = manifest["assets"]
assert len(assets) == manifest["expected_count"] == 33
expected = {a["runtime_path"] for a in assets}
actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "game/images").rglob("*") if p.is_file()}
assert actual == expected, f"Unregistered/missing images: {actual ^ expected}"
for item in assets:
    path = ROOT / item["runtime_path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["runtime_sha256"], f"Hash changed: {path}"
    with Image.open(path) as im:
        assert list(im.size) == item["runtime_size"], f"Unexpected dimensions: {path}"
        if item["alpha_required"]:
            assert im.mode == "RGBA", f"Missing transparency: {path}"
            assert im.getchannel("A").getextrema()[0] == 0, f"Opaque portrait canvas: {path}"
            assert im.getchannel("A").getextrema()[1] >= 250, f"Faded portrait: {path}"
        im.verify()
print(f"PASS: {len(assets)} production images, hashes, dimensions, transparency, exact runtime inventory.")
