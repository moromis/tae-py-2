import copy
import unittest

from core.types.ObjectProperties import OBJECT_PROPERTIES
from core.types.Response import Response
from testing.fixtures import TEST_CHARACTER
from prompt_toolkit.formatted_text import FormattedText


class TestCharacter(unittest.TestCase):

    def test_to_dict(self):
        test_character = copy.deepcopy(TEST_CHARACTER)
        dict_character = test_character.to_dict()
        self.assertEqual(dict_character["name"], TEST_CHARACTER.name)
        self.assertEqual(dict_character["desc"], TEST_CHARACTER.desc)
        self.assertTrue(dict_character[OBJECT_PROPERTIES.IS_CHARACTER])

    def test_talk(self):
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_topic = "air"
        test_response = "...but why is there air?"
        test_character.responses = {test_topic: Response(test_response)}
        res = test_character.handle_command(verb="talk", rest=[test_topic])
        self.assertNotEqual(res, False)
        if isinstance(res, FormattedText):
            self.assertTrue(test_response in str(res))
        elif isinstance(res, str):
            self.assertTrue(test_response in res)
