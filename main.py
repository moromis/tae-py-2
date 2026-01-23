import sys
from editor.editor import main_loop as main_editor_loop
from shared import cls, prompt
from shared.fprint import fprint
from shared.noop import noop
from shared.repl import REPL
from strings import STARTUP, WHICH_APP


def main(session):
    return WHICH_APP, True


main_structure = {
    "": main,
    WHICH_APP: {"Editor": main_editor_loop, "Player": noop, "Exit": sys.exit},
}

if __name__ == "__main__":
    cls()
    fprint(STARTUP, bold=True)
    repl = REPL(main_structure)
    repl.run()
