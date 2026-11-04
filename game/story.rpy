# MADOROMI — adaptasi orisinal berbahasa Indonesia.
# Sumber cerita tidak diubah. Lihat docs/STORY.md untuk ledger dan kontinuitas.

default story_reply = "listen"
default story_company = "quiet"
default story_color = "blue"
default story_courage = "plain"
default story_promise = "goodnight"

label start:
    jump act_1

label act_1:
    $ aoi_outfit = "school"
    $ persistent.chapter_unlocked = max(persistent.chapter_unlocked, 1)
    call chapter_card("I", "Malam yang Menjadi Kebiasaan", "Ada pesan yang selalu kutunggu.")

    # SCENE 01 · Selasa, 01.43 · kamar Ren.
    scene bg bedroom with fade
    play ambience "audio/ambience/night.ogg" fadeout 1.0 fadein 1.5 volume .38
    play music audio.night fadein 2.0
    "Ponselku bergetar ketika ujung pensil hampir menyentuh kertas."
    "Di layar, foto sebutir remah roti tampak sebesar batu. Ada semut di sebelahnya."
    call phone_chat([("aoi", "Menurutmu dia tahu rotinya terlalu besar?"), ("ren", "Jam berapa semut pulang kerja?"), ("aoi", "Ren. Jawab pertanyaanku dulu."), ("ren", "Mungkin dia optimis."), ("aoi", "Tadi dia kembali membawa teman.")], "01.43")
    "Aku memperbesar foto itu. Latar belakangnya bagian bawah pot di teras rumah Aoi."
    "Semut kedua hanya kelihatan sebagai titik gelap. Aku tetap bisa melihat remah yang diperebutkan."
    "Buku matematikaku terbuka di soal yang sama sejak empat puluh menit lalu. Di bawah siku ada sketsa poster band yang belum selesai."
    "Sekarang aku meneliti semut."
    call phone_chat([("ren", "Mereka berhasil?"), ("aoi", "Belum. Rotinya tersangkut."), ("aoi", "Aku mau membantu, tapi kalau kupindahkan mereka mungkin kehilangan jejak."), ("ren", "Kamu masih di teras?"), ("aoi", "Sudah di kamar. Foto dari sore tadi.")], "01.45")
    "Sudah hampir satu setengah bulan kami mengobrol seperti ini."
    "Kadang tugas sekolah. Kadang lagu yang kudengar di kereta. Kadang Aoi mengirim foto benda yang tidak akan kuperhatikan kalau berjalan sendirian."
    "Sebuah payung yang ditambal dengan selotip bergambar ikan. Bayangan pagar yang kelihatan seperti partitur. Harga stroberi yang, menurutnya, sedang bertindak keterlaluan."
    "Selalu ada pesan selamat malam di ujungnya."
    "Aku mulai mengenali kapan pesan itu sungguh berarti ia akan tidur, dan kapan ia hanya mengetik sambil mencoba melawan kantuk."
    call phone_chat([("aoi", "Aku membaca sedikit soal jalur semut."), ("ren", "Definisi sedikit?"), ("aoi", "Tiga artikel."), ("aoi", "Dan satu video yang terlalu panjang."), ("ren", "Kita mulai membahas ini jam berapa?"), ("aoi", "Jangan lihat jam.")], "01.47")
    "Aku melihat jam. Tentu saja."
    "Nyaris satu jam sejak ia bilang, ‘Ada hal aneh di teras.’"
    "Di grup band, Sora mengirim pesan agar kami tidak terlambat latihan sore nanti. Aku menandainya sudah dibaca, lalu kembali ke percakapan Aoi."
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        "Aoi masih ingin bercerita."
        "Dengarkan apa yang membuatnya penasaran.":
            $ story_reply = "listen"
            call phone_chat([("ren", "Bagian mana yang paling kamu suka?"), ("aoi", "Mereka bisa memilih jalur lebih pendek tanpa melihat seluruh jalan."), ("aoi", "Aku bahkan bisa tersesat di toko alat tulis."), ("ren", "Kamu sengaja berlama-lama di rak warna."), ("aoi", "Itu juga benar.")], "01.49")
            "Aku meletakkan pensil. Poster band bisa menunggu dua menit lagi."
        "Ajukan pertanyaan yang sungguh ingin kutahu.":
            $ story_reply = "questions"
            call phone_chat([("ren", "Kalau jalan mereka kita putar, apa yang terjadi?"), ("aoi", "Jangan mengganggu semut, Ren."), ("ren", "Aku bertanya secara ilmiah."), ("aoi", "Sekarang aku juga penasaran. Tunggu, kucari."), ("ren", "Besok saja. Nanti semutnya lulus sebelum kita.")], "01.49")
            "Tiga titik muncul, hilang, lalu muncul lagi. Aku membayangkan ia menahan tawa agar tidak terdengar dari kamar sebelah."
    call phone_chat([("aoi", "Besok kamu bawa poster band itu?"), ("ren", "Versi yang belum selesai."), ("aoi", "Aku mau lihat."), ("ren", "Tidak perlu beli tiket lagi. Kemarin kamu sudah beli satu."), ("aoi", "Aku mau lihat posternya, Ren."), ("aoi", "Tiketnya kusimpan baik-baik.")], "01.52")
    "Tiket pertunjukan hari Rabu lebih murah daripada makan siang di kantin. Aku sudah beberapa kali mengatakan itu pada diri sendiri."
    "Tetap saja, saat ia membelinya dari Sora tanpa menawar atau bertanya siapa lagi yang datang, aku menyetel gitar tiga kali padahal senarnya sudah benar."
    call phone_chat([("ren", "Kamu belum mengantuk?"), ("aoi", "Sedikit."), ("ren", "Sedikit yang mana? Tiga artikel?"), ("aoi", "Mataku sudah menutup sebelah."), ("ren", "Tidur, Aoi."), ("aoi", "Sebentar. Kamu belum bilang bagaimana posternya.")], "01.55")
    "Aku memotret kertas di meja. Sebuah gitar, nama band kecil kami, dan tiga bentuk yang seharusnya ombak."
    "Aoi memberi lingkaran pada salah satunya."
    call phone_chat([("aoi", "Yang ini seperti telur dadar."), ("ren", "Itu ombak."), ("aoi", "Ombak yang enak."), ("ren", "Aku perbaiki besok."), ("aoi", "Jangan semuanya. Sisakan satu.")], "01.57")
    "Di luar jendela, jalan sempit Kazehama sudah kosong. Angin dari arah pelabuhan menggesek kisi-kisi jendela."
    "Aku menulis angka kecil di sudut poster: 01.57. Entah untuk apa."
    call phone_chat([("aoi", "Kamu juga tidur. Besok latihan."), ("ren", "Setelah menyimpan pensil."), ("aoi", "Jangan menggambar satu jam lagi."), ("ren", "Baik."), ("aoi", "Selamat malam, Ren."), ("ren", "Selamat malam, Aoi.")], "02.00")
    "Layar padam. Kamar mendadak terasa lebih besar."
    "Aku menyimpan pensil sungguhan. Lalu, sebelum tidur, memeriksa apakah pesan terakhirnya masih ada."

    # SCENE 02 · Selasa siang · kantin SMA Minato.
    scene bg cafeteria with fade
    stop ambience fadeout 1.0
    play music audio.day fadeout 1.5 fadein 1.5
    show sora easy at leftside with portrait_dissolve
    "Sora menyodorkan sekaleng teh ke pipiku."
    s "Kalau kamu jatuh ke mangkuk, aku tidak akan memancingmu."
    r "Aku cuma menunduk."
    s "Satu menit penuh. Dengan sumpit di udara."
    "Aku menurunkan sumpit. Kantin ramai oleh kaki kursi dan suara baki, terlalu terang untuk orang yang baru tidur pukul dua."
    s "Latihan empat sore. Jangan lupa kabel pendek."
    r "Kabelnya di tas."
    s "Bagus. Sekarang masukkan juga kesadaranmu. Aku ke ruang musik."
    "Sora mengambil roti terakhir di bungkusnya dan pergi. Aku membawa baki ke tempat pengembalian, lalu melihat Aoi di dekat jendela."
    hide sora with portrait_dissolve
    show aoi neutral at heroine with portrait_dissolve
    "Ia menahan halaman buku dengan kotak pensil. Di sebelahnya ada selembar rancangan berisi kotak-kotak kosong dan gambar daun kecil."
    "Segelas teh sudah dingin. Nasi bekalnya nyaris habis, kecuali potongan wortel yang disusun di pinggir."
    r "Kalau kamu sedang menghitung sesuatu, aku bisa pergi."
    "Aoi mengangkat wajah. Ada bekas lipatan kecil di pipinya, mungkin dari lengan seragam."
    a "Jangan. Duduk saja."
    "Ia menggeser kotak pensil, membuat ruang di sisi meja."
    r "Aku bisa duduk di meja lain."
    show aoi smile at heroine with portrait_dissolve
    a "Aku tahu. Aku minta kamu di sini."
    "Aku menarik kursi terlalu jauh. Kakinya berdecit, membuat dua orang menoleh. Aoi menutup mulut dengan punggung tangan."
    r "Kursinya punya pendapat sendiri."
    a "Pendapatnya keras sekali."
    "Aku duduk dengan hati-hati. Di kertasnya tertulis ‘Sudut Hal Kecil’."
    r "Untuk perpustakaan?"
    a "Minggu depan. Satu panel di pameran sekolah. Orang boleh menempelkan gambar atau catatan tentang sesuatu yang mereka lihat dalam perjalanan."
    r "Misalnya telur dadar di laut?"
    a "Itu karya seorang seniman yang belum mau menerima kritik."
    r "Aku membawa bukti revisi."
    "Kukeluarkan poster dari map. Aoi merapikan posisi buku agar tidak terkena kertas."
    "Ia menatap ombak yang sudah kuperbaiki, lalu menunjuk bentuk kecil di sudut."
    a "Kamu menyisakannya."
    r "Pesanan khusus."
    a "Bagus. Sekarang orang akan lapar sebelum band kalian mulai."
    "Ia menguap tepat setelah mengatakan itu. Kami berpaling bersamaan, seolah tertangkap melakukan sesuatu."
    r "Aku tidak akan membahas semut jam satu lagi."
    a "Aku juga tidak akan mengirimnya jam satu."
    r "Kita sepakat?"
    a "Kecuali semutnya membawa sesuatu yang luar biasa."
    "Aku mengambil kotak pensil yang hampir terguling. Ia mengikutinya dengan mata, kemudian kembali ke kertas."
    "Beberapa judul kecil sudah dihapus sampai permukaannya berbulu."
    r "Susah?"
    a "Gambarnya gampang. Kalimat ajakannya belum ketemu. Kalau terlalu panjang, orang lewat saja. Kalau terlalu pendek, kelihatannya seperti tugas."
    "Ia membaca dua versi yang ditulisnya. Keduanya terdengar terlalu resmi untuk seseorang yang semalam menilai kepribadian semut."
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        "Bagaimana aku menemaninya?"
        "Duduk tenang sampai ia menemukan kalimatnya.":
            $ story_company = "quiet"
            r "Aku di sini saja. Panggil kalau perlu pembaca."
            a "Boleh. Tapi jangan tidur."
            "Kukeluarkan buku sendiri. Selama beberapa menit, kami hanya mendengar orang-orang di meja sebelah berebut saus."
            "Aoi menulis satu kata, menghapusnya, lalu mencoret seluruh baris. Aku berpura-pura berhasil mengerjakan soal."
            a "Ren."
            r "Masih bangun."
            a "‘Apa yang hampir kamu lewatkan hari ini?’"
            "Aku membaca kalimat itu lagi dari arah terbalik."
            r "Aku akan berhenti kalau melihatnya."
            a "Kalau begitu, yang ini."
            "Ia menggarisbawahinya satu kali. Kaki sepatunya berhenti mengetuk lantai."
        "Tawarkan diri sebagai pembaca pertamanya.":
            $ story_company = "help"
            r "Coba anggap aku orang yang baru lewat."
            a "Kamu membawa buku matematika terbalik. Sulit dianggap pembaca."
            "Aku membalik buku."
            r "Sekarang?"
            a "Sedikit lebih meyakinkan."
            "Ia menyebut dua calon kalimat. Aku memilih yang pendek, tetapi saat ditanya alasannya, aku malah membahas ukuran tulisan."
            a "Jadi kalimatnya belum bagus."
            r "Aku ingin tahu apa yang akan kutempel di situ. Mungkin kamu bisa menanyakannya."
            "Aoi menatap ujung pensil. Lalu menulis: ‘Apa yang hampir kamu lewatkan hari ini?’"
            r "Itu."
            a "Kamu bahkan belum membacanya sampai selesai."
            r "Dari sini kelihatan."
            "Ia memutar kertas menghadapku. Aku membacanya lagi, kali ini dengan sungguh-sungguh."
    "Bel masuk berbunyi dari lorong. Aoi mulai membereskan meja, lalu berhenti di bungkus bekalnya."
    a "Kamu ke ruang musik nanti?"
    r "Sampai jam lima."
    a "Aku di perpustakaan sampai setengah lima. Mau jalan ke kota setelah itu? Aku perlu kertas yang lebih tebal."
    "Toko alat tulis ada di jalur pulangku. Bukan alasan yang memerlukan banyak pemikiran."
    "Tetap saja, aku menghitung waktu latihan dalam kepala."
    r "Aku bisa keluar lebih awal. Bagian gitarku sudah selesai."
    a "Jangan karena aku. Aku bisa menunggumu."
    "Aoi mengancingkan tas, menungguku berdiri."
    r "Jam lima. Di gerbang."
    show aoi smile at heroine with portrait_dissolve
    a "Baik. Bawa seniman telur dadarnya juga."
    "Ia berjalan di sampingku sampai persimpangan lorong. Aku baru sadar tidak satu pun soal matematikaku selesai."

    # SCENE 03 · Selasa sore · pertokoan dan toko roti.
    scene bg street with fade
    play ambience "audio/ambience/garden.ogg" fadeout 1.0 fadein 1.5 volume .3
    "Pukul lima lewat tujuh, Aoi sudah menungguku dengan dua lembar kertas karton di bawah lengan."
    show aoi neutral at heroine with portrait_dissolve
    a "Aku masuk toko sebentar. Lalu keluar membawa ini."
    r "Sebentar versi tiga artikel?"
    a "Aku masih perlu lem."
    "Kami kembali ke toko. Aku memegang kartonnya sementara ia membandingkan lem yang harga dan bentuknya nyaris sama."
    "Ia memilih yang kecil. Katanya, tutup botol besar selalu mengering sebelum isinya habis."
    "Di luar, kami harus memiringkan karton agar tidak menangkap angin dari ujung jalan. Aoi memegang satu sisi, aku sisi lainnya."
    a "Ini seperti membawa layar perahu yang jelek."
    r "Asal jangan belok ke pelabuhan."
    "Kami melewati toko barang bekas yang memajang pakaian di depan. Sehelai jeans di rak bawah menarik perhatian Aoi."
    "Potongannya lebar, warna birunya hampir abu-abu. Ia mengangkat ujung kaki celana lalu melihat label ukurannya."
    a "Yang seperti ini enak untuk melukis. Tidak perlu memikirkan noda."
    r "Kamu memang butuh yang baru?"
    a "Yang di rumah sobek di lutut. Bukan sobek yang disengaja. Waktu aku jongkok, bunyinya mengkhawatirkan."
    "Ia membentangkan bagian pinggang celana di depan tubuhnya, lalu mengembalikannya ke rak."
    r "Tidak jadi?"
    a "Anggaran minggu ini sudah berubah menjadi kertas."
    "Ia mengetuk karton. Label jeans itu masih menghadap ke luar; angkanya gampang diingat."
    a "Nanti saja. Tidak akan lari."
    r "Kalau lari, itu berita besar."
    "Toko roti kecil di ujung blok hampir tutup. Penjaganya memasang nampan terakhir tepat ketika kami masuk."
    scene bg bakery at scene_drift with dissolve
    stop ambience fadeout 1.0
    show aoi smile at heroine with portrait_dissolve
    "Aoi mengambil roti gulung kacang merah. Aku mengambil roti garam, lalu terpaksa menaruhnya kembali karena hanya punya satu tangan bebas."
    a "Karton sini."
    r "Kamu juga membawa nampan."
    a "Kita bisa membuat persoalan ini lebih rumit, atau kamu bisa menaruh kartonnya di bawah meja itu."
    "Aku memilih saran kedua. Ia menunggu di dekat kasir sambil tersenyum sendiri."
    "Kami sudah empat kali datang ke sini dalam enam minggu. Pada kunjungan pertama, aku salah mengambil roti yang tidak ada isinya."
    "Aoi membagi rotinya menjadi dua. Ia bilang bagian tengah boleh untukku asal aku tidak menjatuhkan kacangnya."
    "Hari ini ia mengambil roti yang sama, lalu mengawasi jepit yang kupegang."
    r "Aku belajar dari kesalahan."
    a "Bagus. Aku tidak membawa roti cadangan."
    "Kami makan di bangku sempit depan toko. Bungkus roti menghangatkan telapak tanganku."
    "Dari sini kelihatan ujung menara katedral tua di atas atap pertokoan. Pintu halamannya masih terbuka, tetapi kami memilih tetap duduk dekat rak roti yang wangi."
    r "Kenapa membuat panel itu sendiri? Mio tidak membantu?"
    a "Mio mengurus daftar peserta. Dia membantu banyak. Aku yang susah meminta orang menggambar."
    r "Kamu tinggal menyerahkan kertas."
    a "Kalau seseorang bilang tidak bisa, aku malah percaya. Lalu aku menggambar sendiri."
    "Ia menatap roti di tangannya, memutar kertas pembungkus agar remah tidak jatuh ke rok."
    a "Aku ingin orang yang merasa gambarnya jelek juga mau menempelkan sesuatu. Tapi posterku malah terlalu rapi."
    r "Tambahkan ombakku."
    show aoi laugh_open at heroine with portrait_dissolve
    a "Sebagai peringatan?"
    r "Sebagai izin."
    "Aoi berhenti tertawa sebentar. Kemudian mengeluarkan pensil dari tas."
    a "Tunggu. Kalimat itu bisa dipakai."
    "Ia menulis di belakang struk. Aku menjaga karton agar tidak menyentuh genangan di bawah bangku."
    "Beberapa siswa dari sekolah kami lewat. Salah satunya mengangkat tangan. Aoi membalas tanpa beranjak."
    r "Kamu mudah sekali mengajak orang bicara."
    a "Tentang roti, mungkin."
    r "Tentang banyak hal."
    a "Tidak selalu. Ada orang yang sudah ingin menjawab sebelum aku selesai. Aku jadi mempercepat semuanya. Akhirnya lupa apa yang mau kukatakan."
    "Pensilnya berhenti di tengah kata."
    a "Denganmu, kalau aku berhenti, kamu menunggu."
    "Aku menggulung ujung bungkus roti. Sedikit terlalu rapat."
    r "Kadang karena aku sedang mencari jawaban."
    a "Aku juga. Jadi pas."
    "Sebuah remah menempel di ibu jarinya. Ia menyentuhkannya ke bungkus, lalu tertawa kecil."
    a "Seharusnya kubawa pulang untuk semut."
    r "Jangan. Nanti kita membahasnya sampai jam dua lagi."
    a "Malam ini paling lambat sebelas."
    r "Janji?"
    a "Kalau kamu selesai latihan dan makan tepat waktu."
    "Kami kembali berjalan ketika toko mulai membereskan nampan. Di persimpangan, Aoi harus naik bus ke arah bukit."
    "Aku menyerahkan kartonnya. Ia menguji pegangannya, lalu meraih lagi sisi yang tadi kupegang."
    a "Besok siang, kamu punya waktu sebentar?"
    r "Sebelum latihan suara."
    a "Mio membawa cetakan gambar. Kita perlu contoh untuk panel."
    r "Kamu yakin memilihku?"
    a "Aku memerlukan satu orang yang tidak takut menggambar ombak seperti telur."
    "Bus datang sebelum aku sempat membela diri. Dari balik kaca, ia mengangkat kantong lem kecil."
    "Pukul sebelas malam, ia benar-benar mengirim selamat malam. Aku sempat kecewa sekitar tiga detik, lalu tertidur dengan lampu meja masih menyala."

    # SCENE 04 · Rabu siang · sudut duduk perpustakaan.
    scene bg lounge at scene_drift with fade
    stop ambience fadeout 1.0
    play music audio.tender fadeout 1.5 fadein 1.5
    "Beanbag di sudut perpustakaan lebih kecil daripada yang terlihat dari pintu."
    "Aku baru mengetahui itu setelah duduk dan Aoi menjatuhkan diri di sisi sebelah."
    show aoi neutral at closeup with portrait_dissolve
    "Bahan kain melesak, mendorong kami ke tengah. Bahunya menyentuh lenganku. Kami memindahkan siku pada saat yang sama, lalu bertabrakan lagi."
    a "Sebentar. Kamu di situ saja."
    r "Aku sudah di sini."
    a "Kamu bergerak terus."
    "Aku berhenti. Aoi memasang papan alas di atas kedua lutut kami. Sebuah gambar kota kecil terbentang di atasnya."
    "Ada toko roti, pohon, stasiun, dan orang-orang yang masih berupa bentuk sederhana. Ruang kosong di pinggirnya disediakan untuk siapa pun yang ingin menambah gambar."
    a "Mio bilang contoh harus selesai hari ini. Tidak perlu indah."
    r "Itu batas yang bisa kuikuti."
    "Aoi menyerahkan sekotak pensil warna. Beberapa ujungnya lebih pendek daripada tutup penghapusku."
    a "Atap stasiunnya mau warna apa?"
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        "Dua pensil terletak di tanganku."
        "Biru, seperti air ketika angin sudah reda.":
            $ story_color = "blue"
            r "Biru yang ini. Boleh?"
            a "Atap biru. Baik. Aku buat lampunya kuning."
            "Aku mencoba membuat garis rata. Aoi menambahkan cahaya kecil di jendela, membiarkan sebagian warna keluar dari batas."
        "Kuning, seperti lampu toko menjelang tutup.":
            $ story_color = "gold"
            r "Kuning. Biar kelihatan masih ada orang di sana."
            a "Kalau begitu langitnya biru gelap. Stasiunnya belum tidur."
            "Aoi menajamkan pensil di atas kertas bekas. Serpihannya berputar kecil sebelum jatuh."
    "Aku mengisi bagian besar, Aoi mengerjakan jendela dan orang-orang. Kami harus bergantian mengambil warna karena kotaknya tersangkut di antara pinggul dan kain beanbag."
    a "Tidak, yang itu hijau."
    r "Aku tahu."
    a "Kamu sedang mewarnai laut."
    r "Mungkin banyak ganggang."
    "Ia tertawa, lalu menggunakan hijau yang sama untuk satu petak air. Kesalahanku menjadi bagian gambar."
    "Mio muncul membawa gunting dan beberapa penjepit. Ia meletakkannya di meja rendah, menatap papan di atas lutut kami, lalu mencari tempat duduk."
    show mio neutral at leftside with portrait_dissolve
    m "Kalian sudah pacaran?"
    stop music fadeout 1.0
    show aoi surprised at closeup with portrait_dissolve
    "Pensilku berhenti tepat di luar garis."
    "Satu detik. Aku menatap warna hijau di ujungnya."
    "Dua. Bahu Aoi masih menempel di lenganku."
    "Di dekat pintu, roda troli buku berderit. Seseorang mengembalikan kamus dengan bunyi terlalu keras."
    "Aku seharusnya menjawab. Pertanyaannya pendek."
    "Kalau aku mengatakan tidak, apakah Aoi akan menggeser tubuhnya?"
    "Kalau aku mengatakan iya, bukankah aku menjawab untuk Aoi juga?"
    show aoi shy_clasp at closeup with portrait_dissolve
    "Aoi menunduk ke gambar. Warna merambat ke telinganya. Aku bisa merasakan wajahku sendiri menghangat."
    "Mio melihat kami bergantian. Tangannya masih memegang sebatang lem."
    "Barangkali hanya sepuluh detik. Aku sempat menghafal seluruh lipatan bungkus lem itu."
    show mio concerned at leftside with portrait_dissolve
    m "Oh. Maaf. Aku boleh duduk?"
    "Ia menunjuk bangku kecil yang tertutup tas Aoi."
    a "Tasnya boleh dipindah."
    "Suara Aoi lebih pelan daripada biasanya. Aku ingin menoleh, tetapi kami terlalu dekat untuk melakukannya dengan santai."
    r "Ini hampir selesai."
    show mio thoughtful at leftside with portrait_dissolve
    m "Bagus. Aku perlu gambar yang bisa bikin orang berani ikut, bukan yang membuat mereka menyerah."
    "Mio menarik bangku, membahas ukuran panel, lalu meminta Aoi mengecek daftar warna. Ia memberiku waktu untuk membuka tangan yang sejak tadi mengepal di atas lutut."
    play music audio.tender fadein 2.0
    "Kami melanjutkan mewarnai. Kali ini Aoi meminta pensil dengan menyebut namaku lebih dulu."
    a "Ren, yang kuning."
    "Aku menyerahkannya. Jari kami menyentuh kotak, lalu sama-sama mundur."
    "Setelah Mio pergi mengambil selotip, Aoi merapikan tepi kertas meskipun sudah lurus."
    hide mio with portrait_dissolve
    a "Dia memang langsung bertanya begitu."
    r "Iya."
    a "Kamu tidak perlu merasa harus menjawab sekarang."
    "Aku menatapnya. Aoi masih melihat gambar."
    r "Kamu juga."
    "Ia mengangguk sekali, lalu mengambil pensilnya lagi."
    "Saat bel berbunyi, aku berdiri lebih dulu agar beanbag tidak membuatnya jatuh. Aoi mengulurkan papan padaku, lalu meraih tanganku untuk bangkit."
    "Ia melepasnya setelah sudah berdiri. Bukan sebelumnya."
    a "Nanti malam, aku datang sebelum mulai."
    r "Tidak perlu terburu-buru."
    show aoi smile at heroine with portrait_dissolve
    a "Aku tahu. Aku tetap mau."
    "Ia membawa gambar itu ke meja Mio. Atap stasiun kami masih sedikit belang. Aku menyukainya begitu."
    jump act_2

label act_2:
    $ aoi_outfit = "school"
    $ persistent.chapter_unlocked = max(persistent.chapter_unlocked, 2)
    call chapter_card("II", "Sepuluh Detik", "Hal yang belum berani kami namai.")

    # SCENE 05 · Rabu, 17.40 · pertunjukan kecil di balai warga.
    scene bg stage with fade
    stop ambience fadeout 1.0
    play music audio.day fadeout 1.5 fadein 2.0
    show sora neutral at leftside with portrait_dissolve
    "Sora menghitung jumlah stik drumnya untuk ketiga kali. Semuanya masih ada."
    r "Sekarang kamu mengerti kenapa aku menyetel gitar terus."
    s "Tidak. Stik bisa hilang. Nada tidak bisa masuk tas orang."
    "Pertunjukan kami ditempatkan setelah kelompok akustik dan sebelum band yang jauh lebih pandai membawa penonton. Empat lagu, dua puluh menit, di panggung balai warga yang berbau kabel hangat."
    "Aku memasang kabel pendek yang kemarin diingatkan Sora. Lalu memeriksa sakelar pedal."
    s "Kalau kamu lihat ke pintu lagi, gitarmu tidak akan ikut menoleh."
    r "Aku mencari jam."
    s "Jamnya di sebelah kanan. Sejak kita datang."
    show sora easy at leftside with portrait_dissolve
    "Aku melihat ke kanan dengan patuh."
    "Tadi siang, pertanyaan Mio tinggal di kepalaku bahkan setelah kelas selesai. Di setiap kalimat biasa Aoi, aku mendengar kemungkinan jawaban yang belum ia berikan."
    "‘Kuningnya mana?’ bisa cuma soal pensil. ‘Aku tetap mau datang’ bisa cuma soal tiket."
    "Mengira semua itu tentangku terasa lancang. Berpura-pura tidak memikirkannya ternyata sama sulitnya."
    show aoi neutral at heroine with portrait_dissolve
    "Aoi masuk membawa tas kanvas dan botol minum. Rambutnya sedikit berantakan karena angin. Ia berhenti dekat deretan kursi, melihat panggung, lalu melambai dengan dua jari."
    "Aku lupa sedang memegang pick. Benda itu jatuh di antara kotak kabel."
    s "Sekarang nada mulai masuk tas orang."
    "Sora mengambilkan pick cadangan. Aku bergumam terima kasih."
    "Aoi memilih kursi di baris kedua. Ia tidak duduk tepat di tengah, tetapi dari tempatku berdiri, aku mudah menemukannya."
    hide aoi with portrait_dissolve
    hide sora with portrait_dissolve
    "Lampu ruang penonton diredupkan. Suara obrolan turun, menyisakan dengung amplifier yang tak pernah benar-benar hilang."
    "Sora mengetukkan stik. Empat hitungan. Kali ini tanganku tahu apa yang harus dikerjakan."
    "Lagu pertama berjalan sedikit terlalu cepat. Pada lagu kedua, aku melewatkan satu nada dan berhasil kembali sebelum ada yang menoleh."
    "Lalu kami memainkan lagu ketiga. Bagian pembukanya hanya gitar."
    "Di sela dua akor, aku mendengar kursi bergeser. Kuregangkan jari, mengambil napas, dan membiarkan jedanya tetap ada."
    "Di baris kedua, tangan Aoi diam di atas tas. Wajahnya terangkat ke arah panggung."
    "Aku menyelesaikan bagian itu. Kali ini tidak dipercepat."
    "Dua puluh menit habis lebih cepat daripada sepuluh detik di perpustakaan."
    scene bg night with fade
    play ambience "audio/ambience/night.ogg" fadeout 1.0 fadein 1.5 volume .38
    play music audio.tender fadeout 2.0 fadein 2.0
    show aoi smile at heroine with portrait_dissolve
    "Di luar balai warga, Aoi menungguku di samping mesin minuman. Ia masih memegang potongan tiket yang sudah disobek."
    a "Lagu ketiga. Yang awalnya sendiri. Itu judulnya apa?"
    r "Belum punya. Di daftar kami tulis ‘Yang Ketiga’."
    a "Judul yang akurat."
    r "Terima kasih sudah datang."
    a "Kamu sudah bilang tadi lewat pesan."
    r "Kalau begitu, ini untuk perjalanan ke sini."
    "Aoi memasukkan tiket ke saku kecil tasnya, di antara kartu perpustakaan dan sebuah klip berbentuk ikan."
    a "Kamu tadi kelihatan takut sebelum mulai. Setelah lagu kedua, lebih enak."
    r "Yang salah justru lagu kedua."
    a "Aku tidak tahu. Tapi waktu kamu melihat Sora, kalian berdua tertawa. Setelah itu aku ikut tenang."
    "Aku biasanya mengingat pertunjukan berdasarkan kesalahan. Bagian kabel yang terinjak, nada yang meleset, rekaman ponsel yang ingin kuhapus."
    "Aoi mengingat tawa yang bahkan hampir kulupakan."
    r "Bagian pembuka itu sebenarnya masih perlu diperbaiki."
    a "Boleh. Tapi versi tadi jangan dihapus. Aku mau dengar lagi."
    r "Kamu menyimpan tiketnya untuk itu?"
    "Ia meraba saku tas, seolah baru sadar aku melihatnya."
    a "Sebagian. Dan gambar di belakangnya lucu."
    "Aku menggambar seekor ikan kecil di tiket-tiket itu saat bosan menjaga meja penjualan. Ekor ikan di tiket Aoi sedikit bengkok."
    r "Aku bisa menggambar yang lebih bagus."
    a "Aku sudah suka yang ini."
    "Pintu balai terbuka. Sora memanggil namaku sambil mengangkat gulungan kabel."
    show sora neutral at leftside with portrait_dissolve
    s "Ini punyamu atau inventaris?"
    r "Punyaku. Sebentar."
    "Ia meletakkan kabel di atas kotak dan kembali masuk. Aoi menggeser tas agar aku bisa menaruh sarung gitar di bangku."
    hide sora with portrait_dissolve
    "Kami berdiri begitu dekat sehingga ujung tali tasnya menyentuh jariku."
    a "Soal tadi siang..."
    "Aku menoleh terlalu cepat."
    a "Gambarnya. Mio sudah menempelkannya untuk contoh. Ada yang menambah kucing di atap."
    r "Oh."
    "Kata itu jatuh lebih datar daripada yang kuinginkan. Aoi menunduk sebentar, lalu membuka foto di ponselnya."
    "Kucing tambahannya lebih besar daripada stasiun. Di bawahnya seseorang menulis, ‘Dia sedang menunggu kereta.’"
    "Aku tertawa. Aoi ikut tertawa setelah melihat wajahku. Ketegangan yang tak punya nama itu bergeser sedikit."
    r "Besok pulang jam berapa?"
    a "Tidak ada rapat. Kenapa?"
    "Aku mengusap bekas tali gitar di leher."
    r "Mau jalan sebentar?"
    a "Mau."
    "Ia menjawab sebelum aku memutuskan apakah harus menyebut tempatnya."
    a "Di gerbang seperti kemarin?"
    r "Iya."
    "Busnya tiba beberapa menit kemudian. Aku membawa kotak peralatan kembali ke dalam dengan kabel yang belum sempat kugulung."
    hide aoi with portrait_dissolve
    show sora easy at leftside with portrait_dissolve
    s "Kamu tersenyum pada kabel."
    r "Besok aku mau bicara dengan Aoi."
    s "Bagus. Minta fotonya yang ada aku juga. Yang tadi dia ambil."
    "Aku membuka mulut, lalu menutupnya."
    "Ujung kabel itu terlepas dari gulungan. Aku mulai lagi dari awal."

    # SCENE 06 · Kamis sore · rencana yang tidak menjadi percakapan.
    scene bg street with fade
    play ambience "audio/ambience/garden.ogg" fadeout 1.0 fadein 1.5 volume .3
    play music audio.day fadeout 1.5 fadein 1.5
    "Hari Kamis, aku melatih satu kalimat sambil mengganti sepatu."
    "‘Aoi, ada yang ingin kubicarakan.’"
    "Terlalu seperti memanggil orang ke ruang guru."
    "‘Aku senang kalau bersamamu.’"
    "Bisa saja ia menjawab bahwa ia juga senang berjalan bersama Mio."
    "Pada percobaan ketiga, tali sepatuku terlepas lagi. Sora berjongkok di sebelahku, menyimpan sepatu dalam ruangan di lokernya."
    show sora neutral at leftside with portrait_dissolve
    s "Aku ikut sampai pertokoan. Kabel semalam harus ditukar konektornya."
    r "Sekarang?"
    s "Besok tokonya tutup lebih cepat. Kamu bawa contoh kabelnya, kan?"
    "Memang kubawa. Semalam aku sendiri yang menawarkan membantu mencari ukuran."
    "Ketika melihat Aoi menunggu di dekat gerbang, aku mencoba memikirkan cara menjelaskan dua rencana yang sudah kutumpuk sendiri."
    show aoi smile at heroine with portrait_dissolve
    a "Sora ikut?"
    s "Sebentar. Ren tahu ukuran konektornya."
    r "Aku bisa tulis ukurannya."
    s "Kalau cuma ditulis, aku mungkin tetap membeli yang salah. Yang kemarin bentuknya sama, ingat?"
    "Aoi mengangkat alis sedikit. Aku melipat kertas kecil yang sejak tadi dipegang di dalam saku."
    a "Tidak apa-apa. Tokonya searah."
    "Kami berjalan bertiga. Sora di tengah, menjelaskan kesalahannya pada lagu terakhir dengan menggunakan botol minum sebagai mikrofon."
    "Aoi menanyakan bagian yang membuat penonton bertepuk tangan lebih cepat. Ia memperhatikan jawaban Sora. Aku menghargai itu dan berharap percakapannya segera selesai."
    "Dua keinginan itu membuatku merasa kekanak-kanakan."
    r "Sora, setelah toko kamu langsung pulang?"
    s "Belum tahu. Kenapa?"
    "Aoi menatapku dari sisi lain."
    r "Cuma bertanya."
    "Sora mengangguk, menerima jawaban itu apa adanya. Tentu saja."
    "Di toko musik kami memerlukan waktu sepuluh menit. Pemiliknya membawa kotak konektor, Sora mencoba dua kabel, dan aku menjelaskan mana yang rusak."
    "Aoi menunggu di luar sambil membaca poster kelas piano. Aku melihat punggungnya melalui kaca."
    "Saat kami keluar, ia memegang tiga lembar selebaran kecil."
    a "Untuk belakang gambar. Sisi satunya kosong. Pemiliknya bilang boleh."
    s "Kamu benar-benar bisa membuat kertas dari mana saja."
    a "Kertasnya sudah ada. Aku hanya meminta."
    "Aku ikut mengangguk, padahal bukan aku yang diajak bicara."
    "Kami mampir ke toko roti. Sora memilih dengan serius, membahas isi dan harga seperti sedang menilai alat musik."
    "Aoi mengangkat satu bungkus roti garam ke arahku. Aku mengangguk. Kebiasaan kecil itu justru membuat kalimat di sakuku terasa makin besar."
    scene bg bakery at scene_drift with dissolve
    stop ambience fadeout 1.0
    show sora neutral at leftside with portrait_dissolve
    show aoi neutral at heroine with portrait_dissolve
    s "Kalian mau duduk di luar? Aku punya waktu sampai kereta berikutnya."
    "Tidak ada yang menjawab selama satu ketukan."
    a "Boleh."
    "Aoi menyebutnya ringan. Aku mengambil baki dari tangannya agar ia bisa membuka tas."
    "Kami duduk di bangku yang sama seperti Selasa, ditambah satu kursi plastik dari depan toko."
    "Sora berbicara tentang rekaman pertunjukan. Aoi menunjukkan foto, memilih yang wajahku tidak tertutup tiang."
    "Aku berusaha hadir dalam percakapan. Sesekali berhasil. Sesekali menghitung berapa menit sebelum bus Aoi datang."
    "Ketika Sora akhirnya melihat jam, bus itu sudah berada di ujung jalan."
    s "Wah. Aku harus ke stasiun. Terima kasih sudah menunggu."
    "Ia mengangkat tangan, membawa roti keduanya, lalu berlari kecil."
    hide sora with portrait_dissolve
    show aoi shy at heroine with portrait_dissolve
    "Aoi menutup tas. Kini kami berdua, dengan waktu yang habis."
    r "Maaf."
    a "Karena Sora?"
    r "Karena aku tidak bilang..."
    "Pintu bus terbuka. Seorang penumpang turun membawa tas belanja besar."
    "Aoi bergeser agar orang itu bisa lewat, lalu kembali menghadapku."
    a "Ren, kalau ada yang ingin dibicarakan, aku bisa dengar lain kali."
    "Aku meremas kertas di saku sampai tepinya terasa menusuk."
    r "Ada. Aku ingin bicara. Berdua."
    "Ia menatapku satu detik lebih lama."
    a "Baik."
    "Aoi naik ke bus. Kali ini ia duduk dekat pintu, mengangkat tangan sebelum aku menemukannya melalui kaca."
    "Aku membalas sampai busnya berbelok. Kertas di sakuku sudah menjadi bola kecil."
    scene bg bedroom with fade
    play ambience "audio/ambience/night.ogg" fadeout 1.0 fadein 1.5 volume .38
    play music audio.night fadeout 1.5 fadein 1.5
    "Malam itu Sora mengirim foto konektor yang sudah terpasang."
    s "Berfungsi. Makasih. Tadi kamu mau mengajaknya bicara, ya?"
    r "Iya."
    s "Aku baru sadar waktu di kereta."
    r "Aku juga tidak bilang jelas."
    s "Besok suruh aku pulang saja. Aku bisa naik kereta sendiri."
    "Aku menatap kalimat itu cukup lama, lalu mengetik terima kasih."
    "Kertas dari sakuku kuletakkan di samping ponsel. Kubuka lipatannya, lalu meratakannya dengan telapak tangan."

    # SCENE 07 · Jumat sore · panel yang mulai dimiliki banyak orang.
    scene bg lounge at scene_drift with fade
    stop ambience fadeout 1.0
    play music audio.tender fadeout 1.5 fadein 1.5
    show mio smile at leftside with portrait_dissolve
    "Hari Jumat, stasiun kecil kami sudah mempunyai tiga kucing, satu pesawat, dan seseorang yang mengaku sedang menggambar kentang."
    m "Dia sebenarnya menggambarku."
    "Mio menunjukkan gambar bulat yang ditempel di sudut. Di bawahnya ada tulisan ‘panitia yang sangat sibuk’."
    r "Kemiripannya di mana?"
    m "Sama-sama perlu makan. Pegang ini."
    "Ia menyerahkan satu ujung tali. Aku mengikatnya pada kaki papan pajangan sementara Aoi memasang penjepit kertas."
    show aoi smile at heroine with portrait_dissolve
    a "Sudah ada dua puluh tiga. Pagi tadi masih sembilan."
    "Sebagian gambar diwarnai rapi. Sebagian hanya satu garis dengan penjelasan panjang. Ada catatan tentang kucing di belakang kantin, ada gambar awan dengan nama yang tidak bisa kubaca."
    "Aoi mengambil selembar yang terlepas, membetulkan penjepitnya, lalu mundur untuk melihat seluruh panel."
    a "Aku hampir menghapus ruang kosong di pinggir. Kupikir kelihatan malas."
    r "Sekarang justru kurang tempat."
    a "Aku bisa menambah kertas. Yang penting mereka mulai."
    "Mio melirik kami saat mengambil gulungan pita."
    show mio concerned at leftside with portrait_dissolve
    m "Soal pertanyaanku dua hari lalu. Maaf kalau membuat kalian tidak nyaman."
    "Aoi memegang dua penjepit di telapak tangannya. Ia melihatku, kemudian kembali pada Mio."
    a "Aku kaget. Tapi tidak apa-apa kamu bertanya."
    m "Aku lebih sering bicara dulu daripada memeriksa situasi."
    r "Kami juga belum tahu harus menjawab apa."
    "Kata ‘kami’ keluar sebelum aku sempat menyaringnya. Aoi berhenti memainkan penjepit."
    "Mio hanya mengangguk."
    show mio thoughtful at leftside with portrait_dissolve
    m "Kalau begitu aku bisa menunggu. Untuk daftar penjaga panel, aku tetap perlu jawaban hari ini."
    play sound audio.page volume .6
    "Ia menyerahkan formulir pada Aoi, lalu pergi mencari meja. Aoi menangkap sudut kertas yang hampir tersapu lengannya."
    hide mio with portrait_dissolve
    a "Senin kamu kebagian persiapan apa?"
    r "Mengangkat alat dari ruang musik setelah makan siang. Jam setengah dua."
    a "Aku memasang panel jam dua."
    "Ia membuka lembar jadwal yang diselipkan di buku. Senin adalah hari persiapan pameran. Jadwal biasa diganti kegiatan kelas pagi dan giliran kerja kelompok."
    "Sekolah mengizinkan siswa yang tidak mendapat giliran kerja untuk makan di luar antara setengah dua belas dan setengah dua. Pemberitahuannya sudah ditandatangani wali kelas."
    "Selama ini aku hanya mengingat bagian ‘tidak perlu membawa bekal’."
    a "Kalau kamu masih mau bicara, kita bisa keluar waktu itu."
    r "Ke toko roti?"
    show aoi smile at heroine with portrait_dissolve
    a "Aku memikirkan tempat yang sama."
    "Ia melipat jadwal. Aku menyentuh ujung tali yang sudah kuikat, menguji simpul yang sebenarnya tidak perlu diuji."
    r "Kita berdua."
    a "Iya, Ren. Berdua."
    "Ia menyebut namaku seperti orang memastikan sebuah pesanan sudah benar. Aku tersenyum meski leherku terasa panas."
    "Kami berdiri lagi di depan panel. Di atas stasiun yang kami warnai, seekor kucing baru membawa roti sebesar tubuhnya."
    a "Semutku punya pesaing."
    r "Yang ini setidaknya bisa naik kereta."
    "Aoi merapikan ujung kertas, lalu mengulurkan satu penjepit kepadaku. Kami memasangnya bersama. Kali ini jari kami tidak buru-buru menjauh."
    "Sepulang sekolah, aku mampir ke toko barang bekas. Jeans abu-abu kebiruan itu masih tergantung di rak bawah."
    "Aku memeriksa jahitan, menanyakan apakah ada cacat lain, dan membandingkan labelnya dengan angka yang kuingat."
    "Pemilik toko mengemasnya dalam kantong kertas. Di perjalanan pulang, kantong itu terus menyentuh lututku."
    "Di rumah, kantong itu kubuka lagi. Kuambil buku sketsa, lalu mulai dari gambar di dekat saku."

    # SCENE 08 · Sabtu dan Minggu · jeans, cat kain, dan ajakan yang jelas.
    scene bg bedroom_day with fade
    stop ambience fadeout 1.0
    play music audio.night fadeout 2.0 fadein 2.0
    "Jeans itu kuperiksa lagi setelah dicuci. Kainnya utuh. Satu sudut saku terlipat, tetapi setrika membuatnya kembali rata."
    "Sabtu pagi, kuletakkan di atas meja yang sudah dilapisi kertas. Kusisipkan karton di dalam kaki celana supaya cat tidak merembes ke sisi lain."
    "Ada cara yang lebih sederhana untuk menghabiskan akhir pekan. Aku bisa mengerjakan tugas yang jatuh tempo Selasa. Bisa memperbaiki pembuka lagu ketiga."
    "Aku melakukan keduanya lebih dulu, lalu kembali ke meja. Jeansnya masih ada."
    "Aku suka menggambar pada benda yang bisa dipakai. Waktu SMP, aku pernah mengecat sepatu sendiri karena noda tintanya tidak hilang."
    "Hasilnya buruk. Aku tetap memakainya sampai solnya lepas."
    "Aoi pernah melihat sketsanya di halaman belakang bukuku. Ia menanyakan apakah aku masih punya sepatu itu. Tidak tertawa saat kubilang iya."
    "Sekarang aku menggambar rancangan dengan kapur kain tipis. Bukan potret. Aoi mungkin tidak ingin berjalan-jalan membawa wajahnya sendiri di lutut."
    "Di tepi saku, seekor semut memanggul remah. Dekat jahitan samping ada roti gulung kecil. Ikan dari tiket band berenang di antara dua ombak."
    if story_color == "blue":
        "Di kaki kiri, kugambar atap stasiun berwarna biru. Di bawahnya ada satu jendela kuning, cukup terang untuk memberi kesan seseorang masih menunggu."
    else:
        "Di kaki kiri, kugambar stasiun kecil berwarna kuning. Di sekitarnya kuberi biru gelap, sama seperti langit yang dibuat Aoi di kertas kami."
    "Aku hampir menambah bunga, awan, dan seluruh kota. Kuangkat kuas, lalu mundur dari meja."
    "Masih perlu ada ruang untuk noda yang dibuatnya sendiri."
    "Ponselku bergetar. Foto panel masuk dari Aoi: seseorang menambahkan sepeda yang rodanya tidak saling sejajar."
    call phone_chat([("aoi", "Pemiliknya bilang tetap bisa jalan."), ("ren", "Kalau jalannya menurun, mungkin."), ("aoi", "Aku suka. Dia menggambar sambil berdiri karena malu duduk."), ("ren", "Sekarang sudah ditempel?"), ("aoi", "Di sebelah stasiun kita.")], "Sabtu · 14.16")
    "Stasiun kita. Aku membaca dua kata itu sambil memegang kuas. Cat biru menetes ke kertas pelapis."
    "Aku menaruh ponsel jauh dari meja. Kalau terus melihatnya, semut di saku akan mempunyai delapan kaki."
    "Goresan pertama tidak rata. Kugunakan kuas lebih kecil untuk memperbaikinya, lalu berhenti sebelum perbaikannya membuat semua hal kaku."
    "Di luar, anak-anak tetangga menendang bola sampai sore. Aku bisa menebak kapan seseorang mendapat giliran jaga gawang dari suara protesnya."
    "Aku bekerja perlahan. Sekali-kali mencuci kuas, minum, atau memeriksa petunjuk cat kain yang sudah kubaca tiga kali."
    scene bg bedroom with dissolve
    play ambience "audio/ambience/night.ogg" fadein 1.5 volume .38
    "Ketika lampu kamar mulai lebih terang daripada jendela, aku menyadari sesuatu yang tidak bisa dibereskan dengan kuas."
    "Bagaimana kalau Aoi merasa harus menerima karena aku sudah membuat ini?"
    "Aku meletakkan kuas melintang di bibir gelas. Jeans itu bagus menurutku. Persoalannya justru karena aku ingin ia menyukainya."
    "Aku mengambil selembar kertas. Menulis satu pengingat dengan huruf besar: BERIKAN SETELAH BICARA."
    "Lalu kutambahkan: Tidak perlu dibawa kalau belum siap."
    "Ujung pensil berhenti di atas baris kedua. Aku menebalkannya."
    call phone_chat([("ren", "Senin kita keluar jam setengah dua belas?"), ("aoi", "Iya. Aku sudah cek jadwalku."), ("ren", "Ada yang ingin kukatakan. Mungkin aku akan agak gugup."), ("aoi", "Aku akan dengarkan."), ("aoi", "Tidak perlu menyelesaikan semuanya lewat pesan sekarang.")], "Sabtu · 20.08")
    "Aku menghapus paragraf yang tadi mulai kutulis. Ucapan terima kasih, lelucon tentang roti, kalimat yang bisa diartikan ke mana saja."
    "Tinggal satu balasan."
    call phone_chat([("ren", "Baik. Sampai Senin."), ("aoi", "Besok masih boleh mengobrol, kan?"), ("ren", "Tentu."), ("aoi", "Bagus. Aku belum selesai cerita soal sepeda tadi.")], "20.10")
    "Kami mengobrol setengah jam. Setelah itu Aoi pergi mencuci piring. Aku membiarkan chat berhenti tanpa mencari topik pengganti."
    "Pada hari Minggu, catnya sudah kering untuk dikerjakan lagi. Aku memperbaiki ekor ikan, menambah dua garis di roti, lalu membuat titik kecil di ujung jendela."
    "Kugunakan kain pelindung ketika menyetrika bagian yang memerlukan panas, mengikuti petunjuk pada botol. Ada aroma kain hangat, sama seperti ketika ibuku menyiapkan seragam dulu."
    "Aku menulis kartu perawatan singkat: jangan dicuci sampai akhir pekan, balik bagian dalam ketika mencuci, setrika melalui kain."
    "Kartu kedua lebih sulit."
    "‘Untuk Aoi.’ Selesai."
    "Aku menambahkan ikan kecil di sudut. Menghapus ekornya. Menggambar lagi."
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        "Besok, bagaimana aku memulai?"
        "Dengan kalimat sederhana yang bisa kuucapkan utuh.":
            $ story_courage = "plain"
            "Aku mencoba mengatakannya pada kamar kosong."
            r "Aku jatuh cinta sama kamu, Aoi. Aku ingin kita berpacaran."
            "Aneh mendengar suaraku sendiri tanpa gitar atau lelucon di belakangnya."
            "Aku mengulang satu kali. Lalu berhenti, sebelum kata-katanya berubah menjadi hafalan."
        "Katakan bahwa aku gugup, lalu tetap lanjutkan.":
            $ story_courage = "slow"
            "Aku mencoba mengatakannya pada kamar kosong."
            r "Aku gugup. Jadi mungkin agak pelan. Tapi aku ingin mengatakannya langsung."
            "Aku mengambil napas lagi."
            r "Aku jatuh cinta sama kamu, Aoi. Aku ingin kita berpacaran."
            "Aku menatap gagang lemari sampai selesai bicara. Besok aku harus bisa menatap Aoi."
    "Kartu itu sudah selesai. Aku membacanya sekali lagi, membetulkan letaknya, lalu membetulkannya lagi."
    "Aku melipat jeans dengan gambar menghadap ke dalam, memasukkannya ke kantong bersih, lalu menyimpan kartu perawatan di atasnya."
    "Ponsel menyala tepat ketika aku menutup lemari."
    call phone_chat([("aoi", "Selamat malam. Besok jangan melewatkan sarapan."), ("ren", "Kamu juga."), ("aoi", "Aku sudah menaruh rotinya di meja."), ("ren", "Aku baru mau mencari."), ("aoi", "Cari sekarang. Aku tunggu sampai ketemu.")], "Minggu · 22.41")
    "Aku pergi ke dapur, mengambil roti, lalu mengirim foto sebagai bukti. Aoi membalas dengan gambar jempol yang setengah tertutup selimut."
    "Kami mengucapkan selamat malam sekali lagi. Kali ini aku tidak memeriksa ponsel setelah layarnya padam."
    jump act_3

label act_3:
    $ aoi_outfit = "school"
    $ persistent.chapter_unlocked = max(persistent.chapter_unlocked, 3)
    call chapter_card("III", "Senin", "Kali ini, aku meminta waktu untuk kami berdua.")

    # SCENE 09 · Senin, 11.30 · toko roti, delapan menit dari sekolah.
    scene bg street with fade
    play ambience "audio/ambience/garden.ogg" fadeout 1.0 fadein 1.5 volume .3
    play music audio.day fadeout 2.0 fadein 2.0
    "Aku tiba di gerbang enam menit sebelum waktu yang kami sepakati."
    "Pemberitahuan izin keluar sudah masuk saku. Dompet di sisi lain. Ponsel di tas. Kantong kertas kupegang dengan tangan kiri agar tidak terus terbentur lutut."
    "Semua benda sudah mendapat tempat. Hanya tangan kananku yang belum."
    "Aku memasukkannya ke saku, mengeluarkannya lagi, lalu merapikan tali tas."
    show aoi smile at heroine with portrait_dissolve
    a "Sudah lama?"
    r "Baru."
    "Aoi menatap gerbang, lalu jam di ponselnya."
    a "Kita sama-sama datang sebelum waktunya."
    "Ia membawa tas kanvas yang biasa. Di dalamnya tampak ujung penggaris panjang dan satu apel."
    r "Apel cadangan?"
    a "Kalau tokonya tutup."
    r "Aku sudah cek. Buka."
    a "Aku tahu. Tapi aku tidak mau membuat keputusan penting saat lapar."
    "Aku tidak berhasil memikirkan jawaban yang sesuai. Aoi merapikan rambut di belakang telinga dan mulai berjalan. Aku mengikuti, bersyukur ia tidak menunggu komentarku."
    "Jalan menuju pertokoan terasa lebih pendek daripada biasanya. Aku mengenali setiap tempat yang pernah membuat kami berhenti: rak pot kecil, papan menu yang salah menulis harga, toko barang bekas."
    "Hari ini aku hampir tidak melihatnya. Kantong kertas di tanganku mengeluarkan bunyi setiap kali terlipat."
    a "Isinya boleh ditaruh di tasku kalau berat."
    r "Tidak berat."
    a "Baik."
    "Ia tidak bertanya lagi. Aku ingin berterima kasih untuk itu, tetapi bahkan ucapan terima kasih bisa membuka pertanyaan tentang isinya."
    scene bg bakery at scene_drift with dissolve
    stop ambience fadeout 1.0
    show aoi neutral at heroine with portrait_dissolve
    "Kami mendorong pintu toko roti pukul sebelas lewat tiga puluh tujuh. Nampan-nampannya masih penuh. Kami belum pernah datang sebelum hampir tutup."
    a "Ternyata roti itu ada versi lengkapnya."
    "Ia menunjuk roti berbentuk kepang yang biasanya hanya menyisakan label harga."
    r "Mau coba?"
    a "Hari ini yang biasa dulu."
    "Aku mengambil dua roti garam, lalu satu yang berisi keju. Aoi mengambil roti kacang merah dan kepang kecil setelah mempertimbangkannya lagi."
    a "Cadangan untuk keputusan berikutnya."
    "Kami membayar masing-masing. Saat penjaga toko menanyakan bungkusnya dipisah atau digabung, aku menoleh pada Aoi."
    a "Gabung saja. Nanti dipisah waktu makan."
    "Aku mengangguk terlalu serius untuk sebuah kantong roti."
    "Di luar, bangku depan toko terkena matahari. Aoi mengangkat tangan untuk melindungi mata, melihat ke arah ujung menara katedral."
    a "Di pohon sana lebih teduh."
    r "Ayo."
    "Kami berjalan melewati pagar rendah menuju halaman yang terbuka bagi pejalan kaki. Tidak ada acara siang itu. Di dekat pintu bangunan, beberapa orang berbicara pelan sambil memindahkan kursi."
    "Aku tidak tahu banyak tentang katedral tua itu. Sejak kecil aku hanya menggunakannya sebagai petunjuk jalan: belok setelah menaranya kelihatan."
    "Aoi lebih mengenal pohonnya. Ia pernah duduk di sana ketika hujan kecil turun dan tak ingin membuka payung untuk perjalanan sesingkat itu."
    a "Bangkunya masih kering kalau hujannya pelan. Kalau angin, tidak menolong sama sekali."
    r "Hari ini tidak ada hujan."
    a "Untung. Aku tidak membawa payung."
    "Kami menemukan bangku di bawah pohon, di sisi halaman yang menghadap jalan kecil. Dari sana kami bisa melihat pejalan kaki tanpa harus ikut bergerak bersama mereka."
    scene bg courtyard at scene_drift with dissolve
    play ambience "audio/ambience/garden.ogg" fadeout 1.0 fadein 1.5 volume .3
    show aoi smile at heroine with portrait_dissolve
    "Pukul sebelas lewat empat puluh lima. Aoi membuka kantong roti di antara kami. Aku menaruh kantongku sendiri di sisi luar kaki kiri."
    "Masih satu jam empat puluh lima menit sebelum aku harus kembali ke ruang musik."
    "Rasanya seperti banyak waktu. Lalu Aoi menoleh dan menanyakan roti yang mana milikku. Mendadak aku tidak tahu harus mulai dari mana."

    # SCENE 10 · Sepuluh menit kemudian · pengakuan.
    play music audio.tender fadeout 2.0 fadein 2.0
    r "Panelnya sudah dapat tempat?"
    a "Dekat pintu perpustakaan. Jadi orang yang datang dari tangga bisa langsung lihat."
    r "Itu bagus."
    "Aku menggigit roti sebelum harus menambahkan kalimat lain. Terlalu besar. Selama beberapa saat, aku sibuk mengunyah sesuatu yang seharusnya tidak rumit."
    a "Pelan-pelan."
    "Ia menahan senyum, mengambil minumannya, lalu menunggu."
    "Kami membicarakan angin yang kemarin menjatuhkan satu penjepit. Sora yang sudah menandai semua kabel dengan pita warna. Tugas matematika yang, untungnya, selesai kukerjakan hari Sabtu."
    "Dua merpati mendekati remah di dekat kaki bangku. Aoi mengangkat ujung sepatunya agar tidak menginjak salah satunya."
    "Aku menyebut pohonnya besar. Ia mengangguk."
    "Aku mengatakan hal yang sama dengan susunan kata berbeda."
    show aoi laugh at heroine with portrait_dissolve
    a "Ren. Aku melihat pohonnya."
    "Aku menutup mata sebentar. Aoi tertawa pelan, lalu melipat bungkus rotinya agar tidak terbang."
    a "Kamu boleh diam dulu."
    "Aku mendengar bunyi sendok dari jendela bangunan seberang. Sebuah sepeda lewat, remnya berdecit pada belokan."
    "Di ponsel yang kuletakkan telungkup, sepuluh menit sudah berlalu sejak kami duduk. Aku tahu karena sempat membaliknya tiga kali."
    "Hari Rabu, sepuluh detik terasa terlalu panjang. Sekarang sepuluh menit terasa seperti sesuatu yang sedang kuhamburkan."
    "Kusapu remah dari telapak tangan. Tidak semuanya terangkat."
    r "Aoi."
    show aoi neutral at closeup with portrait_dissolve
    "Ia berputar sedikit di bangku, menghadapku. Ujung sepatunya menyentuh bayangan sepatuku."
    if story_courage == "plain":
        r "Aku gugup. Padahal sudah latihan."
        r "Aku jatuh cinta sama kamu."
        "Kalimat itu keluar utuh. Setelahnya aku lupa cara mengambil napas yang biasa."
        r "Aku ingin kita berpacaran. Kalau kamu juga menginginkannya."
    else:
        r "Aku gugup. Jadi mungkin agak pelan."
        a "Iya."
        "Ia menaruh kedua tangan di atas tas, memberi seluruh perhatiannya padaku."
        r "Aku ingin mengatakannya langsung. Aku jatuh cinta sama kamu, Aoi."
        "Ujung kalimatnya lebih pelan daripada awalnya. Tetap sampai."
        r "Aku ingin kita berpacaran. Kalau kamu juga menginginkannya."
    stop music fadeout 2.0
    show aoi shy at closeup with portrait_dissolve
    "Aoi menunduk. Kali ini aku bisa melihat warna naik dari pipinya sampai ke telinga, tidak terhalang papan gambar."
    "Aku menunggu. Mencoba tidak mengisi setiap detik dengan permintaan maaf."
    "Ia menarik napas, tersenyum sebentar pada tasnya sendiri, lalu mengangkat wajah."
    show aoi tender_heart at closeup with portrait_dissolve
    a "Aku juga suka kamu. Sangat."
    play music audio.confession fadein 3.0
    "Ada suara pintu menutup di seberang halaman. Aku mendengarnya dengan jelas, seolah seluruh tempat tiba-tiba kembali mempunyai suara."
    r "Oh."
    show aoi laugh_open at closeup with portrait_dissolve
    a "Itu jawabanmu?"
    r "Aku sedang menyusul. Tunggu."
    "Aoi tertawa lagi. Ia menutup mulut dengan tangannya, tetapi matanya tetap melihatku."
    "Aku mulai tertawa juga. Ada banyak udara di dalam dada dan tidak satu pun kalimat yang tahu harus keluar lebih dulu."
    r "Aku senang."
    a "Aku juga."
    "Itu cukup untuk membuat kami diam lagi, dengan diam yang jauh berbeda."
    "Angin mengangkat ujung bungkus roti. Aku menangkapnya, melipatnya kecil-kecil, lalu menindihnya dengan botol."
    a "Aku kira kamu akan bilang Kamis."
    r "Aku memang mau."
    a "Aku agak curiga. Kamu kelihatan marah pada konektor kabel."
    r "Bukan konektornya. Bukan Sora juga. Aku hanya... tidak punya rencana kedua."
    "Aoi menekan bibir agar tidak tertawa lagi."
    a "Sora cerita banyak tentang drum. Aku jadi tahu lebih banyak daripada yang kubutuhkan."
    r "Dia sudah minta maaf."
    a "Tidak perlu. Dia tidak bisa membaca isi kepalamu."
    r "Sekarang aku tahu."
    "Kantong kertas menyentuh sepatuku. Kubiarkan tetap di sana."
    a "Ren, aku benar-benar suka kamu."
    "Mungkin wajahku masih mempertanyakan sesuatu. Aoi mengucapkannya kali ini tanpa tertawa."
    a "Aku tidak bilang cuma supaya kamu berhenti gugup."
    "Aku mengangguk. Sekali, lalu sekali lagi."
    r "Aku dengar. Terima kasih sudah bilang."
    "Ia tersenyum kecil. Aku membiarkan beberapa saat berlalu tanpa menghitungnya."

    # SCENE 11 · Percakapan sekitar satu setengah jam · pelukan dan hadiah.
    "Aoi mengambil minumannya. Tutup botolnya tidak langsung terbuka. Ia mencoba lagi, lalu menyerahkannya padaku dengan ekspresi sebal."
    a "Ternyata tanganku juga aneh."
    "Aku berhasil membukanya pada percobaan kedua. Sedikit air mengenai ibu jariku."
    r "Kita tampak sangat siap."
    a "Aku menyiapkan tiga kalimat kemarin. Semuanya hilang."
    "Ia minum seteguk, meletakkan botol di antara tas dan bangku."
    a "Salah satunya tentang pertama kali kita bicara."
    "Aku ingat sore itu. Sekitar satu setengah bulan sebelumnya, sepulang kegiatan liburan, hujan menahan beberapa siswa di dekat pintu sekolah. Aku menggambar sesuatu di belakang lembar pembagian jadwal."
    "Aoi meminta meminjam penghapus. Ketika mengembalikannya, ia menunjuk sepatu yang kugambar di sudut kertas."
    r "Kamu bilang talinya tidak mungkin diikat begitu."
    a "Memang tidak bisa. Aku mencobanya malam itu."
    r "Kamu mencobanya?"
    show aoi smile at closeup with portrait_dissolve
    a "Itu sebabnya aku mengirim foto. Kamu kira kenapa aku meminta kontakmu?"
    "Aku mengingat foto tali kusut di lantai rumahnya. Pesan pertamanya: ‘Bukti bahwa sepatumu bermasalah.’"
    "Aku menghabiskan lima belas menit menggambar versi yang benar, lalu mengirimnya kembali. Aoi membalas dengan foto percobaan kedua."
    "Percakapan itu mestinya selesai ketika simpulnya berhasil. Entah bagaimana kami mulai membahas hujan, tugas, lalu makanan malam."
    r "Kupikir kamu benar-benar kesal pada tali sepatuku."
    a "Sedikit. Aku juga ingin bicara lagi."
    "Ia mengatakannya sambil melihat lurus ke arahku. Setelah itu baru menunduk, seperti baru sadar ucapannya bisa didengar."
    r "Sejak kapan?"
    a "Aku tidak punya satu tanggal."
    "Aoi mengikuti serat kayu bangku dengan ujung jari, berhenti sebelum bagian yang terkelupas."
    a "Awalnya aku cuma senang menerima balasanmu. Kalau melihat sesuatu, aku mulai berpikir apakah kamu akan tertawa."
    if story_reply == "listen":
        a "Waktu aku cerita soal semut, kamu malah bertanya bagian mana yang paling kusuka. Aku biasa diminta menceritakan versi pendeknya."
        r "Kamu boleh membuat versi pendek kalau sudah mengantuk."
        a "Iya. Aku belajar itu setelah Selasa."
    else:
        a "Waktu aku cerita soal semut, kamu ikut bertanya hal aneh. Aku senang ada orang yang benar-benar ingin tahu jawabannya."
        r "Kita masih belum tahu kalau jalurnya diputar."
        a "Aku sudah tahu. Tapi nanti. Kita sedang membahas sesuatu yang lain."
    "Aku tertawa. Aoi mengangkat satu jari, seperti memberi tanda agar aku tidak mengalihkan pembicaraan lagi."
    a "Lalu waktu di kantin..."
    if story_company == "quiet":
        a "Kamu duduk dan mengerjakan bukumu sendiri. Aku tidak harus membuat percakapan terus. Rasanya enak."
        r "Soalku tidak selesai satu pun."
        a "Aku tahu. Halamannya tidak pindah."
        "Aku menatapnya. Aoi tersenyum tanpa menunjukkan rasa bersalah."
        a "Aku tetap senang kamu tinggal."
    else:
        a "Kamu tidak pura-pura semua kalimatku bagus. Kamu membaca sungguh-sungguh, bahkan setelah bukumu terbalik."
        r "Buku itu akan mengikutiku sampai lulus, ya?"
        a "Mungkin lebih lama."
        "Ia mengusap satu remah dari rok, lalu menambahkan dengan suara lebih kecil:"
        a "Aku senang kamu tinggal."
    "Aku menggosok telapak tangan pada celana. Tanganku mulai gemetar lagi. Kali ini bukan karena masih menunggu jawaban."
    r "Aku juga suka waktu kamu minta aku tinggal."
    a "Kamu sudah suka aku waktu itu?"
    r "Belum berani bilang begitu. Tapi waktu bel berbunyi, aku berharap jamnya salah."
    "Aoi tertawa kecil. Aku menggosok bekas lipatan bungkus roti di telapak tangan."
    "Aoi mendengarkan. Tidak ada bunyi notifikasi atau layar kecil yang bisa kugunakan untuk menyunting kalimat."
    r "Aku selalu mencari alasan yang gampang. Kita satu jalan. Aku butuh kertas. Kamu kebetulan di kantin."
    r "Padahal aku ingin duduk denganmu. Itu saja sudah alasan."
    "Ia mengangguk pelan. Aku melihatnya menahan ujung tas agar tidak jatuh dari bangku."
    r "Dan aku suka kamu bisa mengingat bagian yang orang lain lewati. Waktu konser, aku bahkan sudah lupa kami tertawa di lagu kedua."
    a "Aku melihat kamu senang. Aku ingin melihatnya lagi."
    r "Kalau pertunjukan berikutnya bersamaan dengan panelmu?"
    a "Aku pilih panel. Kamu kirim rekamannya."
    "Ia melirikku, lalu menyenggol sepatuku dengan sepatunya."
    a "Yang ada kamu tertawanya. Jangan cuma panggung kosong."
    r "Aku usahakan."
    "Kami membicarakan saat di beanbag. Aoi ternyata mengira aku tidak menjawab karena tidak ingin dipasangkan dengannya."
    "Aku menjelaskan bahwa aku takut menjawab untuk kami berdua. Ia memandang tangannya sebentar."
    a "Aku juga. Aku ingin bilang iya. Tapi aku belum tahu apa kamu mau."
    r "Kalau Mio bertanya lagi sekarang?"
    "Aoi membuka mulut, lalu tertawa tanpa suara."
    a "Tunggu. Aku ingin memastikan satu hal dulu."
    "Ia belum mengatakannya. Matanya turun pada tanganku yang bergerak kecil di atas lutut."
    show aoi surprised at closeup with portrait_dissolve
    a "Ren. Kamu gemetar."
    r "Aku tahu. Sepertinya tubuhku belum mendapat kabar."
    "Aku mencoba mengepalkan tangan. Gerakannya malah lebih kentara. Aoi memindahkan botol dan kantong roti ke sisi luar bangku."
    a "Boleh aku memelukmu?"
    "Aku mengangguk. Ia menunggu sampai aku benar-benar menatapnya."
    r "Boleh."
    show aoi shy at closeup with portrait_dissolve
    "Aoi mendekat, meletakkan satu lengan di bahuku dan satu lagi di punggung. Aku membalasnya dengan hati-hati, masih memikirkan posisi siku, tas, dan segala sesuatu yang mendadak terlalu banyak."
    "Lalu ia menepuk punggungku sekali."
    a "Tidak usah rapi."
    "Aku mengeluarkan napas yang panjang sekali. Pipiku menyentuh rambutnya. Ada bau sabun yang samar di kerah seragamnya."
    "Tanganku masih gemetar. Aoi tidak meminta agar berhenti."
    "Aku melonggarkan bahu. Kami tetap begitu sampai napasku kembali biasa."
    "Saat ia mundur, ada bekas lipatan lengan seragam di lenganku. Aku tidak buru-buru merapikannya."
    a "Aku punya banyak hal yang mau kubilang. Sekarang yang keluar sedikit sekali."
    r "Tidak harus semuanya hari ini."
    "Aoi mengangguk, melihat wajahku seolah memeriksa apakah aku sungguh-sungguh."
    r "Besok juga boleh. Atau nanti lewat pesan. Atau cuma sebagian dulu."
    show aoi smile at closeup with portrait_dissolve
    a "Kalau aku cerita soal semut lagi?"
    r "Sebelum sebelas."
    "Ia tertawa. Aku akhirnya bisa menggenggam botol tanpa takut menumpahkannya."
    "Waktu berjalan dengan aneh setelah itu. Kami sempat membicarakan kelas, rencana pameran, dan lagu yang belum punya judul. Aoi menunjukkan foto sepeda miring, lalu menjelaskan siapa yang menggambarnya."
    "Ada juga jeda-jeda ketika kami hanya duduk. Aku tidak memakainya untuk mencari jalan keluar."
    play sound audio.bell volume .5
    "Pukul satu lewat lima belas, bel dari menara mengingatkan kami pada waktu. Hampir satu setengah jam di bawah pohon."
    "Kami mulai mengumpulkan bungkus. Aoi memegang tali tasnya, lalu berhenti sebelum berdiri."
    a "Jadi... sekarang kita berpacaran?"
    "Aku berhenti melipat bungkus roti."
    r "Iya. Kalau kamu masih mau."
    show aoi laugh at heroine with portrait_dissolve
    a "Aku baru bilang aku sangat suka kamu."
    r "Iya. Aku tahu. Aku juga mau. Kita berpacaran."
    "Aoi mengangguk satu kali dengan sungguh-sungguh, lalu tersenyum begitu lebar sampai ia perlu menunduk lagi."
    "Baru setelah itu kuambil kantong kertas dari sisi bangku."
    r "Ada sesuatu untukmu. Ini kubuat sebelum hari ini."
    "Ia menatap kantong itu. Aku memegangnya di kedua sisi, tidak menyerahkan terlalu cepat."
    r "Aku sengaja menunggu sampai selesai bicara. Aku tidak ingin kamu merasa harus menjawab karena ini."
    a "Aku sudah jawab."
    r "Iya. Sekarang boleh kuberikan."
    play sound audio.page volume .6
    "Aoi menerimanya. Jarinya membuka lipatan kertas dengan teliti, seolah bungkusnya juga bagian yang harus dijaga."
    "Ia mengangkat jeans itu dari dalam. Ikan di dekat jahitan muncul lebih dulu, lalu stasiun kecil di kaki kiri."
    show screen keepsake_jeans(story_color)
    a "Ini... yang di toko itu?"
    r "Yang kamu lihat waktu itu. Mudah-mudahan pas."
    "Ia menggelar kain di atas tas, menyentuh tepi gambar tanpa menggosoknya."
    a "Ada semut."
    r "Kakinya enam. Sudah kuhitung."
    a "Rotiku juga. Dan ikan tiket."
    if story_color == "blue":
        a "Atap stasiunnya biru. Seperti pilihanmu."
        r "Jendelanya pakai kuningmu."
    else:
        a "Stasiunnya masih menyala."
        r "Biru di sekelilingnya seperti yang kamu buat."
    "Ia menelusuri ombak kecil di dekat ujung kaki. Salah satunya masih menyerupai telur dadar. Sengaja."
    "Aoi menunduk lebih lama. Aku ingin bertanya apakah ia suka, tetapi jarinya sudah menjawab dengan berpindah dari satu gambar ke gambar lain."
    a "Kamu mengingat semuanya."
    r "Tidak semuanya. Aku tidak menggambar tiga artikel."
    "Ia tertawa sekali, lalu mendekatkan kain itu ke dada."
    a "Aku suka sekali. Terima kasih."
    "Di dalam kantong ia menemukan kartu perawatan. Membacanya sampai selesai."
    a "Baik. Tidak dicuci sampai akhir pekan. Aku akan patuh."
    r "Tidak harus sering dipakai."
    a "Ren. Aku ingin memakainya."
    "Aku berhenti memberi petunjuk tambahan. Aoi melipat jeans dengan gambar stasiun tetap terlihat, memasukkannya ke kantong, lalu meraih tanganku yang bebas."
    hide screen keepsake_jeans
    "Ibu jarinya bergerak di atas jariku. Aku baru ingat membalas genggamannya setelah kami berjalan dua langkah."
    a "Ayo. Pacarku harus mengangkat amplifier."
    "Aku tersandung setengah langkah pada kata itu. Aoi menertawakan reaksiku, lalu ikut kehilangan langkah ketika aku menjawab."
    r "Dan pacarku harus memasang panel."
    "Kami kembali ke sekolah dengan empat menit tersisa sebelum giliranku. Sora melihat tangan kami, melihat jam, lalu mengangkat ujung amplifier tanpa komentar."
    scene bg musicroom with dissolve
    stop ambience fadeout 1.0
    show sora easy at leftside with portrait_dissolve
    "Sesudah kami meletakkannya di ruang musik, ia menyenggol lenganku dengan bahu."
    s "Senin berjalan lebih baik?"
    r "Jauh."
    s "Bagus. Sekarang bantu aku cari kabel yang bertanda merah."
    "Aku membantu. Di saku, ponselku bergetar satu kali."
    call phone_chat([("aoi", "Aku sudah di perpustakaan."), ("aoi", "Masih senang."), ("ren", "Aku juga. Sampai nanti.")], "13.29")
    jump epilogue

label epilogue:
    $ aoi_outfit = "blouse"
    # SCENE 12 · Sabtu sesudah pameran, lalu pesan malam.
    scene bg street with fade
    play ambience "audio/ambience/garden.ogg" fadeout 1.0 fadein 1.5 volume .3
    play music audio.tender fadeout 3.0 fadein 2.0
    "Sabtu berikutnya, Aoi datang ke toko roti dengan jeans itu."
    show aoi smile at heroine with portrait_dissolve
    "Ujung kakinya dilipat dua kali. Roti kecil di dekat jahitan berpindah sedikit lebih tinggi. Di saku belakang terselip penggaris pendek."
    a "Pas. Tapi kalau aku terus membawa alat tulis, suatu saat akan ada cat sungguhan di sini."
    r "Masih ada banyak tempat kosong."
    "Ia memperlihatkan titik ungu dekat saku."
    a "Sudah mulai. Kemarin spidolku terbuka."
    "Aku berjongkok sebentar untuk melihatnya. Titik itu tidak mengenai gambar."
    r "Sepertinya perlu diberi kaki. Bisa jadi semut baru."
    a "Tidak semua noda harus menjadi semut."
    "Kami berdiri di depan etalase, memutuskan roti yang akan dibeli. Aoi memilih kepang yang pada hari Senin sempat menjadi cadangan. Aku akhirnya mencoba yang sama."
    "Pameran sekolah selesai sehari sebelumnya. Panel Aoi mendapat empat puluh satu gambar, tujuh catatan, dan satu bungkus permen kosong yang ditempel dengan penjelasan panjang."
    "Ia tidak menyebut jumlah pengunjung ketika bercerita. Ia membahas siswa yang datang kembali untuk memperbaiki roda sepedanya, lalu memutuskan roda lama lebih lucu."
    a "Perpustakaan mengizinkan panelnya tetap di sana sampai akhir bulan. Setelah itu harus dicopot."
    r "Kamu akan simpan gambarnya?"
    a "Kalau pemiliknya mau. Aku sedang membuat amplop. Ada yang ingin dibawa pulang."
    "Ia menunjukkan daftar kecil di ponselnya. Beberapa nama sudah dicentang."
    "Aku punya latihan sore itu. Aoi tahu sejak Kamis, ketika kami menyusun rencana akhir pekan. Kami bertemu lebih pagi supaya sempat makan tanpa membuat Sora menunggu."
    "Dulu aku akan menyembunyikan jam dengan berharap waktunya memanjang sendiri. Hari ini aku menyetel pengingat."
    a "Lagu ketiga sudah punya judul?"
    r "Sora mengusulkan ‘Jangan Injak Kabel’."
    a "Pesan yang penting."
    r "Aku masih berunding."
    "Di bangku depan toko, kami membagi roti kepang. Aoi mengambil bagian yang berisi kacang lebih banyak, lalu memberiku separuh dari bagiannya setelah melihat potonganku."
    "Tidak ada pengakuan besar hari itu. Ia menyuruhku membersihkan remah di dagu. Aku mengingatkannya ada pensil yang hampir jatuh dari saku."
    "Saat ia meraih tanganku di jalan ke halte, aku masih perlu satu detik untuk percaya gerakan itu ditujukan kepadaku."
    "Kami berpisah sebelum tengah hari. Aoi pergi membeli amplop; aku ke latihan."
    r "Besok ada waktu?"
    "Ia sudah menaiki satu anak tangga bus. Aoi menoleh, mengangkat satu jari, lalu menunjuk ponselnya."
    a "Kucek dulu. Nanti kukabari."
    scene bg bedroom with fade
    play ambience "audio/ambience/night.ogg" fadeout 1.0 fadein 1.5 volume .38
    play music audio.night fadeout 3.0 fadein 2.0
    "Malamnya, Aoi mengirim foto meja yang penuh amplop. Di pojok foto tampak jeans terlipat, ikan tiket menghadap ke atas."
    call phone_chat([("aoi", "Empat puluh satu amplop ternyata banyak."), ("ren", "Masih berapa?"), ("aoi", "Sembilan. Yang besar sudah selesai."), ("ren", "Aku punya berita tentang lagu ketiga."), ("aoi", "Kabelnya selamat?")], "22.32")
    "Aku tertawa cukup keras sampai harus melihat pintu kamar. Tidak ada yang memanggil."
    "Kami membahas latihan, amplop, lalu video singkat yang dikirim Sora. Pukul sebelas kurang sepuluh, balasan Aoi mulai mempunyai salah ketik."
    call phone_chat([("aoi", "Aku masih mau dengar."), ("ren", "Aku juga masih mau cerita."), ("aoi", "Tapi aku mulai membaca dua kali."), ("ren", "Berhenti di sini dulu?")], "22.51")
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        "Masih ada banyak malam setelah ini."
        "Jaga ucapan selamat malam kami.":
            $ story_promise = "goodnight"
            call phone_chat([("ren", "Kita tidak perlu menunggu sampai mengantuk sekali untuk bilang selamat malam."), ("aoi", "Tapi aku suka bilangnya."), ("ren", "Aku suka menerimanya."), ("aoi", "Kalau begitu tetap ada. Hanya lebih awal."), ("ren", "Sepakat.")], "22.53")
            "Aku membayangkan Aoi menaruh ponsel di dekat bantal. Besok mungkin ia mengirim foto yang belum kukenal. Aku bisa menunggunya setelah tidur."
        "Simpan sebagian cerita untuk pagi.":
            $ story_promise = "morning"
            call phone_chat([("ren", "Besok pagi aku lanjutkan. Kamu bisa baca sambil sarapan."), ("aoi", "Ada pesan selamat pagi juga?"), ("ren", "Kalau kamu mau."), ("aoi", "Mau. Tapi tidak usah bangun hanya untuk mengirimnya."), ("ren", "Kamu juga.")], "22.53")
            "Aku menulis satu catatan agar tidak lupa cerita latihan. Hanya tiga kata: Sora, kabel, judul. Sisanya masih ada di kepala, menunggu pagi."
    call phone_chat([("aoi", "Ren."), ("ren", "Iya?"), ("aoi", "Aku senang kita sekarang bisa bilang begitu."), ("ren", "Begitu yang mana?"), ("aoi", "Mau. Aku mau."), ("ren", "Aku juga.")], "22.55")
    "Tidak ada yang sedang menghitung sepuluh detik. Aku membiarkan pesan itu terbaca sebelum mengetik balasan terakhir."
    call phone_chat([("ren", "Selamat malam, Aoi."), ("aoi", "Selamat malam, Ren. Sampai besok.")], "22.57")
    "Kusimpan ponsel di meja, di samping pensil yang belum kuraut."
    "Besok aku masih harus memperbaiki lagu. Aoi masih punya sembilan amplop. Ada tugas sekolah, bus yang perlu dikejar, dan percakapan yang belum selesai."
    "Aku mematikan lampu."
    "Untuk pertama kalinya setelah sekian lama, menunggu besok tidak membuatku ingin menahan malam."
    $ persistent.completed = True
    $ renpy.save_persistent()
    call chapter_card("TAMAT", "Sepuluh detik, lalu seterusnya", "Terima kasih telah menemani Ren dan Aoi.")
    stop music fadeout 3.0
    stop ambience fadeout 2.0
    return
