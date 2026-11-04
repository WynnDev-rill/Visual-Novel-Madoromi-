# Native Ren'Py functional tests. Excluded from release distributions.
# Run with an isolated --savedir; see tests/README.md.
init python:
    import itertools as _qa_itertools
    import json as _qa_json
    import os as _qa_os
    import traceback as _qa_traceback

    def _qa_trace_autosave(function):
        def traced(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception:
                with open(_qa_os.environ["MADOROMI_TEST_AUTOSAVE_DEBUG"], "a") as stream:
                    _qa_traceback.print_exc(file=stream)
                raise
        return traced

    if _qa_os.environ.get("MADOROMI_TEST_AUTOSAVE_DEBUG"):
        renpy.loadsave.save = _qa_trace_autosave(renpy.loadsave.save)
        renpy.exports.take_screenshot = _qa_trace_autosave(renpy.exports.take_screenshot)

    _qa_choices = [
        ["Dengarkan apa yang membuatnya penasaran.", "Ajukan pertanyaan yang sungguh ingin kutahu."],
        ["Duduk tenang sampai ia menemukan kalimatnya.", "Tawarkan diri sebagai pembaca pertamanya."],
        ["Biru, seperti air ketika angin sudah reda.", "Kuning, seperti lampu toko menjelang tutup."],
        ["Dengan kalimat sederhana yang bisa kuucapkan utuh.", "Katakan bahwa aku gugup, lalu tetap lanjutkan."],
        ["Jaga ucapan selamat malam kami.", "Simpan sebagian cerita untuk pagi."],
    ]
    _qa_values = [("listen", "questions"), ("quiet", "help"), ("blue", "gold"), ("plain", "slow"), ("goodnight", "morning")]
    _qa_callbacks = [
        ["bertanya bagian mana yang paling kusuka", "kamu ikut bertanya hal aneh"],
        ["Kamu duduk dan mengerjakan bukumu sendiri", "Kamu tidak pura-pura semua kalimatku bagus"],
        ["Atap stasiunnya biru. Seperti pilihanmu", "Stasiunnya masih menyala"],
        ["Kalimat itu keluar utuh", "Ujung kalimatnya lebih pelan daripada awalnya"],
        ["Besok mungkin ia mengirim foto yang belum kukenal", "Hanya tiga kata: Sora, kabel, judul"],
    ]

    def _qa_history_contains(fragment):
        return any(fragment in item.what for item in _history_list)

    def _qa_write_route(route):
        path = _qa_os.environ.get("MADOROMI_TEST_COVERAGE", _qa_os.path.join(config.basedir, "tests", "artifacts", "native-paths.json"))
        _qa_os.makedirs(_qa_os.path.dirname(path), exist_ok=True)
        try:
            with open(path) as stream:
                result = _qa_json.load(stream)
        except (OSError, ValueError):
            result = {"engine": renpy.version_string, "completed_routes": []}
        key = "".join(str(bit) for bit in route)
        if not any(item["route"] == key for item in result["completed_routes"]):
            result["completed_routes"].append({"route": key, "choices": [_qa_choices[i][bit] for i, bit in enumerate(route)], "callbacks_verified": 5, "chapter_unlocked": persistent.chapter_unlocked, "completed": persistent.completed})
        with open(path, "w") as stream:
            _qa_json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write("\n")

testsuite madoromi:
    setup:
        $ _test.timeout = 420.0
        # Unlocked test rendering can starve native background screenshots
        # under software GL. Use the player's normal frame pacing.
        $ _test.maximum_framerate = False
        # Ren'Py also includes game/saves on desktop despite --savedir. Keep
        # native test slots in the explicitly selected isolated directory.
        $ renpy.loadsave.location.locations = [location for location in renpy.loadsave.location.locations if location.directory == config.savedir]
        $ renpy.loadsave.location.scan()
        $ renpy.loadsave.clear_cache()
        $ _test.screenshot_directory = _qa_os.environ.get("MADOROMI_TEST_SCREENSHOTS", "tests/screenshots")
        if eval _qa_os.environ.get("MADOROMI_TEST_SIZE"):
            $ renpy.set_physical_size(tuple(int(part) for part in _qa_os.environ["MADOROMI_TEST_SIZE"].split("x")))
        $ _preferences.text_cps = 0
        $ _preferences.transitions = 0
        $ _preferences.skip_unseen = True
        $ _preferences.skip_after_choices = False
        $ persistent.text_size = 36
        $ persistent.reduce_motion = True
        if eval (_qa_os.environ.get("MADOROMI_TEST_MOTION_PREVIEW") == "1"):
            $ _preferences.transitions = 2
            $ persistent.reduce_motion = False

    before testcase:
        $ renpy.stop_skipping()
        $ _preferences.afm_enable = False
        if not screen "main_menu":
            run MainMenu(confirm=False)
        pause until screen "main_menu"

    teardown:
        exit

    testcase title_and_preferences:
        description "Title renders; accessible text, motion, skipping and mixer settings respond."
        pause .4
        screenshot "01-title.png"
        click "Pengaturan"
        assert screen "preferences"
        pause .4
        screenshot "02-preferences.png"
        click "Besar"
        assert eval (persistent.text_size == 42)
        click "Standar"
        assert eval (persistent.text_size == 36)
        $ persistent.reduce_motion = False
        click "Kurangi gerakan"
        assert eval persistent.reduce_motion
        $ _preferences.skip_unseen = False
        click "skip unseen text"
        assert eval _preferences.skip_unseen
        click "Suara"
        pause .4
        screenshot "02b-sound.png"
        run Preference("music volume", 0.35)
        run Preference("sound volume", 0.60)
        run Preference("mixer ambience volume", 0.25)
        assert eval (abs(_preferences.get_volume("music") - 0.35) < 0.01)
        assert eval (abs(_preferences.get_volume("sfx") - 0.60) < 0.01)
        assert eval (abs(_preferences.get_volume("ambience") - 0.25) < 0.01)
        click "mute all"
        assert eval all(_preferences.get_mute(mixer) for mixer in _preferences.get_all_mixers())
        click "mute all"
        assert eval not any(_preferences.get_mute(mixer) for mixer in _preferences.get_all_mixers())
        click "Kontrol"
        pause .4
        screenshot "02c-controls.png"
        keysym "game_menu"
        assert screen "main_menu"

    testcase phone_backlog:
        description "Progressive phone messages preserve speaker and text in native history."
        click "Cerita baru"
        assert screen "chapter_title"
        pause .4
        screenshot "03-chapter-one.png"
        advance until screen "phone_messages"
        pause .4
        screenshot "04-phone.png"
        assert eval (_phone_index == 1)
        keysym "dismiss" until eval (_phone_index == 4)
        assert eval _qa_history_contains("Mungkin dia optimis.")
        assert eval any(item.who == "Ren · pesan" and item.what == "Mungkin dia optimis." for item in _history_list)
        run ShowMenu("history")
        assert screen "history"
        pause .4
        screenshot "05-phone-history.png"
        keysym "game_menu"
        assert screen "phone_messages" timeout 10.0
        assert eval (_phone_index == 4) timeout 5.0
        run ShowMenu("save")
        run FileSave("2", page="9", confirm=False)
        keysym "game_menu"
        pause until not screen "save"
        keysym "dismiss"
        assert eval (_phone_index == 5) timeout 5.0
        run FileLoad("2", page="9", confirm=False)
        assert screen "phone_messages" timeout 10.0
        assert eval (_phone_index == 4) timeout 5.0
        keysym "dismiss"
        assert eval (_phone_index == 5) timeout 5.0
        assert eval (sum(item.what == "Tadi dia kembali membawa teman." for item in _history_list) == 1)
        run FileDelete("2", page="9", confirm=False)

    testcase choice_autosave:
        description "Optional fresh native choice-autosave diagnostic; software-GL screenshot deadlines can be inconclusive."
        enabled (__import__("os").environ.get("MADOROMI_TEST_REQUIRE_AUTOSAVE") == "1")
        $ renpy.unlink_save("auto-1")
        run Start()
        skip until screen "choice"
        pause 2.0
        assert eval not renpy.is_skipping()
        assert eval renpy.can_load("auto-1") timeout 15.0
        assert eval (renpy.get_save_data("auto-1")["story_reply"] == "listen")

    testcase save_load_and_rollback:
        description "Manual save/load and rollback restore a selected branch and its earlier decision point."
        run Start()
        skip fast until screen "choice"
        assert eval not renpy.is_skipping()
        click expression _qa_choices[0][1]
        pause until not screen "choice" timeout 10.0
        skip fast until screen "choice"
        assert eval (story_reply == "questions")
        assert eval (story_company == "quiet")
        run ShowMenu("save")
        assert screen "save"
        run FilePage("9")
        run FileSave("1", confirm=False)
        assert eval renpy.can_load("9-1")
        assert eval (renpy.get_save_data("9-1")["story_reply"] == "questions")
        pause .4
        screenshot "06-save.png"
        keysym "game_menu"
        pause until not screen "save"
        click expression _qa_choices[1][1]
        pause until not screen "choice" timeout 10.0
        assert eval (story_company == "help") timeout 5.0
        keysym "rollback" until screen "choice" timeout 15.0
        assert expression _qa_choices[1][0]
        assert eval (story_reply == "questions" and story_company == "quiet")
        pause .4
        screenshot "16-rollback-choice.png"
        click expression _qa_choices[1][1]
        pause until not screen "choice" timeout 10.0
        skip fast until screen "choice"
        assert eval (story_company == "help")
        run FileLoad("1", page="9", confirm=False)
        assert screen "choice" timeout 10.0
        assert expression _qa_choices[1][0]
        assert eval (story_reply == "questions" and story_company == "quiet")
        pause .4
        screenshot "07-restored-choice.png"
        run FileDelete("1", page="9", confirm=False)
        assert eval not renpy.can_load("9-1")

    testcase automatic_reading:
        description "Auto advances narration into phone presentation; fast skip stops at a choice."
        run Start()
        keysym "dismiss"
        advance until "Ponselku bergetar"
        $ _preferences.afm_time = 0.1
        click "Auto forward"
        assert eval _preferences.afm_enable timeout 5.0
        pause until screen "phone_messages" timeout 30.0
        pause .4
        screenshot "08-auto-phone.png"
        run Preference("auto-forward", "disable")
        assert eval not _preferences.afm_enable
        skip fast until screen "choice"
        assert eval not renpy.is_skipping()
        pause .4
        screenshot "09-first-choice.png"

    testcase menu_destinations:
        description "Native help, credits, load, chapter and engine information screens open and return."
        parameter destination = ["help", "credits", "load", "chapters", "about"]
        run ShowMenu(destination)
        assert screen destination
        if eval destination == "help":
            click "Layar sentuh"
            assert eval (renpy.get_screen("help").scope["device"] == "touch")
        pause .4
        screenshot ("menu-" + destination + ".png")
        keysym "game_menu"
        pause until screen "main_menu"

    testcase confirmation_and_acting:
        description "Localized confirmation cancels safely; support gestures and the casual epilogue render in real story scenes."
        run Start()
        skip fast until screen "choice"
        run MainMenu()
        assert screen "confirm"
        pause .4
        screenshot "17-confirmation.png"
        click "Tidak"
        assert not screen "confirm"
        assert screen "choice"
        run MainMenu(confirm=False)
        run Start("act_2")
        advance until "Aku melihat ke kanan dengan patuh." timeout 90.0
        assert eval renpy.showing("sora easy")
        pause .4
        screenshot "18-sora-gesture.png"
        advance until "Untuk daftar penjaga panel" timeout 180.0
        assert eval renpy.showing("mio thoughtful")
        pause .4
        screenshot "19-mio-gesture.png"
        run MainMenu(confirm=False)
        run Start("epilogue")
        advance until "Pas. Tapi kalau aku terus" timeout 30.0
        assert eval (aoi_outfit == "blouse")
        pause .4
        screenshot "20-casual-epilogue.png"

    testcase complete_routes:
        description "Contrasting complete routes cover all decisions and later callbacks; optional full matrix covers all32 combinations."
        parameter route = (list(__import__("itertools").product((0, 1), repeat=5)) if __import__("os").environ.get("MADOROMI_TEST_FULL_MATRIX") == "1" else [(0,0,0,0,0), (1,1,1,1,1)])
        $ persistent.completed = False
        $ persistent.chapter_unlocked = 1
        run Start()
        if eval (route == (0, 0, 0, 0, 0) and _qa_os.environ.get("MADOROMI_TEST_SCENE_SAVES") == "1"):
            advance until "Di grup band, Sora mengirim pesan" timeout 120.0
            run FileSave("1", page="7", confirm=False)
        skip fast until screen "choice" timeout 120.0
        click expression _qa_choices[0][route[0]]
        # Click queues input; let the old interaction close before waiting for
        # another choice, or Until can succeed against that old screen.
        pause until not screen "choice" timeout 10.0
        skip fast until screen "choice" timeout 120.0
        assert eval (story_reply == _qa_values[0][route[0]])
        if eval (route == (0, 0, 0, 0, 0)):
            pause .4
            screenshot "14-cafeteria.png"
            if eval (_qa_os.environ.get("MADOROMI_TEST_SCENE_SAVES") == "1"):
                run FileSave("1", page="8", confirm=False)
        click expression _qa_choices[1][route[1]]
        pause until not screen "choice" timeout 10.0
        skip fast until screen "choice" timeout 120.0
        assert eval (story_company == _qa_values[1][route[1]])
        if eval (route == (0, 0, 0, 0, 0)):
            pause .4
            screenshot "15-beanbag-lounge.png"
            if eval (_qa_os.environ.get("MADOROMI_TEST_SCENE_SAVES") == "1"):
                run FileSave("2", page="8", confirm=False)
        click expression _qa_choices[2][route[2]]
        pause until not screen "choice" timeout 10.0
        skip fast until screen "choice" timeout 120.0
        assert eval (story_color == _qa_values[2][route[2]])
        assert eval (persistent.chapter_unlocked == 2)
        assert eval _qa_history_contains("atap stasiun berwarna biru" if route[2] == 0 else "stasiun kecil berwarna kuning")
        click expression _qa_choices[3][route[3]]
        pause until not screen "choice" timeout 10.0
        if eval (route == (0, 0, 0, 0, 0)):
            advance until "Aku juga suka kamu. Sangat." timeout 180.0
            assert eval renpy.showing("aoi tender_heart")
            pause .4
            screenshot "21-aoi-confession-gesture.png"
            advance until "Boleh aku memelukmu?" timeout 180.0
            pause .4
            screenshot "10-courtyard.png"
            if eval (_qa_os.environ.get("MADOROMI_TEST_SCENE_SAVES") == "1"):
                run FileSave("3", page="8", confirm=False)
            advance until screen "keepsake_jeans" timeout 90.0
            pause .4
            screenshot "11-keepsake.png"
        skip fast until screen "choice" timeout 120.0
        assert eval (story_courage == _qa_values[3][route[3]])
        assert eval (persistent.chapter_unlocked == 3)
        assert eval all(_qa_history_contains(_qa_callbacks[i][route[i]]) for i in range(4))
        assert eval (_qa_history_contains("Aku juga suka kamu. Sangat.") and _qa_history_contains("Boleh aku memelukmu?"))
        click expression _qa_choices[4][route[4]]
        pause until not screen "choice" timeout 10.0
        skip fast until eval persistent.completed timeout 120.0
        assert eval (story_promise == _qa_values[4][route[4]])
        assert eval _qa_history_contains(_qa_callbacks[4][route[4]])
        assert eval (persistent.chapter_unlocked == 3 and persistent.completed)
        $ _qa_write_route(route)
        if eval (route == (0, 0, 0, 0, 0)):
            pause until screen "chapter_title" timeout 10.0
            pause .6
            pause .4
            screenshot "12-ending.png"
            if eval (_qa_os.environ.get("MADOROMI_TEST_SCENE_SAVES") == "1"):
                run FileSave("4", page="8", confirm=False)
        advance until screen "main_menu" timeout 30.0
        run ShowMenu("chapters")
        assert screen "chapters"
        if eval (route == (0, 0, 0, 0, 0)):
            pause .4
            screenshot "13-completed-chapters.png"
        keysym "game_menu"
