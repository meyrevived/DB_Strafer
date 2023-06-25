#!/usr/bin/env python3

import sys

from Utilities.main_utils import clear


mode_error_msg = """
    Please choose one of the following modes:
        
        1. Duo mode - running both a Strafer process and the Monitor process on the database server machine.

        2. Split mode - one machine runs the Strafer, stressing the database with queries, while the database server machine is running the Monitor.

        Your choice: """

component_error_msg = """
    Please choose one of the following components:

        1. Strafer - A prcess that connects to a database and runs queries from an SQL file the user provides, at whichever frequency the user configures.

        2. Monitor - A process that gathers information about CPU, RAM and disk space usage from the database server at a frequency the user configures. Can create a CSV report with its findings at user's request.

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

        
        if mode.lower() == "duo":
            # test
            print("You chose due mode")
            
            ## code ##
            break
        elif mode.lower() == "split":
            # test
            print("You chose split mode")

            clear()

            component = input("""
                Which component would you like to be running?

                    1. Strafer

                    2. Monitor 

                if you didn't mean to run DB Strafer, type 'quit'

                Your choice: """)

            if component.lower() == "strafer":
                # test
                print("You chose to run a Strafer")

                ## code ##
                break
            elif component.lower() == "monitor":
                # test
                print("You chose to run a Monitor")

                ## code ##
                break
            elif mode.lower() == "quit":
                # test 
                print("You chose to quit")

                ## code ##
                break
            else:
                clear()
                print(component_error_msg)

        elif mode.lower() == "quit":
            # test 
            print("You chose to quit")

            ## code ##
            break
        else:
            clear()
            print(mode_error_msg)


        

        # Monitor / Strafer are processes

        # Starts logging before other processes

        # In “duo” mode, starts Monitor before Strafer

        # Gracefully exit

