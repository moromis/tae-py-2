import os
import shutil
import unittest
from contextlib import chdir

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
            os.chdir("..")
        except FileNotFoundError:
            print("logger test couldn't remove log folder/file in tearDown")
        return super().tearDown()

    def test_log(self):
        test_log = "test-log"
        logger.log(test_log, TEST_LOG_FOLDER)
        self.assertTrue(os.path.isdir(TEST_LOG_FOLDER))
        with chdir(TEST_LOG_FOLDER):
            if logger.filename:
                with open(logger.filename, "r") as f:
                    contents = f.read()
                    self.assertStartsWith(contents, test_log)
            else:
                raise FileExistsError()
