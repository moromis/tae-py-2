import copy
import unittest

from core.types.Response import Response
from testing.fixtures import TEST_CHARACTER


class TestCharacter(unittest.TestCase):

    def test_to_dict(self):
        test_character = copy.deepcopy(TEST_CHARACTER)
        dict_character = test_character.to_dict()
        self.assertEqual(dict_character["name"], TEST_CHARACTER.name)
        self.assertEqual(dict_character["desc"], TEST_CHARACTER.desc)
        self.assertTrue(dict_character["is_character"])

    def test_talk(self):
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_topic = "air"
        test_response = Response("...but why is there air?", None)
        test_character.responses = {test_topic: test_response}
        res = test_character.handle_command(verb="talk", rest=[test_topic])
        self.assertNotEqual(res, False)
        self.assertEqual(res, test_response.response)
