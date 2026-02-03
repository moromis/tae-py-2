import unittest

from parser.parser import Parser
from parser.types.Verb import Verb
from testing.fixtures import TEST_OBJECT, TEST_VERB


class TestParser(unittest.TestCase):
    def test_get_verb(self):
        parser = Parser()
        verb_name, verb, command = parser.get_verb(
            [TEST_VERB, "test", "asdf", TEST_OBJECT.name]
        )
        self.assertTrue(isinstance(verb, Verb))
        self.assertEqual(verb_name, TEST_VERB)
        self.assertEqual(len(command), 3)
