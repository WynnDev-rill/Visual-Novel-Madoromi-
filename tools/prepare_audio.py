#!/usr/bin/env python3
"""Convert acquired, licensed sources to Ren'Py audio. Requires ffmpeg/ffprobe.

Original downloads stay outside the repository. See docs/licenses/audio.md.
Usage: python tools/prepare_audio.py [/workspace/downloads/audio]
"""
from pathlib import Path
from array import array
import concurrent.futures
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "downloads/audio"
JOBS = [
    ("Dream Culture.mp3", "bgm/night.ogg", "music"),
    ("Easy Lemon.mp3", "bgm/day.ogg", "music"),
    ("Touching Moments Five - Circle.mp3", "bgm/tender.ogg", "music"),
    ("Touching Moments Four - Melody.mp3", "bgm/confession.ogg", "music"),
    ("crickets.mp3", "ambience/night.ogg", "ambience"),
    ("birds.ogg", "ambience/garden.ogg", "birds"),
    ("kenney-interface/Audio/confirmation_002.ogg", "sfx/message.ogg", -6),
    ("kenney-interface/Audio/select_001.ogg", "sfx/ui.ogg", -10),
    ("inventory/inventory_sound_effects/turn_page.wav", "sfx/page.ogg", -7),
    ("pleasing-bell.wav", "sfx/bell.ogg", -8),
]


def run(*args):
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr[-4000:])
    return result.stderr


def loop_birds(src):
    """Wrap-crossfade existing PCM by one second; no new audio is synthesized."""
    pcm = array("f", subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(src), "-map", "0:a:0",
        "-ar", "48000", "-ac", "2", "-f", "f32le", "-"]))
    overlap = 48000 * 2
    wrapped = pcm[overlap:]
    start = len(wrapped) - overlap
    for i in range(overlap):
        gain = (i // 2) / (48000 - 1)
        wrapped[start+i] = wrapped[start+i] * (1-gain) + pcm[i] * gain
    dst = src.with_name("birds-loop.wav")
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", "48000", "-ac", "2",
        "-i", "pipe:0", "-c:a", "pcm_f32le", str(dst)], input=wrapped.tobytes(), check=True)
    return dst


def convert(job):
    original, relative, kind = job
    src, dst = SOURCE / original, ROOT / "game/audio" / relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    source_filter = "anull"
    if kind == "birds":
        src = loop_birds(src)
    if isinstance(kind, (int, float)):
        stats = run("ffmpeg", "-hide_banner", "-i", str(src), "-af",
                    "volumedetect", "-f", "null", "-")
        peak = float(re.search(r"max_volume: ([\d.-]+) dB", stats)[1])
        filter_graph = f"volume={kind-peak:.3f}dB"
    else:
        target = -18 if kind == "music" else -22
        base = f"loudnorm=I={target}:TP=-1.5:LRA=11"
        stats = run("ffmpeg", "-hide_banner", "-i", str(src), "-filter_complex",
                    source_filter + "," + base + ":print_format=json[audio]",
                    "-map", "[audio]", "-f", "null", "-")
        measured, _ = json.JSONDecoder().raw_decode(stats[stats.rfind("{"):])
        correction = (
            f":measured_I={measured['input_i']}:measured_TP={measured['input_tp']}"
            f":measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}"
            f":offset={measured['target_offset']}:linear=true"
        )
        filter_graph = source_filter + "," + base + correction
    run("ffmpeg", "-hide_banner", "-y", "-i", str(src), "-filter_complex",
        filter_graph + "[audio]", "-map", "[audio]", "-ar", "44100", "-c:a", "libvorbis", "-q:a", "4",
        "-map_metadata", "-1", str(dst))
    return describe(original, relative)


def describe(original, relative):
    src, dst = SOURCE / original, ROOT / "game/audio" / relative
    info = json.loads(subprocess.check_output([
        "ffprobe", "-v", "quiet", "-show_format", "-show_streams", "-of", "json", str(dst)]))
    return {
        "path": "game/audio/" + relative, "source": original,
        "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
        "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
        "duration_seconds": round(float(info["format"]["duration"]), 3),
        "bytes": dst.stat().st_size,
        "sample_rate": int(info["streams"][0]["sample_rate"]),
        "codec": info["streams"][0]["codec_name"],
    }


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(convert, JOBS))
    target = ROOT / "docs/licenses/audio-files.json"
    target.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"Converted {len(rows)} files; {sum(x['bytes'] for x in rows)/1048576:.1f} MiB")
