import copy
import unittest

from mock import patch

from core.managers import room_manager
from core.managers.object_manager import Object_Manager
from core.types.ReplResult import ReplResult
from editor.character_creator import create_character
from testing.fixtures import TEST_CHARACTER, TEST_ROOM

side_effect = [TEST_CHARACTER.name, TEST_CHARACTER.desc]


@patch("editor.character_creator.fprint")
@patch("editor.character_creator.prompt", side_effect=side_effect)
@patch("editor.character_creator.yes_no", return_value=True)
@patch("editor.character_creator.choice", return_value=TEST_ROOM.name)
@patch("editor.character_creator.character_responses", return_value=[])
class TestCharacterCreator(unittest.TestCase):

    def tearDown(self) -> None:
        room_manager.reset()
        Object_Manager.reset()
        return super().tearDown()

    @patch("editor.character_creator.write_game_data")
    def test_should_run(self, *args):
        res = create_character()
        self.assertIsInstance(res, ReplResult)

    @patch("editor.character_creator.write_game_data")
    def test_creates_character(self, *args):
        create_character()
        self.assertEqual(len(Object_Manager.objects), 1)
        character = Object_Manager.get_by_name(TEST_CHARACTER.name)
        if character != None:
            self.assertEqual(character.name, TEST_CHARACTER.name)
        else:
            raise TypeError("No character was created")

    def test_write_game_data_is_called(self, *args):
        with patch("editor.character_creator.write_game_data") as write_game_data_mock:
            create_character()
            write_game_data_mock.assert_called_once()

    @patch("editor.character_creator.write_game_data")
    def test_adds_character_to_room(self, *args):
        test_room = copy.deepcopy(TEST_ROOM)
        room_manager.add_room(test_room)
        create_character()
        self.assertEqual(len(test_room.characters), 1)
        self.assertEqual(test_room.characters[0], TEST_CHARACTER.name)
