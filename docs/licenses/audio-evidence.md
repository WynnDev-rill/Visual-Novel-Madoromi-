# Audio license evidence

Fetched 2026-11-03 directly from the linked official catalog/work pages. This file records factual excerpts and SHA-256 of captured source pages, not a replacement license. Complete HTML snapshots and original downloads are retained outside the repository at `/workspace/downloads/audio/evidence`.

## incompetech-music.html

Source: https://incompetech.com/music/royalty-free/music.html

Each rendered catalog item says: “Licensed under Creative Commons: By Attribution 4.0 License” with http://creativecommons.org/licenses/by/4.0/.

Snapshot SHA-256: `cef5484ed154f14f7e4aa9dbc8f126209af5c22c5bb664615e5f728e0017718a`

## incompetech-license.html

Source: https://incompetech.com/music/royalty-free/licenses/

The Creative Commons option states: “No charge. Requires that you credit the music.” The renderCC function generates the attribution block copied in audio.md.

Snapshot SHA-256: `479019ed42fd8384c63c04bd95dc6d0e0e0da505ddd6f567a13018c724f8416d`

## incompetech-selected.json

Source: https://incompetech.com/music/royalty-free/pieces.json

This is a selected-record JSON subset, not the complete raw HTTP response. Full raw catalog response SHA-256: `54802ad340562624b9d1c9c97aa9f005e2b9bf79001f8a1a07ed857e68b2164a`. Selected metadata records titles, filenames, instrumentation, duration, descriptions and ISRCs. Three selected source works use piano; Easy Lemon uses guitar/bass/drums/celesta/marimba, Dream Culture uses piano/percussion.

Snapshot SHA-256: `90fcc84eb234aecfbea9ac3502ac5341236077b2a98ed5c247360fcfc170d46f`

## kenney-interface.html

Source: https://kenney.nl/assets/interface-sounds

The work page links CC0 1.0. The archive License.txt says: “License: (Creative Commons Zero, CC0)” and “This content is free to use in personal, educational and commercial projects.”

Snapshot SHA-256: `1034f6d7c4f5de8fff04d375467fa88baaf75470ce62a3e75268f603d11e3a69`

## oga-crickets-ambient-noise-loopable.html

Source: https://opengameart.org/content/crickets-ambient-noise-loopable

Author: Wolfgang_. License(s): CC0. “Ambient night cricket sounds 11 seconds, but loopable. Preview loops once.” Attribution notice: “(optional) Ted Kerr”.

Snapshot SHA-256: `a5cf9eab393f9a141cb1b186f29c7de3bfbc29fb697d3aee8fb656df890047f5`

## oga-ambient-bird-sounds.html

Source: https://opengameart.org/content/ambient-bird-sounds

Author: isaiah658. License(s): CC0. “I recently discovered that the microphone on my camera is actually pretty good for recording ambient sounds. I still had to heavily clean up the the audio with Audacity.” Notice: “Credit to isaiah658 is not needed but is appreciated.”

Snapshot SHA-256: `d5b152669d3ea8be93cc0325b59c8736bda3f2cb9cf657e1e15f564e4760d132`

## oga-inventory-sound-effects.html

Source: https://opengameart.org/content/inventory-sound-effects

Author: artisticdude (submitted by Ogrebane). License options shown: CC-BY 3.0, CC-BY-SA 3.0, GPL 3.0, GPL 2.0. MADOROMI elects CC BY 3.0. Description lists six WAVs including “turn page”.

Snapshot SHA-256: `6b8d36aef0f9687beb4fe12e2e8016f135303bd53868aeef17dcd15fd8b6a7f8`

## oga-pleasing-bell-sound-effect.html

Source: https://opengameart.org/content/pleasing-bell-sound-effect

Author: Spring Spring. License(s): CC0. Notice: “Produced by Julie Damsgaard/Spring Spring/Spring Enterprises @ https://spring-enterprises.neocities.org”.

Snapshot SHA-256: `76e60a56847ed0ff4477c66b1a4b46dc9630f8c4917f27d142081f4ddec5b8ba`

## Full license texts

Verbatim CC BY 4.0, CC BY 3.0, and CC0 1.0 license texts are included next to this file, obtained from the SPDX license-list-data text mirrors at `https://github.com/spdx/license-list-data/tree/main/text`. The authoritative license links remain those shown on the source work pages. `kenney-interface-license.txt` is the unmodified notice from the acquired archive.

Acquisition decisions: preferred CC0 / CC BY for clear redistribution of selected runtime files and source control. OtoLogic and some Kenney curl requests returned HTTP 403; Kenney succeeded with the ordinary Python HTTP client and official signed download flow. OtoLogic was not used. No need for generated music, restricted DOVA/PeriTune materials, or a paid source was demonstrated.
