#!/usr/bin/env python
import sys

mode_error_msg = """
    Please choose one of the following modes:
        
        1. Due mode - running both a Strafer process and the Monitor process on the database server machine.

        2. Split mode - one machine runs the Strafer, stressing the database with queries, while the database server machine is running the Monitor.
"""

if __name__ == "__main__":
    
    print("""
        Welcome to the DB Strafer, your stress and monitoring tool for databases
    """)
    
    # Accepts “duo” / “monitor” / “strafer”
    mode = input("""
        How would you like to run DB Strafer?
            
            1. Duo mode

            2. Split mode
    
        If you didn't mean to run DB Strafer, type 'quit'""")
    
    if mode.lower() == "Duo":
        # test
        print("You chose due mode")
    elif mode.lower() == "split":
        # test
        print("You chose split mode")
    elif mode.lower() == "quit":
        # test 
        print("You chose to quit")
    else:
        print(mode_error_msg)

    

    

    # Monitor / Strafer are processes

    # Starts logging before other processes

    # In “duo” mode, starts Monitor before Strafer

    # Gracefully exit

