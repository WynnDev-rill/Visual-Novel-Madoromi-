#!/usr/bin/env python3
"""Check narrative contracts, then optionally require actual native route evidence.

This does not simulate Ren'Py. Only the engine's completed-route evidence can
establish interactive coverage; static text checks establish preservation only.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import re
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--coverage", type=Path, help="native-paths.json from a fresh isolated engine test run")
    parser.add_argument("--coverage-mode", choices=("matrix", "choices"), default="matrix", help="matrix requires all 32 combinations; choices requires two contrasting complete paths")
    parser.add_argument("--report", type=Path, help="stdout from the native Ren'Py test runner")
    args = parser.parse_args()
    story = (args.project / "game/story.rpy").read_text()

    labels = re.findall(r"^label (\w+)", story, re.M)
    require(len(labels) == len(set(labels)), "Duplicate story labels")
    require({"start", "act_1", "act_2", "act_3", "epilogue"} <= set(labels), "The complete three-act story and epilogue must be present")
    for target in re.findall(r"^\s+jump (\w+)\s*$", story, re.M):
        require(target in labels, f"Story jumps to missing label {target}")

    # A new menu changes the interactive route matrix and must get engine tests.
    menu_blocks = re.split(r"^    menu:\s*$", story, flags=re.M)[1:]
    widths = []
    for block in menu_blocks:
        lines = block.splitlines()
        options = []
        for line in lines:
            if line.strip() and not line.startswith("        "):
                break
            match = re.match(r'^        "(.+)":\s*$', line)
            if match:
                options.append(match[1])
        widths.append(len(options))
    require(widths == [2, 2, 2, 2, 2], f"Update the native route tests for this choice matrix: {widths}")

    beats = {
        "night messages until two": "02.00",
        "ants": "jalur semut",
        "band": "poster band",
        "cafeteria invitation": "Aku minta kamu di sini",
        "beanbag": "beanbag",
        "ten seconds": "Sepuluh detik",
        "interrupted confession": "Bukan Sora juga",
        "favorite bakery": "Toko roti kecil",
        "tree by cathedral": "Aoi lebih mengenal pohonnya",
        "reciprocal confession": "Aku juga suka kamu. Sangat.",
        "consensual hug": "Boleh aku memelukmu?",
        "painted jeans": "Ia mengangkat jeans itu dari dalam",
        "life after acceptance": "Sabtu berikutnya, Aoi datang ke toko roti dengan jeans itu",
    }
    for beat, phrase in beats.items():
        require(phrase.casefold() in story.casefold(), f"Missing source-story beat: {beat}")

    # These are source-story sequencing constraints, not implementation details.
    acceptance = story.index('a "Aku juga suka kamu. Sangat."')
    hug = story.index('a "Boleh aku memelukmu?"')
    agreement = story.index('r "Iya. Aku tahu. Aku juga mau. Kita berpacaran."')
    gift = story.index('"Ia mengangkat jeans itu dari dalam')
    require(acceptance < hug < agreement < gift, "Acceptance, hug, relationship agreement, then gift must retain that order")
    require('"Aku sengaja menunggu sampai selesai bicara.' in story, "The gift must not pressure her answer")
    require('persistent.completed = True' in story and '"TAMAT"' in story, "Missing completed ending")

    dialogue = re.findall(r'^\s*(?:[rasm] )?"(.+)"\s*$', story, re.M)
    word_count = sum(len(line.split()) for line in dialogue)
    require(word_count >= 6000, f"Unexpectedly short story: {word_count} narrative/dialogue words")
    scenes = len(re.findall(r"# SCENE \d+", story))
    require(scenes >= 12, f"Missing story scenes: {scenes}")
    print(f"Story contracts PASS: {scenes} scenes, {word_count:,} narrative/dialogue words, five binary decisions (32 combinations).")

    if args.coverage:
        evidence = json.loads(args.coverage.read_text())
        rows = evidence.get("completed_routes", [])
        expected = ({"".join(map(str, route)) for route in itertools.product((0, 1), repeat=5)}
                    if args.coverage_mode == "matrix" else {"00000", "11111"})
        actual = {row["route"] for row in rows}
        require(actual == expected, f"Native route matrix incomplete: {sorted(expected - actual)}")
        require(len(rows) == len(expected), "Duplicate or unexpected native route records")
        require(all(row.get("completed") and row.get("chapter_unlocked") == 3 and row.get("callbacks_verified") == 5 for row in rows), "A route lacks completion, chapter unlock, or later callbacks")
        label = "all 32 combinations" if args.coverage_mode == "matrix" else "both contrasting paths (all decision options)"
        print(f"Native route evidence PASS: {label} completed; all five later callbacks verified on each path.")

    if args.report:
        report = re.sub(r"\x1b\[[0-9;]*m", "", args.report.read_text(errors="replace"))
        statuses = re.findall(r"\[rpytest\]\s+Status:\s+(\w+)", report)
        require(bool(statuses) and statuses[-1] == "PASSED", "Native runner report did not end with PASSED (process exit alone is insufficient)")
        require("Assertions :" in report, "Report does not include actual assertions")
        print("Native runner report PASS.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, OSError, ValueError, KeyError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
