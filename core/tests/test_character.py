import unittest

from core.types.Character import Character

TEST_NAME = "test"
TEST_DESC = "test-desc"


class TestCharacter(unittest.TestCase):

    def test_to_dict(self):
        test_character = Character(name=TEST_NAME, desc=TEST_DESC)
        dict_character = test_character.to_dict()
        self.assertEqual(dict_character["name"], TEST_NAME)
        self.assertEqual(dict_character["desc"], TEST_DESC)
        self.assertTrue(dict_character["is_character"])
