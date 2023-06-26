#!/usr/bin/env python3

import sys


import Utilities.main_utils as main
import Monitor.monitor as monitor
import Strafer.strafer as strafer
import Utilities.logger as logger


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
 
        
        # Accepts “duo” / “monitor” / “strafer”
        mode = input("""
            How would you like to run DB Strafer?
                
                1. Duo mode

                2. Split mode
        
            If you didn't mean to run DB Strafer, type 'quit'
            
            Your choice: """)

        
        if mode.lower() in ("duo", "1"):
            # DEBUG
            print("You chose due mode")
            
            ## code ##
            main.run_process(logger.run_logger)
            main.run_process(monitor.run_monitor)
            main.run_process(strafer.run_strafer)
            break
        elif mode.lower() in ("split", "2"):
            # DEBUG
            print("You chose split mode")

            main.clear()

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

                main.run_process(logger.run_logger)
                main.run_process(strafer.run_strafer)
                break
            elif component.lower() in ("monitor", "2"):
                # DEBUG
                print("You chose to run a Monitor")

                main.run_process(logger.run_logger)
                main.run_process(monitor.run_monitor)
                break
            elif component.lower() == "quit":
                # DEBUG 
                print("You chose to quit")
                break
            elif component.lower() == "back":
                # DEBUG 
                main.clear()
                print(mode_error_msg)
            else:
                main.clear()
                print(component_error_msg)

        elif mode.lower() == "quit":
            # DEBUG 
            print("You chose to quit")

            ## code ##
            break
        else:
            main.clear()
            print(mode_error_msg)


        

        # Monitor / Strafer are processes

        # Starts logging before other processes

        # In “duo” mode, starts Monitor before Strafer

        # Gracefully exit

