from typing import Callable


from core.helpers.yes_no import yes_no
from strings import CONTINUE_ON


def confirm(f: Callable):
    res = yes_no("Are you sure?")
    if res:
        f()
    else:
        return CONTINUE_ON
