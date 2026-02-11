import unittest

from parser.verbs.hit import DEFAULT_HIT_RESPONSE, INDIRECT_HIT_RESPONSE, WHAT_HIT, hit
from testing.fixtures import TEST_I_OBJ, TEST_OBJECT


class TestHit(unittest.TestCase):
    def test_hit_no_obj(self):
        res = hit()
        self.assertEqual(res, WHAT_HIT)

    def test_hit_obj(self):
        res = hit(TEST_OBJECT)
        self.assertEqual(res, DEFAULT_HIT_RESPONSE(TEST_OBJECT.name))

    def test_hit_indirect_obj(self):
        res = hit(TEST_OBJECT, TEST_I_OBJ)
        self.assertEqual(res, INDIRECT_HIT_RESPONSE(TEST_OBJECT.name, TEST_I_OBJ.name))
