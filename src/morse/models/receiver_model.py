# import libraries
import numpy as np
from morse.controllers.receiver import ArduinoVISADevice, list_resources
import time


#print(list_resources())


device = ArduinoVISADevice(port = 'ASRL11::INSTR')

device.set_output_value(1023)

start = time.time()

for i in range(100):
    volt_U1 = float(device.get_input_voltage(channel=1))
    volt_resistor = float(device.get_input_voltage(channel=2))
    volt_LED = volt_U1 - volt_resistor
    
    time.sleep(0.1)
        
    if volt_LED > 1.5:
        
        time_on = time.time() - start
        
        #print(f"Light was on for {time_on} seconds")
        start = time.time()
        
        
        if time_on > 0.15:
            print(f"Light was on for {time_on} seconds")
            
        
        
        

    
    
    #print(volt_LED)