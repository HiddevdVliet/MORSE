# import libraries
import numpy as np
from morse.controllers.receiver import ArduinoVISADevice, list_resources
import time
from MorseCodePy import decode
import matplotlib.pyplot as plt

#print(list_resources())


device = ArduinoVISADevice(port = 'ASRL11::INSTR')

device.set_output_value(1023)



start = time.time()
start_off = time.time()

list_volt = []
list_time = []


for i in range(600):
    volt_U1 = float(device.get_input_voltage(channel=1))
    volt_resistor = float(device.get_input_voltage(channel=2))
    volt_LED = volt_U1 - volt_resistor
    
    time.sleep(0.1)
        
    list_volt.append(volt_LED)
    list_time.append(i/10)
    


plt.plot(list_time, list_volt)
plt.show()
    
    
    

