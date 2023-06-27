from datetime import datetime
from typing import List

class Querier:

    def __init__(self, queries: List[str]) -> None:
        self._queries = queries

    def run_querier() -> None:
        run_start_time = datetime.now().strftime("%H:%M:%S")
        # DEBUG
        print("run_querier started running")
        run_end_time = datetime.now().strftime("%H:%M:%S")
        print(f"run_querier started at {run_start_time}")
        print(f"run_querier ended at {run_end_time}")