from typing import List



from abs_querier import Querier, QuerierFactory

class MongoDBQuerier(Querier):

    def run_queries(self) -> None:
        pass



class MongoDBQuerierFactory(QuerierFactory):

    def get_querier(self, config_dictionary: dict) -> Querier:
        return MongoDBQuerier(config_dictionary)