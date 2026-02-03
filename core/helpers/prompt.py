import prompt_toolkit

from core import logger
from core.helpers.fprint import fprint
from strings import PROMPT_CHAR

session = None


def prompt(s: str = "", multiline=False, **kwargs) -> str:
    global session
    if not session:
        session = prompt_toolkit.PromptSession(message=PROMPT_CHAR)
    fprint(s)
    if multiline:
        fprint("(Hint: multiline input -- press Esc then Enter once you're done)")
    fprint("\n", skip_logging=True)
    res = session.prompt(multiline=multiline, **kwargs)
    logger.log(f"{PROMPT_CHAR}{res}")
    fprint("\n", skip_logging=True)
    return res
