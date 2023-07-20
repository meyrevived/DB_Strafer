from typing import List



from abs_querier import Querier, QuerierFactory

class OracleQuerier(Querier):

    def run_queries(self) -> None:
        pass



class OracleQuerierFactory(QuerierFactory):

    def get_querier(self, config_dictionary: dict) -> Querier:
        return OracleQuerier(config_dictionary)