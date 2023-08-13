from datetime import datetime
from abc import ABC, abstractmethod


class Querier(ABC):

    def __init__(self, config_dictionary: dict) -> None:
        self._user_name = config_dictionary["user_name"]
        self._password = config_dictionary["password"]
        self._ip = config_dictionary["ip"]
        self._port = config_dictionary["port"]
        self._db_name = config_dictionary["db_name"]
        self._schema = config_dictionary["schema"]
        self._queries = config_dictionary["queries"]

    def run_querier(self) -> None:
        run_start_time = datetime.now().strftime("%H:%M:%S")
        # DEBUG
        print("run_querier started running")

        self.run_queries()

        # DEBUG
        run_end_time = datetime.now().strftime("%H:%M:%S")
        print(f"run_querier started at {run_start_time}")
        print(f"run_querier ended at {run_end_time}")

    @abstractmethod
    def run_queries(self) -> None:
        ...


class QuerierFactory(ABC):

    @abstractmethod
    def get_querier(self, config_dictionary: dict) -> Querier:
        ...
