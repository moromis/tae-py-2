import sys
from editor.editor import main_loop as main_editor_loop
from shared import cls, prompt
from shared.fprint import fprint
from shared.repl import REPL, repl_noop
from shared.types.ReplResult import ReplResult
from strings import STARTUP, WHICH_APP


def main():
    return ReplResult(path=WHICH_APP, clear=True)


main_structure = {
    "": main,
    WHICH_APP: {"Editor": main_editor_loop, "Player": repl_noop, "Exit": sys.exit},
}

if __name__ == "__main__":
    repl = REPL(main_structure, pins=[STARTUP])
    repl.run()
