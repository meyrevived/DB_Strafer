
from typing import List
from threading import Thread
from time import sleep
import json

from Queriers.abs_querier import QuerierFactory
from Utilities.validation import validate_json
from Queriers import *
from Utilities.Counters.strafer_counters import StraferCounters


class Strafer:

    def __init__(self) -> None:
        # DEBUG
        print("Strafer initiated")

        # database configuration
        self._DB_COINFIG = {
            "_DB_TYPE": "",
            "_USER_NAME": "",
            "_PASSWORD": "",
            "_IP": "",
            "_PORT": "",
            "_DB_NAME": "",
            "_SCHEMA": "N/A",
            "_QUERIES": []
        }

        # strafing configuration
        self._STRAFING_CONFIG = {
            "_FREQUENCY_SECS": 0,
            "_STRAFING_THREADS_NUM": 0,
            "_STRAFING_CYCLES_NUM": 0,
            "_STRAFE_ENDLESSLY": False
        }

        self.load_configuration()

        self._QUARIER_FACTORY = self.create_querier_factory()

        self._COUNTERS = StraferCounters.StraferCounters.get_instance()

    def run_strafer(self) -> None:
        """
        Strafing element - starts as many Querier threads as customer tells to, sleeps as much as the customer tells it to and then starts threading again
        """
        # DEBUG
        print("run_strafer started running")

        if not self._STRAFING_CONFIG["_STRAFE_ENDLESSLY"]:
            for strafing_cycle in range(self._STRAFING_CONFIG["_STRAFING_CYCLES_NUM"]):
                self.strafing_element(self._QUARIER_FACTORY)
                sleep(self._STRAFING_CONFIG["_FREQUENCY_SECS"])
        else:
            while True:
                self.strafing_element(self._QUARIER_FACTORY)
                sleep(self._STRAFING_CONFIG["_FREQUENCY_SECS"])

    def create_querier_factory(self) -> QuerierFactory:
        """
        Creates a Querier with the given queries and returns it
        """
        # DEBUG
        print("create_querier started running")
        factories = {
            "postgresql": postgresql_querier.PostgreSQLQuerierFactory(self._DB_COINFIG),
            "db2": db2_querier.DB2QuerierFactory(self._DB_COINFIG),
            "mongodb": mongodb_querier.MongoDBQuerierFactory(self._DB_COINFIG),
            "mysql": mysql_querier.MySQLQuerierFactory(self._DB_COINFIG),
            "oracle": oracle_querier.OracleQuerierFactory(self._DB_COINFIG),
            "sqlserver": sqlserver_querier.SQLServerQuerierFactory(self._DB_COINFIG)
        }

        if self._DB_COINFIG["_DB_TYPE"] in factories:
            return factories[self._DB_COINFIG["_DB_TYPE"]]
        else:
            # DEBUG
            print("Requested database not supported")
            raise SystemExit

    def strafing_element(self, querier_factory: QuerierFactory) -> None:
        """
        Recieves a list of queriers and starts them running, then waits for them to finish running
        """
        # DEBUG
        print("strifing_element started running")

        querier_threads = []

        for thread_num in range(self._STRAFING_CONFIG["_STRAFING_THREADS_NUM"]):
            querier = querier_factory.get_querier()
            querier_thread = Thread(target=querier.run_querier())
            querier_threads.append(querier_thread)
            querier_thread.start()

        for querier_thread in querier_threads:
            querier_thread.join()

        self._COUNTERS.increase_querier_threads_run(
            self._STRAFING_CONFIG["_STRAFING_THREADS_NUM"])

    def load_configuration(self, config_json_path: str) -> None:
        """
        Load configuration from configuration JSON and saves them in the configuration variables
        """
        # DEBUG
        print("load_configuration started running")

        # validate configuration json is valid
        if validate_json(config_json_path, "strafer"):

            try:
                # configuration json is valid, we can use data from it to configure the Strafer
                with open(config_json_path) as config_json:
                    config_data = json.load(config_json)

                    self._DB_COINFIG["_DB_TYPE"] = config_data["db_config"]["db_type"].lower(
                    )
                    self._DB_COINFIG["_USER_NAME"] = config_data["db_config"]["user_name"].lower(
                    )
                    self._DB_COINFIG["_PASSWORD"] = config_data["db_config"]["password"]
                    self._DB_COINFIG["_IP"] = config_data["db_config"]["IP"]
                    self._DB_COINFIG["_PORT"] = config_data["db_config"]["port"]
                    self._DB_COINFIG["_DB_NAME"] = config_data["db_config"]["db_name"].lower(
                    )
                    self._DB_COINFIG["_SCHEMA"] = config_data["db_config"]["schema"].lower(
                    )
                    self._DB_COINFIG["_QUERIES"] = config_data["db_config"]["queries"]

                    self._STRAFING_CONFIG["_FREQUENCY_SECS"] = config_data["strafing_config"]["frequency_secs"]
                    self._STRAFING_CONFIG["_STRAFING_THREADS_NUM"] = config_data["strafing_config"]["strafing_threads_num"]
                    self._STRAFING_CONFIG["_STRAFING_CYCLES_NUM"] = config_data["strafing_config"]["strafing_cycles_num"]
                    self._STRAFING_CONFIG["_STRAFE_ENDLESSLY"] = config_data["strafing_config"]["strafe_endlessly"]

            except OSError:
                # DEBUG
                print(f"Cannot open configuration file at {config_json_path}")
                raise SystemExit
