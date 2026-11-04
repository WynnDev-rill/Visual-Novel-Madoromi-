# MADOROMI — Sepuluh Detik

Visual novel romance berbahasa Indonesia, berlatar kota pesisir Jepang yang fiktif. Ren dan Aoi sudah terbiasa mengobrol hingga larut malam. Sebuah pertanyaan sederhana membuat keduanya berhenti selama sepuluh detik—dan mulai memikirkan apa yang ingin mereka katakan.

Cerita utuh dalam **tiga bab, dua belas adegan, dan epilog**, dikembangkan dari naskah asli pengguna. Lima pilihan memengaruhi percakapan dan respons berikutnya, tanpa poin afeksi atau hukuman tersembunyi. Perkiraan durasi baca 40–60 menit; waktu bergantung pada kecepatan membaca.

## Bermain

Unduh APK bertanda **Android** dari [Releases](https://github.com/WynnDev-rill/Visual-Novel-Madoromi-/releases). Salin ke ponsel, buka berkasnya, lalu izinkan pemasangan dari pengelola berkas ketika Android meminta. Game dimainkan secara offline dalam orientasi landscape; minimum Android 5.0 dengan OpenGL ES 3.0.

Ketuk untuk membaca dan pilih jawaban tanpa batas waktu. Tersedia simpan/muat, simpan otomatis native, rollback, riwayat, mode otomatis, lewati, pilihan bab, ukuran teks, pengurangan gerakan, serta pengaturan musik/efek/suasana terpisah. Tidak ada voice acting karakter.

Desktop: ekstrak paket PC, lalu jalankan `Madoromi.exe` di Windows atau `Madoromi.sh` di Linux. Enter/Spasi melanjutkan, Escape membuka menu, Page Up kembali, dan H menyembunyikan antarmuka.

## Presentasi

Referensi UI ATRI dan Please Be Happy yang disediakan melalui Google Drive menjadi dasar revisi tata letak: ilustrasi mendapat ruang lebih besar, dialog terang, narasi terpisah, navigasi sistem berbentuk tab, serta tombol yang lebih nyaman disentuh. The NOexistenceN of you AND me menambah referensi ekspresi dan perpindahan komposisi. Ilustrasi, font, musik, dan kode ketiga game tersebut tidak disalin.

Karakter menggunakan sprite 2D berekspresi dari satu keluarga aset berlisensi, dengan dissolve dan staging native Ren'Py. Latar dan audio matang diprioritaskan; tiga lokasi spesifik dan prop hadiah dilengkapi ilustrasi orisinal buatan AI. Ikon aplikasi memakai master pilihan pengguna dari Drive.

## Mengembangkan dan membangun

Menggunakan **Ren'Py 8.5.3**, RAPT, JDK 21, dan Android SDK 36. SDK, cache dan kunci signing berada di luar Git.

```bash
tools/build.sh bootstrap
python3 -m pip install Pillow
python3 tools/acquire_visuals.py --cache /tmp/madoromi-visuals
tools/build.sh lint
tools/build.sh run
# Mesin Linux tanpa display:
xvfb-run -a tools/build.sh test
tools/build.sh desktop
tools/build.sh bootstrap-android
tools/build.sh android
```

Petunjuk lengkap, dependensi, signing, dan perintah instalasi ADB: [docs/BUILD.md](docs/BUILD.md). Kunci signing pertama disimpan secara privat di direktori toolchain; cadangkan untuk mempertahankan kemampuan memperbarui aplikasi.

## Dokumentasi

- [Desain](docs/DESIGN.md), [naskah dan kontinuitas](docs/STORY.md), [benchmark](docs/BENCHMARKS.md).
- [Hasil verifikasi](docs/VERIFICATION.md) dan [pengujian native](tests/README.md).
- [Skill yang dipakai](docs/SKILLS.md) dan [panduan agen](AGENTS.md).
- [Kredit dan lisensi](THIRD_PARTY_NOTICES.md), [register visual](docs/licenses/visual-art.md), [audio](docs/licenses/audio.md), [font](docs/licenses/fonts.md).

Aset karakter/latar pihak ketiga tidak dipublikasikan sebagai gambar mandiri di repository; skrip akuisisi mengambilnya dari kreator untuk bundel game. Hak cerita dan ikon sumber tidak digantikan oleh lisensi engine. Asal serta batas dokumentasi hak ikon tercatat di [docs/licenses/icon.md](docs/licenses/icon.md).
