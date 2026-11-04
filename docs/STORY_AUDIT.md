# Audit dan polish naskah MADOROMI

Tanggal: 4 November 2026. Lingkup: seluruh [game/story.rpy](../game/story.rpy), dua belas adegan, tiga bab, dan epilog. Audit dimulai dari naskah lengkap yang sudah ada pada baseline `c3cf727`; bukan membuat cerita atau demo baru. Cerpen asli, label engine, lima menu, lima flag, dan callback pengujian dipertahankan.

## Diagnosis dan urutan kerja

Janji pembuka adalah romance hangat tentang dua orang yang sudah saling memperhatikan, tetapi belum berani menamai kedekatannya. Janji itu dipenuhi oleh pengakuan timbal balik, pelukan, hubungan yang dipastikan, hadiah, dan kehidupan sesudahnya. Struktur tidak memerlukan penggantian bab, konflik tambahan, atau ending baru.

Kekuatan utama naskah adalah perhatian yang bisa dilihat: karton yang dibawa bersama, ombak telur, tiket ikan, kursi yang ditarik terlalu jauh, remah roti, dan gambar yang sengaja menyisakan ruang. Aoi juga mempunyai pekerjaan dan kehendaknya sendiri. Ia membeli tiket, meminta Ren tinggal, mengajak pergi, menentukan kesempatan Senin, membalas perasaan, memulai pelukan, menanyakan status hubungan, dan memilih memakai hadiah.

Masalah dominan adalah penjelasan sesudah tindakan yang sudah berhasil menyampaikan makna. Beberapa tokoh juga sesekali berbicara terlalu lancar tentang hubungan dibanding kecanggungan mereka di bagian lain. Revisi memusatkan tiga prioritas:

1. Lengkapi dua detail sumber yang belum sama jelasnya pada semua jalur: pengakuan gugup dalam cabang `plain` dan percakapan tentang kapan Ren mulai jatuh cinta.
2. Perbaiki waktu, sudut pandang, serta penempatan benda yang dapat mengusik pembacaan.
3. Pangkas kesimpulan berulang dan ubah beberapa penjelasan menjadi tindakan atau percakapan yang sesuai suara tokoh.

Dua belas adegan dibaca seluruhnya sebelum diagnosis tertulis dan sebelum penyuntingan. Setelah diagnosis struktur, pass kedua memeriksa suara, kalimat, dan kontinuitas. Reviewer terpisah membaca seluruh snapshot awal beserta cerpen/bible, lalu memeriksa diff akhir. Temuannya disintesis; naskah tidak mengikuti setiap kemungkinan perubahan hanya karena disebut dalam review.

## Skill yang benar-benar dipasang dan digunakan

Sumber: [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills/tree/1cb520f9c61e79ce2b1c56dba18601b2d6873433), commit `1cb520f9c61e79ce2b1c56dba18601b2d6873433`, Apache-2.0. Empat skill lokal memuat 37 berkas skill/resource upstream tanpa perubahan, salinan LICENSE, serta manifest asal dan SHA-256. [Bukti instalasi](licenses/creative-writing-skills.md).

| Skill / bagian metode | Penerapan yang dapat diperiksa |
|---|---|
| [writing-principles](../.agents/skills/writing-principles/SKILL.md), *Trust the Reader* dan *Economy* | Hapus kesimpulan moral setelah Sora meminta maaf, penjelasan niat hadiah yang berulang sebelum pemberian, dan ringkasan makna pelukan/genggaman. Pertahankan tindakan serta dialog yang sudah menyampaikan hal itu. |
| `writing-principles/resources/failure-modes.md` dan `antipatterns.md` | Cari pola *tidy-summary endings*, komentar emosional, suara seragam, dan gerakan berulang. Pola dinilai dalam konteks, bukan dianggap bukti asal tulisan atau alasan menghapus semua pengulangan. |
| [creative-writing-craft](../.agents/skills/creative-writing-craft/SKILL.md), `prose-modes` | Pakai *Revision* dan *Line Polish*: ubah bagian terkecil yang menyelesaikan temuan; pertahankan adegan yang sudah bekerja, humor, jeda, dan kecanggungan yang disengaja. |
| `creative-writing-craft/resources/scene-construction.md` dan `genre/romance.md` | Periksa perubahan hubungan dalam tiap adegan, dialog yang mengembangkan tokoh sekaligus ketegangan, serta chemistry lewat bantuan, waktu yang dipilih, gerak dan respons timbal balik. |
| [story-review](../.agents/skills/story-review/SKILL.md), `editorial-review`, `line-edit`, `prose-critique/character`, `voice`, `continuity` | Dahulukan janji cerita/struktur, kemudian suara dan detail. Temuan memakai adegan tertentu, akibat bagi pembaca, dan tindakan revisi; termasuk pemeriksaan independen sebelum/sesudah. |
| [story-memory](../.agents/skills/story-memory/SKILL.md), `fact-extraction` | Cocokkan perubahan keadaan tokoh, jadwal, benda, pengetahuan, dan hubungan antarscene dengan ledger [STORY.md](STORY.md). Tidak membuat sistem memori/backend baru. |

Tidak ada skor otomatis kualitas prosa atau klaim peningkatan persentase. Script upstream yang menganalisis pola bahasa Inggris tidak dipakai sebagai penilai mutu bahasa Indonesia. Metode editorial dipakai melalui pembacaan dan revisi teks yang sebenarnya.

## Peninjauan semua adegan

| Adegan | Fungsi dan hasil review | Revisi / keputusan akhir |
|---|---|---|
| 1 · Selasa dini hari | Mengubah rasa ingin tahu kecil menjadi kebiasaan yang ditunggu. Obrolan semut, kantuk, tiket, dan poster sekaligus menyiapkan payoff. Ritme pesan pendek dan saling menyela sudah alami. | Narasi latihan `besok` diperjelas menjadi `sore nanti`, sebab jam sudah melewati tengah malam dan latihan terjadi Selasa. Perbandingan harga tiket diperhalus. `Besok` dalam chat tetap dipakai sebagai ujaran menjelang tidur yang wajar. |
| 2 · Kantin | Aoi memilih ditemani; pemain menentukan cara memberi perhatian. Proyek Aoi mempunyai masalah nyata, bukan sekadar alasan menunggu Ren. Humor kursi dan buku terbalik membedakan respons. | Akhiri adegan pada soal matematika yang tidak selesai; hapus kalimat tambahan yang menilai makan siang itu produktif. Permintaan Aoi tinggal dan kedua pilihan/callback tetap utuh. |
| 3 · Pertokoan dan bakery | Kedekatan dibangun lewat kerja kecil dan percakapan tentang gambar. Selera, ukuran jeans, kebiasaan bakery, dan alasan nyaman ditanam sebelum pengakuan/hadiah. | Aksi memeriksa jeans diperjelas menjadi membentangkan pinggang celana, bukan membandingkan label dengan tubuh. Label masih terlihat oleh Ren; pembelian ukuran yang sama nanti tetap punya dasar. Percakapan roti dan alasan Aoi nyaman dipertahankan. |
| 4 · Beanbag | Pertanyaan Mio menaikkan tekanan. Sepuluh detik diberi ruang lewat bunyi troli, warna, dan bungkus lem; tidak perlu countdown yang mengunci input. Kedua tokoh sama-sama belum dapat menjawab. | Pikiran Ren tentang menjawab untuk Aoi diperjelas. Mio beralih dengan pertanyaan konkret `Aku boleh duduk?`. Setelah Ren menjawab `Kamu juga`, Aoi mengambil pensil lagi; maknanya tidak dijelaskan ulang. |
| 5 · Band | Aoi memilih hadir setelah kecanggungan. Kontras Ren mengingat kesalahan dan Aoi mengingat tawa memperlihatkan ketertarikan yang spesifik. | Pengamatan panggung dibatasi pada tangan/wajah Aoi yang terlihat, bukan keadaan pikirannya. Respons tentang lagu menjadi permintaan mendengar versinya lagi. Penutup memakai kabel yang lepas, tanpa merangkum kegagalan komunikasi. |
| 6 · Kamis | Kesempatan gagal karena dua rencana yang Ren sendiri tidak jelaskan. Sora tetap teman praktis yang berniat baik; Ren akhirnya meminta waktu berdua secara eksplisit. | Diksi sepatu dalam ruangan diperjelas. Respons Ren pada Aoi yang meminta kertas menjadi gestur kecil. Sora memakai gurauan kereta ketika membahas pulang. Bola kertas dan tindakan meratakannya menggantikan penjelasan pelajaran yang baru dipahami Ren. |
| 7 · Jumat | Proyek mulai dimiliki banyak orang; undangan menggambar yang tidak sempurna mempunyai hasil. Aoi ikut menyediakan kesempatan Senin. Pembelian jeans mengikuti persiapan yang sudah terlihat. | `Kemarin lusa` menjadi `dua hari lalu`. Hapus uraian bahwa Mio tidak menggoda dan Ren berterima kasih; Mio langsung bekerja. Penutup bergerak ke buku sketsa. Izin keluar dan jam kerja tetap eksplisit agar rencana Senin masuk akal. |
| 8 · Akhir pekan | Perhatian menjadi benda; kegugupan tetap belum selesai walau hadiah sudah dibuat. Proses cat, pengeringan, fiksasi, dan kartu perawatan membuat benda itu nyata. | Keraguan ditunjukkan melalui menebalkan catatan, menatap gagang lemari saat latihan, serta membetulkan letak kartu berulang. Aktivitas Aoi selepas chat 20.38 menjadi mencuci piring. Pilihan pengakuan, dua warna, dan catatan agar hadiah diberikan sesudah bicara dipertahankan. |
| 9 · Senin ke bakery/pohon | Rencana dijalankan. Kedua tokoh memilih datang; apel cadangan dan kantong roti mengisi ketegangan dengan kebiasaan mereka sendiri. | Kalimat pintu `terbuka pukul 11.37` menjadi tindakan mereka mendorong pintu pada jam itu, agar tidak terbaca sebagai pernyataan jam buka toko. Geografi, perjalanan, dan posisi awal kantong hadiah tetap konsisten. |
| 10 · Pengakuan | Sepuluh menit basa-basi dibayar dengan cinta yang diucapkan jelas dan jawaban Aoi. Humor setelah `Oh` mengembalikan napas tanpa menunda penerimaan. | Cabang `plain` sekarang juga mengucapkan kegugupan sebelum kalimat cinta yang lama. Tangan sibuk melipat bungkus; hadiah tetap di kaki. Hapus penjelasan panjang tentang hadiah yang sudah ditanam pada adegan 8 dan akan ditegaskan saat pemberian. |
| 11 · Percakapan, pelukan, hadiah | Keduanya membandingkan pengalaman, memberi ruang pada kata-kata yang belum siap, berpelukan, memastikan hubungan, baru memberi hadiah. Seluruh urutan sumber terjaga. | Tambahkan jawaban Ren tentang perasaan yang mulai ia kenali di kantin. Awal perkenalan diberi konteks kegiatan liburan. Dialog tentang jadwal dibuat konkret lewat pilihan panel/rekaman, botol dan roti dipindahkan sebelum pelukan, serta beberapa ringkasan makna dihapus. Hadiah tetap baru dibuka sesudah penerimaan, pelukan, dan kesepakatan berpacaran. |
| 12 · Afterstory | Jeans benar-benar dipakai dan mendapat noda, panel selesai, band berlanjut. Hubungan mengubah cara membuat rencana tanpa menghapus kegiatan masing-masing. Selamat malam menutup motif awal. | Penjelasan bahwa mereka kini tidak membutuhkan alasan bertemu diganti dengan Ren langsung bertanya waktu besok dan Aoi mengecek jadwalnya. Kedua opsi kebiasaan malam dan narasi penutup tetap memberi rasa selesai, bukan teaser rute lanjutan. |

## Contoh sebelum / sesudah

| Temuan | Sebelum | Sesudah dan tujuan |
|---|---|---|
| Waktu latihan, adegan 1 | `tidak terlambat latihan besok` | `tidak terlambat latihan sore nanti`: pembaca tidak memindahkan latihan ke Rabu. |
| Aksi jeans, adegan 3 | `Ia membandingkan label itu dengan pinggangnya` | `Ia membentangkan bagian pinggang celana di depan tubuhnya`: aksi dapat dibayangkan dan ukuran hadiah tetap ditanam. |
| Batas POV, adegan 5 | `Aoi menatap panggung tanpa sedang menyiapkan apa pun untuk dikatakan` | `tangan Aoi diam di atas tas. Wajahnya terangkat ke arah panggung`: Ren hanya melaporkan yang terlihat. |
| Suara Sora, adegan 6 | `Aku tidak tersinggung` | `Aku bisa naik kereta sendiri`: niat baik disampaikan lewat urusan praktis dan gurauan teman. |
| Kesimpulan sesudah aksi, adegan 6 | `Tidak ada orang yang mencuri kesempatanku. Aku belum meminta kesempatan itu dengan benar.` | Ren membuka dan meratakan kertas latihan di samping ponsel. Pembaca menyimpulkan perubahan dari percakapan sebelumnya. |
| Kejelasan sumber, adegan 10 | Cabang `plain` langsung mengucapkan cinta | `Aku gugup. Padahal sudah latihan.` ditambahkan sebelum pengakuan lama; sumber terjaga pada kedua opsi. |
| Perasaan Ren, adegan 11 | Ren terutama menyebut alasan menyukai Aoi | Aoi bertanya apakah ia sudah suka di kantin; Ren mengakui belum berani menamainya dan berharap jam bel salah. Momen yang telah dimainkan kini memperoleh jawaban dari kedua pihak. |
| Suara dan chemistry, adegan 11 | Dialog menjelaskan kewajiban menyediakan waktu untuk kegiatan masing-masing | `Aku pilih panel. Kamu kirim rekamannya.` diikuti permintaan rekaman saat Ren tertawa. Aoi punya pilihan, perhatian, dan humor dalam ujaran yang sama. |
| Blocking pelukan, adegan 11 | Kantong roti tetap disebut berada di antara tubuh mereka | Aoi memindahkan botol dan kantong roti ke sisi luar bangku sebelum mendekat. Aroma roti hangat setelah hampir satu jam juga diganti detail sabun pada kerah. |
| Penutup afterstory, adegan 12 | Narator menerangkan bahwa ia tak perlu menciptakan alasan bertemu | Ren bertanya `Besok ada waktu?`; Aoi dari anak tangga bus menjawab akan mengecek. Perubahan hubungan tampak melalui tindakan. |

## Suara, bahasa, dan keputusan yang dipertahankan

**Ren** memperhatikan benda, kabel, posisi tangan, noda, dan kalimat yang gagal ia ucapkan. Ia tetap canggung; revisi tidak membuat semua pikirannya bijak atau semua percakapannya lancar. **Aoi** mengamati hal kecil, menindaklanjuti rasa ingin tahu, serta menyela gurauan dengan permintaan konkret. **Sora** membaca urusan yang disampaikan jelas dan kembali pada alat musik/kereta. **Mio** singkat, langsung, dan membawa pekerjaan panitia. Bahasa Indonesia tetap memakai register `aku/kamu` dengan narasi sedikit lebih rapi; tidak menambahkan sapaan/honorifik Jepang atau slang lokal yang mengubah suara seluruh proyek.

Pengulangan semut, ombak telur, ikan tiket, stasiun, selamat malam, dan sepuluh detik sengaja dipertahankan karena maknanya berubah ketika kembali. Tidak setiap gestur menunduk atau menarik napas dihapus; beberapa diperlukan untuk tekanan adegan dan teks yang terbagi ke layar kecil. Pernyataan cinta serta status hubungan juga tetap eksplisit: subteks tidak dipakai untuk menyamarkan keputusan akhir yang diminta sumber.

Pertengahan September tetap berada di kota pesisir Kazehama dan SMA Minato yang fiktif di Jepang. Kegiatan liburan menjelaskan pertemuan awal sekitar Agustus. Izin makan di luar pada Senin berasal dari jadwal acara khusus yang tertulis, bukan klaim kebiasaan umum sekolah Jepang. Katedral tetap bangunan fiktif yang menjadi petunjuk jalan, dengan adegan berada di halaman terbuka dekat pohon.

Review menemukan jadwal 13.15–13.30 cukup rapat tetapi masih mungkin: berkemas/hadiah, perjalanan sekitar delapan menit, kembali empat menit sebelum giliran kerja. Tidak ditambahkan waktu tunggu atau perhentian baru yang membuat mereka terlambat. Adegan ini tetap layak diperiksa dalam playtest ritme; waktu diegetik bukan waktu pembacaan layar.

## Kontinuitas dan verifikasi

Kontrak yang dicek: malam sampai pukul dua; percakapan semut; band/tiket; permintaan tinggal di kantin; satu beanbag dan sepuluh detik; Kamis terhalang teman; persiapan jeans; Senin bakery/pohon di luar katedral; gugup/cinta/jawaban; perkenalan dan kapan perasaan tumbuh; izin pelukan; sekitar satu setengah jam; status berpacaran; jeans diberikan sesudah penerimaan; afterstory yang selesai. Hadiah tidak berfungsi sebagai alat mendapatkan jawaban.

Lima label utama dan seluruh target jump tetap sama. Kelima pasangan opsi menu, nama/nilai flag, dan fragmen callback yang dibaca pengujian native tidak berubah. Pilihan warna konsisten pada gambar bersama, proses jeans, dan respons penerimaan. Tidak menambah rute gagal, poin afeksi, menu, atau dependency.

Hasil pemeriksaan pada revisi ini:

- `python3 tests/check_story.py`: **PASS**, 12 adegan, 7.540 kata narasi/dialogue, lima keputusan biner. Ini pemeriksaan kontrak teks; tidak dianggap bukti memainkan 32 kombinasi.
- `tools/build.sh lint` dengan Ren’Py 8.5.3: **exit 0**, tanpa diagnostic kesalahan; 732 blok dialogue / 7.518 kata menurut hitungan engine.
- Integritas empat instalasi skill: semua berkas sesuai byte upstream dan semua SHA-256 manifest cocok.
- Pemeriksaan diff independen: tidak menemukan regresi struktur, urutan sumber, atau revisi berlebihan. Satu saran diksi sepatu diterapkan.
- Sumber tetap utuh: SHA-256 `docs/source/cerita-asli.txt` adalah `d1d4b6e72dd344cdce0af377152153f9c9f3be570c9cc913f2cb9153c06eb2ab`; `cerita-asli.docx` adalah `38585d3821448c158b760206b4fb0b5258bb150780de02946d401cd7cc564438`, sama sebelum dan sesudah pass.

Ukuran teks berubah dari 7.601 menjadi 7.540 kata narasi/dialogue pada pemeriksa yang sama. Ini mengukur lingkup teks, bukan mutu. Seluruh string berpetik setelah revisi berjumlah 8.248 kata dengan hitungan whitespace, termasuk teks alternatif dan identifier teknis. Tidak ada klaim durasi sesi atau skor kualitas dari angka tersebut.

Pengujian UI, save/load/rollback, seluruh opsi dan callback di engine, screenshot, serta build Android tetap dilaporkan dalam [VERIFICATION.md](VERIFICATION.md). Bukti native sebelum revisi tidak diberi tanggal ulang atau diperlakukan sebagai pengujian naskah baru.
