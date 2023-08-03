#!/usr/bin/env python3
import time

from helper import dumper
import myaudio
import TimeController
import time

import PySimpleGUI as sg


def logger(msg):
    print(msg)
    window["Status"].update(msg)


FONT_SIZE = 400
BUTTON_RESTART = "(Re)Start"
BUTTON_PAUSE_UNPAUSE = "Pause/Unpause"
BUTTON_RESET = "Reset"
BUTTON_EXIT = "Exit"

sg.theme("GrayGrayGray")

layout = [
    [sg.Text(key="-EXPAND1-", font="ANY 1", pad=(0, 0))],
    [
        sg.Text(
            "00:00",
            key="-TimeBox-",
            auto_size_text=True,
            justification="center",
            font=("Courier New", FONT_SIZE),
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
    [sg.Text("", key="StatusBar"), sg.Sizegrip()]
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


tc = TimeController.TimeController()
while True:
    if tc.is_running():
        event, values = window.read(timeout=10)
        window["-TimeBox-"].update(tc.status_pretty())
    else:
        event, values = window.read()

    # event, values = window.read()
    print(event)
    dumper(values)
    if event in (None, sg.WIN_CLOSED, BUTTON_EXIT):
        # if user closes window or clicks cancel
        break
    elif event == BUTTON_RESTART:
        window[BUTTON_PAUSE_UNPAUSE].set_focus()
        tc.start()

    elif event == BUTTON_PAUSE_UNPAUSE:
        tc.pause_or_unpause()
    elif event == BUTTON_RESET:
        tc.reset()
        window["-TimeBox-"].update(tc.status_pretty())
    else:
        time.sleep(.5)


    print("go")
    # logger(f"You entered {values[0]}")

window.close()
