from typing import Callable


from core.helpers.yes_no import yes_no
from strings import CONTINUE_ON


def confirm(f: Callable, message="Are you sure?"):
    res = yes_no(message)
    if res:
        f()
    else:
        return CONTINUE_ON
