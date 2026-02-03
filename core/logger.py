from datetime import datetime
import os
from pathlib import Path


timestamp = datetime.now()


# TODO: allow for choosing log files location
def log(str: str):
    global timestamp
    log_folder = "logs"
    filename = Path(log_folder, f"{timestamp}.log.txt")
    if not os.path.isdir(log_folder):
        os.makedirs(log_folder)
    with open(filename, "a+") as file:
        file.write(str)
        file.write("\n")
