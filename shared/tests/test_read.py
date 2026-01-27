import unittest
from mock import patch
from unittest.mock import MagicMock

from prompt_toolkit import PromptSession

from shared.prompt import prompt


class TestAsk(unittest.TestCase):

    def test_print_list(self):
        session = PromptSession()
        session.prompt = MagicMock(return_value="test")
        result = prompt(session=session)
        self.assertGreaterEqual(session.prompt.call_count, 1)
        self.assertEqual(result, "test")
