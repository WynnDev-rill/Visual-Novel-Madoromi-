define config.name = _("MADOROMI")
define config.version = "1.0.0"
define build.name = "Madoromi"
define config.save_directory = "WynnDev-Madoromi-1"
define config.window_icon = "gui/window_icon.png"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.has_sync = False
define config.main_menu_music = "audio/bgm/tender.ogg"
define config.sample_sound = "audio/sfx/message.ogg"
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.enter_transition = Dissolve(.25)
define config.exit_transition = Dissolve(.25)
define config.intra_transition = Dissolve(.15)
define config.after_load_transition = Dissolve(.25)
define config.end_game_transition = Fade(.4, .2, .6)
define config.history_length = 400
define config.autosave_on_choice = True
define config.autosave_on_quit = True
define config.default_fullscreen = False
default preferences.text_cps = 35
default preferences.afm_time = 12
define gui.show_name = False
define gui.about = _p("""
MADOROMI — Sepuluh Detik

Adaptasi romance dari cerita pendek pengguna. Produksi: WynnDev.
Naskah, penyutradaraan, dan integrasi dikembangkan dengan bantuan AI.

Desain tokoh: pengguna. Pengembangan ilustrasi: bantuan AI.
Musik: Kevin MacLeod (incompetech.com), CC BY 4.0.
Efek antarmuka: Kenney, CC0. Font: Noto, SIL Open Font License.
Kredit lengkap dan ketentuan aset tersedia dalam menu Kredit.

Dibuat dengan Ren'Py. Komponen engine menggunakan MIT/LGPL dan lisensi terkait.
""")

init python:
    build.archive("visuals", "all")
    if __import__("os").environ.get("MADOROMI_NATIVE_ANDROID") == "1":
        build.classify("game/images/**", "all")
        build.classify("game/visuals.rpa", None)
    elif __import__("os").environ.get("MADOROMI_PREARCHIVED") == "1":
        build.classify("game/images/**", None)
        build.classify("game/visuals.rpa", "all")
    else:
        build.classify("game/images/**", "visuals")
        build.classify("game/visuals.rpa", None)
    build.classify("**.keystore", None)
    build.classify("**.jks", None)
    build.classify("**.pyc", None)
    build.classify("**~", None)
    build.classify(".git/**", None)
    build.classify(".github/**", None)
    build.classify("dist/**", None)
    build.classify("build/**", None)
    build.classify(".impeccable/**", None)
    build.classify("AGENTS.md", None)
    build.classify("PRODUCT.md", None)
    build.classify("**.bak", None)
    build.classify(".agents/**", None)
    build.classify("tests/**", None)
    build.classify("tools/**", None)
    build.classify("docs/**", None)
    build.classify("android.json", None)
    build.classify("android-icon**", None)
    build.classify("game/test**.rpy", None)
    build.classify("game/test**.rpyc", None)
    build.documentation("README.md")
    build.documentation("THIRD_PARTY_NOTICES.md")
