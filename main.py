import sys
from editor.editor import main_loop as main_editor_loop
from core import cls, fprint
from core.repl import REPL
from player.player import Player
from strings import SHUTDOWN, STARTUP, WHICH_APP

debug = False


def quit():
    cls()
    fprint(SHUTDOWN, bold=True)
    sys.exit()


def get_main_structure():
    player = Player()
    return {WHICH_APP: {"Editor": main_editor_loop, "Player": player.run, "Exit": quit}}


if __name__ == "__main__":
    if sys.argv and len(sys.argv) > 2:
        debug = bool(sys.argv[2])
        print(f"debug: {debug}")
    else:
        print("No arguments provided (except the script name).")

    repl = REPL(get_main_structure(), pins=[STARTUP])
    repl.run(WHICH_APP)
