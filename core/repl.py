import prompt_toolkit
from const import GO_BACK_CODE, STOP_CODE
from shared import cls
from shared.fprint import fprint
from shared.types.ReplResult import ReplResult
from strings import BASE_PATH

ResultType = ReplResult | object | str | None


def repl_noop():
    return ReplResult(clear=True)


class REPLRouter:
    def __init__(self, structure) -> None:
        self.history_stack = [BASE_PATH]
        self.structure = structure

    def peek(self, idx=1):
        return self.history_stack[-idx]

    def push(self, new_index):
        self.history_stack.append(new_index)

    def pop(self, num_times=1):
        popped = []
        for n in range(num_times):
            popped.append(self.history_stack.pop())

    def clear(self):
        self.history_stack = []

    def traverse_history(self):
        current_pointer = self.structure
        for index in self.history_stack:
            current_pointer = current_pointer[index]
        return current_pointer


class REPL:
    def __init__(self, structure, pins=[]) -> None:
        self.router = REPLRouter(structure)
        self.structure = structure
        self.running = True
        self.pinned = pins

    # for printing messages after a cls
    # think of it like toasts. Remove from the end
    # of the stack as needed/once done presenting the message
    def print_pinned(self):
        for p in self.pinned:
            if callable(p):
                p()
            else:
                fprint(p, bold=True)

    def run(self, entrypoint=BASE_PATH):

        if entrypoint:
            self.router.clear()
            self.router.push(entrypoint)

        cls()

        while self.running:
            self.print_pinned()
            try:
                pointer = self.router.traverse_history()

                result: ResultType = None

                if pointer is STOP_CODE:
                    self.stop()
                    break
                elif pointer is GO_BACK_CODE:
                    self.router.pop(2)
                    continue
                elif callable(pointer):
                    result = pointer()
                elif isinstance(pointer, dict):
                    result = self._prompt_options(self.router.peek(1), pointer)

                if isinstance(result, ReplResult):
                    if result.clear:
                        self.router.clear()
                    elif result.replace:
                        self.router.pop()

                    if result.path:
                        self.router.push(result.path)
                else:
                    self.router.pop()
            except (EOFError, KeyboardInterrupt):
                self.stop()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                self.stop()
                break

    def stop(self):
        self.running = False

    def _prompt_options(self, message: str, options: dict) -> ReplResult:
        cls()
        self.print_pinned()

        labeled_options = [(o, o) for o in list(options.keys())]

        # get the user's choice
        try:
            chosen = prompt_toolkit.choice(
                message,
                options=labeled_options,
                mouse_support=True,
                enable_interrupt=True,
            )
        except (EOFError, KeyboardInterrupt):
            return ReplResult(path=BASE_PATH, replace=True)
        cls()
        return ReplResult(path=chosen)
