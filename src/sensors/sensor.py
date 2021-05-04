from osc4py3.as_eventloop import osc_startup, osc_udp_client, osc_send, osc_process, osc_terminate
from osc4py3.oscbuildparse import OSCMessage

from .constants import ADDRESS, PORT, CLIENT_NAME


class Sensor:
    def __init__(self) -> None:
        osc_startup()
        osc_udp_client(ADDRESS, PORT, CLIENT_NAME)  # Make client channels to send packets.

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        osc_terminate()

    def run(self) -> None:
        while True:
            data = self.read_device()
            print(data)
            # self.send_data(data)

    def read_device(self):
        raise NotImplementedError

    def format_data(self, data) -> OSCMessage:
        raise NotImplementedError

    def send_data(self, data: OSCMessage) -> None:
        osc_send(data, CLIENT_NAME)
        osc_process()  # Needs to be called for the thread to process the "transaction"

