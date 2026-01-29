import sys
from editor.editor import main_loop as main_editor_loop
from shared import cls, prompt
from shared.fprint import fprint
from shared.repl import REPL, repl_noop
from shared.types.ReplResult import ReplResult
from strings import SHUTDOWN, STARTUP, WHICH_APP


def quit():
    cls()
    fprint(SHUTDOWN, bold=True)
    sys.exit()


main_structure = {
    WHICH_APP: {"Editor": main_editor_loop, "Player": repl_noop, "Exit": quit}
}

if __name__ == "__main__":
    repl = REPL(main_structure, pins=[STARTUP])
    repl.run(WHICH_APP)
