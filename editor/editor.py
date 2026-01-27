from prompt_toolkit import PromptSession
from const import STOP_CODE
from editor.character import create_character
from editor.room import create_room
from shared import file_io
from shared.file_io import select_folder, write_game_data
from shared.noop import noop
from shared.prompt import prompt
from shared.repl import REPL
from strings import GO_BACK
import os

GAME = "Start a new game or load an existing one?"
MAIN = "What do you want to do?"
filepath = ""


def main_menu(session):
    return GAME, True


def new_game(session: PromptSession):
    # filepath = file_io.select_file()
    title: str = prompt(session, "What's the new game's title?")
    print("\n Select the folder to place the game's files in")
    filename = title.lower().replace(" ", "_")
    folder = select_folder()
    print(filename, folder)
    filepath = os.path.join(folder, filename)
    input("Press Enter to continue...")
    write_game_data(filepath)
    return MAIN, True
    # print(filepath)


editor_structure = {
    "": main_menu,
    GAME: {"New game": new_game, "Load game": noop},
    MAIN: {
        "Create a character": create_character(filepath),
        "Create a room": create_room(filepath),
        "Create an object": noop,
        GO_BACK: STOP_CODE,
    },
}


# main loop
def main_loop(session: PromptSession):
    repl = REPL(editor_structure)
    repl.run()
