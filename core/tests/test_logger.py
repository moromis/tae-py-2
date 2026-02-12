import os
import shutil
import unittest

from core import logger


class TestLogger(unittest.TestCase):

    def tearDown(self) -> None:
        shutil.rmtree(logger.log_folder)
        return super().tearDown()

    def test_log(self):
        test_log = "test-log"
        logger.log(test_log)
        self.assertTrue(os.path.isdir(logger.log_folder))
        with open(logger.filename) as f:
            contents = f.read()
            self.assertStartsWith(contents, test_log)
