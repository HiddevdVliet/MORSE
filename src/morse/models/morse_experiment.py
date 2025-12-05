"""Model for Pythondaq, communicates with controller and view.

This is the model part of the three parted Model-View-Controller code.
It communicates with the arduino via the controller and does all necessary
calculations. It then gives the results to the view.
"""

import time

import numpy as np

from morse.controllers.arduino_device import ArduinoVISADevice, list_resources
from morse.controllers.morse_translation import translation

device = ArduinoVISADevice("ASRL7::INSTR")


# class MorseExperiment:
#     def __init__(self):
#         self.device = ArduinoVISADevice("ASRL7::INSTR")


def scan(text):
    lijst_letters = translation(text=text)
    for i in range(len(lijst_letters)):
        for j in range(len(lijst_letters[i])):
            if lijst_letters[i][j] == ".":
                device.set_output_voltage(volt=3.3)
                print("punt")
                time.sleep(0.2)
                device.set_output_voltage(volt=0)
                time.sleep(0.2)
            if lijst_letters[i][j] == "-":
                device.set_output_voltage(volt=3.3)
                print("streep")
                time.sleep(0.6)
                device.set_output_voltage(volt=0)
                time.sleep(0.2)
        if lijst_letters[i] == "spatie":
            time.sleep(1)
        time.sleep(1)

    # turn off LED after measurements
    device.set_output_value(value=0)


scan("sos sos")
