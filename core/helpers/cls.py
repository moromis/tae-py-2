# from https://www.geeksforgeeks.org/clear-screen-python/
import os


def cls():
    # for windows
    if os.name == "nt":
        _ = os.system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system("clear")
