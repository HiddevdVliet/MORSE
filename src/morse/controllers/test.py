# import libraries
import numpy as np
from morse.controllers.receiver import ArduinoVISADevice, list_resources
import time
from MorseCodePy import decode

#print(list_resources())


device = ArduinoVISADevice(port = 'ASRL11::INSTR')

device.set_output_value(1023)


for i in range(50):
    
    volt_U1 = float(device.get_input_voltage(channel=1))
    volt_resistor = float(device.get_input_voltage(channel=2))
    volt_LED = volt_U1 - volt_resistor
    
    
    print(volt_LED)
    
    
    time.sleep(0.1)