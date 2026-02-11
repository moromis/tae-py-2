import copy
import unittest

from core.managers.object_manager import Object_Manager
from core.types.Character import Character
from core.types.Response import Response
from testing.fixtures import TEST_CHARACTER


class TestObjectManager(unittest.TestCase):
    def testSetFromJsonSetsCharacter(self):
        test_char = copy.deepcopy(TEST_CHARACTER)
        Object_Manager.set_from_json({test_char.name: test_char.to_dict()})
        res = Object_Manager.get_all_list()
        self.assertEqual(len(res), 1)
        self.assertIsInstance(res[0], Character)

    def testSetFromJsonSetsCharacterResponses(self):
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_character_json = test_character.to_dict()
        test_topic = "air"
        test_response = "...but why is there air?"
        test_character_json["responses"] = {
            test_topic: {"response": test_response, "condition": None}
        }
        Object_Manager.set_from_json({test_character.name: test_character_json})
        res = Object_Manager.get_all_list()
        if isinstance(res[0], Character):
            self.assertEqual(len(res[0].responses), 1)
            self.assertIsInstance(res[0].responses[test_topic], Response)
