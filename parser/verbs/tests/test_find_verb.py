import unittest

from parser.types.Verb import Verb
from parser.verbs.verbs import VERBS, find_verb
from testing.fixtures import TEST_OBJECT, TEST_VERB

v = "hit"


class TestFindVerb(unittest.TestCase):
    def test_find_verb(self):
        verb_name, verb = find_verb(v)
        self.assertTrue(isinstance(verb, Verb))
        self.assertEqual(verb_name, v)

    def test_find_verb_by_synonym(self):
        test_verb = VERBS[v].synonyms[0]
        verb_name, verb = find_verb(test_verb)
        self.assertTrue(isinstance(verb, Verb))
        self.assertEqual(verb_name, v)

    def test_find_verb_not_found(self):
        verb_name, verb = find_verb("gobblidyagoaskdity")
        self.assertTrue(isinstance(verb, Verb))
        self.assertTrue(isinstance(verb_name, str))
        self.assertNotEqual(verb_name, v)
