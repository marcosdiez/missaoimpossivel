#!/usr/bin/env python3

import simpleaudio as sa
import time

FILENAME="assets/mission_impossible.wav"

wave_obj = sa.WaveObject.from_wave_file(FILENAME)
play_obj = wave_obj.play()

time.sleep(3)
play_obj.pause()
print("paused")
time.sleep(3)
play_obj.resume()
print("resumed")
time.sleep(3)
play_obj.stop()
print("stoped")