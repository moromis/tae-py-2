import prompt_toolkit
from prompt_toolkit.formatted_text import FormattedText

from core import logger


def _bold(s: str):
    return FormattedText([("bold", s)])


def fprint(s: str, bold=False, pinned=False, skip_logging=False):
    if not pinned and not skip_logging:
        logger.log(s)
    fs = s
    if bold:
        fs = _bold(s)
    prompt_toolkit.print_formatted_text(fs)
