import os
import unittest
from unittest import mock

from core.helpers.cls import cls


class TestCls(unittest.TestCase):

    @mock.patch("os.system")
    def test_cls_unix(self, os_system):
        os.name = "nt"
        print("test")
        cls()
        os_system.assert_called_once_with("cls")

    @mock.patch("os.system")
    def test_cls_posix(self, os_system):
        os.name = "posix"
        print("test")
        cls()
        os_system.assert_called_once_with("clear")
