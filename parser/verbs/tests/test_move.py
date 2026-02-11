import copy
import unittest

from core.managers import room_manager
from editor.shared.directions import DIRECTIONS, reverse_direction
from parser.verbs.move import move
from strings import CANT_MOVE_THAT_WAY, GO_WHERE, NOTHING_THAT_DIRECTION
from testing.fixtures import TEST_ROOM


class TestMove(unittest.TestCase):
    def setUp(self) -> None:
        room_manager.reset()
        return super().setUp()

    def tearDown(self) -> None:
        room_manager.reset()
        return super().setUp()

    def test_move_no_direction(self):
        res = move()
        self.assertEqual(res, GO_WHERE)

    def test_move_no_rooms(self):
        res = move(rest=[DIRECTIONS.NORTH])
        self.assertEqual(res, CANT_MOVE_THAT_WAY)

    def test_move_one_room(self):
        test_room = copy.deepcopy(TEST_ROOM)
        room_manager.add_room(test_room)
        self.assertEqual(room_manager.current_room, test_room)
        res = move(rest=[DIRECTIONS.NORTH])
        self.assertEqual(res, NOTHING_THAT_DIRECTION)
        self.assertEqual(room_manager.current_room, test_room)

    def test_move_one_adjacency(self):
        test_room = copy.deepcopy(TEST_ROOM)
        test_room_2 = copy.deepcopy(TEST_ROOM)
        test_room_2.name = "another test room"
        test_room.add_adjacency(test_room_2.name, DIRECTIONS.NORTH)
        test_room_2.add_adjacency(test_room.name, reverse_direction(DIRECTIONS.NORTH))
        room_manager.add_room(test_room)
        room_manager.add_room(test_room_2)
        self.assertEqual(room_manager.current_room, test_room)
        res = move(rest=[DIRECTIONS.NORTH])
        self.assertEqual(room_manager.current_room, test_room_2)
        res = move(rest=["south"])
        self.assertEqual(room_manager.current_room, test_room)
