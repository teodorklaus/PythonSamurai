__author__ = 'Ihor'

import unittest

from Fesianov_Ihor.week_3.Task_4 import Calc


class TestCalc(unittest.TestCase, Calc):
    def test_get_key(self):
        self.assertEqual(self.get_key('*'), 2)

    def test_addition(self):
        self.first_num = 8
        self.second_num = 4
        self.addition()
        self.assertEqual(self.result, 12)

    def test_subtraction(self):
        self.first_num = 8
        self.second_num = 4
        self.subtraction()
        self.assertEqual(self.result, 4)

    def test_multiplication(self):
        self.first_num = 8
        self.second_num = 4
        self.multiplication()
        self.assertEqual(self.result, 32)

    def test_division(self):
        self.first_num = 8
        self.second_num = 4
        self.division()
        self.assertEqual(self.result, 2.0)

    def test_calculation(self):
        self.first_num = 8
        self.second_num = 4
        self.action = 1
        self.calculation()
        self.assertEqual(self.result, 4)


if __name__ == '__main__':
    unittest.main()
