from .sensor import Sensor
from multiprocessing import Queue


class VaisalaSensor(Sensor):
    def __init__(self, queue: Queue) -> None:
        super().__init__(queue)

    def read_device(self):
        return 0

    def format_data(self, data):
        return data
