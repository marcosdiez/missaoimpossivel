#!/usr/bin/env python3
import datetime

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

class TimeController:
    def __init__(self):
        self.running = False
        self.beginning = datetime.timedelta(seconds=0)
        self.delta_since_last_pause = datetime.timedelta(seconds=0)
        self.one_minute = datetime.timedelta(seconds=60)

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

    def is_running(self) -> bool:
        return self.running

    def status_pretty(self) -> str:
        status = self.status()
        hours, seconds_in_minutes = divmod(status.seconds, 3600)
        minutes, seconds = divmod(seconds_in_minutes, 60)
        if hours == 0:
            return f"{minutes:02d}:{seconds:02d}"
        else:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
