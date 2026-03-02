import prompt_toolkit
from prompt_toolkit.formatted_text import FormattedText

from core.logger import log


def _bold(s: str):
    return FormattedText([("bold", s)])


def fprint(
    s: str | FormattedText, bold=False, pinned=False, skip_logging=False, debug=False
):
    fs = f"{"DEBUG: " if debug else ""}{s}"
    if not pinned and not skip_logging:
        log(fs)
    if bold and isinstance(fs, str):
        fs = _bold(fs)
    prompt_toolkit.print_formatted_text(fs)
