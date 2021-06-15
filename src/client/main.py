from threading import Thread

from constants import BOLTEK_NAME, LIDAR_NAME, MULTISENSOR_NAME
from sensors import ElectricFieldMonitor, Lidar, MultiSensor


def main() -> None:
    sensors = [Lidar(LIDAR_NAME),
               ElectricFieldMonitor(BOLTEK_NAME)]

    for thread in [Thread(target=s.run) for s in sensors]:
        thread.start()


if __name__ == "__main__":
    main()
