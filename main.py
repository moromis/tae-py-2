from argparse import ArgumentParser
import sys
from core.gamestate import load_game
from editor.editor import main_loop as main_editor_loop
from core import cls, fprint, logger
from core.repl import REPL
from player.player import PLAY_GAME, PLAYER_MAIN, Player, play
from strings import SHUTDOWN, STARTUP, TAE, TAE_DESC, TAE_EPILOG, WHICH_APP

PLAYER = "player"
EDITOR = "editor"
MAIN = "main"
START_PLAYING = [PLAYER_MAIN, PLAY_GAME]
PROGRAMS = {
    PLAYER: [WHICH_APP, PLAYER.capitalize()],
    EDITOR: [WHICH_APP, EDITOR.capitalize()],
    MAIN: [WHICH_APP],
}


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
    parser = ArgumentParser(prog=TAE, description=TAE_DESC, epilog=TAE_EPILOG)
    parser.add_argument("-p", "--program", default=MAIN, choices=PROGRAMS.keys())
    parser.add_argument("-f", "--filename")
    parser.add_argument(
        "-s", "--start", help="overrides --program", action="store_true"
    )
    parser.add_argument("-debug", "--debug", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_false")

    args = parser.parse_args()
    logger.log(str(args))

    if args.filename:
        load_game(args.filename)

    if args.start:
        play()
    else:
        repl = REPL(get_main_structure(), pins=[STARTUP])
        repl.run(START_PLAYING if args.start else PROGRAMS[args.program])


if __name__ == "__main__":
    main()
