import copy
import unittest

from core.managers import room_manager
from core.managers.object_manager import Object_Manager
from parser.verbs.look import look
from strings import DONT_SEE_HERE, FLOATING_IN_SPACE
from testing.fixtures import TEST_OBJECT, TEST_ROOM


class TestLook(unittest.TestCase):
    def setUp(self) -> None:
        Object_Manager.reset()
        room_manager.reset()
        return super().setUp()

    def tearDown(self) -> None:
        Object_Manager.reset()
        room_manager.reset()
        return super().tearDown()

    def test_look_no_obj_no_room(self):
        res = look()
        self.assertEqual(res, FLOATING_IN_SPACE)

    def test_look_no_obj(self):
        room_manager.add_room(TEST_ROOM)
        res = look()
        self.assertEqual(res, TEST_ROOM.desc)

    def test_look_obj_in_room(self):
        test_room = copy.deepcopy(TEST_ROOM)
        test_room.objects = [TEST_OBJECT.name]
        room_manager.add_room(test_room)
        res = look(object=TEST_OBJECT)
        self.assertEqual(res, TEST_OBJECT.desc)

    def test_look_obj_not_in_current_room(self):
        test_room = copy.deepcopy(TEST_ROOM)
        test_room.objects = []
        # testing the test
        self.assertEqual(len(room_manager.get_rooms()), 0)
        room_manager.add_room(test_room)
        res = look(object=TEST_OBJECT)
        self.assertEqual(res, DONT_SEE_HERE)
