# returns true if "y" is typed, and false if "n" is typed
from prompt_toolkit import PromptSession
import prompt_toolkit


def yes_no(session: PromptSession, question):
    answer = prompt_toolkit.choice(question, options=[("y", "Yes"), ("n", "No")])
    if answer == "y":
        return True
    return False
