from contextlib import chdir
from datetime import datetime
import os
from prompt_toolkit.formatted_text import FormattedText


timestamp = datetime.now()
LOG_FOLDER = "logs"
filename = None
log_folder = LOG_FOLDER


def log(s: str | FormattedText, folder=None):
    global timestamp
    global filename
    global log_folder

    if folder:
        log_folder = folder
    filename = f"{timestamp}.log.txt"
    if not os.path.isdir(log_folder):
        os.makedirs(log_folder)

    # maybe hacky but required to make tests work...?
    with chdir(log_folder):
        with open(filename, "a+") as file:
            if isinstance(s, FormattedText):
                s = str(s)
            file.write(s)
            file.write("\n")
