#!/usr/bin/env python3
import datetime


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


class TimeController:
    def __init__(self, seconds=0):
        self.running = False
        self.beginning = datetime.timedelta(seconds=0)
        self.delta_since_last_pause = datetime.timedelta(seconds=0)
        self.one_minute = datetime.timedelta(seconds=60)
        self.time_zero = datetime.timedelta(seconds=0)
        self.time_maxseconds = datetime.timedelta(seconds=seconds)

    def start(self) -> None:
        self.running = True
        self.beginning = datetime.datetime.utcnow()

    def is_timer_over(self) -> bool:
        return self.running and ( self.status() <= self.time_zero )

    def status(self) -> datetime.timedelta:
        if self.running:
            elapsed = (datetime.datetime.utcnow() - self.beginning) + self.delta_since_last_pause
            if self.time_maxseconds != self.time_zero:
                result = self.time_maxseconds - elapsed
                if result < self.time_zero:
                    return self.time_zero
                return result
            return elapsed
        else:
            if self.time_maxseconds != self.time_zero:
                return self.time_maxseconds - self.delta_since_last_pause
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
