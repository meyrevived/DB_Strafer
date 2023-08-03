import os
import subprocess
from multiprocessing import Process
from typing import Callable
import platform
from pathlib import Path


TIME_TO_RUN_TESTS = 60 * 60  * 24 * 4

def clear() -> None:
    """
    Clearing the console between screens in  the main menue for choosing mode and module.
    Code taken from https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


def run_process(function: Callable[[], None]) -> None:
    """
    Function for running a function as a process. 
    Unless told otherwise, will run the process for four days
    :return: None
    """
    p = Process(target=function)
    p.start()
    p.join(TIME_TO_RUN_TESTS)

    if p.is_alive():
        p.terminate()
        p.join()

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

  
            
        except Exception as e:
            # DEBUG
            print(f"""
                  Cannot create Logger, encountered
                  {e} 
                  """)
            raise SystemExit



