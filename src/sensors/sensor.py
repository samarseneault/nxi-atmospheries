from multiprocessing import Queue

class Sensor:
    def __init__(self, queue: Queue) -> None:
        self.queue = queue

    def run(self) -> None:
        while True:
            data = self.read_device()
            self.send_data(data)

    def read_device(self):
        raise NotImplementedError

    def format_data(self, data):
        raise NotImplementedError

    def send_data(self, data) -> None:
        self.queue.put(data)
