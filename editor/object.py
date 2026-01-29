from prompt_toolkit import PromptSession, choice

from editor import object_manager, room_manager
from shared import ReplResult, Object
from shared.file_io import write_game_data
from shared.fprint import fprint
from shared.prompt import prompt
from shared.yes_no import yes_no


def create_object():
    name = prompt("Object name?")
    desc = prompt("Object description?", multiline=True)

    room = None
    rooms = room_manager.get_rooms()
    if len(rooms) == 0:
        fprint(
            "The object can't be placed in a room, since you haven't made any. You can associate the object with a room later if you want.",
            bold=True,
        )
    else:
        ans = yes_no("Add the object to a room?")
        if ans:
            room_name = choice("Which room?", options=[(r, r) for r in rooms.keys()])
            room = rooms[room_name]

    new_object = Object(name, desc)

    object_manager.add_object(new_object)
    if room:
        room_manager.add_object_to_room(new_object.name, room.name)
    write_game_data()

    return ReplResult(replace=True)
