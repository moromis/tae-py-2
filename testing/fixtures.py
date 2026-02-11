from core.types.Character import Character
from core.types.Object import Object
from core.types.Room import Room
from strings import DEFAULT_VERB_RESPONSE, WHAT_ARE_YOU_TALKING_ABOUT

# Objects
TEST_ROOM = Room("test", "test-desc")
TEST_OBJECT = Object("nail", "ready to get hammered sir", "shiny")
TEST_CHARACTER = Character("man", "an okay guy I guess... for a test fixture", "hype")

# Parser/grammar
TEST_VERB = "hit"


def TEST_HANDLER(**kwargs):
    object = kwargs.get("object", None)
    if object:
        return f"You cleave the {object.name} in twain!"
    else:
        return WHAT_ARE_YOU_TALKING_ABOUT


TEST_I_OBJ = Object(
    "hammer",
    "goes whackity",
    "evil",
    handlers={TEST_VERB: TEST_HANDLER},
)

TEST_COMMANDS = {
    "DIRECT": f"{TEST_VERB} {TEST_OBJECT.name}",
    "INDIRECT": f"{TEST_VERB} {TEST_OBJECT.name} with {TEST_I_OBJ.name}",
    "ADJECTIVE_1": f"{TEST_VERB} {TEST_OBJECT.adjective} {TEST_OBJECT.name}",
    "ADJECTIVE_2": f"{TEST_VERB} {TEST_OBJECT.adjective} {TEST_OBJECT.name} with {TEST_I_OBJ.adjective} {TEST_I_OBJ.name}",
}

OBJECT_RESPONSE = lambda o: f"You do the thing with the {o}"
INDIRECT_RESPONSE = lambda o, i: f"You do the action on the {o} with the {i}"


def TEST_VERB_HANDLER(**kwargs):
    obj = kwargs.get("object")
    i_obj = kwargs.get("indirect_object")
    if obj and i_obj:
        return INDIRECT_RESPONSE(obj.name, i_obj.name)
    elif obj:
        return OBJECT_RESPONSE(obj.name)
    return DEFAULT_VERB_RESPONSE
