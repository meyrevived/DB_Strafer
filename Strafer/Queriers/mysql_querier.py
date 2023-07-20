from typing import List



from abs_querier import Querier, QuerierFactory

class MySQLQuerier(Querier):

    def run_queries(self) -> None:
        pass



class MySQLQuerierFactory(QuerierFactory):

    def get_querier(self, config_dictionary: dict) -> Querier:
        return MySQLQuerier(config_dictionary)