# import libraries
import numpy as np
from morse.controllers.receiver import ArduinoVISADevice, list_resources
import time
from MorseCodePy import decode

#print(list_resources())


device = ArduinoVISADevice(port = 'ASRL11::INSTR')

device.set_output_value(1023)


list_word = []
list_letter = []
list_symbol = []


start = time.time()
start_off = time.time()
time_off = 0

while time_off < 9.5:
    volt_U1 = float(device.get_input_voltage(channel=1))
    volt_resistor = float(device.get_input_voltage(channel=2))
    volt_LED = volt_U1 - volt_resistor
    
#    time.sleep(0.00025)
        
    
    # measures time of light
    if volt_LED > 1.5:
        
        time_on = time.time() - start
        
        #print(f"Light was on for {time_on} seconds")
        start = time.time()
                
        # adds '.' to symbols list
        if 0.2 < time_on < 0.65:
            list_symbol.append(".")
            print("dot")
            
        # adds '-' to symbols list
        if 1.0 < time_on < 1.4:
            list_symbol.append("-")
            print('dash')
        
            
    # measures time darkness
    if volt_LED < 1.5:
        
        time_off = time.time() - start_off
        
        #print(f"Light was on for {time_on} seconds")
        start_off = time.time()              
                
        # new letter
        if 2.5 < time_off < 4:            
            list_symbol.append(" ")
            
                
        # new word when it was dark for 2s
        if time_off > 5:
            #print(f"Light was off for {time_off} seconds, NEW WORD")
            print("space")
            
            list_symbol.append(" / ")


string_symbols = "".join(list_symbol)
sentence_: str = decode(string_symbols, language= 'english')        
        

print(string_symbols)
print(sentence_)