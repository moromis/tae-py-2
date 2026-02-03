from const import GO_BACK_CODE, STOP_CODE
from core.gamestate import load_game, unload_game
from core.helpers.fprint import fprint
from editor.character import create_character, view_characters
from editor.object import create_object
from editor.room import create_room
from core import prompt
from core.managers.meta_manager import set_meta_by_key, META_KEYS, print_title
from core.file_io import write_game_data
from core.repl import REPL, repl_noop
from core.types.ReplResult import ReplResult
from player import player
from strings import GO_BACK
import os

GAME = "Start a new game or load an existing one?"
MAIN = "What do you want to do?"
CREATE = "Create"
VIEW_EDIT = "View/Edit"
filepath = ""
file_loaded = False


def new_game():
    title: str = prompt("What's the new game's title?")
    set_meta_by_key(META_KEYS.TITLE, title)

    fprint("\n Select the folder to place the game's files in")
    filename = title.lower().replace(" ", "_")
    # folder = select_folder()
    # TODO: revert, uncomment above, delete below
    folder = "/Users/momo/Projects/tae-2026-test-games"
    fprint(filename)
    fprint(folder)
    global filepath
    filepath = os.path.join(folder, filename)
    set_meta_by_key(META_KEYS.FILEPATH, filepath)
    # TODO: revert
    # input("Press Enter to continue...")
    write_game_data()
    return ReplResult(path=MAIN, clear=True)


def change_game_title():
    new_title = prompt("What is the new game title?")
    set_meta_by_key(META_KEYS.TITLE, new_title)
    write_game_data()
    return ReplResult(replace=True)


def exit_main():
    unload_game()
    return ReplResult(path=GAME, clear=True)


def _load_game():
    load_game()
    return ReplResult(path=MAIN, clear=True)


editor_structure = {
    GAME: {
        "New game": new_game,
        "Load game": _load_game,
        GO_BACK: STOP_CODE,
    },
    MAIN: {
        CREATE: {
            "Create a character": create_character,
            "Create a room": create_room,
            "Create an object": create_object,
            GO_BACK: GO_BACK_CODE,
        },
        VIEW_EDIT: {
            "View/edit characters": view_characters,
            "View/edit rooms": repl_noop,
            "View/edit objects": repl_noop,
            GO_BACK: GO_BACK_CODE,
        },
        "Play/test": player.play,
        "Change game title": change_game_title,
        GO_BACK: exit_main,
    },
}


# main loop
def main_loop():
    repl = REPL(editor_structure, pins=[print_title])
    repl.run(GAME)
