from __future__ import annotations
from abc import ABCMeta, abstractmethod

from time import sleep


class Counters(object):

    def __init__(self, log_dir_path: str):
        self._counters_file_path = f"{log_dir_path}counters"

    __INSTANCE: Counters = None

    @classmethod
    def singleton(cls) -> Counters:
        if cls._INSTANCE is None:
            cls._INSTANCE = cls.create_singleton()
            return cls._INSTANCE

    @classmethod
    @abstractmethod
    def create_singleton(cls) -> Counters:
        ...

    @abstractmethod
    def get_instance() -> Counters:
        ...

    def write_to_file(self) -> None:
        with open(self._counters_file_path) as counters_file:
            counters_file.write(self.__dict__)

        sleep(15)
