from datetime import datetime
import os
from pathlib import Path
from prompt_toolkit.formatted_text import FormattedText


timestamp = datetime.now()
LOG_FOLDER = "logs"
filename = None


def log(s: str | FormattedText, folder=LOG_FOLDER):
    global timestamp
    global filename
    filename = Path(folder, f"{timestamp}.log.txt")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    with open(filename, "a+") as file:
        if isinstance(s, FormattedText):
            s = str(s)
        file.write(s)
        file.write("\n")
