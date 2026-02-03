import unittest

from core.types.Object import Object

TEST_NAME = "test"
TEST_DESC = "test-desc"


class TestObject(unittest.TestCase):

    def test_to_dict(self):
        test_object = Object(name=TEST_NAME, desc=TEST_DESC)
        dict_object = test_object.to_dict()
        self.assertEqual(dict_object["name"], TEST_NAME)
        self.assertEqual(dict_object["desc"], TEST_DESC)
        self.assertFalse(dict_object["is_character"])
