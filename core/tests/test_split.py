from shared.split import split_by_and, split_by_dot
import unittest


class TestSplit(unittest.TestCase):
    def test_split_by_and(self):
        assert split_by_and("command1 and command2 and command3andbadcommand") == [
            "command1",
            "command2",
            "command3andbadcommand",
        ]

    def test_split_by_dot(self):
        assert split_by_dot("thing1.thing2.thing.1") == [
            "thing1",
            "thing2",
            "thing",
            "1",
        ]
