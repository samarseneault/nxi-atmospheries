from contextlib import ExitStack
from multiprocessing import Process, Queue

from sensors import BoltekSensor, Lidar
from streaming.stream_service import StreamService


def main() -> None:
    communication_queue = Queue()
    sensors = [Lidar(communication_queue)]
    streams = [StreamService(communication_queue)]

    for process in [Process(target=s.run) for s in sensors + streams]:
        process.start()


if __name__ == "__main__":
    main()
