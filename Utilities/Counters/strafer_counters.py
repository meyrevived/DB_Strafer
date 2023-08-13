from __future__ import annotations

from counters_parent import Counters
from counter import Counter


class StraferCounters(Counters):

    def __init__(self, log_dir_path: str) -> None:
        super().__init__(log_dir_path)
        self._queries_run_counter = Counter(0)
        self._logins_run_counter = Counter(0)
        self._logouts_run_counter = Counter(0)
        self._querier_threads_run = Counter(0)

    @classmethod
    def create_singleton(cls) -> StraferCounters:
        return StraferCounters()

    @staticmethod
    def get_instance() -> StraferCounters:
        if StraferCounters._INSTANCE == None:
            # DEBUG
            print("StraferCounters called but not initialized")
            raise SystemExit
        return StraferCounters._INSTANCE

    def increase_queries_run_counter(self) -> None:
        self._queries_run_counter.setter()

    def increase__logins_run_counter(self) -> None:
        self._logins_run_counter.setter()

    def increase_logouts_run_counter(self) -> None:
        self._logouts_run_counter.setter()

    def increase_querier_threads_run(self) -> None:
        self._querier_threads_run.setter()
