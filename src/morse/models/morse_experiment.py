"""Model for Pythondaq, communicates with controller and view.

This is the model part of the three parted Model-View-Controller code.
It communicates with the arduino via the controller and does all necessary
calculations. It then gives the results to the view.
"""

import time

import numpy as np

from morse.controllers.arduino_device import ArduinoVISADevice, list_resources
from morse.controllers.morse_translation import translation


# initiate communication with Arduino

def scan(text, port):

    device = ArduinoVISADevice(port)

    # translate message to morse coe
    lijst_letters = translation(message=text)
    device.set_output_voltage(0)


    device.set_output_voltage(3.3)
    # time.sleep(0.01)
    device.set_output_voltage(0)
    time.sleep(1)

    # for every letter
    for i in range(len(lijst_letters)):

        # for every symbol in a letter
        for j in range(len(lijst_letters[i])):

            # light up for 1t
            if lijst_letters[i][j] == ".":
                device.set_output_voltage(volt=3.3)
                print("punt")
                time.sleep(0.04)
                device.set_output_voltage(volt=0)
                time.sleep(0.04)

            # light up for 3t
            if lijst_letters[i][j] == "-":
                device.set_output_voltage(volt=3.3)
                print("streep")
                time.sleep(0.12)
                device.set_output_voltage(volt=0)
                time.sleep(0.04)

        # wait 3.5 seconds for a space
        if lijst_letters[i] == "spatie":
            time.sleep(0.16)
        
        # wait 3t seconds after a letter
        time.sleep(0.08)

    time.sleep(2)
    device.set_output_voltage(3.3)
    time.sleep(0.2)
    device.set_output_voltage(0)


if __name__ == "__main__":
    scan("sos sos")


