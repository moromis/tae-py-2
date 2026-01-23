import prompt_toolkit

from strings import PROMPT_CHAR


def prompt(
    session: prompt_toolkit.PromptSession, s: str = "", multiline=False, **kwargs
) -> str:
    prompt_toolkit.print_formatted_text(s)
    if multiline:
        prompt_toolkit.print_formatted_text(
            "(Hint: multiline input -- press Esc then Enter once you're done)"
        )
    print("\n")
    res = session.prompt(multiline=multiline, **kwargs)
    print("\n")
    return res
