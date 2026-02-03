import unittest
from mock import patch

from core import prompt


class TestAsk(unittest.TestCase):

    @patch("prompt_toolkit.PromptSession.prompt", return_value="test")
    def test_print_list(self, promptsession_mock):
        result = prompt()
        self.assertGreaterEqual(promptsession_mock.call_count, 1)
        self.assertEqual(result, "test")
