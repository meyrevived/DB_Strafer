from typing import List
import psycopg2


from abs_querier import Querier, QuerierFactory

class PostgreSQLQuerier(Querier):

    def run_queries(self) -> None:
        try:
            # DEBUG
            print("run_queries for PostgreSQL is running")

            postgresql_connection = psycopg2.connect(
            host = self._ip,
            dbname = self._instace,
            user = self._user_name,
            password = self._password,
            port = self._port
            )

            cursor = postgresql_connection.cursor()

            # DEBUG 
            print("Successfully connected to PostgreSQL")

            for query in self._queries:
                cursor.execute(query)

            cursor.close()

        except(Exception, psycopg2.DatabaseError) as e:
            # DEBUG
            print("run_querier for PostgreSQL can into an exception:")
            print(e)
        
        finally:
            if postgresql_connection is not None:
                postgresql_connection.close()



class PostgreSQLQuerierFactory(QuerierFactory):

    def get_querier(self, user_name: str, password: str, ip: str, port: str, instance: str, schema: str, queries: List[str]) -> Querier:
        return PostgreSQLQuerier(user_name, password, ip, port, instance, schema, queries)