#!/usr/bin/env python3
import serial
import time
from multiprocessing import Process, Value
# https://stackoverflow.com/questions/38803153/python-have-a-process-run-in-the-background-and-get-status-from-the-main-thread

ALARM_NOT_TRIGGERED = "alarm,0"
ALARM_TRIGGERED = "alarm,1"
PLAYER_WON = "tom"


def _parse_serial(shared_data):
    print("Initializing Serial")
    while True:
        try:
            the_serial = serial.Serial('COM4')
            while True:
                line = the_serial.readline().decode('ascii').strip()
                if line == ALARM_NOT_TRIGGERED:
                    continue
                elif line == ALARM_TRIGGERED:
                    shared_data.value |= 1
                elif PLAYER_WON in line.lower():
                    shared_data.value |= 2
                else:
                    print(f"Unknown line: [{line}]")

        except Exception as e:
            print("Serial Error. Sleeping one second and reconnecting...")
            print(e)
            time.sleep(1)


class MySerial:

    def __init__(self):
        self.shared_data = Value('i', 0)

    def set_alarm_triggered(self):
        self.shared_data.value |= 1

    def set_player_won(self):
        self.shared_data.value |= 2

    def get_alarm_triggered(self):
        return (self.shared_data.value & 1) > 0

    def get_player_won(self):
        return (self.shared_data.value & 2) > 0

    def reset(self):
        self.shared_data.value = 0

    def start_in_background(self):
        p = Process(target=_parse_serial, args=(self.shared_data,))
        p.start()


if __name__ == '__main__':

    x = MySerial()
    x.start_in_background()

    counter = 0
    while True:
        time.sleep(.5)
        print(x.shared_data.value)
        counter += 1
        if counter % 10 == 0:
            print("reset")
            x.reset()
