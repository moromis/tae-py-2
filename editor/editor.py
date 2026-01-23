from editor.character import create_character
from editor.room import create_room
from shared.noop import noop
from shared.repl import REPL

MAIN = "What do you want to do?"


def main_menu(session):
    return MAIN, True


editor_structure = {
    "": main_menu,
    MAIN: {
        "Create a character": create_character,
        "Create a room": create_room,
        "Create an object": noop,
    },
}


# main loop
def main_loop(session):
    repl = REPL(editor_structure)
    repl.run()
