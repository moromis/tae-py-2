import unittest

from core.managers import room_manager
from parser import inventory
from parser.verbs.drop import drop
from strings import DONT_HAVE_THAT, FLOATING_IN_SPACE
from testing.fixtures import TEST_OBJECT, TEST_ROOM

room = TEST_ROOM
obj = TEST_OBJECT


class TestDrop(unittest.TestCase):
    def tearDown(self) -> None:
        room_manager.reset()
        inventory.reset()
        return super().tearDown()

    def test_drop_no_room(self):
        res = drop(object=obj)
        self.assertEqual(res, FLOATING_IN_SPACE)

    def test_drop_no_item(self):
        room_manager.add_room(room)
        res = drop(object=obj)
        self.assertEqual(res, DONT_HAVE_THAT)

    def test_drop_with_item(self):
        room_manager.add_room(room)
        inventory.add_to_inventory(obj)
        res = drop(object=obj)
        self.assertNotEqual(res, DONT_HAVE_THAT)
