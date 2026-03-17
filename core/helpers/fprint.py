from time import sleep

import prompt_toolkit
from prompt_toolkit.formatted_text import FormattedText

from core.logger import log

delay = 0


def _bold(s: str):
    return FormattedText([("bold", s)])


def fprint(
    s: str | FormattedText, bold=False, pinned=False, skip_logging=False, debug=False
):
    global delay
    sleep(delay / 1000)
    fs = f"{"DEBUG: " if debug else ""}{s}"
    if not pinned and not skip_logging:
        log(fs)
    if bold and isinstance(fs, str):
        fs = _bold(fs)
    prompt_toolkit.print_formatted_text(fs)


def set_print_delay(new_delay: int):
    global delay
    delay = new_delay
