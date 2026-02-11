import unittest
from unittest.mock import MagicMock

from mock import patch

from core.helpers.confirm import confirm
from strings import CONTINUE_ON


class TestConfirm(unittest.TestCase):

    @patch("core.logger.log")
    @patch("core.helpers.confirm.yes_no", return_value=True)
    def testConfirmAffirmative(self, choice_mock, logger_mock):
        mock_f = MagicMock()
        res = confirm(mock_f)
        choice_mock.assert_called_once()
        mock_f.assert_called_once()
        self.assertEqual(res, None)

    @patch("core.logger.log")
    @patch("core.helpers.confirm.yes_no", return_value=False)
    def testConfirmDecline(self, choice_mock, logger_mock):
        mock_f = MagicMock()
        res = confirm(mock_f)
        choice_mock.assert_called_once()
        mock_f.assert_not_called()
        self.assertEqual(res, CONTINUE_ON)
