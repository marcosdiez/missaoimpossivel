#!/usr/bin/env python3
import time

from helper import dumper
import myaudio
import myserial
import TimeController

import PySimpleGUI as sg

# settings
GUI_REFRESH_LOOP = 0.1
FONT_SIZE = 400
TIME_IN_SECONDS = 180


MUSIC_AMBIENT = "assets/ambient"
MUSIC_VICTORY = "assets/victory"
MUSIC_ALARM = "assets/alarm"

SHOULD_PLAY_MUSIC = True
# SHOULD_PLAY_MUSIC = False

# settings we should not want to change
BUTTON_RESTART = "(Re)Start"
BUTTON_PAUSE_UNPAUSE = "Pause/Unpause"
BUTTON_RESET = "Reset"
BUTTON_EXIT = "Exit"

# FONT_NAME = "Courier New"
FONT_NAME = "IntelOne Mono"


def logger(msg):
    print(msg)
    window["Status"].update(msg)


sg.theme("GrayGrayGray")

layout = [
    [sg.Text(key="-EXPAND1-", font="ANY 1", pad=(0, 0))],
    [
        sg.Text(
            "00:00",
            key="-TimeBox-",
            auto_size_text=True,
            justification="center",
            font=(FONT_NAME, FONT_SIZE),
            expand_x=True,
            expand_y=False,
            # background_color="#00aaaa",
        )
    ],
    [sg.Text(key="-EXPAND2-", font="ANY 1", pad=(0, 0))],
    [
        sg.Button(BUTTON_RESTART),
        sg.Button(BUTTON_PAUSE_UNPAUSE),
        sg.Button(BUTTON_RESET),
        sg.Button(BUTTON_EXIT),
    ],
    [sg.Text("", key="StatusBar"), sg.Sizegrip()],
]

# Create the Window
window = sg.Window(
    "Mission Impossible: The Laser Challange",
    layout,
    auto_size_text=True,
    auto_size_buttons=True,
    resizable=True,
    element_justification="center",
    finalize=True,
)
window.maximize()
window["-EXPAND1-"].expand(True, True, True)
window["-EXPAND2-"].expand(True, True, True)
window[BUTTON_RESTART].set_focus()

should_be_playing_boom = False

timecontroller = TimeController.TimeController(TIME_IN_SECONDS)
musicplayer = myaudio.MyAudio(SHOULD_PLAY_MUSIC)
serialcontroller = myserial.MySerial()

serialcontroller_started = False

while True:
    if timecontroller.is_running():
        event, values = window.read(timeout=10)
        window["-TimeBox-"].update(timecontroller.status_pretty())

        if serialcontroller.get_player_won():
            should_be_playing_boom = False
            print("victory")
            musicplayer.start(MUSIC_VICTORY)
            timecontroller.reset()
            window[BUTTON_RESTART].set_focus()

        elif serialcontroller.get_alarm_triggered() or timecontroller.is_timer_over():
            if not should_be_playing_boom:
                should_be_playing_boom = True
                print("boom")
                musicplayer.start(MUSIC_ALARM)
                timecontroller.reset()
                window[BUTTON_RESTART].set_focus()

    else:
        event, values = window.read()

    # event, values = window.read()
    # print(event)
    # dumper(values)
    if event in (None, sg.WIN_CLOSED, BUTTON_EXIT):
        print(f"{timecontroller.status()} EVENT={event} ")
        serialcontroller.stop()
        musicplayer.stop()
        # if user closes window or clicks cancel
        break
    elif event == BUTTON_RESTART:
        print(f"{timecontroller.status()} EVENT={event} ")
        window[BUTTON_PAUSE_UNPAUSE].set_focus()
        musicplayer.stop()
        timecontroller.reset()
        serialcontroller.reset()
        timecontroller.start()
        musicplayer.start(MUSIC_AMBIENT)
        should_be_playing_boom = False

    elif event == BUTTON_PAUSE_UNPAUSE:
        print(f"{timecontroller.status()} EVENT={event} ")
        timecontroller.pause_or_unpause()
        musicplayer.pause_or_unpause()
        serialcontroller.reset()
    elif event == BUTTON_RESET:
        print(f"{timecontroller.status()} EVENT={event} ")
        timecontroller.reset()
        musicplayer.reset()
        serialcontroller.reset()
        should_be_playing_boom = False
        window["-TimeBox-"].update(timecontroller.status_pretty())
        window[BUTTON_RESTART].set_focus()
    else:
        time.sleep(GUI_REFRESH_LOOP)

    if not serialcontroller_started:
        serialcontroller_started = True
        serialcontroller.start_in_background()

    # logger(f"You entered {values[0]}")

window.close()
