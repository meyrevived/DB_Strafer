
from typing import List
from threading import Thread
from time import sleep
import json

from querier import Querier
from Utilities.validation import validate_json

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

    load_configuration()

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
    # code


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


def load_configuration(config_json_path: str) -> None:
    """
    Load configuration from configuration JSON and saves them in the configuration variables
    """
    # DEBUG
    print("load_configuration started running")

    # validate configuration json is valid
    if validate_json(config_json_path, "strafer"):
        
        try:
            # configuration json is valid, we can use data from it to configure the Strafer
            with open(config_json_path) as config_json:
                config_data = json.load(config_json)

                _DB_TYPE = config_data["db_config"]["db_type"]
                _USER_NAME = config_data["db_config"]["user_name"]
                _PASSWORD = config_data["db_config"]["password"]
                _IP = config_data["db_config"]["IP"]
                _PORT = config_data["db_config"]["port"]
                _INSTANCE = config_data["db_config"]["instance"]
                _SCHEMA = config_data["db_config"]["schema"]
                _QUERIES = config_data["db_config"]["queries"]

                _FREQUENCY_SECS = config_data["strafing_config"]["frequency_secs"]
                _STRAFING_THREADS_NUM = config_data["strafing_config"]["strafing_threads_num"]
                _STRAFING_CYCLES_NUM = config_data["strafing_config"]["strafing_cycles_num"]
                _STRAFE_ENDLESSLY = config_data["strafing_config"]["strafe_endlessly"]

        except OSError:
            # DEBUG
            print(f"Cannot open configuration file at {config_json_path}")
            raise SystemExit
        