import os
import shutil
import unittest

from core import logger

TEST_LOG_FOLDER = "test-logs-folder"


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        try:
            shutil.rmtree(TEST_LOG_FOLDER)
        except FileNotFoundError:
            pass
        return super().setUp()

    def tearDown(self) -> None:
        try:
            shutil.rmtree(TEST_LOG_FOLDER)
        except FileNotFoundError:
            pass
        return super().tearDown()

    def test_log(self):
        test_log = "test-log"
        logger.log(test_log, TEST_LOG_FOLDER)
        self.assertTrue(os.path.isdir(TEST_LOG_FOLDER))
        with open(logger.filename) as f:
            contents = f.read()
            self.assertStartsWith(contents, test_log)
