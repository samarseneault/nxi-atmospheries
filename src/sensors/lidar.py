from .sensor import Sensor

from osc4py3.oscbuildparse import OSCMessage
from serial import Serial, SEVENBITS, PARITY_MARK, STOPBITS_ONE


END_OF_READING = b'\x03\r\n'


class Lidar(Sensor):
    def __init__(self, client_name: str) -> None:
        super().__init__(client_name)
        self.serial_reader = Serial(port="COM8",
                                    baudrate=9600,
                                    bytesize=SEVENBITS,
                                    parity=PARITY_MARK,
                                    stopbits=STOPBITS_ONE)
        

    def read_device(self):
        reading = b""
        line = self.serial_reader.readline()
        
        while line != END_OF_READING:
            line = self.serial_reader.readline()
            reading += line
        
        return reading
        
    def format_data(self, data)  -> OSCMessage:
        return data
