#!/usr/bin/env python3

import PySimpleGUI as sg
import myaudio


# sg.theme_previewer()
sg.theme("GrayGrayGray")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("Some text on Row 1")],
    [sg.Text("Enter something on Row 2"), sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancel"), sg.Button("Play"), sg.Button("Stop")],
    [sg.Text("Some text on Row 2")],
]

# Create the Window
window = sg.Window("Window Title", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        break
    if event == "Play":
        print("play play play")
        myaudio.play(myaudio.AUDIO)
        print("playerd")
        continue
    if event == "Stop":
        print("stopping")
        myaudio.stop()
        print("stopped")
        continue
    print("You entered ", values[0])

window.close()
