import copy
import unittest

from core.managers import room_manager
from core.types.Room import Room
from testing.fixtures import TEST_CHARACTER, TEST_OBJECT, TEST_ROOM


class TestRoomManager(unittest.TestCase):
    def setUp(self) -> None:
        room_manager.reset()
        return super().setUp()

    def tearDown(self) -> None:
        room_manager.reset()
        return super().tearDown()

    def test_add_room(self):
        self.assertEqual(len(room_manager.rooms), 0)
        room_manager.add_room(TEST_ROOM)
        self.assertEqual(len(room_manager.rooms), 1)

    def test_get_rooms(self):
        self.assertEqual(len(room_manager.rooms), 0)
        room_manager.add_room(TEST_ROOM)
        rooms = room_manager.get_rooms()
        self.assertEqual(len(rooms), 1)

    def test_reset(self):
        room_manager.add_room(TEST_ROOM)
        room_manager.reset()
        rooms = room_manager.get_rooms()
        self.assertEqual(len(rooms), 0)

    def test_get_entrance_room_no_rooms(self):
        entrance_room = room_manager.get_entrance_room()
        self.assertIsNone(entrance_room)

    def test_get_entrance_room(self):
        room = copy.deepcopy(TEST_ROOM)
        room_manager.rooms = {room.name: room}
        room_manager.set_entrance_room(room)
        entrance_room = room_manager.get_entrance_room()
        self.assertEqual(entrance_room, room)

    def test_get_entrance_room_auto_set(self):
        room = copy.deepcopy(TEST_ROOM)
        room_manager.add_room(room)
        entrance_room = room_manager.get_entrance_room()
        self.assertEqual(entrance_room, room)

    def test_set_rooms(self):
        room = copy.deepcopy(TEST_ROOM)
        room_manager.set_rooms({room.name: room})
        rooms = room_manager.get_rooms()
        self.assertEqual(len(rooms), 1)

    def test_set_rooms_auto_set_current_room(self):
        room = copy.deepcopy(TEST_ROOM)
        room.is_entrance = False
        room_manager.set_rooms({room.name: room})
        rooms = room_manager.get_rooms()
        self.assertEqual(room_manager.current_room, rooms[room.name])

    def test_set_rooms_json(self):
        room = copy.deepcopy(TEST_ROOM)
        room_manager.set_rooms_json({room.name: room.to_dict()})
        rooms = room_manager.get_rooms()
        self.assertEqual(len(rooms), 1)
        self.assertIsInstance(rooms[room.name], Room)
        self.assertEqual(rooms[room.name], room)

    def test_set_rooms_json_auto_set_current_room(self):
        room = copy.deepcopy(TEST_ROOM)
        room.is_entrance = False
        room_manager.set_rooms_json({room.name: room.to_dict()})
        rooms = room_manager.get_rooms()
        self.assertEqual(room_manager.current_room, rooms[room.name])

    def test_add_object_to_room_should_cast(self):
        room = copy.deepcopy(TEST_ROOM)
        object = copy.deepcopy(TEST_OBJECT)
        room_manager.add_room(room)
        room_manager.add_object_to_room(object, room)
        self.assertEqual(len(room.objects), 1)
        self.assertEqual(room.objects[0], object.name)

    def test_get_object_from_room_should_cast(self):
        room = copy.deepcopy(TEST_ROOM)
        object = copy.deepcopy(TEST_OBJECT)
        room.objects = [object.name]
        room_manager.add_room(room)
        res = room_manager.get_object_from_room(object, room)
        self.assertEqual(res, object.name)

    def test_remove_object_from_room_should_cast(self):
        room = copy.deepcopy(TEST_ROOM)
        object = copy.deepcopy(TEST_OBJECT)
        room.objects = [object.name]
        room_manager.add_room(room)
        res = room_manager.remove_object_from_room(object, room)
        self.assertEqual(len(room.objects), 0)

    def test_add_character_to_room(self):
        room = copy.deepcopy(TEST_ROOM)
        character = copy.deepcopy(TEST_CHARACTER)
        room_manager.add_room(room)
        room_manager.add_character_to_room(character.name, room.name)
        self.assertEqual(len(room.characters), 1)
        self.assertEqual(room.characters[0], character.name)

    def test_add_character_to_room_should_cast(self):
        room = copy.deepcopy(TEST_ROOM)
        character = copy.deepcopy(TEST_CHARACTER)
        room_manager.add_room(room)
        room_manager.add_character_to_room(character, room)
        self.assertEqual(len(room.characters), 1)
        self.assertStartsWith(room.characters[0], character.adjective)
        self.assertEndsWith(room.characters[0], character.name)
