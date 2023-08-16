#!/usr/bin/env python3
# 159280161

import serial

s = serial.Serial('COM4')
while True:
    res = s.read()
    print(res)