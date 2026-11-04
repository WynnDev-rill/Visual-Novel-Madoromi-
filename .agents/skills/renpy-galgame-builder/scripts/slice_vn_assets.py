#!/usr/bin/env python3
"""Slice and normalize Ren'Py visual novel image assets.

Common uses:
  1. Crop a generated UI sheet with a JSON crop spec.
  2. Recreate clean text-free cyber VN UI fallback PNGs.
  3. Center-crop/resize backgrounds and CGs to 1280x720.
  4. Resize transparent sprites to a safe bust height.

The script intentionally avoids OCR/text removal magic. If a sheet crop contains
baked labels, recreate that UI piece with --make-ui-fallback instead.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError as exc:
    raise SystemExit(
        "Pillow is required. Install it with: "
        "python -m pip install -r <skill-dir>/scripts/requirements.txt"
    ) from exc


RGBA = tuple[int, int, int, int]


UI_SIZES = {
    "dialogue_box.png": (1160, 170),
    "choice_button_idle.png": (900, 58),
    "choice_button_hover.png": (900, 58),
    "status_panel.png": (760, 520),
    "status_button.png": (150, 48),
}


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def open_rgba(path: Path) -> Image.Image:
    return Image.open(path).convert("RGBA")


def center_crop_resize(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    src_w, src_h = img.size
    dst_w, dst_h = size
    src_ratio = src_w / src_h
    dst_ratio = dst_w / dst_h
    if src_ratio > dst_ratio:
        new_w = int(src_h * dst_ratio)
        left = (src_w - new_w) // 2
        box = (left, 0, left + new_w, src_h)
    else:
        new_h = int(src_w / dst_ratio)
        top = (src_h - new_h) // 2
        box = (0, top, src_w, top + new_h)
    return img.crop(box).resize(size, Image.Resampling.LANCZOS)


def fit_sprite_height(img: Image.Image, height: int) -> Image.Image:
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    scale = height / img.height
    width = max(1, int(img.width * scale))
    return img.resize((width, height), Image.Resampling.LANCZOS)


def draw_glow_rect(
    size: tuple[int, int],
    radius: int,
    fill: RGBA,
    border: RGBA,
    glow: RGBA,
    border_width: int = 2,
    accents: bool = True,
) -> Image.Image:
    w, h = size
    pad = 10
    glow_layer = Image.new("RGBA", size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    gd.rounded_rectangle(
        (pad, pad, w - pad, h - pad),
        radius=radius,
        outline=glow,
        width=5,
        fill=(0, 0, 0, 0),
    )
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(8))

    img = Image.new("RGBA", size, (0, 0, 0, 0))
    img.alpha_composite(glow_layer)
    d = ImageDraw.Draw(img)
    rect = (pad, pad, w - pad, h - pad)
    d.rounded_rectangle(rect, radius=radius, fill=fill, outline=border, width=border_width)

    if accents:
        cyan = (110, 235, 255, 145)
        pink = (255, 120, 220, 120)
        d.line((pad + 30, pad + 1, pad + 180, pad + 1), fill=cyan, width=2)
        d.line((w - pad - 180, h - pad - 1, w - pad - 30, h - pad - 1), fill=pink, width=2)
        d.line((pad + 28, h - pad - 18, pad + 78, h - pad - 18), fill=cyan, width=1)
        d.line((w - pad - 78, pad + 18, w - pad - 28, pad + 18), fill=pink, width=1)
    return img


def make_title_bg(size: tuple[int, int] = (1280, 720)) -> Image.Image:
    w, h = size
    img = Image.new("RGBA", size, (13, 22, 45, 255))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(18 + 20 * t)
        g = int(28 + 28 * t)
        b = int(62 + 48 * t)
        d.line((0, y, w, y), fill=(r, g, b, 255))
    for x in range(0, w, 80):
        d.line((x, 0, x + 220, h), fill=(95, 220, 255, 28), width=1)
    for x in range(40, w, 120):
        d.line((x, h, x + 160, 0), fill=(255, 130, 220, 24), width=1)
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((120, 90, 520, 470), fill=(100, 230, 255, 42))
    gd.ellipse((720, 160, 1200, 680), fill=(255, 120, 220, 38))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(48)))
    return img


def make_ui_fallbacks(out_dir: Path) -> None:
    ensure_dir(out_dir)
    make_title_bg().save(out_dir / "title_bg.png")
    draw_glow_rect(
        UI_SIZES["dialogue_box.png"],
        18,
        (8, 18, 36, 205),
        (118, 235, 255, 190),
        (116, 220, 255, 150),
    ).save(out_dir / "dialogue_box.png")
    draw_glow_rect(
        UI_SIZES["choice_button_idle.png"],
        16,
        (14, 26, 52, 215),
        (120, 235, 255, 150),
        (120, 235, 255, 110),
    ).save(out_dir / "choice_button_idle.png")
    draw_glow_rect(
        UI_SIZES["choice_button_hover.png"],
        16,
        (36, 35, 76, 230),
        (255, 145, 225, 205),
        (255, 130, 220, 160),
    ).save(out_dir / "choice_button_hover.png")
    draw_glow_rect(
        UI_SIZES["status_panel.png"],
        24,
        (8, 18, 40, 225),
        (135, 235, 255, 180),
        (255, 130, 220, 125),
    ).save(out_dir / "status_panel.png")
    draw_glow_rect(
        UI_SIZES["status_button.png"],
        14,
        (12, 24, 48, 220),
        (125, 235, 255, 170),
        (125, 235, 255, 120),
        accents=False,
    ).save(out_dir / "status_button.png")


def crop_from_spec(sheet: Path, spec_path: Path, out_dir: Path) -> None:
    ensure_dir(out_dir)
    img = open_rgba(sheet)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    for item in spec.get("crops", spec if isinstance(spec, list) else []):
        name = item["filename"]
        box = tuple(item["box"])
        target_size = tuple(item.get("size", (box[2] - box[0], box[3] - box[1])))
        crop = img.crop(box)
        if crop.size != target_size:
            crop = crop.resize(target_size, Image.Resampling.LANCZOS)
        crop.save(out_dir / name)


def normalize_images(paths: Iterable[Path], out_dir: Path, mode: str, height: int) -> None:
    ensure_dir(out_dir)
    for path in paths:
        img = open_rgba(path)
        if mode in {"background", "cg"}:
            out = center_crop_resize(img, (1280, 720))
        elif mode == "sprite":
            out = fit_sprite_height(img, height)
        else:
            raise ValueError(f"unknown mode: {mode}")
        out.save(out_dir / path.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sheet", type=Path, help="Generated UI sheet to crop.")
    parser.add_argument("--spec", type=Path, help="JSON crop spec with filename, box, and optional size.")
    parser.add_argument("--make-ui-fallback", action="store_true", help="Create clean text-free UI PNGs.")
    parser.add_argument("--normalize", nargs="*", type=Path, help="Images to normalize.")
    parser.add_argument("--mode", choices=["background", "cg", "sprite"], default="background")
    parser.add_argument("--sprite-height", type=int, default=560)
    parser.add_argument("--out", type=Path, required=True, help="Output directory.")
    args = parser.parse_args()

    if args.make_ui_fallback:
        make_ui_fallbacks(args.out)
    if args.sheet and args.spec:
        crop_from_spec(args.sheet, args.spec, args.out)
    if args.normalize:
        normalize_images(args.normalize, args.out, args.mode, args.sprite_height)


if __name__ == "__main__":
    main()
