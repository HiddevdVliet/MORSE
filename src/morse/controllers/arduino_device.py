"""Controller for Pythondaq, to be used with arduino.

This is the controller part of the three-parted Model-View-Controller code,
that does the raw communication with the arduino.
"""

import pyvisa

rm = pyvisa.ResourceManager("@py")


# function that returns list of ports
def list_resources():
    """Returns list of all active USB ports."""
    ports = rm.list_resources()
    return ports


class ArduinoVISADevice:
    """Communicate with the arduino.

    This class lets you request the identification string from the arduino.
    It also lets you put voltages on channel 0 and can return the voltage on any channel.

    Attributes:
        port (string): a port ID given by the user which will be opened.
        value (int): A voltage ADC value to put on channel 0.
        channel (int): The channel that should be interacted with.
    """

    def __init__(self, port):
        """Opens contact with arduino connected to port.

        Args:
            port (string): USB port that should be used to communicate with arduino.
        """
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """returns identification string of connected arduino."""
        identification = self.device.query("*IDN?")
        return identification

    def set_output_value(self, value):
        """Sets a voltage on channel 0.

        Args:
            value (int): A voltage in ADC values.
        """
        value_int = int(value)
        self.device.query(f"OUT:CH0 {value_int}")

    def set_output_voltage(self, volt):
        """Sets a voltage on channel 0.

        Args:
            volt (float): A voltage in volt.
        """
        value = int(volt * (1023 / 3.3))
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """Returns the voltage on channel 0 in ADC values."""
        value_out = int(self.device.query("OUT:CH0?"))
        return value_out

    def get_input_value(self, channel):
        """Returns the voltage on a given channel in ADC values.

        Args:
            channel (int): The channel from which the voltage should be returned.
        """
        channel_int = int(channel)
        input_value = int(self.device.query(f"MEAS:CH{channel_int}?"))
        return input_value

    def get_input_voltage(self, channel):
        """Returns the voltage on a given channel in volts.

        Args:
            channel (int): The channel from which the voltage should be returned.
        """
        channel_int = int(channel)
        input_value = int(self.get_input_value(channel_int))
        input_volt = input_value * (3.3 / 1023)
        return input_volt

    def close_communication(self):
        """Closes all communication with the current Arduino."""
        self.device.close()


if __name__ == "__main__":
    print(list_resources())
