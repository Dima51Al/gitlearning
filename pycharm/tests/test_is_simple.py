import unittest

from pycharm.src.any_versions_file import is_simple


class Any_versions_test(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(is_simple(5), True)
