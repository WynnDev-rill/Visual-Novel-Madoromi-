# Madoromi art direction, built on native Ren'Py screens/actions.
init offset = 2

screen say(who, what):
    if who is None:
        add "gui/madoromi/reading_shade.png" xysize (1920, 430) yalign 1.0
        window:
            id "window"
            background None
            ysize None
            xpos 160
            xanchor 0.0
            ypos (650 if renpy.get_screen("choice") else 916)
            yanchor 1.0
            xsize 1600
            padding (0, 0)
            text what id "what" xpos 0 ypos 0 font "fonts/NotoSerif-Regular.ttf" size persistent.text_size color "#fffaf1" line_spacing 10 outlines [(1, "#12243ac0", 0, 1)]
    else:
        window:
            id "window"
            background Frame("gui/madoromi/bubble.png", 34, 34)
            ysize None
            xpos 150
            xanchor 0.0
            ypos 920
            yanchor 1.0
            xsize 1480
            padding (42, 27)
            vbox:
                spacing 12
                text who id "who" font "fonts/NotoSans-Regular.ttf" size 29 bold True color "#8c513f"
                text what id "what" xpos 0 ypos 0 font "fonts/NotoSerif-Regular.ttf" size persistent.text_size color "#293d50" line_spacing 8

screen quick_menu():
    zorder 100
    if quick_menu:
        frame:
            style "reading_toolbar"
            hbox:
                spacing 12
                style_prefix "quick"
                textbutton "Kembali" action Rollback()
                textbutton "Riwayat" action ShowMenu("history")
                textbutton "Lewati" action Skip() alternate Skip(fast=True, confirm=True)
                textbutton "Otomatis" action Preference("auto-forward", "toggle")
                textbutton "Simpan" action ShowMenu("save")
                textbutton "Muat" action ShowMenu("load")
                textbutton "Menu" action Show("reading_menu")


screen reading_menu():
    modal True
    zorder 120
    button:
        xfill True
        yfill True
        background Solid("#0b203655")
        action Hide("reading_menu")
    frame:
        xalign .94
        ypos 150
        xsize 360
        padding (22, 20)
        background Frame("gui/madoromi/panel.png", 34, 34)
        vbox:
            spacing 12
            text "MADOROMI" size 24 color "#466e85" xalign .5
            for caption, destination in [("Simpan", "save"), ("Muat", "load"), ("Riwayat", "history"), ("Pengaturan", "preferences"), ("Bab & kenangan", "chapters")]:
                textbutton caption action [Hide("reading_menu"), ShowMenu(destination)] style "reading_menu_button"
            textbutton "Halaman judul" action [Hide("reading_menu"), MainMenu()] style "reading_menu_button"
            textbutton "Lanjut membaca" action Hide("reading_menu") style "reading_menu_button"
    key "game_menu" action Hide("reading_menu")

screen main_menu():
    tag menu
    add "images/originals/courtyard.webp" at scene_drift
    add "gui/madoromi/title_veil.png" xysize (1180, 1080)
    add "aoi smile" at title_character
    text "まどろみ" font "fonts/MadoromiTitleJP.otf" size 47 color "#3b6177" xpos 128 ypos 90
    text "MADOROMI" font "fonts/NotoSerif-Regular.ttf" size 95 color "#203f57" xpos 123 ypos 148
    text "Sepuluh Detik" font "fonts/NotoSerif-Italic.ttf" size 32 color "#875d4c" xpos 133 ypos 270
    text "Ada hal-hal kecil yang ingin\nkuceritakan hanya kepadamu." font "fonts/NotoSerif-Italic.ttf" size 30 color "#344f63" xpos 133 ypos 332 line_spacing 8
    vbox:
        xpos 117
        ypos 440
        spacing 5
        style_prefix "title"
        textbutton "Lanjutkan" action Continue()
        textbutton "Cerita baru" action Start()
        textbutton "Bab & kenangan" action ShowMenu("chapters")
        textbutton "Pengaturan" action ShowMenu("preferences")
        textbutton "Kredit" action ShowMenu("credits")
        if renpy.variant("pc"):
            textbutton "Keluar" action Quit(confirm=False)
    text "Sebuah kisah tentang berani tinggal sedikit lebih lama." size 22 color "#365468" xpos 133 ypos 1020
    text "WYNNDEV  /  1.0" size 20 color "#fff7ed" outlines [(1, "#263a4b", 0, 1)] xalign .955 yalign .947



screen chapters():
    tag menu
    use game_menu("Bab & kenangan", scroll="viewport"):
        vbox:
            spacing 25
            text "Mulai ulang suatu bab tanpa mengubah simpanan manual." size 26 color "#526d7f"
            for number, label_name, title, subtitle in [(1,"act_1","01 — Hal-hal kecil","Pesan pukul 01.43 • kantin • sepuluh detik"),(2,"act_2","02 — Kalimat yang tertunda","Konser • Kamis • warna pada kain"),(3,"act_3","03 — Sedikit lebih lama","Toko roti • pengakuan • hari-hari sesudahnya")]:
                button:
                    action Start(label_name)
                    sensitive persistent.chapter_unlocked >= number
                    xsize 1120
                    padding (30, 22)
                    background Solid("#e4edf0")
                    hover_background Solid("#cedfe7")
                    vbox:
                        spacing 10
                        text title size 34 color ("#2e5369" if persistent.chapter_unlocked >= number else "#8295a2")
                        text (subtitle if persistent.chapter_unlocked >= number else "Terbuka setelah bab sebelumnya selesai.") size 25 color "#526d7f"
            if persistent.completed:
                null height 20
                text "Terima kasih telah menemani Ren dan Aoi." font "fonts/NotoSerif-Regular.ttf" size 36 color "#91543e"
                text "Kenangan tersimpan dalam hal-hal kecil." size 27
                hbox:
                    spacing 24
                    for image_name in ["courtyard", "bakery", "lounge"]:
                        add ("images/originals/" + image_name + ".webp") xysize (342, 193)

screen credits():
    tag menu
    use game_menu("Kredit", scroll="viewport"):
        vbox:
            spacing 20
            text "MADOROMI — Sepuluh Detik" font "fonts/NotoSerif-Regular.ttf" size 42 color "#345b72"
            text "Produksi: WynnDev\nAdaptasi cerita pendek pengguna. Naskah, penyutradaraan dan integrasi dengan bantuan AI.\nTanpa voice acting karakter." size 27
            text "Karakter & latar" size 34 color "#91543e"
            text "Potat0Master — Character Sets A01/A02 dan environment packs. Digunakan dengan izin komersial untuk bundel game. Hak ilustrasi tetap pada kreator.\nLatar katedral, toko roti dan lounge: ilustrasi orisinal melalui OpenAI image generation.\nIkon aplikasi: master pilihan pengguna dari Google Drive." size 26 xsize 1120
            text "Musik" size 34 color "#91543e"
            text "Dream Culture, Easy Lemon, Touching Moments Five – Circle, Touching Moments Four – Melody\nKevin MacLeod (incompetech.com)\nLicensed under Creative Commons: By Attribution 4.0\nhttps://creativecommons.org/licenses/by/4.0/\nDikonversi ke Ogg dan disesuaikan level volumenya." size 26 xsize 1120
            text "Efek, suasana & font" size 34 color "#91543e"
            text "Interface Sounds — Kenney (kenney.nl), CC0.\nInventory Sound Effects (turn_page.wav) by artisticdude, submitted by Ogrebane.\nhttps://opengameart.org/content/inventory-sound-effects\nLicensed under CC BY 3.0: https://creativecommons.org/licenses/by/3.0/\nConverted to Ogg Vorbis and level adjusted for MADOROMI.\n\nCrickets — Ted Kerr / Wolfgang_, CC0.\nAmbient Bird Sounds — isaiah658, CC0.\nPleasing Bell — Julie Damsgaard / Spring Spring / Spring Enterprises, CC0.\n\nNoto Sans / Noto Serif / Noto Serif CJK JP — SIL Open Font License 1.1.\nKredit dan lisensi lengkap juga disertakan di berkas distribusi game." size 26 xsize 1120
            text "Engine" size 34 color "#91543e"
            text "Ren'Py 8.5.3 — www.renpy.org\nRen'Py menyertakan komponen MIT, LGPL dan lisensi lain. Lisensi engine disertakan dalam distribusi." size 26
            textbutton "Informasi Ren'Py" action ShowMenu("about")

screen about():
    tag menu
    use game_menu("Tentang", scroll="viewport"):
        vbox:
            spacing 20
            text gui.about size 27 xsize 1120
            text "Dibuat dengan Ren'Py [renpy.version_only]." size 27
            textbutton "Lisensi engine" action OpenURL("https://www.renpy.org/doc/html/license.html")

screen chapter_title(number, title, subtitle):
    modal True
    button:
        xfill True
        yfill True
        action Return()
        background Solid("#101b2a")
    vbox:
        xalign .5
        yalign .46
        spacing 30
        at card_in
        text "B A G I A N  [number]" xalign .5 size 26 color "#e4b49d"
        add Solid("#e4b49d") xalign .5 xysize (72, 2)
        text title xalign .5 font "fonts/NotoSerif-Regular.ttf" size 72 color "#f4e5ce"
        text subtitle xalign .5 size 29 color "#b8c7d7"
    text "Ketuk untuk melanjutkan" xalign .5 yalign .87 size 24 color "#a4b7c8"
    key "dismiss" action Return()
    if renpy.is_skipping():
        timer .05 action Return()
    elif _preferences.afm_enable:
        timer 3.0 action Return()

screen phone_messages(messages, time_label):
    modal True
    button:
        xfill True
        yfill True
        action Return()
        background Solid("#071322a8")
    frame:
        xalign .5
        yalign .43
        xsize 1050
        ysize 790
        padding (44, 28)
        background Solid("#15283aef")
        vbox:
            spacing 14
            hbox:
                xfill True
                text "AOI  /  PESAN" size 24 color "#e7b49f"
                text time_label xalign 1.0 size 24 color "#b3c4d3"
            add Solid("#64809960") xysize (962, 1)
            viewport:
                ysize 610
                yinitial 1.0
                mousewheel True
                draggable True
                vbox:
                    xfill True
                    spacing 18
                    for sender, message in messages:
                        frame:
                            xalign (1.0 if sender == "ren" else 0.0)
                            xmaximum 830
                            padding (24, 16)
                            background Solid("#34516a" if sender == "ren" else "#263b4e")
                            vbox:
                                spacing 6
                                text ("Ren" if sender == "ren" else "Aoi") size 20 color "#e7b49f"
                                text message size (persistent.text_size - 3) color "#f5f1e8" xmaximum 778 line_spacing 5
    text "Ketuk untuk pesan berikutnya   ·   pesan tercatat di Riwayat" xalign .5 yalign .86 size 24 color "#d1d9e0"
    key "dismiss" action Return()
    if renpy.is_skipping():
        timer .05 action Return()
    elif _preferences.afm_enable:
        timer (max(2.0, len(messages[-1][1]) / 18.0)) action Return()

screen keepsake_jeans(palette):
    zorder 40
    frame:
        xalign .15
        yalign .24
        xsize 760
        padding (18, 18)
        background Solid("#f2e6d8f5")
        vbox:
            spacing 12
            add "images/originals/jeans.webp" xysize (724, 543)
            text "Dilukis satu per satu. Untuk Aoi." font "fonts/NotoSerif-Italic.ttf" size 26 color "#35485e" xalign .5

style title_button is button:
    xsize 560
    ysize (108 if renpy.mobile else 82)
    padding (14, 8)
    background None
    hover_background Solid("#b7d1df80")
style title_button_text is button_text:
    size 33
    color "#294b62"
    hover_color "#914c38"
    insensitive_color "#7c8b91"
style quick_button is button:
    xminimum 135
    yminimum 108
    padding (15, 17)
    background None
    hover_background Solid("#c4dce8")
    selected_background Solid("#bfd8e5")
style quick_button_text is button_text:
    size 26
    idle_color "#36576d"
    hover_color "#7c452f"
    selected_color "#204e68"
style reading_toolbar is frame:
    xalign .95
    xoffset -40
    yalign 1.0
    yoffset -24
    padding (10, 0)
    background Frame("gui/madoromi/panel.png", 34, 34)
style reading_menu_button is button:
    xfill True
    yminimum 108
    padding (18, 16)
    hover_background Solid("#d5e6ed")
style reading_menu_button_text is button_text:
    size 29
    color "#36576d"
    hover_color "#8c513f"
style choice_vbox:
    ypos 915
    yanchor 1.0
    spacing 18
style choice_button:
    background Frame("gui/madoromi/choice.png", 34, 34)
    hover_background Frame("gui/madoromi/choice_hover.png", 34, 34)
    xsize 1500
    yminimum 108
    padding (40, 22)
style choice_button_text:
    size 33
    color "#293e51"
    hover_color "#1e5873"
style button:
    selected_background Solid("#bfd8e560")
    activate_sound "audio/sfx/ui.ogg"
style button_text:
    hover_color "#8c513f"
style bar:
    ysize 34
    left_bar Solid("#638fa5")
    right_bar Solid("#d2dce1")
    thumb Solid("#365f79", xysize=(18, 46))
style slider:
    ysize 34
    base_bar Solid("#d2dce1")
    thumb Solid("#365f79", xysize=(18, 46))
    left_bar Solid("#638fa5")
    right_bar Solid("#d2dce1")
style say_dialogue:
    xpos 0
    ypos 0
    xsize None
    xalign 0.0
style say_label:
    xalign 0.0
    yalign 0.0
