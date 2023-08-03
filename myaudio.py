import simpleaudio as sa

class MyAudio:
    def __init__(self, should_play=True):
        self.is_playing = False
        self.should_play = True
        self.wave_obj = None
        self.play_obj = None

    def start(self, filename: str) -> None:
        if not self.should_play:
            return
        self.wave_obj = sa.WaveObject.from_wave_file(filename)
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

    def is_playing(self) -> None:
        return self.is_playing

