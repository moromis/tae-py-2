import copy
import unittest
from unittest.mock import _patch_dict, patch

from core.managers.object_manager import Object_Manager
from parser.parser import Parser
from parser.types.Verb import Verb
from testing.fixtures import (
    INDIRECT_RESPONSE,
    OBJECT_RESPONSE,
    TEST_I_OBJ,
    TEST_OBJECT,
    TEST_VERB,
    TEST_VERB_HANDLER,
)


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
        verb_name, verb, command = parser.get_verb(
            [TEST_VERB, "test", "asdf", TEST_OBJECT.name]
        )
        self.assertTrue(isinstance(verb, Verb))
        self.assertEqual(verb_name, TEST_VERB)
        self.assertEqual(len(command), 3)

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
        self.assertIsNotNone(indirect_obj)
        self.assertEqual(indirect_obj.name, TEST_OBJECT.name)  # type: ignore

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
        self.assertEqual(response, test_i_obj.handlers[TEST_VERB](TEST_OBJECT.name))
