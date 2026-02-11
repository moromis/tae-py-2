import unittest

from mock import patch

from core.helpers.yes_no import yes_no


class TestYesNo(unittest.TestCase):

    @patch("core.logger.log")
    @patch("core.helpers.yes_no.prompt_toolkit.choice", return_value="y")
    def testYes(self, choice_mock, logger_mock):
        res = yes_no("test")
        choice_mock.assert_called_once()
        logger_mock.assert_called_once()
        self.assertEqual(res, True)

    @patch("core.logger.log")
    @patch("core.helpers.yes_no.prompt_toolkit.choice", return_value="n")
    def testNo(self, choice_mock, logger_mock):
        res = yes_no("test")
        choice_mock.assert_called_once()
        logger_mock.assert_called_once()
        self.assertEqual(res, False)
