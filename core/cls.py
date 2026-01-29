# from https://www.geeksforgeeks.org/clear-screen-python/

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


def cls():
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")
