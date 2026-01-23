from prompt_toolkit import PromptSession, choice

from editor.shared.directions import DIRECTIONS
from editor.shared.get_rooms import get_rooms
from shared.prompt import prompt
from shared.types.Room import Room
from shared.write_data_json import write_data_json


def create_room(session: PromptSession):
    name = prompt(session, "Room name?")
    desc = prompt(session, "Room description?", multiline=True)
    rooms = get_rooms()
    if len(rooms) > 0:
        attached = choice(
            "Which room should this one be attached to?",
            options=[(r.name, r.name) for r in rooms],
        )
        # get_valid_directions(attached)
        direction = choice("Which direction?", options=DIRECTIONS)
        x = 0
        y = 0
    else:
        x = 0
        y = 0
    room = Room(name, desc, x, y)

    write_data_json(f"room_{room}", room.to_dict())
