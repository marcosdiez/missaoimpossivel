#!/usr/bin/env python3
import time

from helper import dumper
import myaudio

import PySimpleGUI as sg


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
            font=("Courier New", 180),
            expand_x=True,
            expand_y=False,
            # background_color="#00aaaa",
        )
    ],
    [sg.Text(key="-EXPAND2-", font="ANY 1", pad=(0, 0))],
    [
        sg.Button("Start"),
        sg.Button("Pause"),
        sg.Button("Reset"),
        sg.Button("Exit"),
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
window["Start"].set_focus()
while True:
    event, values = window.read()
    print(event)
    dumper(values)
    if event in (None, sg.WIN_CLOSED, "Exit"):
        # if user closes window or clicks cancel
        break
    elif event == "Go":
        # print(dir(window["-TimeBox-"]))
        print(window["-TimeBox-"].get())
        print(window["-TimeBox-"].get_size())
        print(window.get_size())

        window["-TimeBox-"].update(window["-TimeBox-"].get() + " bob!")
        # dumper(window.__dict__)
    if event == "Play":
        logger("play play play")
        myaudio.play(myaudio.AUDIO)
        logger("playerd")
        continue
    if event == "Stop":
        logger("stopping")
        myaudio.stop()
        logger("stopped")
        continue
    print("go")
    # logger(f"You entered {values[0]}")

window.close()
