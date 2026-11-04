# Audio credits and source register

Acquired and license pages checked **2026-11-03**. All shipped files are existing composer/recordist work; no generated music, voices, or copied benchmark assets are used. The four compositions share one composer and a restrained piano-led palette. Scene suitability still requires a listening pass in context.

| Runtime file (`game/audio/`) | Original / creator | Source and downloadable original | License |
|---|---|---|---|
| `bgm/night.ogg` | **Dream Culture** — Kevin MacLeod, ISRC USUAN1300046 | [official catalog](https://incompetech.com/music/royalty-free/music.html); [MP3](https://incompetech.com/music/royalty-free/mp3-royaltyfree/Dream%20Culture.mp3) | CC BY 4.0 |
| `bgm/day.ogg` | **Easy Lemon** — Kevin MacLeod, ISRC USUAN1200076 | [official catalog](https://incompetech.com/music/royalty-free/music.html); [MP3](https://incompetech.com/music/royalty-free/mp3-royaltyfree/Easy%20Lemon.mp3) | CC BY 4.0 |
| `bgm/tender.ogg` | **Touching Moments Five - Circle** — Kevin MacLeod, ISRC USUAN1100041 | [official catalog](https://incompetech.com/music/royalty-free/music.html); [MP3](https://incompetech.com/music/royalty-free/mp3-royaltyfree/Touching%20Moments%20Five%20-%20Circle.mp3) | CC BY 4.0 |
| `bgm/confession.ogg` | **Touching Moments Four - Melody** — Kevin MacLeod, ISRC USUAN1100040 | [official catalog](https://incompetech.com/music/royalty-free/music.html); [MP3](https://incompetech.com/music/royalty-free/mp3-royaltyfree/Touching%20Moments%20Four%20-%20Melody.mp3) | CC BY 4.0 |
| `ambience/night.ogg` | **Crickets Ambient Noise (Loopable)** — Wolfgang_; optional credit **Ted Kerr** | [work page](https://opengameart.org/content/crickets-ambient-noise-loopable); [MP3](https://opengameart.org/sites/default/files/crickets_1.mp3) | CC0 1.0 |
| `ambience/garden.ogg` | **Ambient Bird Sounds** — isaiah658 | [work page](https://opengameart.org/content/ambient-bird-sounds); [OGG](https://opengameart.org/sites/default/files/birds-isaiah658_0.ogg) | CC0 1.0 |
| `sfx/message.ogg`, `sfx/ui.ogg` | **Interface Sounds 1.0**, `confirmation_002.ogg`, `select_001.ogg` — Kenney | [work page / download](https://kenney.nl/assets/interface-sounds) | CC0 1.0 |
| `sfx/page.ogg` | **Inventory Sound Effects**, `turn_page.wav` — artisticdude; submitted by Ogrebane | [work page](https://opengameart.org/content/inventory-sound-effects); [ZIP](https://opengameart.org/sites/default/files/inventory_sound_effects.zip) | CC BY 3.0, selected from the page's alternative licenses |
| `sfx/bell.ogg` | **Pleasing Bell Sound Effect** — Julie Damsgaard / Spring Spring / Spring Enterprises | [work page](https://opengameart.org/content/pleasing-bell-sound-effect); [WAV](https://opengameart.org/sites/default/files/pleasing-bell.wav) | CC0 1.0 |

The small bell is a musical transition/notification cue, **not a recording of a Japanese school chime**. Do not stage it as an authentic school announcement. No dialogue/voice is present.

## Attribution for the game's credits

The following composer block follows the official [license generator](https://incompetech.com/music/royalty-free/licenses/):

> "Dream Culture", "Easy Lemon", "Touching Moments Five - Circle", "Touching Moments Four - Melody"  
> Kevin MacLeod (incompetech.com)  
> Licensed under Creative Commons: By Attribution 4.0  
> http://creativecommons.org/licenses/by/4.0/

> "Inventory Sound Effects" (turn_page.wav) by artisticdude, submitted by Ogrebane.  
> https://opengameart.org/content/inventory-sound-effects  
> Licensed under CC BY 3.0: https://creativecommons.org/licenses/by/3.0/  
> Converted to Ogg Vorbis and level adjusted for MADOROMI.

Optional CC0 acknowledgments, included in the game's credits:

> Interface Sounds — Kenney (kenney.nl), CC0.  
> Crickets — Ted Kerr / Wolfgang_, CC0.  
> Ambient Bird Sounds — isaiah658, CC0.  
> Pleasing Bell — Julie Damsgaard / Spring Spring / Spring Enterprises, CC0.

## Edits, redistribution, and evidence

CC BY allows commercial redistribution and modification with attribution, the license link, and change notices; CC0 allows redistribution and modification without mandatory attribution. These licenses do not impose a separate prohibition on an AI-assisted coding workflow. Nothing here was submitted to a generative music service. Preserve these notices with releases and in the game credits. The game's code license does not replace the asset licenses.

Modifications: decoded originals, two-pass loudness adjustment (BGM −18 LUFS, ambience −22 LUFS, true peak ceiling −1.5 dBTP), Ogg Vorbis quality 4 at 44.1 kHz; SFX gain adjusted to peaks −6/−7/−8/−10 dBFS. Birds receive a one-second wrap crossfade. Music keeps its complete composition and natural ending; it is not claimed to be a sample-seamless loop. Crickets are described as loopable by their author. Runtime mixers should lower music and ambience under the reading experience, and crossfade between compositions.

[`audio-files.json`](audio-files.json) records source hashes, shipped hashes, durations and codecs. [`audio-evidence.md`](audio-evidence.md) records exact source statements and snapshot hashes. Originals and downloaded archives stay outside the repository at `/workspace/downloads/audio`; only the selected runtime files are bundled. [`tools/prepare_audio.py`](../../tools/prepare_audio.py) reproduces conversions from those originals. The source catalog metadata for the selected tracks is in [`incompetech-selected.json`](incompetech-selected.json).

Validation performed: all ten final Ogg files decode completely through ffmpeg; codec and duration recorded in audio-files.json, measured output levels in audio-qa.json. Gameplay/headphone/speaker listening QA remains a separate human-perceptual check, not established by loudness meters.
