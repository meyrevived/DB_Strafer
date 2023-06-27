
from typing import List
from threading import Thread
from time import sleep

from querier import Querier

# database configuration
_DB_TYPE = ""
_USER_NAME = ""
_PASSWORD = ""
_IP = ""
_PORT = ""
_INSTANCE = ""
_SCHEMA = "N/A"
_QUERIES = []

# strafing configuration
_FREQUENCY_SECS = 0
_STRAFING_THREADS_NUM = 0
_STRAFING_CYCLES_NUM = 0
_STRAFE_ENDLESSLY = False



def run_strafer() -> None:
    """
    Strafing element - starts as many Querier threads as customer tells to, sleeps as much as the customer tells it to and then starts threading again
    """
    # DEBUG
    print("run_strafer started running")

    if not load_configuration():
        # break here
        pass

    queriers = []

    for thread_num in range(_STRAFING_THREADS_NUM):
        querier = create_querier()
        queriers.append(querier)

    if not _STRAFE_ENDLESSLY:
        for strafing_cycle in range(_STRAFING_CYCLES_NUM):
            strifing_element(queriers)
            sleep(_FREQUENCY_SECS)
    else:
        while True:
            strifing_element(queriers)
            sleep(_FREQUENCY_SECS)


def create_querier(queries: List[str]) -> Querier:
    """
    Creates a Querier with the given queries and returns it
    """
    # DEBUG
    print("create_querier started running")


def strifing_element(queriers: List[Querier]) -> None:
    """
    Recieves a list of queriers and starts them running, then waits for them to finish running
    """
    # DEBUG
    print("strifing_element started running")
    querier_threads = []

    for querier in queriers:
        querier_thread = Thread(target=querier.run_querier())
        querier_threads.append(querier_thread)
        querier_thread.start()
    
    for querier_thread in querier_threads:
        querier_thread.join()


def load_configuration(config_json_path: str) -> True:
    """
    Load configuration from configuration JSON (for now!) and saves them in the configuration variables
    """
    # DEBUG
    print("load_configuration started running")
    