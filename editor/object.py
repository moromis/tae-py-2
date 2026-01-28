from prompt_toolkit import PromptSession, choice

from editor import object_manager, room_manager
from shared.file_io import write_game_data
from shared.fprint import fprint
from shared.prompt import prompt
from shared.types.Object import Object
from shared.yes_no import yes_no


def create_object(filepath: str):
    def _create_object(session: PromptSession):
        name = prompt(session, "Room name?")
        desc = prompt(session, "Room description?", multiline=True)

        room = None
        rooms = room_manager.get_rooms()
        if len(rooms) == 0:
            fprint(
                "The object can't be placed in a room, since you haven't made any. You can associate the object with a room later if you want.",
                bold=True,
            )
        else:
            ans = yes_no(session, "Add the object to a room?")
            if ans:
                room_name = choice(
                    "Which room?", options=[(r, r) for r in rooms.keys()]
                )
                room = rooms[room_name]

        new_object = Object(name, desc, room)

        object_manager.add_object(new_object)
        write_game_data(filepath)

    return _create_object
