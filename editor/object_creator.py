from prompt_toolkit import choice

from core.helpers.yes_no import yes_no
from core.managers import room_manager
from core import ReplResult, Object
from core.file_io import write_game_data
from core import fprint, prompt
from core.managers.object_manager import Object_Manager
from prompt_toolkit.shortcuts import checkboxlist_dialog

from core.types.ObjectProperties import OBJECT_PROPERTIES


# TODO: get rid of character creator and instead make this a workflow, and change the steps depending on what
# type of object we're creating, such as a character
def create_object():
    name = prompt("Object name?")
    adjective = ""
    split_name = name.split(" ")
    if len(split_name) == 2:
        set_adj = yes_no(f"Is {split_name[0]} an adjective for this object?")
        if set_adj:
            adjective = split_name[0]
            name = " ".join(split_name[1:])
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

    properties = checkboxlist_dialog(
        title="Add object properties",
        text="What properties should this object have?",
        values=[(p, p.value) for p in OBJECT_PROPERTIES],
    ).run()

    properties = {p: False for p in properties}

    new_object = Object(name, desc, adjective, properties=properties)

    Object_Manager.add(new_object)
    if room:
        room_manager.add_object_to_room(new_object.name, room.name)
    write_game_data()

    return ReplResult(replace=True)
