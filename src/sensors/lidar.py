from .sensor import Sensor

from osc4py3.oscbuildparse import OSCMessage
from serial import Serial, SEVENBITS, PARITY_MARK, STOPBITS_ONE


class Lidar(Sensor):
    def __init__(self) -> None:
        super().__init__()
        self.serial_reader = Serial(port="COM5",
                                    baudrate=9600,
                                    bytesize=SEVENBITS,
                                    parity=PARITY_MARK,
                                    stopbits=STOPBITS_ONE)

    def read_device(self):
        return self.serial_reader.readline()

    def format_data(self, data)  -> OSCMessage:
        return data
