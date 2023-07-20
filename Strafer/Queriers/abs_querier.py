from datetime import datetime
from typing import List
from abc import ABC, abstractmethod



class Querier(ABC):

    def __init__(self, user_name: str, password: str, ip: str, port: str, instance: str, schema: str, queries: List[str]) -> None:
        self._user_name = user_name
        self._password = password
        self._ip = ip
        self._port = port
        self._instace = instance
        self._schema = schema
        self._queries = queries

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
        pass



class QuerierFactory(ABC):

    @abstractmethod
    def get_querier(self, user_name: str, password: str, ip: str, port: str, instance: str, schema: str, queries: List[str]) -> Querier:
        pass