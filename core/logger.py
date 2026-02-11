from datetime import datetime
import os
from pathlib import Path
from prompt_toolkit.formatted_text import FormattedText


timestamp = datetime.now()
log_folder = "logs"
filename = Path(log_folder, f"{timestamp}.log.txt")


# TODO: allow for choosing log files location
def log(s: str | FormattedText):
    global timestamp
    if not os.path.isdir(log_folder):
        os.makedirs(log_folder)
    with open(filename, "a+") as file:
        if isinstance(s, FormattedText):
            s = str(s)
        file.write(s)
        file.write("\n")
