#!/usr/bin/env python3
"""Check Ren'Py VN image references, dimensions, and sprite transparency."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None


IMAGE_DECL_RE = re.compile(
    r'^\s*image\s+[^=]+=\s*(?:Transform\()?["\']([^"\']+\.(?:png|jpg|jpeg|webp))["\']',
    re.IGNORECASE,
)

EXPECTED_UI_SIZES = {
    "title_bg.png": (1280, 720),
    "dialogue_box.png": (1160, 170),
    "choice_button_idle.png": (900, 58),
    "choice_button_hover.png": (900, 58),
    "status_panel.png": (760, 520),
    "status_button.png": (150, 48),
}


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def print(self) -> None:
        for message in self.errors:
            print(f"ERROR: {message}")
        for message in self.warnings:
            print(f"WARN: {message}")
        if not self.errors and not self.warnings:
            print("VN asset check passed with no warnings.")
        else:
            print(f"VN asset check finished: {len(self.errors)} error(s), {len(self.warnings)} warning(s).")


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def iter_image_declarations(game_dir: Path) -> list[tuple[Path, str]]:
    declarations: list[tuple[Path, str]] = []
    for rpy in sorted(game_dir.rglob("*.rpy")):
        for line in rpy.read_text(encoding="utf-8", errors="replace").splitlines():
            match = IMAGE_DECL_RE.search(line)
            if match:
                declarations.append((rpy, match.group(1)))
    return declarations


def has_alpha(img: Image.Image) -> bool:
    if img.mode in {"RGBA", "LA"}:
        return True
    return "transparency" in img.info


def has_some_transparency(img: Image.Image) -> bool:
    if not has_alpha(img):
        return False
    alpha = img.convert("RGBA").getchannel("A")
    lo, hi = alpha.getextrema()
    return lo < 255 and hi > 0


def looks_like_checkerboard(img: Image.Image) -> bool:
    small = img.convert("RGB").resize((64, 64))
    pixels = list(small.getdata())
    light = sum(1 for p in pixels if all(230 <= c <= 255 for c in p))
    gray = sum(1 for p in pixels if all(170 <= c <= 225 for c in p) and max(p) - min(p) < 12)
    total = len(pixels)
    return light / total > 0.18 and gray / total > 0.18


def check_dimensions(path: Path, root: Path, reporter: Reporter, strict: bool) -> None:
    if Image is None:
        reporter.warn("Pillow is not installed; skipped dimension and alpha checks.")
        return

    try:
        img = Image.open(path)
    except Exception as exc:
        reporter.error(f"{rel(path, root)} could not be opened: {exc}")
        return

    parts = path.parts
    name = path.name
    size = img.size

    expected: tuple[int, int] | None = None
    if "backgrounds" in parts or "cg" in parts:
        expected = (1280, 720)
    elif "ui" in parts and name in EXPECTED_UI_SIZES:
        expected = EXPECTED_UI_SIZES[name]

    if expected and size != expected:
        message = f"{rel(path, root)} is {size[0]}x{size[1]}, expected {expected[0]}x{expected[1]}"
        reporter.error(message) if strict else reporter.warn(message)

    if "characters" in parts:
        if not has_alpha(img):
            message = f"{rel(path, root)} has no alpha channel; character sprites should usually be transparent PNGs"
            reporter.error(message) if strict else reporter.warn(message)
        elif not has_some_transparency(img):
            message = f"{rel(path, root)} alpha is fully opaque; check for a baked background"
            reporter.error(message) if strict else reporter.warn(message)
        if looks_like_checkerboard(img):
            message = f"{rel(path, root)} looks like it may contain baked checkerboard transparency"
            reporter.error(message) if strict else reporter.warn(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, required=True, help="Ren'Py project directory containing game/.")
    parser.add_argument("--strict", action="store_true", help="Treat dimension and sprite warnings as errors.")
    args = parser.parse_args()

    project = args.project.resolve()
    game_dir = project / "game"
    reporter = Reporter()

    if not game_dir.exists():
        reporter.error(f"{project} does not contain a game/ directory")
        reporter.print()
        return 1

    declared_paths = iter_image_declarations(game_dir)
    seen: set[Path] = set()
    for rpy, image_path in declared_paths:
        target = game_dir / image_path
        if not target.exists():
            reporter.error(f"{rel(rpy, project)} declares missing image: {image_path}")
        else:
            seen.add(target.resolve())

    images_dir = game_dir / "images"
    if images_dir.exists():
        for path in sorted(images_dir.rglob("*")):
            if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                check_dimensions(path, project, reporter, args.strict)
    else:
        reporter.warn("game/images/ directory does not exist")

    if declared_paths:
        undeclared = [
            path for path in seen
            if path.exists() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        ]
        _ = undeclared

    reporter.print()
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    sys.exit(main())
