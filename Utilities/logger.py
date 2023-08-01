import os
import platform
from pathlib import Path

from counters import Counters



class Logger:

  
    def run_logger(self) ->     None:
        # DEBUG
        print("run_logger starter running")
        pass


    def create_logging_directory(self) -> str:
        
        is_windows = False 
        logs_dir_path = ""

        if platform.system() == "Windows":
             is_windows = True 

        cwd = Path.cwd()

        try:
            # create the logs and counters directory
            if is_windows:
                logs_dir_path = f"{cwd}\\Logs\\"
            else:
                logs_dir_path = f"{cwd}/Logs/"

            if not os.path.exists(logs_dir_path):
                os.makedirs(logs_dir_path)

                # creates counters file 
                # call write-counters functionh

                # creates log file - ???
            
        except Exception as e:
            # DEBUG
            print(f"""
                  Cannot create Logger, encountered
                  {e} 
                  """)
            raise SystemExit