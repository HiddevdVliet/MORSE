"""A module that communicates with the Arduino device.

This module contains classes and methods to communicate with the Arduino device
using PyVISA commands. It also includes ADC-to-voltage conversions.
"""



# import libraries
import pyvisa
import warnings



# ignores the warning concerning the psutil and zerconf packages
warnings.filterwarnings("ignore", message="TCPIP:instr resource discovery is limited to the default interface")
warnings.filterwarnings("ignore", message="TCPIP::hislip resource discovery requires the zeroconf package to be installed... try 'pip install zeroconf")



# get port list
def list_resources():
    """Lists the available ports.

    Returns:
        list: Tuple of available ports detected by the pyvisa resource manager.
    """

    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()

    return ports


# Class with methods that handle the communication with the arduino device
class ArduinoVISADevice:
    """Handles communication with the Arduino device.
    
    This class provides methods to interact with the Arduino device. 
    These methods can set output values, read input values and
    convert between ADC values and voltages.
    
    Attributes:
        rm: The PyVISA resource manager.
        device: The opened VISA device.
    """
    
    def __init__ (self, port):
        """Makes the connection to the Arduino device.

        Args:
            port: The port number which connects to the Arduino device.
        """
        self.rm = pyvisa.ResourceManager("@py")
        self.device = self.rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        """Returns the identification of the Arduino device.
        
        Returns:
            str: Device identification string.
        """
        identification = self.device.query("*IDN?")
   
        return identification

    def set_output_value(self, value):
        """Sets the output value on channel 0.
        
        Args:
            value: Output value, which will be set on channel 0.
        """
        ADC_value = value

        self.device.query(f"OUT:CH0 {ADC_value}")

    def get_output_value(self):
        """Measures and returns the output value from channel 0.
        
        Returns:
            float: Measured output value from channel 0.
        """
        output_value = float(self.device.query("OUT:CH0?"))

        return output_value
    
    def get_input_value(self, channel):
        """Measures and returns the input value from the chosen channel.
        
        Args:
            channel: Channel number to read the input value from.

        Returns:
            float: Measured input value from the chosen channel.
        """ 
        input_value = float(self.device.query(f"MEAS:CH{channel}?"))

        return input_value

    def get_input_voltage(self, channel):
        """Returns input voltage, using the conversion from ADC to voltage.
        
        Args:
            channel: Channel number to read the voltage from.

        Returns:
            float: The voltage value of the chosen channel, converted from the ADC reading.
        """
        input_value = self.get_input_value(channel)
        
        input_voltage = self.ADC_volt(input_value)

        return input_voltage

    def ADC_volt(self, ADC):
        """Converts ADC value to voltage.

        Args:
            ADC: An ADC value between 0 and 1023.

        Returns:
            float: Voltage value converted from ADC.
        """
        
        voltage = (ADC / 1023) * 3.3
        
        return voltage

    def volt_ADC(self, voltage):
        """Converts voltage to ADC value.

        Args:
            voltage: A voltage value between 0 and 3.3.

        Returns:
            integer: ADC value converted from voltage.
        """
        
        ADC = int((voltage / 3.3) * 1023)
        
        return ADC

    def close_device(self):
        """
        
        """
        
        self.device.close()