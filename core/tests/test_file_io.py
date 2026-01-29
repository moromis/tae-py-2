import unittest
import os
import json

from core.managers import meta_manager
from core.file_io import (
    create_json_file_if_not_exists,
    write_data_json,
    write_game_data,
)
from core.types.Character import Character

TEST_FILENAME = "test"
TEST_DATA = {"test": "testing-data"}


class TestFileIO(unittest.TestCase):

    def test_create_json_file_if_not_exists(self):
        create_json_file_if_not_exists(TEST_FILENAME)
        # check that the file now exists
        my_file = TEST_FILENAME
        if os.path.exists(f"{my_file}.json"):
            pass
        else:
            self.fail()

    def test_create_json_file_if_not_exists_empty_object(self):
        create_json_file_if_not_exists(TEST_FILENAME)
        # check that the file now exists
        with open(f"{TEST_FILENAME}.json") as file:
            file_contents = json.load(file)
            self.assertDictEqual(file_contents, {})

    def test_write_data_json_creates_file(self):
        # should create a json file if it doesn't exist
        write_data_json(TEST_FILENAME, TEST_DATA)
        if os.path.exists(f"{TEST_FILENAME}.json"):
            pass
        else:
            self.fail()

    def test_write_data_json_dict(self):
        # should create a json file if it doesn't exist
        write_data_json(TEST_FILENAME, TEST_DATA)
        # the file should have the correct contents
        with open(f"{TEST_FILENAME}.json", "r") as file:
            file_contents = json.load(file)
            self.assertDictEqual(file_contents, TEST_DATA)

    def test_write_data_json_writeable(self):
        # should create a json file if it doesn't exist
        test_character = Character("test", "desc")
        write_data_json(TEST_FILENAME, test_character)
        # the file should have the correct contents
        with open(f"{TEST_FILENAME}.json", "r") as file:
            file_contents = json.load(file)
            self.assertDictEqual(file_contents, test_character.to_dict())

    # NOTE: integration test, otherwise could mock all the managers... probably would want a fixture for that
    def test_write_game_data(self):
        meta_manager.set_meta_by_key(meta_manager.META_KEYS.FILEPATH, TEST_FILENAME)
        write_game_data()
        # the file should have the correct contents
        with open(f"{TEST_FILENAME}.json", "r") as file:
            file_contents = json.load(file)
            self.assertTrue("rooms" in file_contents)
            self.assertTrue("characters" in file_contents)
            self.assertTrue("objects" in file_contents)

    def tearDown(self) -> None:
        super().tearDown()
        os.remove(f"{TEST_FILENAME}.json")
