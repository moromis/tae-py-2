import copy
import unittest
from core.types.ObjectProperties import OBJECT_PROPERTIES
from strings import CANT_OPEN, DONT_SEE_HERE
from testing.fixtures import TEST_OBJECT
from parser.verbs.open import open


class TestOpen(unittest.TestCase):
    def test_open_not_openable(self):
        test_obj = copy.deepcopy(TEST_OBJECT)
        res = open(object=test_obj)
        self.assertEqual(res, CANT_OPEN)

    def test_open_is_closed(self):
        test_obj = copy.deepcopy(TEST_OBJECT)
        test_obj.set_property(OBJECT_PROPERTIES.OPEN, False)
        res = open(object=test_obj)
        self.assertEndsWith(res, "now open")

    def test_open_is_open(self):
        test_obj = copy.deepcopy(TEST_OBJECT)
        test_obj.set_property(OBJECT_PROPERTIES.OPEN, True)
        res = open(object=test_obj)
        self.assertEndsWith(res, "already open")

    def test_open_no_object(self):
        res = open()
        self.assertEqual(res, DONT_SEE_HERE)
