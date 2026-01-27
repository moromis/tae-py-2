from prompt_toolkit import PromptSession, print_formatted_text
import prompt_toolkit
from const import STOP_CODE
from shared import cls, get_from_path
from shared.go_back_path import go_back_path
from shared.prompt import prompt
from strings import PROMPT_CHAR


class REPL:
    def __init__(self, structure) -> None:
        session = PromptSession(message=PROMPT_CHAR)
        self.structure = structure
        self.session = session
        self.keep_running = True

    def run(self):
        # location in structure
        location = ""

        cls()

        while self.keep_running:
            try:
                current = get_from_path(location, self.structure)
                next = ""
                back = False
                res = None
                if current is STOP_CODE:
                    self.stop()
                    break
                if isinstance(current, str):
                    res = prompt(self.session, current)
                elif callable(current):
                    res = current(self.session)
                elif isinstance(current, dict):
                    res = self._prompt_options(location, current)
                if not res:
                    back = True
                elif isinstance(res, tuple):
                    next = str(res[0])
                    back = bool(res[1])
                else:
                    next = str(res)
                if back and location != "":
                    location = go_back_path(location)
                elif not back:
                    location = location + "." + str(next)
                else:
                    location = str(next)
            except (EOFError, KeyboardInterrupt):
                self.stop()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                self.stop()
                break

    def stop(self):
        self.keep_running = False

    def _prompt_options(self, message: str, options: dict) -> str:
        cls()
        labeled_options = [(o, o) for o in list(options.keys())]
        chosen = prompt_toolkit.choice(
            message, options=labeled_options, mouse_support=True, enable_interrupt=True
        )
        cls()
        return chosen
