from contextlib import ExitStack
from typing import List

from context import Process, Queue
from sensors import BoltekSensor, VaisalaSensor, Sensor


def main() -> None:
    with ExitStack() as stack, Queue() as communication_queue:
        sensors: List[Sensor] = [
            BoltekSensor(communication_queue),
            VaisalaSensor(communication_queue)
        ]

        for process in [Process(target=s.run) for s in sensors]:
            stack.enter_context(process)



if __name__ == "__main__":
    main()
