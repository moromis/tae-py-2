from prompt_toolkit import PromptSession, choice
from editor import character_manager, room_manager
from core import fprint, prompt, yes_no
from core.types.ReplResult import ReplResult
from core.types.Character import Character
from core.file_io import write_game_data


def create_character():
    name = prompt("Character name?")
    desc = prompt("Character description?", multiline=True)
    room = None
    rooms = room_manager.get_rooms()
    if len(rooms) == 0:
        fprint(
            "The character can't be placed in a room, since you haven't made any. You can associate the character with a room later if you want.",
            bold=True,
        )
    else:
        ans = yes_no("Add the character to a room?")
        if ans:
            room_name = choice("Which room?", options=[(r, r) for r in rooms.keys()])
            room = rooms[room_name]
    responses = character_responses()

    new_character = Character(name, desc, responses)

    character_manager.add_character(new_character)
    if room:
        room_manager.add_character_to_room(new_character.name, room.name)
    write_game_data()

    return ReplResult(replace=True)


def get_condition():
    return "test-condition"


def character_responses():
    responses = dict()
    ans = yes_no("Add a response to a question for this character?")
    while ans:
        topic = prompt(
            'What should the response be in regards to? (i.e., if asked via "talk to {{character}} about ____)',
        )
        response = prompt("What should the character's response be?")
        dependent = yes_no("Is this response dependent on a condition?")
        condition = None
        if dependent:
            condition = get_condition()
        responses[topic] = {"response": response, "condition": condition}
        ans = yes_no("Add another response?")

    return responses


# TODO: change to choice, allow editing of characters
def view_characters():
    characters = character_manager.get_characters()
    for c in characters.keys():
        fprint(f"- {c}")
    input("Press any key to continue...")
