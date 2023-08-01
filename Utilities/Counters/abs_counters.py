

class Counters:

    def __init__(self, log_dir_path: str) -> None:
        self._counters_file_path = f"{log_dir_path}counters"
        self._counters_dict = {}