from .sensor import Sensor

from multiprocessing import Queue
from osc4py3.oscbuildparse import OSCMessage
from serial import Serial


class VaisalaSensor(Sensor):
    def __init__(self, queue: Queue) -> None:
        super().__init__(queue)
        self.serial_reader = Serial("COM5", 9600)

    def read_device(self):
        return self.serial_reader.readline()

    def format_data(self, data)  -> OSCMessage:
        return data
