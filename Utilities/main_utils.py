import os
import subprocess
from multiprocessing import Process
from typing import Callable


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




