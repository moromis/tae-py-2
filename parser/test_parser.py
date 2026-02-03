import unittest

from parser.parser import Parser
from parser.types.Verb import Verb

VERB = "hit"
ADJECTIVE = "evil"
OBJECT = "man"
INDIRECT_OBJECT = "hammer"

TEST_COMMANDS = {
    "DIRECT": f"{VERB} {OBJECT}",
    "INDIRECT": f"{VERB} {OBJECT} with {INDIRECT_OBJECT}",
    "ADJECTIVE_1": f"{VERB} {ADJECTIVE} {OBJECT}",
    "ADJECTIVE_2": f"{VERB} {ADJECTIVE} {OBJECT} with {ADJECTIVE} {INDIRECT_OBJECT}",
}


class TestParser(unittest.TestCase):
    def test_get_verb(self):
        parser = Parser()
        verb_name, verb, command = parser.get_verb([VERB, OBJECT])
        self.assertTrue(isinstance(verb, Verb))
        self.assertEqual(verb_name, VERB)
        self.assertEqual(command, [OBJECT])
