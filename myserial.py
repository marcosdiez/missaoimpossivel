#!/usr/bin/env python3
import serial
import time
import threading
# from multiprocessing import Process, Value
# https://stackoverflow.com/questions/38803153/python-have-a-process-run-in-the-background-and-get-status-from-the-main-thread

# https://medium.com/@chanon.krittapholchai/pysimplegui-in-production-with-threading-e24a648d9e99

ALARM_NOT_TRIGGERED = "alarm,0"
ALARM_TRIGGERED = "alarm,1"
PLAYER_WON = "tom"


def _parse_serial(shared_data):
    while True:
        try:
            print("Initializing Serial")
            the_serial = serial.Serial('COM4')
            while True:
                line = the_serial.readline().decode('ascii').strip()
                if line == ALARM_NOT_TRIGGERED:
                    continue
                elif line == ALARM_TRIGGERED:
                    old_value = shared_data.value
                    shared_data.value |= 1
                    if shared_data.value != old_value:
                        print("Serial: ALARM_TRIGGERED")
                elif PLAYER_WON in line.lower():
                    old_value = shared_data.value
                    shared_data.value |= 2
                    if shared_data.value != old_value:
                        print("Serial: PLAYER_WON")
                else:
                    print(f"Unknown line: [{line}]")

        except Exception as e:
            print("Serial Error. Sleeping one second and reconnecting...")
            print(e)
            time.sleep(1)

class SharedData:
    def __init__(self):
        self.value = 0

class MySerial:

    def __init__(self):
        # self.shared_data = Value('i', 0)
        self.shared_data = SharedData()
        self.job_threading = None
        self.running = False

    def set_alarm_triggered(self):
        self.shared_data.value |= 1

    def set_player_won(self):
        self.shared_data.value |= 2

    def get_alarm_triggered(self):
        return (self.shared_data.value & 1) > 0

    def get_player_won(self):
        return (self.shared_data.value & 2) > 0

    def reset(self):
        print("Serial: reset")
        self.shared_data.value = 0

    def stop(self):
        self.running = False
        print("Serial: stop")

    def start_in_background(self):
        self.running = True
        self.job_threading = threading.Thread(target=self.job_processing)
        self.job_threading.start()


        # p = Process(target=_parse_serial, args=(self.shared_data,))
        # p.start()
        # return self
    def job_processing(self):
        while self.running:
            try:
                print("Initializing Serial")
                the_serial = serial.Serial('COM4')
                while self.running:
                    line = the_serial.readline().decode('ascii').strip()
                    if line == ALARM_NOT_TRIGGERED:
                        continue
                    elif line == ALARM_TRIGGERED:
                        old_value = self.shared_data.value
                        self.shared_data.value |= 1
                        if self.shared_data.value != old_value:
                            print("Serial: ALARM_TRIGGERED")
                    elif PLAYER_WON in line.lower():
                        old_value = self.shared_data.value
                        self.shared_data.value |= 2
                        if self.shared_data.value != old_value:
                            print("Serial: PLAYER_WON")
                    else:
                        print(f"Unknown line: [{line}]")

            except Exception as e:
                print("Serial Error. Sleeping one second and reconnecting...")
                print(e)
                time.sleep(1)

if __name__ == '__main__':

    x = MySerial()
    x.start_in_background()

    counter = 0
    while True:
        time.sleep(.5)
        print(x.shared_data.value)
        counter += 1
        if counter % 10 == 0:
            x.reset()
