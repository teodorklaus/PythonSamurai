__author__ = 'Ihor'

import unittest

from Fesianov_Ihor.week_3.Task_2 import Number


class TestNumber(unittest.TestCase):
    def test__add__(self):
        test_num = Number(4) + Number(5)
        self.assertEqual(test_num.value, Number(9).value)

    def test__sub__(self):
        test_num = Number(4) - Number(5)
        self.assertEqual(test_num.value, Number(-1).value)

    def test__mul__(self):
        test_num = Number(4) * Number(5)
        self.assertEqual(test_num.value, Number(20).value)

    def test__truediv__(self):
        test_num = Number(9) / Number(4.5)
        self.assertEqual(test_num.value, Number(2).value)

    def test__pow__(self):
        test_num = Number(9) / Number(4.5)
        self.assertEqual(test_num.value, Number(2).value)

    def test_factorial(self):
        test_num = Number(4)
        fact = test_num.factorial()
        self.assertEqual(fact.value, 24)

    def test__mod__(self):
        test_num = Number(9) % Number(4)
        self.assertEqual(test_num.value, Number(1).value)

    def test_cmp(self):
        test_num1 = Number()
        test_num2 = Number(2)
        self.assertEqual(test_num1.cmp(test_num2), -1)


if __name__ == '__main__':
    unittest.main()
