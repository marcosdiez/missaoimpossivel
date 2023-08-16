import simpleaudio as sa
import os
import os.path
import random

class MyAudio:
    def __init__(self, should_play=True):
        self.filename = None
        self.is_playing = False
        self.should_play = True
        self.wave_obj = None
        self.play_obj = None

    def _get_filename(self, filename_or_foldername: str) -> str:
        if os.path.isfile(filename_or_foldername):
            return filename_or_foldername
        if os.path.isdir(filename_or_foldername):
            all_files = os.listdir(filename_or_foldername)
            choosen_file = random.choice(all_files)
            print(choosen_file)
            return os.path.join(filename_or_foldername, choosen_file)

    def start(self, filename_or_foldername: str) -> None:
        if not self.should_play:
            return
        self.filename = self._get_filename(filename_or_foldername)
        self.wave_obj = sa.WaveObject.from_wave_file(self.filename)
        self.play_obj = self.wave_obj.play()
        self.is_playing = True

    def pause(self) -> None:
        if not self.should_play:
            return
        if self.is_playing:
            self.play_obj.pause()
            self.is_playing = False

    def unpause(self) -> None:
        if not self.should_play:
            return
        if not self.is_playing:
            self.play_obj.resume()
            self.is_playing = True

    def pause_or_unpause(self) -> None:
        if self.is_playing:
            self.pause()
        else:
            self.unpause()

    def stop(self) -> None:
        if not self.is_playing:
            return
        if not self.should_play:
            return

        self.is_playing = False
        self.play_obj.stop()

    def reset(self) -> None:
        if not self.should_play:
            return
        self.play_obj.stop()

    def is_playing(self) -> bool:
        return self.is_playing

