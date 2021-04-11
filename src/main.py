from contextlib import ExitStack
from multiprocessing import Queue

from context import Process
from sensors import BoltekSensor, VaisalaSensor
from streaming.stream_service import StreamService


def main() -> None:
    communication_queue = Queue()
    with ExitStack() as stack:
        sensors = [BoltekSensor(communication_queue)]
        streams = [StreamService(communication_queue)]

        for process in [Process(target=s.run) for s in sensors + streams]:
            process.start()
            stack.enter_context(process)


if __name__ == "__main__":
    main()
