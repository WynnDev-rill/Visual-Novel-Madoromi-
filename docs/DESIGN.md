# Madoromi — design decision, 3 November 2026

A complete intimate school romance adapted from the user's short story, with Indonesian prose, Japanese setting, three acts, an earned confession and a playable afterstory. Choices change the way the pair open up and later callbacks, without punitive affection scores. The original ending is preserved.

Ren'Py 8.5.3 is the selected baseline: native save/load, rollback, history, accessibility and Android packaging leave production effort for art, staging, music and prose. Installed Godot 4.6.3 is the comparison candidate, but would require VN-system integration for no requested gameplay advantage. The toolchain must prove this choice with actual builds.

Visual direction revised from the user's twelve ATRI / Please Be Happy references: mid-September light, sea-blue ink, warm ivory system surfaces, restrained coral accents, a world-dominant title, cream spoken-dialogue balloons, separate cinematic narration and a compact touch toolbar. System screens use horizontal navigation and segmented preferences; choices stay below faces. One mature consistent character family uses native 2D expressions, short dissolves and restrained ATL framing, with no Live2D requirement. Assets require actual license evidence. The chosen Drive icon is app identity, not the heroine design.

Reading text is Noto Serif; interface labels are Noto Sans. Colors: ink `#293d50`, ivory `#faf7f0`, sea-blue `#35738b`, coral `#a25f4c`. Default dialogue sizes 36 / 42 virtual pixels on a 1920×1080 reference, assessed in real scaled Android screenshots. Primary touch controls are at least 108 virtual pixels tall before device scaling. On the tested 1280×720, 240 dpi Android emulator this renders 72 physical pixels, or 48 dp. Other densities still require device-specific checks; virtual coordinates are not universally Android dp.

Desktop and Android share a 1920×1080 design with scalable touch controls. Native engine features cover standard VN systems. Custom work is limited to Madoromi's title/menu, readable dialogue, chapter navigation, phone scene presentation and art direction. Preferences include motion reduction, font size, text/auto speed and audio channels.

## Acceptance
Complete story; choices and callbacks; no missing assets; readable real screenshots at desktop/mobile sizes; native persistence and history work; audio legal and mixed; final APK exists, is signed, has the provided icon, and passes available installation/launch checks. Physical-device testing is reported honestly if unavailable. Aspirational Steam quality is not a ranking claim.
