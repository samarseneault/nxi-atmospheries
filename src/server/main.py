from multiprocessing import Process, Queue

from flask import Flask

from constants import BOLTEK_NAME, LIDAR_NAME, MULTISENSOR_NAME
from osc import OSCServer


app = Flask(__name__)
boltek_data, lidar_data, multisensor_data = Queue(), Queue(), Queue()


@app.route("/")
def root() -> str:
    return "Root for Atmospheries data streaming"


@app.route(f"/{BOLTEK_NAME}")
def stream_boltek() -> str:
    return boltek_data.get()


@app.route(f"/{LIDAR_NAME}")
def stream_lidar() -> str:
    return lidar_data.get()


@app.route(f"/{MULTISENSOR_NAME}")
def stream_multisensor() -> str:
    return multisensor_data.get()


def start_osc_server() -> None:
    print("Starting OSC server thread...")

    osc_server = OSCServer(boltek_data, lidar_data, multisensor_data)
    osc_server_thread = Process(target=osc_server.run)
    osc_server_thread.start()

    print("Done.")


def main() -> None:
    start_osc_server()

    app.run(host="0.0.0.0", port=5001)


if __name__ == "__main__":
    main()
