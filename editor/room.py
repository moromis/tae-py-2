from prompt_toolkit import choice

from core.managers import room_manager
from editor.shared.directions import DIRECTIONS
from core import ReplResult, Room, prompt
from core.file_io import write_game_data
from prompt_toolkit.shortcuts import checkboxlist_dialog


def create_room():
    name = prompt("Room name?")
    desc = prompt("Room description?", multiline=True)
    rooms = room_manager.get_rooms()
    adjacencies = {}
    if len(rooms) > 0:
        adjacent_rooms = checkboxlist_dialog(
            title="Add room attachments",
            text="Which room(s) should this one be attached to?",
            values=[(r, r) for r in rooms.keys() if r != name],
        ).run()
        # attached = choice(
        #     "Which room should this one be attached to?",
        #     options=[(r.name, r.name) for r in rooms],
        # )
        # get_valid_directions(attached)
        if len(adjacent_rooms):
            direction_choices = DIRECTIONS
            for ar in adjacent_rooms:
                direction = choice("Which direction?", options=direction_choices)
                adjacencies[direction] = ar
                # drop the chosen direction as a choice
                direction_choices = [d for d in direction_choices if d[0] != direction]
                if len(direction_choices) == 0:
                    break

    new_room = Room(name, desc, adjacencies)
    room_manager.add_room(new_room)

    write_game_data()

    return ReplResult(replace=True)
