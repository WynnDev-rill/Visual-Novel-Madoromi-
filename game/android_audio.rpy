# Select SDL's Java AudioTrack backend before the audio device opens.
# OpenSLES stalled input on the API21 software device while waiting on its
# buffer mutex. AudioTrack kept music, ambience and SFX responsive in that test.
init -999 python:
    if renpy.android:
        import os as _madoromi_android_os
        _madoromi_android_os.environ.setdefault("SDL_AUDIODRIVER", "android")
