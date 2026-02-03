from const import STOP_CODE
from core import logger
from core.gamestate import load_game
from core.helpers.cls import cls
from core.helpers.fprint import fprint
from core.helpers.newline import newline
from core.helpers.prompt import prompt
from core.managers.room_manager import get_entrance_room
from core.repl import REPL
from parser.parser import Parser
from strings import (
    GAME_LOAD_FAILED,
    GAME_LOADED,
    GAME_SAVED,
    GO_BACK,
    PROMPT_CHAR,
    WHAT_TO_DO,
)

MAIN = "Welcome to the TAE Player"
LOAD_GAME = "Load a game"
LOAD_GAME_DIFFERENT = "Load a different game"
PLAY_GAME = "Play the game"


class Player:
    def __init__(self) -> None:
        self.loaded = False
        self.player_structure = {MAIN: {LOAD_GAME: self.load_game, GO_BACK: STOP_CODE}}
        self.player_structure_loaded = {
            MAIN: {
                PLAY_GAME: self.play_game,
                LOAD_GAME_DIFFERENT: self.load_game,
                GO_BACK: STOP_CODE,
            }
        }
        self.repl = REPL(self.player_structure)
        self.parser = Parser()

    def save_game(self):
        return GAME_SAVED

    def load_game(self):
        if load_game():
            fprint(GAME_LOADED)
            self.loaded = True
            self.repl.stop()
            self.repl = REPL(self.player_structure_loaded)
            self.repl.run(MAIN)
        else:
            fprint(GAME_LOAD_FAILED)

    def play_game(self):
        room = get_entrance_room()
        cls()
        while True:
            fprint(room.name, bold=True)
            fprint(room.desc)
            newline()
            if len(room.objects):
                fprint("Here there is:")
                for o in room.objects:
                    fprint(o)
            newline()
            if len(room.characters):
                fprint("People here:")
                for c in room.characters:
                    fprint(c)
            newline()
            command = prompt(WHAT_TO_DO)
            cls()
            fprint(self.parser.parse(command))
            newline()

    def run(self):
        self.repl.run(MAIN)
