from queue import Queue

from flask import Flask
from osc4py3.as__common import osc_method, osc_startup, osc_udp_server

from constants import OSC_PORT, BOLTEK_NAME, LIDAR_NAME, MULTISENSOR_NAME


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


def osc_handle_boltek(data: str) -> None:
    boltek_data.put(data)


def osc_handle_lidar(data: str) -> None:
    lidar_data.put(data)


def osc_handle_multisensor(data: str) -> None:
    multisensor_data.put(data)


def setup_osc_servers() -> None:
    osc_startup()
    osc_udp_server(BOLTEK_NAME, "0.0.0.0", OSC_PORT)
    osc_udp_server(LIDAR_NAME, "0.0.0.0", OSC_PORT)
    osc_udp_server(MULTISENSOR_NAME, "0.0.0.0", OSC_PORT)


def setup_osc_handlers() -> None:
    osc_method(f"/{BOLTEK_NAME}", osc_handle_boltek)
    osc_method(f"/{LIDAR_NAME}", osc_handle_lidar)
    osc_method(f"/{MULTISENSOR_NAME}", osc_handle_multisensor)


def main() -> None:
    setup_osc_servers()
    setup_osc_handlers()

    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
