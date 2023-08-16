import vlc
import os
import os.path
import random

class MyAudio:
    def __init__(self, should_play=True):
        self.filename = None
        self.should_play = True
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
        self.stop()
        self.filename = self._get_filename(filename_or_foldername)
        self.play_obj = vlc.MediaPlayer(self.filename)
        self.play_obj.play()

    def pause(self) -> None:
        if not self.should_play:
            return
        if self.is_playing():
            self.play_obj.pause()

    def unpause(self) -> None:
        if not self.should_play:
            return
        if not self.is_playing():
            self.play_obj.play()

    def pause_or_unpause(self) -> None:
        if self.is_playing():
            self.pause()
        else:
            self.unpause()

    def stop(self) -> None:
        if not self.is_playing():
            return
        if not self.should_play:
            return
        if self.play_obj:
            self.play_obj.stop()

    def reset(self) -> None:
        if not self.should_play:
            return
        self.play_obj.stop()

    def is_playing(self) -> bool:
        if self.play_obj is None:
            return False
        return self.play_obj.is_playing()
