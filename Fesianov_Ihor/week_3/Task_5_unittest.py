__author__ = 'Ihor'

import unittest

from Fesianov_Ihor.week_3.Task_5 import List


class TestFraction(unittest.TestCase):
    def test_minimum(self):
        test_sample = List(8, 4, 2, 6, 9, 188, -67)
        self.assertEqual(test_sample.minimum(), -67)

    def test_maximum(self):
        test_sample = List(8, 4, 2, 6, 9, 188, -67)
        self.assertEqual(test_sample.maximum(), 188)

    def test_increase(self):
        test_sample = List(8, 4, 2, 6, 9, 188, -67)
        test_sample.increase(3)
        self.assertEqual(test_sample.elements, [8, 4, 2, 6, 9, 188, -67, 0, 0, 0])

    def test_sort_list(self):
        test_sample = List(8, 4, 2, 6, 9, 188, -67)
        test_sample.sort_list()
        self.assertEqual(test_sample.elements, [-67, 2, 4, 6, 8, 9, 188])

    def test_cmp(self):
        test_sample = List(8, 4, 2, 6, 9, 188, -67)
        test_sample2 = List(8, 4, 2, 5, 8, 2000, 11, 34, 5)
        self.assertEqual(test_sample.cmp(test_sample2), 1)

        test_sample3 = List(8, 4, 2, 10, 8, 2000, 11, 34, 5)
        self.assertEqual(test_sample.cmp(test_sample3), -1)

        test_sample4 = List(8, 4, 2, 6, 9, 188, -67, 0)
        self.assertEqual(test_sample.cmp(test_sample4), -1)


if __name__ == '__main__':
    unittest.main()
