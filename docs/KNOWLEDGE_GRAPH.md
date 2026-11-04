# Knowledge graph untuk pengembangan MADOROMI

Graphify **0.9.102** sudah dipasang dalam environment pengembangan terpisah di
`/workspace/toolchains/graphify-venv`. Skill Codex asli, resource, Apache-2.0,
lisensi MIT historis dan NOTICE disimpan di
[`.agents/skills/graphify`](../.agents/skills/graphify/). `UPSTREAM.json` mencatat
versi paket, hash wheel yang diterbitkan PyPI dan hash setiap berkas skill.
Tidak ada dependency Graphify di APK atau paket permainan.

## Pakai dari AI coding

Jalankan dari root repository:

```sh
# Hanya pada mesin baru; environment tetap di luar Git.
MADOROMI_GRAPHIFY_ENV=/path/outside/repository/graphify-venv tools/knowledge_graph.sh setup

# Environment workspace saat ini otomatis ditemukan.
tools/knowledge_graph.sh build
python3 tests/check_knowledge_graph.py
tools/knowledge_graph.sh query "story_color" --budget 1500
tools/knowledge_graph.sh path "label:start" "label:act_3"
tools/knowledge_graph.sh explain "screen:save"
```

Pada mesin selain workspace ini, tetapkan `MADOROMI_GRAPHIFY_ENV` pada path
environment yang dipakai saat `setup`, atau `MADOROMI_TOOLCHAINS` untuk parent
direktorinya. Query/path/explain memakai CLI Graphify asli dengan graph proyek
yang dipilih secara eksplisit. Semua query melalui wrapper memeriksa freshness
lebih dahulu. Bila source berubah, jalankan `build`; jangan mengutip graph lama.
Tidak perlu API key, daemon, MCP, hook global atau model tambahan untuk rebuild.

AI coding memakai graph sebagai indeks sebelum perubahan yang menyentuh
beberapa file: cari label/screen/state/asset terkait, ikuti koneksinya, kemudian
baca source pada baris yang dikutip. Setelah mengubah input graph, regenerate
dan jalankan checker sebelum commit. Graph membantu penelusuran; lint Ren’Py,
test native, tinjauan screenshot dan tes APK tetap diperlukan.

## Artefak yang dibagikan

- [graph.json](graph/graph.json): graph terarah yang kompatibel dengan Graphify,
  mempertahankan semua evidence edge beserta jenis, confidence dan sumber.
- [graph.html](graph/graph.html): tampilan interaktif dari exporter Graphify;
  pencarian, community filter dan inspeksi tetangga. Versi exporter memakai
  `vis-network@9.1.6` dari CDN dengan Subresource Integrity; viewer membutuhkan
  akses ke CDN. JSON dan query CLI bekerja offline.
- [GRAPH_REPORT.md](graph/GRAPH_REPORT.md): analisis community/cohesion dan batas
  cakupan. Hitungan visual menggabungkan evidence berulang pada endpoint sama.
- [extraction.json](graph/extraction.json): evidence sebelum penggabungan untuk
  pemeriksaan source dan penelusuran seluruh baris yang berulang.
- [manifest.json](graph/manifest.json): fingerprint input dan output, versi tool,
  serta hitungan node/edge. Output graph tidak menjadi inputnya sendiri.

## Dukungan Ren’Py yang sebenarnya

Classifier Graphify 0.9.102 mengembalikan `None` untuk `.rpy`. Proyek memakai
adapter deterministik kecil di [knowledge_graph.py](../tools/knowledge_graph.py)
untuk deklarasi label/screen/transform, jump/call/use, native action, lima menu
dan state/callback, karakter, cue gambar/audio, serta referensi aset. Adapter
memberi source file dan nomor baris pada setiap hubungan yang diekstrak.
Ini bukan parser Ren’Py lengkap atau pembuktian semua jalur runtime. Ekspresi
dinamis yang tidak dapat ditetapkan tidak ditebak.

Kode Python tooling diperiksa oleh tree-sitter milik Graphify asli. Hasilnya
digabung dengan adapter, dibangun lewat `graphify.build`, dikelompokkan lewat
`graphify.cluster`, lalu diekspor lewat `graphify.export`. Import/call Python
yang definisinya tidak ditemukan ditandai sebagai unresolved external symbol;
graph tidak mengklaim telah mengaudit implementasi library tersebut.

Tiga dokumen terpilih—story bible, workflow build dan audit naskah—memiliki
ekstraksi semantik oleh reviewer AI terpisah. Hasilnya ada di
[semantic.json](graph/semantic.json), dengan anchor baris asli. Anchor yang
hanya berpindah akan direbase; anchor yang berubah harus direview sebelum
rebuild dapat diteruskan. Token host-agent tidak tersedia, sehingga field nol
pada laporan upstream bukan klaim bahwa seluruh pembuatan graph tanpa biaya.

Input dibatasi pada source game, tooling/test produksi, workflow CI, tiga
dokumen tersebut dan manifest seni. Gambar diindeks dari manifest tanpa
mengekstrak piksel. Skill upstream, SDK, signing key, cache, dokumen Drive privat,
referensi JPG dan aset mentah tidak dipindai.

## Verifikasi

Checker tanpa dependency tambahan memastikan input belum berubah, fingerprint
artefak cocok, semua endpoint ada, confidence dan nomor baris valid, lima
pilihan memiliki penulisan state dan callback baca, serta hubungan start → act1,
act3 → courtyard dan quick menu → save masih ada. Hash aset aktual juga harus
cocok dengan manifest produksi. Pemeriksaan freshness telah terbukti menolak
graph ketika source UI berubah saat produksi, lalu lulus setelah rebuild.

Riwayat hasil query dan uji viewer disertakan bila telah dijalankan. Rebuild
ulang setelah perubahan source apa pun adalah langkah wajib sebelum memakai
hasil tersebut sebagai bukti versi terbaru.
