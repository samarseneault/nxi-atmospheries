from contextlib import ExitStack

from context import Process, Queue
from sensors import BoltekSensor, VaisalaSensor
from streaming.stream_service import StreamService


def main() -> None:
    with ExitStack() as stack, Queue() as communication_queue:
        sensors = [
            BoltekSensor(communication_queue),
            VaisalaSensor(communication_queue)
        ]

        streams = [StreamService()]

        for process in [Process(target=s.run) for s in sensors + streams]:
            stack.enter_context(process)


if __name__ == "__main__":
    main()
