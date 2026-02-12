import copy
import unittest

from mock import patch


from parser.verbs.undo import NOTHING_TO_UNDO, undo
from player.player import Player
from testing.fixtures import TEST_COMMANDS


@patch("core.logger.log")
class TestUndo(unittest.TestCase):
    def test_undo(self, *args):
        player = Player()
        test_command = copy.deepcopy(list(TEST_COMMANDS.values())[0])
        player.add_to_history(test_command)
        self.assertEqual(len(player.get_history()), 1)
        undo()
        self.assertEqual(len(player.get_history()), 0)

    def test_undo_no_history(self, *args):
        player = Player()
        self.assertEqual(len(player.get_history()), 0)
        res = undo()
        self.assertEqual(res, NOTHING_TO_UNDO)
