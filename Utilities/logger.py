from Utilities.Counters.strafer_counters import StraferCounters
from main_utils import Mode, run_process
# from Counters import *


class Logger:

    def __init__(self, log_dir_path: str, mode: Mode) -> None:
        self._logging_directory_path = log_dir_path

        if mode == Mode.STRAFER:
            self._counters = StraferCounters.StraferCounters.get_instance()

        # set counters file writing to run
        run_process(self._counters.write_to_file())

        # creates log file - ???

    def run_logger(self) -> None:
        # DEBUG
        print("run_logger starter running")
        pass
