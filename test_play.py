#!/usr/bin/env python3

import myaudio
import sys

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} WAVFILE_OR_FOLDER")
    sys.exit(1)

player = myaudio.MyAudio()
player.start(sys.argv[1])
input("Press Enter to Quit...")