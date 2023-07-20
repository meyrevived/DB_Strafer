#!/usr/bin/env python3

import sys
from time import sleep


import Utilities.main_utils
from Monitor.monitor import Monitor
from Strafer.strafer import Strafer
from Utilities.logger import Logger


mode_error_msg = """
    Please choose one of the following modes:
        
        1. Duo mode - running both a Strafer process and the Monitor process on the database 
        server machine.

        2. Split mode - one machine runs the Strafer, stressing the database with queries, 
        while the database server machine is running the Monitor.

        Your choice: """

component_error_msg = """
    Please choose one of the following components:

        1. Strafer - A prcess that connects to a database and runs queries from an SQL file 
        the user provides, at whichever frequency the user configures.

        2. Monitor - A process that gathers information about CPU, RAM and disk space usage 
        from the database server at a frequency the user configures. Can create a CSV report 
        with its findings at user's request.

        Your choice: """

if __name__ == "__main__":

    print("""
        Welcome to the DB Strafer, your stress and monitoring tool for databases
    """)

    while True: 
 
        try:

            _LOGGER = Logger()
            # Accepts “duo” / “monitor” / “strafer”
            mode = input("""
                How would you like to run DB Strafer?
                    
                    1. Duo mode

                    2. Split mode
            
                If you didn't mean to run DB Strafer, type 'quit'
                
                Your choice: """)

            
            if mode.lower() in ("duo", "1"):
                # DEBUG
                print("""You chose due mode. 
                      Strafer will start running two minutes after Monitor begins to run""")

                _STRAFER = Strafer()
                _MONITOR = Monitor()

                Utilities.main_utils.run_process(_LOGGER.run_logger)
                Utilities.main_utils.run_process(_MONITOR.run_monitor)
                sleep(120)
                Utilities.main_utils.run_process(_STRAFER.run_strafer)
                break
            elif mode.lower() in ("split", "2"):
                # DEBUG
                print("You chose split mode")

                Utilities.main_utils.clear()

                component = input("""
                    Which component would you like to be running?

                        1. Strafer

                        2. Monitor 

                    If you didn't mean to run DB Strafer, type 'quit'
                    To go back to the previous menue, type 'back'

                    Your choice: """)

                if component.lower() in ("strafer", "1"):
                    # DEBUG
                    print("You chose to run a Strafer")

                    _STRAFER = Strafer()

                    Utilities.main_utils.run_process(_LOGGER.run_logger)
                    Utilities.main_utils.run_process(_STRAFER.run_strafer)
                    break
                elif component.lower() in ("monitor", "2"):
                    # DEBUG
                    print("You chose to run a Monitor")

                    _MONITOR = Monitor()

                    Utilities.main_utils.run_process(_LOGGER.run_logger)
                    Utilities.main_utils.run_process(_MONITOR.run_monitor)
                    break
                elif component.lower() == "quit":
                    # DEBUG 
                    print("You chose to quit")
                    break
                elif component.lower() == "back":
                    # DEBUG 
                    Utilities.main_utils.clear()
                    print(mode_error_msg)
                else:
                    Utilities.main_utils.clear()
                    print(component_error_msg)

            elif mode.lower() == "quit":
                # DEBUG 
                print("You chose to quit")

                ## code ##
                break
            else:
                Utilities.main_utils.clear()
                print(mode_error_msg)
        
        except SystemExit:
            # DEBUG
            print("Something went wrong, DB Strafer had to exit")


        

        # Monitor / Strafer are processes

        # Starts logging before other processes

