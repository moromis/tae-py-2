import unittest

from parser import parser

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
        for c in TEST_COMMANDS.values():
            verb = parser.get_verb(c)
            self.assertEqual(verb, VERB)
