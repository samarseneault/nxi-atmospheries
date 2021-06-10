from threading import Thread

from sensors import ElectricFieldMonitor, Lidar, MultiSensor


def main() -> None:
    sensors = [Lidar("lidar"),
               ElectricFieldMonitor("boltek"),
               MultiSensor("multisonde")]

    for thread in [Thread(target=s.run) for s in sensors]:
        thread.start()


if __name__ == "__main__":
    main()
