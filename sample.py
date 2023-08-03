#!/usr/bin/env python3
import json
import PySimpleGUI as sg
import myaudio
import random


def dumper(arg):
    def json_default(arg):
        # if isinstance(arg, datetime.datetime) or isinstance(arg, Enum):
        #     return "{}".format(arg)
        raise TypeError(arg)

    # return json.dumps(data, sort_keys=True, default=json_default, indent=2)
    print(json.dumps(arg, sort_keys=True, default=json_default, indent=2))


def logger(msg):
    print(msg)
    window["Status"].update(msg)

# python3 -m pip install psgdemos
# sg.theme_previewer()
sg.theme("GrayGrayGray")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("Some text on Row 1", auto_size_text=True)],
    [sg.Text("Enter something on Row 2"), sg.InputText(expand_x=True, expand_y=True)],
    [sg.Button("Ok"), sg.Button("Cancel"), sg.Button("Play"), sg.Button("Stop")],
    [sg.Text("Status", key="Status")],
]

# Create the Window
window = sg.Window("Window Title", layout, auto_size_text=True, auto_size_buttons=True, resizable=True, element_justification='center')
# Event Loop to process "events" and get the "values" of the inputs
# window = sg.Window(
#     "Sudoku",
#     [
#         [
#             sg.Frame(
#                 "",
#                 [
#                     [
#                         sg.I(
#                             random.randint(1, 9),
#                             justification="r",
#                             size=(3, 1),
#                             # key=f"{frow * 10000  + row}-{fcol * 3 + col}",
#                             key=f"{frow}-{fcol}-{row}-{col}"
#                         )
#                         for col in range(3)
#                     ]
#                     for row in range(3)
#                 ],
#             )
#             for fcol in range(3)
#         ]
#         for frow in range(3)
#     ]
#     + [
#         [sg.B("Exit")],
#         [sg.Text("StatusBar"), sg.Sizegrip()]
#     ],

#     # expand_x=True, expand_y=True,
#     resizable=True
# )

while True:
    event, values = window.read()
    print(event)
    dumper(values)
    if event in (None, sg.WIN_CLOSED, "Cancel"):
        # if user closes window or clicks cancel
        break
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
