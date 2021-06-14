from multiprocessing import Queue
from osc4py3.as_eventloop import osc_method, osc_process, osc_startup, osc_udp_server
from time import sleep

from constants import OSC_PORT, BOLTEK_NAME, LIDAR_NAME, MULTISENSOR_NAME


class OSCServer:
    def __init__(self, boltek_data: Queue, lidar_data: Queue, multisensor_data: Queue) -> None:
        self.boltek_data = boltek_data
        self.lidar_data = lidar_data
        self.multisensor_data = multisensor_data

        self.setup_osc_servers()
        self.setup_osc_handlers()

    def run(self) -> None:
        while True:
            osc_process()
            sleep(0.01)

    def osc_handle_boltek(self, data: str) -> None:
        if not self.boltek_data.empty():
            self.boltek_data.get()

        self.boltek_data.put(data)

    def osc_handle_lidar(self, data: str) -> None:
        if not self.lidar_data.empty():
            self.lidar_data.get()
        
        self.lidar_data.put(data)

    def osc_handle_multisensor(self, data: str) -> None:
        if not self.multisensor_data.empty():
            self.multisensor_data.get()
        
        self.multisensor_data.put(data)

    def setup_osc_servers(self) -> None:
        osc_startup()
        osc_udp_server("0.0.0.0", OSC_PORT, BOLTEK_NAME)
        osc_udp_server("0.0.0.0", OSC_PORT, LIDAR_NAME)
        osc_udp_server("0.0.0.0", OSC_PORT, MULTISENSOR_NAME)

    def setup_osc_handlers(self) -> None:
        osc_method(f"/{BOLTEK_NAME}", self.osc_handle_boltek)
        osc_method(f"/{LIDAR_NAME}", self.osc_handle_lidar)
        osc_method(f"/{MULTISENSOR_NAME}", self.osc_handle_multisensor)
