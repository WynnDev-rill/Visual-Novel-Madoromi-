# Coastal blue system screens. All progress/settings use native Ren'Py actions.
init offset = 3

init python:
    def madoromi_system_panel(fill, border="#79cde5"):
        # A crisp frame made from native displayables; no copied UI graphics.
        return Frame(Composite((8, 8), (0, 0), Solid(border, xysize=(8, 8)),
            (1, 1), Solid(fill, xysize=(6, 6))), 2, 2)

    def madoromi_history_color(who):
        name = renpy.filter_text_tags(who or "", allow=set()).split(" · ", 1)[0]
        return {
            "Aoi": "#ffcfb5",
            "Ren": "#a9deff",
            "Sora": "#daedb7",
            "Mio": "#ddc6f5",
        }.get(name, "#f3faff")

    def madoromi_slot_excerpt(slot):
        excerpt = renpy.filter_text_tags(FileSaveName(slot), allow=set())
        excerpt = " ".join(excerpt.split())
        if not excerpt:
            return "Bagian cerita tersimpan."
        return excerpt if len(excerpt) <= 64 else excerpt[:61].rstrip() + "…"


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "system"
    $ history_mode = title == "Riwayat"

    add Solid("#eff9ff")
    add "images/originals/courtyard.webp" alpha (.22 if history_mode else .08)
    if history_mode:
        add Solid("#082d42df")
    add Solid("#22779f" if not history_mode else "#071f2d") xysize (1920, 190)
    add Transform("images/originals/courtyard.webp", crop=(0, 0, 1920, 600), xysize=(1920, 190), alpha=.18)
    text ("Kenangan" if title == "Bab & kenangan" else title) style "system_heading" xpos 70 ypos 30 xanchor 0.0 yanchor 0.0

    hbox:
        xpos 550
        ypos 76
        spacing 0

        textbutton "Simpan":
            style "system_tab_button"
            action ShowMenu("save")
            selected title == "Simpan"
            sensitive not main_menu
        textbutton "Muat":
            style "system_tab_button"
            action ShowMenu("load")
            selected title == "Muat"
        textbutton "Riwayat":
            style "system_tab_button"
            action ShowMenu("history")
            selected title == "Riwayat"
            sensitive not main_menu and bool(_history_list)
        textbutton "Pengaturan":
            style "system_tab_button"
            action ShowMenu("preferences")
            selected title == "Pengaturan"
        textbutton "Kenangan":
            style "system_tab_button"
            action ShowMenu("chapters")
            selected title == "Bab & kenangan"
            sensitive renpy.has_screen("chapters")
        textbutton "Kredit":
            style "system_tab_button"
            action ShowMenu("credits")
            selected title in ("Kredit", "Tentang")
            sensitive renpy.has_screen("credits")
        textbutton "Bantuan":
            style "system_tab_button"
            action ShowMenu("help")
            selected title == "Bantuan"
            sensitive renpy.has_screen("help")

    add Solid("#79cde5") ypos 188 xysize (1920, 2)

    frame:
        style "system_content_frame"
        xpos 100
        ypos 220
        xysize (1720, 690)

        if scroll == "viewport":
            viewport:
                style "system_viewport"
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True

                vbox:
                    xfill True
                    spacing spacing
                    transclude

        elif scroll == "vpgrid":
            vpgrid:
                style "system_viewport"
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                spacing spacing
                transclude

        else:
            transclude

    add Solid("#082d42f0" if history_mode else "#f6fcfff2") ypos 936 xysize (1920, 144)
    add Solid("#79cde5") ypos 936 xysize (1920, 2)
    textbutton "Kembali":
        style "system_footer_button"
        xpos 90
        ypos 952
        action Return()

    if not main_menu:
        textbutton "Halaman judul":
            style "system_footer_button"
            xalign 1.0
            xoffset -90
            ypos 952
            action MainMenu()
    else:
        key "game_menu" action ShowMenu("main_menu")


screen system_setting_heading(caption):
    vbox:
        spacing 8
        hbox:
            spacing 12
            add Solid("#47b6dc") xysize (10, 10) yalign .5
            text caption style "system_section_heading"
        add Solid("#9cd5e5") xysize (760, 1)


screen preferences():
    tag menu
    default preference_tab = "Membaca"

    use game_menu("Pengaturan"):
        fixed:
            hbox:
                spacing 16
                for tab in ("Membaca", "Suara", "Kontrol"):
                    textbutton tab:
                        style "system_subtab_button"
                        action SetScreenVariable("preference_tab", tab)
                        selected preference_tab == tab

            viewport:
                style_prefix "system"
                ypos 132
                xysize (1720, 558)
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                vbox:
                    xfill True
                    if preference_tab == "Membaca":
                        hbox:
                            spacing 80

                            vbox:
                                xsize 760
                                spacing 18

                                use system_setting_heading("Ukuran teks")
                                hbox:
                                    spacing 16
                                    textbutton "Standar":
                                        style "system_option_button"
                                        action SetField(persistent, "text_size", 36)
                                        selected persistent.text_size == 36
                                    textbutton "Besar":
                                        style "system_option_button"
                                        action SetField(persistent, "text_size", 42)
                                        selected persistent.text_size == 42

                                use system_setting_heading("Kecepatan teks")
                                bar:
                                    style "system_slider"
                                    value Preference("text speed")
                                    alt "Kecepatan teks"

                                use system_setting_heading("Jeda mode otomatis")
                                bar:
                                    style "system_slider"
                                    value Preference("auto-forward time")
                                    alt "Jeda mode otomatis"

                                text "Pilihan dialog tidak dibatasi waktu." style "system_note" yoffset 8

                            vbox:
                                xsize 760
                                spacing 16

                                button:
                                    style "system_toggle_button"
                                    action Preference("skip", "toggle")
                                    fixed:
                                        xfill True
                                        yfill True
                                        text "Lewati teks belum dibaca" style "system_toggle_button_text"
                                        text ("Aktif" if _preferences.skip_unseen else "Nonaktif") style "system_toggle_button_text" xalign 1.0

                                button:
                                    style "system_toggle_button"
                                    action Preference("after choices", "toggle")
                                    fixed:
                                        xfill True
                                        yfill True
                                        text "Lewati setelah pilihan" style "system_toggle_button_text"
                                        text ("Aktif" if _preferences.skip_after_choices else "Nonaktif") style "system_toggle_button_text" xalign 1.0

                                button:
                                    style "system_toggle_button"
                                    action ToggleField(persistent, "reduce_motion")
                                    selected persistent.reduce_motion
                                    fixed:
                                        xfill True
                                        yfill True
                                        text "Kurangi gerakan" style "system_toggle_button_text"
                                        text ("Aktif" if persistent.reduce_motion else "Nonaktif") style "system_toggle_button_text" xalign 1.0

                                button:
                                    style "system_toggle_button"
                                    action Preference("transitions", "toggle")
                                    selected bool(_preferences.transitions)
                                    fixed:
                                        xfill True
                                        yfill True
                                        text "Transisi" style "system_toggle_button_text"
                                        text ("Aktif" if _preferences.transitions else "Nonaktif") style "system_toggle_button_text" xalign 1.0

                                text "Gerak latar dan karakter dibuat lebih tenang." style "system_note" xsize 740 yoffset 8

                    elif preference_tab == "Suara":
                        hbox:
                            spacing 80

                            vbox:
                                xsize 760
                                spacing 18

                                use system_setting_heading("Musik")
                                bar:
                                    style "system_slider"
                                    value Preference("music volume")
                                    alt "Volume musik"

                                use system_setting_heading("Efek suara")
                                bar:
                                    style "system_slider"
                                    value Preference("sound volume")
                                    alt "Volume efek suara"

                                use system_setting_heading("Suasana lingkungan")
                                bar:
                                    style "system_slider"
                                    value Preference("mixer ambience volume")
                                    alt "Volume suasana lingkungan"

                            vbox:
                                xsize 760
                                spacing 24

                                button:
                                    style "system_toggle_button"
                                    action Preference("all mute", "toggle")
                                    fixed:
                                        xfill True
                                        yfill True
                                        text "Senyapkan semua" style "system_toggle_button_text"
                                        text ("Aktif" if all(_preferences.get_mute(mixer) for mixer in _preferences.get_all_mixers()) else "Nonaktif") style "system_toggle_button_text" xalign 1.0

                                textbutton "Uji efek":
                                    style "system_option_button"
                                    action Play("sound", audio.message)

                                text "Musik, efek, dan suasana dapat diatur terpisah." style "system_note" xsize 730

                    else:
                        hbox:
                            spacing 80

                            vbox:
                                xsize 760
                                spacing 24
                                text "Layar sentuh" style "system_section_heading"
                                text "Ketuk dialog untuk melanjutkan cerita. Ketuk jawaban untuk memilih." style "system_text" xsize 740
                                text "Gunakan Menu untuk membuka simpan, muat, riwayat, dan pengaturan." style "system_text" xsize 740
                                text "Geser riwayat untuk membaca ulang. Tombol Kembali menutup menu yang sedang dibuka." style "system_text" xsize 740

                            vbox:
                                xsize 760
                                spacing 22

                                if renpy.variant("pc"):
                                    text "Layar" style "system_section_heading"
                                    hbox:
                                        spacing 16
                                        textbutton "Jendela":
                                            style "system_option_button"
                                            action Preference("display", "window")
                                        textbutton "Penuh":
                                            style "system_option_button"
                                            action Preference("display", "fullscreen")

                                text "Keyboard" style "system_section_heading"
                                text "Enter / Spasi   Lanjut membaca\nEscape   Buka atau tutup menu\nTombol panah   Pilih kontrol\nCtrl   Tahan untuk melewati dialog\nPage Up   Kembali ke dialog sebelumnya" style "system_text" xsize 750 line_spacing 10

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern="Halaman {}", auto="Simpanan otomatis", quick="Simpanan cepat")

    use game_menu(title):
        fixed:
            # Preserve the native page-name field's input priority.
            order_reverse True

            hbox:
                spacing 16
                if config.has_autosave:
                    textbutton "Otomatis":
                        style "system_subtab_button"
                        action FilePage("auto")
                if config.has_quicksave:
                    textbutton "Cepat":
                        style "system_subtab_button"
                        action FilePage("quick")

            button:
                style "system_page_name_button"
                xpos 620
                key_events True
                action page_name_value.Toggle()
                input:
                    style "system_page_name_text"
                    value page_name_value

            grid 2 2:
                ypos 132
                spacing 24

                for i in range(4):
                    $ slot = i + 1
                    $ occupied = FileLoadable(slot)

                    fixed:
                        xysize (848, 190)

                        button:
                            style "system_slot_button"
                            background madoromi_system_panel("#f6fcff" if occupied else "#48749a")
                            hover_background madoromi_system_panel("#ddf5ff" if occupied else "#376b98", "#1776a1")
                            action FileAction(slot)
                            alt ("Muat slot %02d" % slot if title == "Muat" else "Simpan slot %02d" % slot)

                            if occupied:
                                add FileScreenshot(slot) xpos 22 ypos 20 xysize (264, 148)
                                vbox:
                                    xpos 316
                                    ypos 20
                                    xsize 354
                                    spacing 8
                                    text ("Slot %02d" % slot) style "system_slot_number"
                                    text FileTime(slot, format="%d/%m/%Y  %H:%M") style "system_slot_date"
                                    text madoromi_slot_excerpt(slot) style "system_slot_excerpt" substitute False
                            else:
                                text ("Slot %02d" % slot) style "system_slot_number" color "#e6f7ff" xpos 26 ypos 16
                                text "Belum ada simpanan" style "system_slot_empty" xpos 26 ypos 58
                                text ("Ketuk untuk menyimpan." if title == "Simpan" else "Pilih halaman lain untuk mencari simpanan.") size 24 color "#ffffff" xpos 26 ypos 130

                            key "save_delete" action FileDelete(slot)

                        if occupied:
                            textbutton "Hapus":
                                style "system_delete_button"
                                xpos 692
                                ypos 78
                                action FileDelete(slot)

            hbox:
                xalign .5
                ypos 566
                spacing 12

                textbutton "Sebelum":
                    style "system_page_arrow_button"
                    action FilePagePrevious()
                for page in range(1, 10):
                    textbutton "[page]":
                        style "system_page_button"
                        action FilePage(page)
                textbutton "Sesudah":
                    style "system_page_arrow_button"
                    action FilePageNext()

            key "save_page_prev" action FilePagePrevious()
            key "save_page_next" action FilePageNext()


screen history():
    tag menu
    predict False

    use game_menu("Riwayat", scroll="viewport", yinitial=1.0, spacing=0):
        if _history_list:
            for index, h in enumerate(_history_list):
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                $ identifier = getattr(h, "rollback_identifier", None)
                $ rollback_action = RollbackToIdentifier(identifier) if identifier is not None else None

                frame:
                    style "system_history_row"
                    background Solid("#0c3d57c8" if index % 2 == 0 else "#154b65a8")

                    hbox:
                        spacing 24

                        text (h.who or ""):
                            style "system_history_speaker"
                            color madoromi_history_color(h.who)
                            substitute False

                        text what:
                            style "system_history_text"
                            size (36 if persistent.text_size == 42 else 32)
                            substitute False

                        if rollback_action is not None and rollback_action.get_sensitive():
                            textbutton "Ke sini":
                                style "system_history_jump_button"
                                action rollback_action
                        else:
                            null width 176
        else:
            vbox:
                spacing 20
                null height 150
                text "Belum ada dialog dalam riwayat." style "system_section_heading" color "#ffffff"
                text "Dialog yang sudah dibaca akan tercatat di sini." style "system_text" color "#d5ecf6"


style system_text is text:
    font "fonts/NotoSans-Regular.ttf"
    size 30
    color "#153d5a"
    line_spacing 6

style system_heading is system_text:
    font "fonts/NotoSans-Regular.ttf"
    size 72
    color "#ffffff"
    outlines [(1, "#153d5a50", 0, 1)]

style system_section_heading is system_text:
    size 34
    color "#153d5a"

style system_note is system_text:
    size 26
    color "#385f78"

style system_button is button:
    xminimum 72
    ysize 108
    padding (24, 12)
    background madoromi_system_panel("#f8fdff")
    hover_background madoromi_system_panel("#176f96", "#176f96")
    selected_background madoromi_system_panel("#176f96", "#176f96")
    selected_hover_background madoromi_system_panel("#135d80", "#135d80")
    insensitive_background madoromi_system_panel("#e1edf3", "#b5ced9")

style system_button_text is system_text:
    color "#153d5a"
    hover_color "#ffffff"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    insensitive_color "#617d8e"
    xalign .5
    yalign .5

style system_tab_button is system_button:
    xsize 180
    padding (12, 12)
    background madoromi_system_panel("#1e648a", "#79cde5")
    hover_background madoromi_system_panel("#2a7ba3", "#bcefff")
    selected_background madoromi_system_panel("#f5fcff", "#a7e4f3")
    selected_hover_background madoromi_system_panel("#ffffff", "#79cde5")
    insensitive_background madoromi_system_panel("#236384", "#4e8daa")

style system_tab_button_text is system_button_text:
    size 26
    color "#ffffff"
    hover_color "#ffffff"
    selected_color "#153d5a"
    selected_hover_color "#153d5a"
    insensitive_color "#b8d3e0"

style system_subtab_button is system_button:
    xsize 248

style system_subtab_button_text is system_button_text

style system_option_button is system_button:
    xsize 248

style system_option_button_text is system_button_text

style system_toggle_button is system_button:
    xsize 760
    ysize 108
    padding (24, 18)

style system_toggle_button_text is system_button_text:
    xalign 0.0

style system_footer_button is system_button:
    xminimum 248
    background madoromi_system_panel("#176f96", "#79cde5")

style system_footer_button_text is system_button_text:
    color "#ffffff"

style system_content_frame is empty:
    padding (0, 0)

style confirm_frame:
    background madoromi_system_panel("#f3faff")
    padding (56, 44)

style confirm_prompt_text:
    color "#153d5a"
    size 36
    xmaximum 1320
    line_spacing 8

style confirm_button is system_button:
    xsize 300
    ysize 108

style confirm_button_text is system_button_text

style system_viewport is viewport:
    xfill True
    yfill True

style system_side is side:
    spacing 0

style system_vscrollbar is vscrollbar:
    xsize 72
    base_bar Frame(Composite((72, 12), (33, 0), Solid("#a6cee0", xysize=(6, 12))), 0, 0)
    thumb Frame(Composite((72, 12), (24, 0), Solid("#47b6dc", xysize=(24, 12))), 0, 0)
    hover_thumb Frame(Composite((72, 12), (24, 0), Solid("#2086b5", xysize=(24, 12))), 0, 0)
    top_gutter 0
    bottom_gutter 0
    thumb_offset 0
    unscrollable "hide"

style system_slider is bar:
    xsize 760
    ysize 108
    left_bar Solid("#2086b5", ysize=6)
    right_bar Solid("#b0d8e6", ysize=6)
    thumb Composite((28, 108), (0, 32), Solid("#176f96", xysize=(28, 44)), (2, 34), Solid("#47b6dc", xysize=(24, 40)))
    hover_thumb Composite((28, 108), (0, 32), Solid("#153d5a", xysize=(28, 44)), (2, 34), Solid("#176f96", xysize=(24, 40)))
    thumb_shadow None
    thumb_offset 0
    thumb_align .5
    left_gutter 0
    right_gutter 0
    bar_resizing True

style system_page_name_button is system_button:
    xsize 1100
    background None
    hover_background madoromi_system_panel("#e3f7ff")
    selected_background None

style system_page_name_text is system_text:
    size 28
    yalign .5
    color "#153d5a"
    hover_color "#176f96"

style system_page_button is system_button:
    xysize (108, 108)
    padding (8, 12)

style system_page_button_text is system_button_text

style system_page_arrow_button is system_button:
    xsize 164
    padding (16, 12)

style system_page_arrow_button_text is system_button_text:
    size 27

style system_slot_button is system_button:
    xysize (848, 190)
    padding (0, 0)
    background madoromi_system_panel("#f6fcff")
    hover_background madoromi_system_panel("#ddf5ff", "#2086b5")
    selected_background madoromi_system_panel("#ddf5ff", "#2086b5")
    insensitive_background madoromi_system_panel("#e1edf3")

style system_slot_number is system_text:
    size 25
    color "#176f96"

style system_slot_date is system_text:
    size 24
    color "#385f78"

style system_slot_excerpt is system_text:
    size 24
    line_spacing 3
    xsize 354

style system_slot_empty is system_text:
    size 40
    color "#ffffff"

style system_delete_button is system_button:
    xysize (148, 108)
    padding (16, 12)
    background madoromi_system_panel("#f6fcff")
    hover_background madoromi_system_panel("#8a4253", "#8a4253")

style system_delete_button_text is system_button_text:
    size 26
    color "#854052"

style system_history_row is empty:
    xfill True
    padding (24, 26)

style system_history_speaker is system_text:
    xsize 200
    min_width 200
    size 28

style system_history_text is system_text:
    xsize 1060
    min_width 1060
    line_spacing 9
    color "#ffffff"
    outlines [(1, "#082d4260", 0, 1)]

style system_history_jump_button is system_button:
    xsize 176
    background madoromi_system_panel("#176f96", "#79cde5")

style system_history_jump_button_text is system_button_text:
    size 26
    color "#ffffff"
