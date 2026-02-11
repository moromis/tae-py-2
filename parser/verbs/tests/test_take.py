import unittest
from core.managers import room_manager
from parser import inventory
from parser.verbs.take import take
from strings import DONT_SEE_HERE, FLOATING_IN_SPACE
from testing.fixtures import TEST_OBJECT, TEST_ROOM


room = TEST_ROOM
obj = TEST_OBJECT


class TestTake(unittest.TestCase):
    def setUp(self) -> None:
        room_manager.reset()
        inventory.reset()
        room.objects = []
        return super().setUp()

    def tearDown(self) -> None:
        room_manager.reset()
        inventory.reset()
        room.objects = []
        return super().tearDown()

    def test_take_no_room(self):
        res = take(object=obj)
        self.assertEqual(res, FLOATING_IN_SPACE)

    def test_take_no_object(self):
        room_manager.add_room(room)
        res = take(object=obj)
        self.assertEqual(res, DONT_SEE_HERE)

    def test_take_with_object(self):
        room_manager.add_room(room)
        room_manager.add_object_to_room(obj.name, room.name)
        res = take(object=obj)
        self.assertIn(obj.name, res)
        self.assertTrue(inventory.has(obj.name))
        self.assertIsNone(room_manager.get_object_from_room(obj.name, room.name))
