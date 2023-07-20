from typing import List



from abs_querier import Querier, QuerierFactory

class SQLServerQuerier(Querier):

    def run_queries(self) -> None:
        pass



class SQLServerQuerierFactory(QuerierFactory):

    def get_querier(self, config_dictionary: dict) -> Querier:
        return SQLServerQuerier(config_dictionary)