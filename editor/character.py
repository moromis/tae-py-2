from prompt_toolkit import PromptSession
import prompt_toolkit
from editor.shared.get_rooms import get_rooms
from shared.cls import cls
from shared.fprint import fprint
from shared.prompt import prompt
from shared.types.Character import Character
from shared.write_data_json import write_data_json
from shared.yes_no import yes_no
from prompt_toolkit.formatted_text import FormattedText


def create_character(session: PromptSession):
    name = prompt(session, "Character name?")
    desc = prompt(session, "Character description?", multiline=True)
    room = None
    rooms = get_rooms()
    if len(rooms) == 0:
        fprint(
            "The character can't be placed in a room, since you haven't made any. You can associate the character with a room later if you want.",
            bold=True,
        )
    else:
        ans = yes_no(session, "Add the character to a room?")
        if ans:
            # room = get_rooms()
            room = None
    responses = character_responses(session)

    character = Character(name, desc, room, responses)

    cls()
    fprint(character)

    write_data_json(f"character_{name}", character)


def get_condition():
    return "test-condition"


def character_responses(session):
    responses = dict()
    ans = yes_no(session, "Add a response to a question for this character?")
    while ans:
        topic = prompt(
            session,
            'What should the response be in regards to? (i.e., if asked via "talk to {{character}} about ____)',
        )
        response = prompt(session, "What should the character's response be?")
        dependent = yes_no(session, "Is this response dependent on a condition?")
        condition = None
        if dependent:
            condition = get_condition()
        responses[topic] = {"response": response, "condition": condition}
        ans = yes_no(session, "Add another response?")

    return responses
