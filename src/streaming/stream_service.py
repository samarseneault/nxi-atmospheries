from multiprocessing import Queue

from osc4py3.as_eventloop import osc_startup, osc_udp_client, osc_send, osc_process, osc_terminate
from osc4py3.oscbuildparse import OSCMessage

from .constants import ADDRESS, PORT, CLIENT_NAME


class StreamService:
    def __init__(self, queue: Queue[OSCMessage]) -> None:
        self.__queue = queue

    def __enter__(self) -> "StreamService":
        osc_startup()
        osc_udp_client(ADDRESS, PORT, CLIENT_NAME)  # Make client channels to send packets.

        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        osc_terminate()


    def run(self) -> None:
        while True:
            osc_send(self.__queue.get(), CLIENT_NAME)
            osc_process()  # Needs to be called for the thread to process the "transaction"
