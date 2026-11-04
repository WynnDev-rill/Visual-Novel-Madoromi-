#!/usr/bin/env python3
"""Acquire audited creator downloads and derive the game's selected runtime art.

Raw packs stay outside the repository. Install Pillow, then run this file.
Never commit the images as a reusable asset pack; bundle them inside the game.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import http.cookiejar
import io
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request
import zipfile

from PIL import Image

CREATOR = "https://potat0master.itch.io/"
# slug, published download filename, sha256 of the audited archive, local cache filename
PACKS = {
    "rooms": ("free-visual-novel-backgrounds-personal-rooms-pack-1", "PersonalRooms1_2160p_WEBP.zip", "aa12ef5ebc337fbacf5fd513010ce1ca9ae9d2f044b0bc4b7c8449d658d95ff7", "free-visual-novel-backgrounds-personal-rooms-pack-1.zip"),
    "a01": ("free-characters-for-visual-novels-set-a01", "BasicCharacterSetA01_2160p_WEBP_Free.zip", "68d37c8c03c8164b9c2852c6d6df5f68806a3b42aa9af39b23189d78b9f01905", "characters.zip"),
    "a02": ("characters-set-a02", "BasicCharacterSetA02_2160p_WEBP_Free.zip", "815a5f406705f01e3d5aa2ff30458441513b51996d3a6b69586e0096c6a215de", "characters-set-a02.zip"),
    "school1": ("free-visual-novel-backgrounds-school-mini-pack-1", "SchoolMiniPack_2160p_WEBP.zip", "3c0d4d9b9546b1353dcc115733fd37ff5fcdda1009267cf29533c9e2caad114a", "free-visual-novel-backgrounds-school-mini-pack-1.zip"),
    "school2": ("free-visual-novel-backgrounds-school-mini-pack-2", "SchoolMiniPack2_2160p_WEBP.zip", "a1866968936cdf2b54559092b11e2746a45104f52ddf9c04eb916fa01256afd8", "free-visual-novel-backgrounds-school-mini-pack-2.zip"),
    "mini1": ("free-visual-novel-backgrounds-mini-pack-1", "MiniPack1_2160p_WEBP.zip", "f77ba5978fc243115bb78e0bb587759839b05abe5fa5d87e8961949e6d89f2c3", "free-visual-novel-backgrounds-mini-pack-1.zip"),
    "mini2": ("free-visual-novel-backgrounds-mini-pack-2", "MiniPack2_2160p_WEBP.zip", "35dbe2b977021bcb528f1ff38d553a95a1bfe66257cd53cc15c72723ecbe8906", "free-visual-novel-backgrounds-mini-pack-2.zip"),
    "starter2": ("free-visual-novel-backgrounds-starter-pack-2", "Visual Novel Backgrounds (Starter Pack 2).zip", "edb7359231c91bed0ae3c073921d51ad38e6152f97a001ad6deecda1b8939a7e", "free-visual-novel-backgrounds-starter-pack-2.zip"),
    "random": ("free-stylized-backgrounds-for-visual-novels-random-pack-a", "RandomPackA_2160p_1080p_WEBP.zip", "c147523e3439cc2608245721ebeafe3a711cf54818140e3fb80577b967c31b4e", "free-stylized-backgrounds-for-visual-novels-random-pack-a.zip"),
}

BACKGROUNDS = {
    "bedroom": ("rooms", "PersonalRooms1_2160p_WEBP/pra_a1_night1_lights.webp"),
    "bedroom_day": ("rooms", "PersonalRooms1_2160p_WEBP/pra_a1_day2.webp"),
    "cafeteria": ("mini2", "MiniPack2_2160p_WEBP/canteen_day2.webp"),
    "artroom": ("school2", "SchoolMiniPack2_2160p_WEBP/smp2_ar_day2.webp"),
    "artroom_evening": ("school2", "SchoolMiniPack2_2160p_WEBP/smp2_ar_evening1.webp"),
    "cafe": ("mini1", "MiniPack1_2160p_WEBP/coffee_shop_day1.webp"),
    "cafe_evening": ("mini1", "MiniPack1_2160p_WEBP/coffee_shop_evening1.webp"),
    "school": ("school1", "SchoolMiniPack_2160p_WEBP/smp_front_day1.webp"),
    "school_evening": ("school1", "SchoolMiniPack_2160p_WEBP/smp_front_evening1.webp"),
    "classroom": ("school1", "SchoolMiniPack_2160p_WEBP/smp_classroom1_day2.webp"),
    "classroom_evening": ("school1", "SchoolMiniPack_2160p_WEBP/smp_classroom1_evening1.webp"),
    "hallway": ("school1", "SchoolMiniPack_2160p_WEBP/smp_hallway11_day1.webp"),
    "street": ("starter2", "Visual Novel Backgrounds (Starter Pack 2)/city a s3st2 day.png"),
    "street_evening": ("starter2", "Visual Novel Backgrounds (Starter Pack 2)/city a s3st2 evening.png"),
    "night": ("starter2", "Visual Novel Backgrounds (Starter Pack 2)/city a s1st2 nightlights.png"),
    "stage": ("starter2", "Visual Novel Backgrounds (Starter Pack 2)/school a auditorium inuse2.png"),
    "nature": ("random", "RandomPackA_2160p_WEBP/forest_a_day1a.webp"),
    "river_arch": ("random", "RandomPackA_2160p_WEBP/railarea_a_day1a.webp"),
}

EXPRESSIONS = {
    "neutral": "normal", "smile": "normalblush", "shy": "blush",
    "sad": "upset", "surprised": "huh", "laugh": "happy",
    "talk": "talk", "tears": "tears", "pout": "pout", "frown": "frown",
    "angry": "angry", "angrytalk": "angrytalk", "disgusted": "disgusted",
    "smirk": "evilsmirk", "poutangry": "poutangry", "dread": "purp",
    "sadtalk": "upsettalk",
}


def token(page: str) -> str:
    return html.unescape(re.search(r'name="csrf_token" value="([^"]+)"', page)[1])


def acquire(cache: Path, spec: tuple[str, str, str, str]) -> Path:
    slug, published_name, digest, cached_name = spec
    path = cache / cached_name
    if not path.exists():
        page_url = CREATOR + slug
        session = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
        page = session.open(page_url, timeout=45).read().decode()
        # License changes must receive human review before an updated archive is accepted.
        page_text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", page))).lower()
        if "commercial projects" not in page_text or "modif" not in page_text:
            raise RuntimeError(f"Creator terms changed; review {page_url}")

        def post(url: str, csrf: str) -> dict:
            request = urllib.request.Request(url, data=urllib.parse.urlencode({"csrf_token": csrf}).encode(), headers={"Referer": page_url, "X-Requested-With": "XMLHttpRequest"})
            return json.loads(session.open(request, timeout=45).read())

        download_page = session.open(post(page_url + "/download_url", token(page))["url"], timeout=45).read().decode()
        uploads = re.findall(r'data-upload_id="(\d+)".*?<strong title="([^"]+)"', download_page, re.S)
        upload_id = next((uid for uid, name in uploads if html.unescape(name) == published_name), None)
        if not upload_id:
            raise RuntimeError(f"Audited free download missing: {published_name}")
        download = post(page_url + "/file/" + upload_id, token(download_page))
        if not download.get("url") or download.get("external"):
            raise RuntimeError(f"Unexpected download response for {published_name}")
        temporary = path.with_suffix(".part")
        urllib.request.urlretrieve(download["url"], temporary)
        temporary.replace(path)
        time.sleep(1)  # Respect the creator storefront rate limit.
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != digest:
        raise RuntimeError(f"Archive changed; audit before using {path.name}: {actual}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path("/workspace/downloads/visuals"))
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    archives = {key: zipfile.ZipFile(acquire(args.cache, spec)) for key, spec in PACKS.items()}
    records = []

    def write(pack: str, member: str, relative: str, sprite=False) -> None:
        image = Image.open(io.BytesIO(archives[pack].read(member)))
        native_size = list(image.size)
        if sprite:
            # One common crop across EVERY outfit/expression prevents pose jumping.
            image = image.convert("RGBA").crop((80, 420, 1320, 2160))
            image = image.resize((770, 1080), Image.Resampling.LANCZOS)
        else:
            image = image.convert("RGB").resize((1920, 1080), Image.Resampling.LANCZOS)
        output = args.project / relative
        output.parent.mkdir(parents=True, exist_ok=True)
        valid_existing = False
        if output.exists():
            try:
                with Image.open(output) as previous:
                    previous.verify()
                valid_existing = True
            except (OSError, ValueError):
                pass
        if not valid_existing:
            temporary = output.with_suffix(".part")
            image.save(temporary, "WEBP", quality=95, method=4)
            temporary.replace(output)
        records.append({"asset_id": Path(relative).stem, "runtime_path": relative, "creator": "Potat0Master", "source_page": CREATOR + PACKS[pack][0], "source_archive": PACKS[pack][1], "source_archive_sha256": PACKS[pack][2], "source_member": member, "source_size": native_size, "runtime_size": list(image.size), "runtime_sha256": hashlib.sha256(output.read_bytes()).hexdigest(), "license": "Royalty-free custom; commercial game use and editing permitted; standalone redistribution prohibited", "credit": "Character and background art: Potat0Master", "ai_restriction": "No restriction stated on audited creator page; creator declares no generative AI used", "adaptation": "Common transparent crop and Lanczos resizing" if sprite else "Lanczos resizing only", "audited": "2026-11-03", "status": "approved for integrated game only"})

    for alias, (pack, member) in BACKGROUNDS.items():
        write(pack, member, f"game/images/backgrounds/{alias}.webp")
    outfits = {"school": ("a01", "BasicCharacterSetA01_2160p_WEBP_Free/kohaku_schwin_"), "summer": ("a01", "BasicCharacterSetA01_2160p_WEBP_Free/kohaku_schsum_"), "casual": ("a02", "BasicCharacterSetA02_2160p_WEBP_Free/kohaku_whitetop_"), "blouse": ("a02", "BasicCharacterSetA02_2160p_WEBP_Free/kohaku_shirttop_")}
    for outfit, (pack, prefix) in outfits.items():
        for expression, source_expression in EXPRESSIONS.items():
            write(pack, prefix + source_expression + ".webp", f"game/images/characters/aoi/{outfit}_{expression}.webp", sprite=True)
    manifest = args.project / "docs/licenses/visual-assets.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"note": "Runtime art excluded from source-control redistribution; rebuild from creator storefronts using this script.", "assets": records}, indent=2) + "\n")
    print(f"Prepared {len(records)} runtime images; manifest: {manifest}")


if __name__ == "__main__":
    main()
