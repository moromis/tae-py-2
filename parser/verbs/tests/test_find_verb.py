import unittest

from parser.types.Verb import Verb
from parser.verbs.verbs import VERBS, find_verb
from testing.fixtures import TEST_VERB


class TestFindVerb(unittest.TestCase):
    def test_find_verb(self):
        res = find_verb(TEST_VERB)
        if res:
            verb_name, verb = res
            self.assertTrue(isinstance(verb, Verb))
            self.assertEqual(verb_name, TEST_VERB)

    def test_find_verb_by_synonym(self):
        test_verb = VERBS[TEST_VERB].synonyms[0]
        res = find_verb(test_verb)
        if res:
            verb_name, verb = res
            self.assertTrue(isinstance(verb, Verb))
            self.assertEqual(verb_name, TEST_VERB)

    def test_find_verb_not_found(self):
        res = find_verb("gobblidyagoaskdity")
        if res:
            verb_name, verb = res
            self.assertTrue(isinstance(verb, Verb))
            self.assertTrue(isinstance(verb_name, str))
            self.assertNotEqual(verb_name, TEST_VERB)
