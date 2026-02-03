from core.types.Object import Object
from core.types.Room import Room

# Objects
TEST_ROOM = Room("test", "test-desc")
TEST_OBJECT = Object("man", "an okay guy I guess... for a test fixture", "cool")

# Parser/grammar
TEST_VERB = "hit"
TEST_I_OBJ = Object("hammer", "goes whackity", "evil")

TEST_COMMANDS = {
    "DIRECT": f"{TEST_VERB} {TEST_OBJECT.name}",
    "INDIRECT": f"{TEST_VERB} {TEST_OBJECT.name} with {TEST_I_OBJ.name}",
    "ADJECTIVE_1": f"{TEST_VERB} {TEST_OBJECT.adjective} {TEST_OBJECT.name}",
    "ADJECTIVE_2": f"{TEST_VERB} {TEST_OBJECT.adjective} {TEST_OBJECT.name} with {TEST_I_OBJ.adjective} {TEST_I_OBJ.name}",
}
