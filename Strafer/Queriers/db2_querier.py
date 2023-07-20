from typing import List



from abs_querier import Querier, QuerierFactory

class DB2Querier(Querier):

    def run_queries(self) -> None:
        pass



class DB2QuerierFactory(QuerierFactory):

    def get_querier(self, config_dictionary: dict) -> Querier:
        return DB2Querier(config_dictionary)