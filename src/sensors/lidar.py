from .sensor import Sensor

from osc4py3.oscbuildparse import OSCMessage
from serial import Serial, EIGHTBITS, PARITY_NONE, STOPBITS_ONE


class Lidar(Sensor):
    def __init__(self, client_name: str) -> None:
        super().__init__(client_name)
        self.serial_reader = Serial(port="COM8",
                                    baudrate=9600,
                                    bytesize=EIGHTBITS,
                                    parity=PARITY_NONE,
                                    stopbits=STOPBITS_ONE)
        

    def read_device(self):
        return self.serial_reader.readline()

    def format_data(self, data)  -> OSCMessage:
        return data
