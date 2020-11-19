from .sensor import Sensor
from multiprocessing import Queue

from osc4py3.oscbuildparse import OSCMessage


class BoltekSensor(Sensor):
    def __init__(self, queue: Queue[OSCMessage]) -> None:
        super().__init__(queue)

    def read_device(self):
        return 0

    def format_data(self, data)  -> OSCMessage:
        return data
