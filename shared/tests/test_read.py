import unittest
from mock import patch

from shared.prompt import prompt


class TestAsk(unittest.TestCase):

    @patch("builtins.input", return_value="test")
    def test_print_list(self, input_mock):
        result = prompt()
        self.assertGreaterEqual(input_mock.call_count, 1)
        self.assertEqual(result, "test")
