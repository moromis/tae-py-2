import prompt_toolkit

from strings import PROMPT_CHAR

session = None


def prompt(s: str = "", multiline=False, **kwargs) -> str:
    global session
    if not session:
        session = prompt_toolkit.PromptSession(message=PROMPT_CHAR)
    prompt_toolkit.print_formatted_text(s)
    if multiline:
        prompt_toolkit.print_formatted_text(
            "(Hint: multiline input -- press Esc then Enter once you're done)"
        )
    print("\n")
    res = session.prompt(multiline=multiline, **kwargs)
    print("\n")
    return res
