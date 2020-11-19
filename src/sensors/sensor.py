from multiprocessing import Queue

from osc4py3.oscbuildparse import OSCMessage


class Sensor:
    def __init__(self, queue: Queue[OSCMessage]) -> None:
        self.queue = queue

    def run(self) -> None:
        while True:
            data = self.read_device()
            self.send_data(data)

    def read_device(self):
        raise NotImplementedError

    def format_data(self, data) -> OSCMessage:
        raise NotImplementedError

    def send_data(self, data: OSCMessage) -> None:
        self.queue.put(data)
