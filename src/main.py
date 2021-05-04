from threading import Thread

from sensors import BoltekSensor, Lidar


def main() -> None:
    sensors = [Lidar()]

    for thread in [Thread(target=s.run) for s in sensors]:
        thread.start()


if __name__ == "__main__":
    main()
