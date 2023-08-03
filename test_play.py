#!/usr/bin/env python3

import simpleaudio as sa
import sys

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} WAVFILE")
    sys.exit(1)

wave_obj = sa.WaveObject.from_wave_file(sys.argv[1])
play_obj = wave_obj.play()
play_obj.wait_done()
