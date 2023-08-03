from __future__ import annotations

from time import sleep

class Counters:

    __instance = None

    @staticmethod
    def get_instance() -> Counters:
        if Counters.__instance == None:
            #DEBUG
            print("Counters called but not initialized")
            raise SystemExit  
        return Counters.__instance
    
    def __init__(self, log_dir_path: str) -> None:
        self._counters_file_path = f"{log_dir_path}counters"
        self._counters_dict = {}

    def write_to_file(self) -> None:
        with open(self._counters_file_path) as counters_file:
            counters_file.write(self._counters_dict)
        
        sleep(15)

