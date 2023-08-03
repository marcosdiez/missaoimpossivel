#!/usr/bin/env python3

import os
import simpleaudio as sa

FILENAME=f"assets{os.sep}mission_impossible.wav"


wave_obj = sa.WaveObject.from_wave_file(FILENAME)
play_obj = wave_obj.play()
play_obj.wait_done()

# wave_obj = sa.WaveObject.from_wave_file("mission_impossible.wav")
# play_obj = wave_obj.play()

# time.sleep(3)
# play_obj.pause()
# print("paused")
# time.sleep(3)
# play_obj.resume()
# print("resumed")
# time.sleep(3)
# play_obj.stop()
# print("stoped")

play_obj.wait_done()



# import simpleaudio as sa
# import time

# class PlayObject:
#     def __init__(self, play_id):
#         self.play_id = play_id

#     def pause(self):
#         return _sa._pause(self.play_id)

#     def resume(self):
#         return _sa._resume(self.play_id)

#     def stop(self):
#         _sa._stop(self.play_id)

#     def wait_done(self):
#         while self.is_playing():
#             sleep(0.05)

#     def is_playing(self):
#         return _sa._is_playing(self.play_id)

# wave_obj = sa.WaveObject.from_wave_file("assets/mission_impossible.wav")
# play_obj = wave_obj.play()

# time.sleep(3)
# play_obj.pause()
# print("paused")
# time.sleep(3)
# play_obj.resume()
# print("resumed")
# time.sleep(3)
# play_obj.stop()
# print("stoped")

# import winsound
# import time

# winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
# time.sleep(1)
# winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
# time.sleep(1)
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
# time.sleep(1)
# winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
# time.sleep(1)
# winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
# time.sleep(1)
# winsound.PlaySound("*", winsound.SND_ALIAS)