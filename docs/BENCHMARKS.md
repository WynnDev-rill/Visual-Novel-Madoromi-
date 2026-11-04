# Benchmark presentasi MADOROMI

Ditinjau 3 November 2026. Catatan ini memakai halaman pengembang/penerbit,
screenshot resmi Steam, dan 30 detik pertama video resmi yang tercantum di Steam.
Screenshot dan video diamati sebagai bukti hasil tampilan, bukan bukti kode atau
format aset internal. Materi riset tersimpan di luar repo pada
`/workspace/downloads/benchmarks-research/`; tidak dimasukkan ke game.

## Yang dapat diverifikasi

| Referensi | Fakta tampilan atau sumber primer | Prinsip yang cocok untuk MADOROMI |
|---|---|---|
| **ATRI -My Dear Moments-** | Screenshot resmi menunjukkan menu vertikal di kiri (`CONTINUE`, `START`, `LOAD`, `SYSTEM`, `EXTRA`, `INFORMATION`, `EXIT`) di atas ilustrasi dunia. Adegan dialog memakai area bawah transparan, nama terpisah, dan toolbar kecil kanan bawah dengan `Auto`, `Skip`, `Log`. Gambar karakter dan latar tetap menjadi bidang terbesar. [Halaman dan screenshot resmi Steam](https://store.steampowered.com/app/1230140/ATRI_My_Dear_Moments/), [screenshot dialog](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1230140/ss_bdbf991588b1589c9efadf9351fc36521ca80e0b.1920x1080.jpg). | Title screen mengundang masuk ke dunia; hierarki menu tenang; textbox cukup memberi kontras tanpa menjadi panel aplikasi yang dominan. Ukuran toolbar pada screenshot PC bukan standar ukuran sentuh Android. |
| **The NOexistenceN of you AND me** | Screenshot resmi memakai ilustrasi dengan palet merah/putih/biru gelap, subtitle putih ber-outline langsung di atas gambar, nama beraksen, dan `History`/`Options` di bawah. Pilihan diletakkan di tengah adegan. Pada video resmi **Gameplay footage~** sekitar 6–18 detik terlihat ilustrasi ditahan, pergantian komposisi/pose, gerak posisi, lalu fade karakter. [Halaman, screenshot, dan video resmi Steam](https://store.steampowered.com/app/2873080/The_NOexistenceN_of_you_AND_me/), [screenshot pilihan](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2873080/ss_4b62db0b4506aa78b106cc8c2df5d1217325791b.1920x1080.jpg). | Perubahan ekspresi, framing dan perpindahan adegan dapat membuat presentasi hidup. Ambil disiplin palet dan staging; bentuk horor, glitch, serta kontras ekstremnya tidak cocok dengan nada romansa hangat MADOROMI. |
| **Please Be Happy** | Screenshot resmi memperlihatkan balon dialog krem dekat karakter, nama berwarna, narasi terpisah di bawah dengan gradient gelap, bingkai sudut dekoratif tipis, penanda waktu, serta panel NVL untuk teks panjang. Ada layar peta berilustrasi. Video resmi **Main PV EN** memperlihatkan fade dan perubahan framing; video promosi tidak membuktikan seluruh gerak tersebut terjadi dalam gameplay. [Halaman dan screenshot resmi Steam](https://store.steampowered.com/app/844670/Please_Be_Happy/), [screenshot narasi dan dialog](https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/844670/117ed898009a39158b43fd5b6e7cd88a8379bfe5/ss_117ed898009a39158b43fd5b6e7cd88a8379bfe5.1920x1080.jpg). | Dekorasi kecil yang konsisten, teks berjarak nyaman, warna hangat, dan latar yang tetap terbaca. MADOROMI tetap memakai satu sistem ADV agar percakapan panjang dan layar kecil tidak membutuhkan reposisi balon per baris. |

**Menu dan kenyamanan membaca.** Pengembang Please Be Happy mendokumentasikan
Episode Replay, galeri CG, quick menu yang dapat disembunyikan, serta tombol
cancel yang konsisten pada versi 1.2. Catatan itu juga menyatakan navigasi seluruh
menu dengan keyboard/controller belum lengkap pada versi tersebut; jangan
menganggapnya klaim kondisi versi terbaru. Catatan 2.0.6 mengonfirmasi penggunaan
NVL dan perbaikan posisi/layout. [Devlog 1.2](https://vnstudioelan.itch.io/please-be-happy/devlog/722126/please-be-happy-12),
[devlog 2.0.6](https://vnstudioelan.itch.io/please-be-happy/devlog/1564642/please-be-happy-206-205-204-203-202).

**Audio.** Sumber resmi ATRI mencantumkan Fuminori Matsumoto sebagai komposer dan
Yow pada kredit animasi. Please Be Happy mencantumkan soundtrack orisinal; paket
gratis **Demo 2.0.6 — Extras and Documentation**, berkas `Sound Effect
Attribution.txt`, secara eksplisit mencatat penggunaan SFX dari beberapa sumber.
Ini mendukung pemisahan fungsi musik dan efek, bukan peniruan track, mixing, atau
voice mereka. MADOROMI tidak menggunakan voice acting sesuai brief.
[Kredit resmi ATRI](https://store.steampowered.com/app/1230140/ATRI_My_Dear_Moments/),
[halaman dan dokumentasi demo resmi Please Be Happy](https://vnstudioelan.itch.io/please-be-happy).

## Teknik sprite: hasil pengamatan dan batas bukti

- **Teramati:** ilustrasi 2D, pose/ekspresi berbeda, framing, pergantian gambar,
  fade dan perpindahan posisi. Sampel video NOexistenceN menunjukkan gambar yang
  ditahan selama sebagian dialog; sampel itu tidak membuktikan seluruh game
  menggunakan satu teknik saja.
- **Belum dikonfirmasi dari sumber primer yang dibaca:** rig Live2D, E-mote,
  format sprite, dan engine ATRI/NOexistenceN. Kata “animation” pada kredit atau
  sebuah screenshot tidak mengidentifikasi teknologinya.
- **Pembedaan penting:** bundle resmi menyebut **The NOexistenceN of Lilith**,
  aplikasi companion desktop yang terpisah, sebagai Live2D. Pernyataan itu tidak
  berlaku otomatis untuk VN **The NOexistenceN of you AND me**.
  [Deskripsi bundle resmi](https://store.steampowered.com/bundle/81409/?l=english).
- **Engine Please Be Happy dikonfirmasi pengembang:** game penuh memakai
  Unity/Naninovel; demo lama memakai Ren’Py. Jangan menggeneralisasi dari demo
  lama ke seluruh rilis. [Jawaban pengembang](https://itch.io/t/3132870/blind-accessibility),
  [devlog versi PC 2.0.6](https://vnstudioelan.itch.io/please-be-happy/devlog/1564642/please-be-happy-206-205-204-203-202).

**Keputusan implementasi MADOROMI, bukan klaim tentang benchmark:** gunakan
ekspresi/pose 2D yang tersedia dengan image attributes atau `layeredimage`,
transisi pendek, dan ATL untuk posisi, zoom, serta reaksi sesekali yang mengikuti
dialog. Hentikan gerak selama teks perlu dibaca; beri momen diam pada pengakuan.
Ren’Py mendukung komposisi sprite dan transformasi ini secara native. Live2D
adalah jalur tersendiri yang memerlukan model/rig dan Cubism SDK; jangan menyebut
animasi sprite PNG sebagai Live2D.
[Layered images](https://www.renpy.org/doc/html/layeredimage.html),
[ATL dan transforms](https://www.renpy.org/doc/html/transforms.html),
[integrasi Live2D resmi](https://www.renpy.org/doc/html/live2d.html).

## Typography dan penerapan sekarang

Nama font utama ketiga VN belum diverifikasi dari sumber primer yang dibaca.
Tampilan serif pada Please Be Happy atau sans pada menu ATRI adalah pengamatan
bentuk, bukan identifikasi keluarga font. Jangan menamai font dari kemiripan.
Catatan 2.0.3 Please Be Happy menyebut perbaikan varian font Unihan untuk
lokalisasi, tanpa mengidentifikasi font utama. [Devlog resmi](https://vnstudioelan.itch.io/please-be-happy/devlog/1564642/please-be-happy-206-205-204-203-202).

Prioritas polish: satu keluarga dekorasi hangat untuk title/save/history/settings;
textbox dengan gradient gelap dan aksen nama; tombol sentuh yang cukup luas;
teks Indonesia dibaca pada ukuran kirim; fungsi save/load, history, auto, skip,
rollback dan preferences tetap native. Ekspresi serta penekanan kamera harus
mengikuti emosi naskah. Benchmark menjadi referensi prinsip dan pengujian, tidak
menjadi sumber aset, logo, musik, atau template yang disalin.
