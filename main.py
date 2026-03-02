import sys
from core.args_parser import ArgsParser
from core.gamestate import load_game
from editor.editor import main_loop as main_editor_loop
from core import cls, fprint
from core.repl import REPL
from main_structure import EDITOR, PLAYER, PROGRAMS, START_PLAYING
from player.player import Player, play
from strings import SHUTDOWN, STARTUP, WHICH_APP


def quit():
    cls()
    fprint(SHUTDOWN, bold=True)
    sys.exit()


def get_main_structure():
    player = Player()
    return {
        WHICH_APP: {
            EDITOR.capitalize(): main_editor_loop,
            PLAYER.capitalize(): player.run,
            "Exit": quit,
        }
    }


def main():
    args = ArgsParser.parse_args()

    if args.filename:
        load_game(args.filename)

    if args.start:
        play()
    else:
        repl = REPL(get_main_structure(), pins=[STARTUP], type="Main")
        repl.run(START_PLAYING if args.start else PROGRAMS[args.program])


if __name__ == "__main__":
    main()
