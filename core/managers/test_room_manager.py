import unittest

from core.managers import room_manager
from core.types.Room import Room
from testing.fixtures import TEST_ROOM


class TestRoomManager(unittest.TestCase):
    def test_add_room(self):
        room_manager.add_room(TEST_ROOM)
        self.assertEqual(len(room_manager.rooms), 1)

    def test_get_rooms(self):
        room_manager.add_room(TEST_ROOM)
        rooms = room_manager.get_rooms()
        self.assertEqual(len(rooms), 1)
