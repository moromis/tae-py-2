import prompt_toolkit
from prompt_toolkit.formatted_text import FormattedText


def _bold(s):
    return FormattedText([("bold", s)])


def fprint(s, bold=False):
    if bold:
        s = _bold(s)
    prompt_toolkit.print_formatted_text(s)
