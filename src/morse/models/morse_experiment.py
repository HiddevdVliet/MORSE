"""Model for Pythondaq, communicates with controller and view.

This is the model part of the three parted Model-View-Controller code.
It communicates with the arduino via the controller and does all necessary
calculations. It then gives the results to the view.
"""

import time
import numpy as np

from morse.controllers.arduino_device import ArduinoVISADevice
from morse.controllers.morse_translation import translation

# initiate communication with Arduino
device = ArduinoVISADevice("ASRL8::INSTR")


def scan(text):
    # translate message to morse coe
    lijst_letters = translation(message=text)

    # for every letter
    for i in range(len(lijst_letters)):

        # for every symbol in a letter
        for j in range(len(lijst_letters[i])):

            # light up for a short time
            if lijst_letters[i][j] == ".":
                device.set_output_voltage(volt=3.3)
                print("punt")
                time.sleep(0.3)
                device.set_output_voltage(volt=0)
                time.sleep(0.5)

            # light up for a long time
            if lijst_letters[i][j] == "-":
                device.set_output_voltage(volt=3.3)
                print("streep")
                time.sleep(1.2)
                device.set_output_voltage(volt=0)
                time.sleep(0.5)

        # wait 3.5 seconds for a space
        if lijst_letters[i] == "spatie":
            time.sleep(3.5)
        
        # wait 2.5 + 0.5 seconds after a letter
        time.sleep(2.5)

    time.sleep(7)
    device.set_output_voltage(3.3)
    time.sleep(0.2)
    device.set_output_voltage(0)


if __name__ == "__main__":
    scan("sos sos")
