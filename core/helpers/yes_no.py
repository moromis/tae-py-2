# returns true if "y" is typed, and false if "n" is typed
from prompt_toolkit import PromptSession
import prompt_toolkit

from core import logger
from strings import PROMPT_CHAR


def yes_no(question):
    answer = prompt_toolkit.choice(question, options=[("y", "Yes"), ("n", "No")])
    logger.log(f"{PROMPT_CHAR}{answer}")
    if answer == "y":
        return True
    return False
