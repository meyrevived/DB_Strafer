from counters_parent import Counters


class MonitorCounters(Counters):

    def __init__(self, log_dir_path: str) -> None:
        if MonitorCounters.__instance != None:
            #DEBUG
            print("Monitor counter attemped to be created twice")
            raise SystemExit
        else:
            super().__init__(log_dir_path)
            self._counters_dict = {}
            MonitorCounters.__instance = self
