# Revisi antarmuka berbasis referensi ATRI

4 November 2026. Revisi ini mengikuti permintaan pengguna untuk mendekatkan
bahasa visual MADOROMI pada contoh ATRI yang disediakan di Drive. Lima gambar
sistem dipelajari langsung: display/teks, audio, keyboard/kontrol, save/load,
dan backlog. Salinan privat tetap di `/workspace/reference/ui/atri/` dan tidak
disertakan sebagai aset game.

## Keputusan visual

- Bidang krem dan heading serif menu sistem diganti dengan bidang putih kebiruan,
  header pesisir biru, heading sans besar, tab kanan atas, dan bingkai tipis.
  Ilustrasi halaman katedral milik proyek menjadi lapisan samar; tidak ada
  grafik, font, awan, logo atau kode ATRI yang disalin.
- Tab utama berukuran 180×108 pada kanvas 1920×1080. Heading berada di kiri,
  tab di kanan, isi mulai pada y=220, dan footer memiliki ruang tetap sendiri.
  Urutan navigasi serta tindakan native tidak berubah.
- Save/load mempertahankan empat slot besar dalam grid 2×2. Contoh ATRI memiliki
  sepuluh baris kecil; MADOROMI mengadaptasi hierarki thumbnail, nomor, waktu,
  kutipan, halaman, serta keadaan kosongnya untuk kebutuhan sentuh. Tombol hapus
  tidak bertumpuk dengan kutipan simpanan.
- Backlog memakai lapisan navy, teks putih, penanda pembicara berwarna terang,
  dan tombol kembali ke baris yang tersedia melalui `RollbackToIdentifier`.
  Pemisahan kolom serta kemampuan scroll native tetap dipakai.
- Pengaturan memakai judul bagian dan garis tipis, kontrol rata kiri, slider
  tipis dengan daerah sentuh besar, serta keadaan aktif yang jelas. Bantuan dan
  konfirmasi menggunakan palet dan ukuran kontrol yang sama.

## Skill dan implementasi

Impeccable 4.8.0 dipakai untuk hierarki, konsistensi mode membaca/operasi,
kualitas state, dan pemeriksaan hasil render. `reference/craft-floor.md`
dibaca sebelum penyuntingan. Konteks Impeccable sudah dimuat oleh workflow
induk; launcher tidak diulang.

UI UX Pro Max 2.15.0 dipakai melalui pencarian lokal `mobile touch target size
contrast focus spacing` pada domain `ux`. Hasil menegaskan target Android
48dp, jarak kontrol, dan indikator fokus. Grafik dekorasi dibuat memakai
`Solid`, `Composite`, `Frame` dan `Transform` bawaan Ren'Py; tidak ada framework
UI baru atau bitmap referensi yang disertakan. Lihat [SKILLS.md](SKILLS.md).

## Ukuran dan kontras

Kontrol utama, tombol konfirmasi, serta daerah sentuh slider tetap setinggi
108 unit virtual. Pada kalibrasi 1280×720 dengan densitas 240dpi, tingginya
72 piksel fisik atau 48dp. Ini adalah kalibrasi viewport pengujian, bukan
klaim ukuran fisik yang identik untuk seluruh ponsel.

| Pasangan teks / permukaan | Rasio kontras terhitung |
| --- | --- |
| `#153d5a` / `#f3faff` | 10,79:1 |
| Putih / tombol terpilih `#176f96` | 5,60:1 |
| Putih / tab biru `#1e648a` | 6,47:1 |
| Putih / slot kosong `#48749a` | 4,95:1 |

Rasio dihitung dari warna sRGB solid. Header berilustrasi serta state lain
tetap perlu dilihat pada screenshot runtime; angka ini tidak menggantikan
pemeriksaan visual atau menyatakan seluruh game sudah diaudit aksesibilitas.

## Verifikasi

`renpy.sh /workspace/madoromi compile` dan whitespace check untuk dua berkas
UI lulus setelah perubahan ini. Pengujian fungsional penuh, screenshot pada
1280×720, dan pengujian APK dilakukan secara terpusat setelah penyutradaraan,
ilustrasi jeans, serta layar cerita dari workflow induk selesai. Dokumen ini
tidak mengklaim APK revisi sudah dibangun atau diuji.
