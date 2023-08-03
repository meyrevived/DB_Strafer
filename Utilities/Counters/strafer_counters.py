from counters_parent import Counters

class StraferCounters(Counters):

    def __init__(self, log_dir_path: str) -> None:
        if StraferCounters.__instance != None:
            #DEBUG
            print("Strafer counter attemped to be created twice")
            raise SystemExit
        else:
            super().__init__(log_dir_path)
            self._counters_dict = {
                "Queries run" : 0,
                "Logins run" : 0,
                "logouts run": 0, 
                "Querier threads run" : 0
            }
            StraferCounters.__instance = self

    