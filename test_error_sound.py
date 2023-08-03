#!/usr/bin/env python3

import simpleaudio as sa
import random



FILENAMES = ["assets/Klaxon.wav", "assets/alarm_1.wav", "assets/siren_1.wav"]

FILENAME= random.choice(FILENAMES)
print(FILENAME)
wave_obj = sa.WaveObject.from_wave_file(FILENAME)
play_obj = wave_obj.play()
play_obj.wait_done()
