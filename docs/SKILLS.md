# Skill produksi MADOROMI

Ditinjau dan dipasang lokal pada 3 November 2026. Permintaan terbaru pengguna
memperbarui keputusan audit sebelumnya: **Ren’Py Galgame Builder, Game UI/UX,
Impeccable, dan UI UX Pro Max sekarang terpasang**, bersama Visual Novel yang
sudah ada. Skill adalah alat produksi; cerita, aset legal, desain proyek, dan
fitur native Ren’Py tetap menjadi acuan.

## Yang terpasang

| Skill lokal | Sumber dan pin | Pemakaian dalam proyek |
|---|---|---|
| [Ren’Py Galgame Builder](../.agents/skills/renpy-galgame-builder/SKILL.md) | [jaywang172/renpy-galgame-builder](https://github.com/jaywang172/renpy-galgame-builder/tree/fdcaa89aa30d45d9d9141df089353097a4e71f39), MIT | Integrasi `.rpy`, ekspresi/staging, layar pilihan, pengecekan label/aset, dan lint. Sumber memang menyebut Codex dan Ren’Py. Pertahankan label, flag cerita, ID gambar, alur, serta resolusi proyek yang sudah dipilih. |
| [Game UI/UX](../.agents/skills/game-ui-ux/SKILL.md) | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/19d93f97c9c1ea0f8b306e77aa81e0d3e352d3e9), Apache-2.0 | Reference resolution/aspect policy, safe margins, ukuran kontrol sentuh, fokus keyboard, kontras, dan alur kembali. Implementasi memakai screen language/style/action Ren’Py. |
| [Impeccable 4.8.0](../.agents/skills/impeccable/SKILL.md) | [pbakaus/impeccable](https://github.com/pbakaus/impeccable/tree/9fadc41729c38fd47d7ae622b501558653f9d2e9), Apache-2.0 | `polish`, `critique`, `typeset`, `layout`, dan `animate`: baca hasil render, jaga identitas, benahi hierarki/ritme/kontras, dan buat gerak yang punya tujuan. Mode cerita adalah Experience; save/load/preferences adalah Operate. |
| [UI UX Pro Max 2.15.0](../.agents/skills/ui-ux-pro-max/SKILL.md) | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/713eef51b04efc98d6fa565323b495f7c9c89fd4), MIT | Pencarian lokal terarah untuk keterbacaan, fokus, target sentuh, dan reduced motion. Hasil adalah bahan audit yang harus cocok dengan VN. Tidak ada stack Ren’Py dalam katalog; penerapan API memakai dokumentasi Ren’Py. |
| [Visual Novel](../.agents/skills/visual-novel/SKILL.md) | repositori/pin Game UI/UX di atas, Apache-2.0 | Checklist ekspresi, pilihan dengan callback, save-anywhere, rollback, backlog, skip teks terbaca, auto, dan text speed. Reuse sistem native Ren’Py. |

[UPSTREAM.json](../.agents/skills/UPSTREAM.json) mencatat dua instalasi awal dan
menautkan manifest tiap instalasi baru. Setiap manifest memuat commit, asal file,
dan SHA-256; LICENSE dan NOTICE upstream disertakan bila ada. Berkas upstream
disalin apa adanya. Satu pengecualian yang dicatat: `ui-ux-pro-max/SKILL.md`
dirender dari template resmi platform **Codex**, dengan path lokal `.agents`,
mengikuti fungsi `renderSkillFile` upstream.

Instalasi tambahan berukuran sekitar 5,5 MiB: referensi, data pencarian, dan
skrip. Tidak memasang CLI global, npm dependencies, browser, hook, server,
subskill web lain, atau runtime game tambahan. Template Ren’Py tetap berada
di direktori skill sebagai contoh; tidak menimpa berkas `game/`. Demo gambar
upstream tidak disalin menjadi aset game.

## Cara bekerja bersama

1. Baca [DESIGN.md](DESIGN.md), [STORY.md](STORY.md), naskah dan screen aktual,
   lalu cocokkan benchmark dengan screenshot resmi dan referensi pengguna.
   Gunakan [BENCHMARKS.md](BENCHMARKS.md) untuk memisahkan fakta dari inferensi.
2. Ren’Py Galgame Builder menentukan perubahan engine yang kecil dan lengkap:
   image attributes/layered images untuk ekspresi bila cocok dengan aset, ATL
   untuk perpindahan/zoom yang disengaja, serta action native untuk menu.
3. Game UI/UX menguji komposisi pada canvas 1920×1080 dan ukuran tampilan
   desktop/Android yang benar-benar diuji: textbox, pilihan panjang, kontrol
   sentuh, fokus, history, preferences, dan jalan kembali.
4. Impeccable mengarahkan satu putaran polish menyeluruh setelah arah visual
   disepakati. Baca `reference/polish.md` dan `reference/craft-floor.md` sebelum
   mengedit UI; nilai narasi, art, dan kontrol dari hasil render game.
5. UI UX Pro Max menambah pemeriksaan terarah, misalnya
   `python3 .agents/skills/ui-ux-pro-max/scripts/search.py "keyboard focus visibility" --domain ux`.
   Pertahankan rekomendasi yang relevan; verifikasi di game, lalu lint dan
   uji alur/save/load sesuai perubahan.

## Batas penerapan yang telah diperiksa

- Default 1280×720 dan soft-cyber/anime dalam Galgame Builder adalah contoh
  upstream; proyek tetap 1920×1080 dengan arah sekolah Jepang yang sudah
  dipilih. `check_vn_assets.py` mengasumsikan beberapa ukuran 1280×720 dan hanya
  mengenali sebagian bentuk deklarasi gambar. `--help` sudah berhasil; hasilnya
  bukan pengganti lint, pemeriksaan asset manifest, atau QA visual. Slicer
  bersifat opsional dan tidak dijalankan untuk mengolah ulang aset.
- Impeccable menyediakan launcher yang dapat mengunduh engine binernya sekali
  saat pertama dijalankan. Instalasi ini menyalin launcher dan referensi;
  engine biner belum diunduh dan hook belum diaktifkan. Setup upstream
  menyediakan fallback bila launcher tidak tersedia/ditolak: baca konteks
  proyek langsung dan lanjutkan playbook. Gunakan `docs/DESIGN.md` sebagai
  desain proyek yang sudah ada. Scanner DOM/web dan panduan native
  SwiftUI/UIKit/Compose/RN/Flutter tidak memahami screen language Ren’Py;
  hasil kosong tidak membuktikan game bersih. Ukuran CSS, browser selectors,
  dan jargon web tidak dipaksakan menjadi aturan layout VN.
- Search UI UX Pro Max berjalan dengan Python standard library yang sudah
  tersedia, tanpa network atau dependency baru. Query fokus di atas berhasil
  menghasilkan panduan fokus yang relevan. Tidak membuat design-system web
  otomatis, mengunduh font rekomendasi, atau mengganti font hanya karena
  katalog menyarankannya. Lisensi font game diperiksa tersendiri.
- Audio tetap memakai kanal music/ambience/SFX/UI native Ren’Py, fade/crossfade,
  dan uji dengar. Voice tidak ditambahkan. Animation tidak memerlukan Live2D:
  expression switch dan ATL adalah pilihan implementasi proyek; teknik
  internal game referensi hanya disebut bila ada bukti primer.

Permintaan lanjutan pengguna menambahkan Graphify. Graphify **0.9.102** sekarang
terpasang dalam environment pengembangan terpisah, dengan skill Codex asli,
lisensi dan provenance di `.agents/skills/graphify/`. Classifier upstream tetap
tidak mengenali `.rpy`; adapter proyek memberi evidence Ren'Py ke pipeline
build/cluster/export/query Graphify asli. Python memakai AST upstream. Graph,
query dengan kutipan baris, pemeriksaan freshness dan integrasi AI coding
didokumentasikan dalam [KNOWLEDGE_GRAPH.md](KNOWLEDGE_GRAPH.md).
Shader, backend, SEO, physics, dan tooling 3D tidak memiliki kebutuhan mekanik
di VN ini. Jumlah skill tidak menjadi ukuran kualitas; build, alur interaksi,
render, dan audio yang diuji menjadi bukti hasil.

## Creative Writing Skills (haowjy)

Pada 4 November 2026, permintaan eksplisit pengguna mengubah keputusan lama
untuk hanya membaca tautan: empat skill asli **sudah dipasang dan digunakan**
di `.agents/skills`. Sumber
[haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills/tree/1cb520f9c61e79ce2b1c56dba18601b2d6873433)
dipin pada `1cb520f9c61e79ce2b1c56dba18601b2d6873433`, Apache-2.0.

| Skill lokal | Metode yang diterapkan pada naskah lengkap |
|---|---|
| [writing-principles](../.agents/skills/writing-principles/SKILL.md) | *Trust the Reader*, *Economy*, `failure-modes` dan `antipatterns`: kurangi kesimpulan setelah gestur, jaga detail yang mengembangkan tokoh sekaligus menyiapkan payoff. |
| [creative-writing-craft](../.agents/skills/creative-writing-craft/SKILL.md) | `prose-modes` (*Revision*, *Line Polish*), `scene-construction`, dan `genre/romance`: revisi permukaan terkecil yang memperbaiki masalah, pertahankan kecanggungan, dialog timbal balik, dan tindakan konkret. |
| [story-review](../.agents/skills/story-review/SKILL.md) | Editorial sebelum line edit; review character, voice, continuity. Satu reviewer terpisah membaca semua adegan/sumber, lalu memeriksa diff akhir. |
| [story-memory](../.agents/skills/story-memory/SKILL.md) | `fact-extraction`: catat perubahan fakta per adegan, urutan pengakuan/pelukan/hadiah, pengetahuan tokoh, jadwal, benda, dan flag pilihan dalam story bible yang sudah ada. |

Keempat direktori memuat **37 berkas skill/resource upstream tanpa perubahan**,
empat salinan LICENSE, dan empat `UPSTREAM.json` berisi asal setiap berkas serta
SHA-256. Manifest lokal terpisah ini melengkapi indeks instalasi awal; indeks
lama tidak mengklaim mencakup instalasi baru. Lihat
[lisensi dan verifikasi instalasi](licenses/creative-writing-skills.md).

Tidak memasang Mars, Meridian, plugin Claude, agent upstream, hook, paket
Python/npm, CLI global, atau scaffold proyek; game tetap memakai Ren’Py dan
naskah yang sudah ada. Rujukan slash-command di skill adalah jalur baca
upstream, bukan klaim bahwa seluruh ekosistem terpasang. Script analisis
berbasis pola bahasa Inggris tidak dipakai sebagai skor mutu bahasa Indonesia.

Hasil pemakaian berupa audit **12 adegan / 3 bab / epilog**, revisi terarah
pada semua bagian itu, dan [STORY_AUDIT.md](STORY_AUDIT.md) dengan contoh
sebelum/sesudah. Lima menu, flag, label, callback pengujian, dan urutan sumber
tetap dipertahankan. Tidak ada klaim angka peningkatan kualitas atau durasi
pemain yang belum diukur.
