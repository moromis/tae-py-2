import os
import unittest

from mock import patch

from core.file_io import write_game_data
from core.gamestate import load_game
from core.managers.meta import meta_manager

TEST_FILENAME = "test.json"


class TestGameState(unittest.TestCase):

    def tearDown(self) -> None:
        super().tearDown()
        os.remove(TEST_FILENAME)

    @patch("core.managers.meta.migrations.fprint")
    @patch("core.gamestate.fprint")
    @patch("builtins.input")
    @patch("core.gamestate.select_file", return_value=TEST_FILENAME)
    def test_load_game_migrates_version(self, *args, **kwargs):
        meta_manager.set_meta_by_key(
            meta_manager.META_KEYS.FILEPATH, TEST_FILENAME.replace(".json", "")
        )
        meta_manager.set_meta_by_key(
            meta_manager.META_KEYS.SCHEMA, meta_manager.SCHEMA_VERSIONS._0_0_2.value
        )
        write_game_data()
        load_game()
        self.assertEqual(
            meta_manager.get_meta_by_key(meta_manager.META_KEYS.SCHEMA),
            meta_manager.SCHEMA_VERSIONS._0_0_3.value,
        )
        self.assertEndsWith(
            meta_manager.get_meta_by_key(meta_manager.META_KEYS.FILEPATH), ".json"
        )
