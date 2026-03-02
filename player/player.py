from const import STOP_CODE
from core.gamestate import load_game
from core.helpers.cls import cls
from core.helpers.fprint import fprint
from core.helpers.newline import newline
from core.helpers.prompt import prompt
from core.managers.meta import meta_manager
from core.managers.room_manager import get_entrance_room
from core.repl import REPL
from parser.parser import Parser
from player.history import History
from player.player_structure import (
    LOAD_GAME,
    LOAD_GAME_DIFFERENT,
    PLAY_GAME,
    WELCOME_TO_PLAYER,
)
from strings import (
    GAME_LOAD_FAILED,
    GAME_LOADED,
    GAME_SAVED,
    GO_BACK,
    NO_GAME_LOADED,
    NONE,
)


class Player:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.loaded = meta_manager.get_meta_by_key(meta_manager.META_KEYS.TITLE) != NONE
        self.new_room = True
        self.player_structure = {
            WELCOME_TO_PLAYER: {LOAD_GAME: self.load_game, GO_BACK: STOP_CODE}
        }
        self.player_structure_loaded = {
            WELCOME_TO_PLAYER: {
                PLAY_GAME: self.play_game,
                LOAD_GAME_DIFFERENT: self.load_game,
                GO_BACK: STOP_CODE,
            }
        }
        self.repl = REPL(
            self.player_structure_loaded if self.loaded else self.player_structure,
            type="Player",
        )
        self.parser = Parser()

    def add_to_history(self, command: str) -> None:
        History.push_history(command)

    def get_history(self):
        return History.get_history()

    def save_game(self):
        return GAME_SAVED

    def load_game(self):
        if load_game():
            fprint(GAME_LOADED)
            self.loaded = True
            self.repl.stop()
            self.repl = REPL(
                self.player_structure_loaded,
                type="Player Load Game",
            )
            self.repl.run(WELCOME_TO_PLAYER)
        else:
            fprint(GAME_LOAD_FAILED)

    def play_game(self):
        self.keep_playing = True
        room = get_entrance_room()
        cls()
        while self.keep_playing:
            if self.new_room and room:
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
                self.new_room = False
                newline()
            command = prompt()
            cls()
            res = self.parser.parse(command)
            if res and res != STOP_CODE:
                fprint(res)
            else:
                self.keep_playing = False

            newline()

            # add the command to history
            self.add_to_history(command)

        # done playing, make sure the player is reset to play again
        self.reset()

    def run(self, entrypoint: str | list[str] = WELCOME_TO_PLAYER):
        self.repl.run(entrypoint)


# assuming we already have a game loaded, skip the loading and play the game
def play():
    if meta_manager.get_meta_by_key(meta_manager.META_KEYS.TITLE) != NONE:
        Player().play_game()
    else:
        return NO_GAME_LOADED
