#!/usr/bin/env python3
import time
import datetime


class TimeController:
    def __init__(self):
        self.running = False
        self.beginning = datetime.timedelta(seconds=0)
        self.delta_since_last_pause = datetime.timedelta(seconds=0)

    def start(self) -> None:
        self.running = True
        self.beginning = datetime.datetime.utcnow()

    def status(self) -> datetime.timedelta:
        if self.running:
            return (
                datetime.datetime.utcnow() - self.beginning
            ) + self.delta_since_last_pause
        else:
            return self.delta_since_last_pause

    def pause(self) -> None:
        now = datetime.datetime.utcnow()
        self.running = False
        self.delta_since_last_pause += now - self.beginning

    def unpause(self) -> None:
        self.start()

    def pause_or_unpause(self) -> None:
        if self.running:
            self.pause()
        else:
            self.unpause()

    def reset(self) -> None:
        self.running = False
        self.delta_since_last_pause = datetime.timedelta(seconds=0)
