from osc4py3.as_eventloop import osc_startup, osc_udp_client, osc_send, osc_process, osc_terminate
from osc4py3.oscbuildparse import OSCMessage

from constants import OSC_ADDRESS, OSC_PORT


class Sensor:
    def __init__(self, client_name: str) -> None:
        self.client_name = client_name
        osc_startup()
        osc_udp_client(OSC_ADDRESS, OSC_PORT, client_name)  # Make client channels to send packets.

    def __del__(self) -> None:
        osc_terminate()

    def run(self) -> None:
        while True:
            data = self.read_device()
            print(data)
            self.send_data(data)

    def read_device(self):
        raise NotImplementedError

    def format_data(self, data) -> OSCMessage:
        raise NotImplementedError

    def send_data(self, data: OSCMessage) -> None:
        osc_send(OSCMessage(f"/{self.client_name}", ",s", [data]), self.client_name)
        osc_process()  # Needs to be called for the thread to process the "transaction"

