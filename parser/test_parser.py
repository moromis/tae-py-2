import copy
import unittest
from unittest.mock import patch

from core.managers.object_manager import Object_Manager
from core.types.Character import Character
from parser.parser import Parser
from parser.types.Verb import Verb
from strings import THEY_DONT_WANT_TO_TALK
from testing.fixtures import (
    INDIRECT_RESPONSE,
    OBJECT_RESPONSE,
    TEST_CHARACTER,
    TEST_I_OBJ,
    TEST_OBJECT,
    TEST_VERB,
    TEST_VERB_HANDLER,
)
from prompt_toolkit.formatted_text import FormattedText


@patch.dict("parser.verbs.verbs.VERBS", {"hit": Verb(TEST_VERB_HANDLER)})
class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        Object_Manager.reset()
        return super().setUp()

    def tearDown(self) -> None:
        Object_Manager.reset()
        return super().tearDown()

    def test_get_verb(self):
        parser = Parser()
        res = parser.get_verb([TEST_VERB, "test", "asdf", TEST_OBJECT.name])
        if res != None:
            verb_name, verb, command = res
            self.assertTrue(isinstance(verb, Verb))
            self.assertEqual(verb_name, TEST_VERB)
            self.assertEqual(len(command), 3)
        else:
            raise TypeError("get_verb result should not be None")

    def test_get_object(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        obj, command = parser.get_object(["asdf", "qwer", TEST_OBJECT.name, "zxcv"])
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, TEST_OBJECT.name)  # type: ignore
        self.assertEqual(len(command), 1)

    def test_get_object_not_found(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        obj, command = parser.get_object(["asdf", "qwer", "zxcv"])
        self.assertIsNone(obj)
        self.assertEqual(len(command), 0)

    def test_get_indirect_object(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        indirect_obj = parser.get_indirect_object(
            ["asdf", "qwer", TEST_OBJECT.name, "zxcv"]
        )
        if indirect_obj:
            self.assertEqual(indirect_obj.name, TEST_OBJECT.name)
        else:
            raise TypeError("indirect object should not be None")

    def test_parse_object(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        command = f"{TEST_VERB} {TEST_OBJECT.name}"
        response = parser.parse(command)
        self.assertEqual(response, OBJECT_RESPONSE(TEST_OBJECT.name))

    def test_parse_indirect_no_handler(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        test_i_obj = copy.deepcopy(TEST_I_OBJ)
        test_i_obj.handlers = {}
        Object_Manager.add(test_i_obj)
        command = f"{TEST_VERB} {TEST_OBJECT.name} with {test_i_obj.name}"
        response = parser.parse(command)
        self.assertEqual(response, INDIRECT_RESPONSE(TEST_OBJECT.name, test_i_obj.name))

    def test_parse_indirect_with_handler(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        test_i_obj = copy.deepcopy(TEST_I_OBJ)
        Object_Manager.add(test_i_obj)
        command = f"{TEST_VERB} {TEST_OBJECT.name} with {test_i_obj.name}"
        response = parser.parse(command)
        self.assertEqual(response, test_i_obj.handlers[TEST_VERB](object=TEST_OBJECT))

    def test_parse_talk(self):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_topic = "air"
        test_response = "...but why is there air?"
        test_character.add_response(test_topic, test_response)
        Object_Manager.add(test_character)
        self.assertIsInstance(test_character, Character)
        command = f"talk to {TEST_CHARACTER.name} about {test_topic}"
        res = parser.parse(command)
        self.assertTrue(test_response in str(res))

    @patch("core.types.Character.prompt_toolkit.choice", return_value="air")
    def test_parse_talk_no_topic(self, choice_mock):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_character.responses = {}
        Object_Manager.add(test_character)
        self.assertIsInstance(test_character, Character)
        self.assertEqual(len(test_character.responses), 0)
        command = f"talk to {TEST_CHARACTER.name}"
        response = parser.parse(command)
        choice_mock.assert_not_called()
        self.assertEqual(response, THEY_DONT_WANT_TO_TALK)

    @patch("core.types.Character.prompt_toolkit.choice", return_value="air")
    def test_parse_talk_topic_selection(self, choice_mock):
        parser = Parser()
        Object_Manager.add(TEST_OBJECT)
        test_character = copy.deepcopy(TEST_CHARACTER)
        test_topic = "air"
        test_response = "...but why is there air?"
        test_character.add_response(test_topic, test_response)
        Object_Manager.add(test_character)
        self.assertIsInstance(test_character, Character)
        command = f"talk to {TEST_CHARACTER.name}"
        response = parser.parse(command)
        choice_mock.assert_called_once()
        self.assertIsInstance(response, FormattedText)
        self.assertTrue(test_response in str(response))
