from prompt_toolkit import PromptSession, choice

from editor import room_manager
from editor.shared.directions import DIRECTIONS
from shared.file_io import write_data_json, write_game_data
from shared.prompt import prompt
from shared.types.Room import Room
from prompt_toolkit.shortcuts import checkboxlist_dialog


def create_room(filepath: str):
    def _create_room(session: PromptSession):
        name = prompt(session, "Room name?")
        desc = prompt(session, "Room description?", multiline=True)
        rooms = room_manager.get_rooms()
        if len(rooms) > 0:
            attached = checkboxlist_dialog(
                title="Add room attachments",
                text="Which room(s) should this one be attached to?",
                values=[(r, r) for r in rooms.keys()],
            ).run()
            # attached = choice(
            #     "Which room should this one be attached to?",
            #     options=[(r.name, r.name) for r in rooms],
            # )
            # get_valid_directions(attached)
            direction = choice("Which direction?", options=DIRECTIONS)
            x = 0
            y = 0
        else:
            x = 0
            y = 0

        new_room = Room(name, desc, x, y)
        room_manager.add_room(new_room)

        write_game_data(filepath)

    return _create_room
