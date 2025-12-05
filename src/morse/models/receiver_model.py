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

for i in range(10000):
    volt_U1 = float(device.get_input_voltage(channel=1))
    volt_resistor = float(device.get_input_voltage(channel=2))
    volt_LED = volt_U1 - volt_resistor
    
    time.sleep(0.05)
        
    
    # measures time of light
    if volt_LED > 1.5:
        
        time_on = time.time() - start
        
        #print(f"Light was on for {time_on} seconds")
        start = time.time()
                
        # adds '.' to symbols list
        if 0.2 < time_on < 0.3:
            list_symbol.append(".")
            #print("dot")
            
        # adds '-' to symbols list
        if 0.6 < time_on < 0.75:
            list_symbol.append("-")
            #print('dash')
        
            
    # measures time darkness
    if volt_LED < 1.5:
        
        time_off = time.time() - start_off
        
        #print(f"Light was on for {time_on} seconds")
        start_off = time.time()
        
        # # new dot or stripe if it was dark for 0.2s
        # if 0.15 < time_off < 0.3:
        #     list_symbol.append()
                
        # new letter if it was dark for 0.6s
        if 0.5 < time_off < 1.0:
            #print(list_symbol)
            string_symbols = print("".join(list_symbol))
            print(string_symbols)
            letter = decode(f"'{string_symbols}'", language= 'english')
            
            print("na decode")
            
            list_letter.append(letter)
            
            #print(letter)
            
            # clears symbol list 
            list_symbol = []
                
                
        # new word when it was dark for 1.4s
        if time_off > 1.4:
            #print(f"Light was off for {time_off} seconds, NEW WORD")
            
            if len(list_letter) > 0:
            
                string_letter = print("".join(list_letter))
                word = string_letter
                list_word.append(word)
                
                print(word)
                
                # clears letter list
                list_letter = []

        
        
string_words = print(" ".join(list_word))
sentence = decode(string_words)
    
print(sentence)