__author__ = 'Ihor'

import unittest

from Fesianov_Ihor.week_3.Task_3 import Fraction


class TestFraction(unittest.TestCase):
    def test__add__(self):
        test_fract = Fraction(4, 3) + Fraction(4, 6)
        self.assertEqual(test_fract.denominate, Fraction(2, 1).denominate)
        self.assertEqual(test_fract.numerator, Fraction(2, 1).numerator)

    def test__sub__(self):
        test_fract = Fraction(4, 3) - Fraction(4, 6)
        self.assertEqual(test_fract.denominate, Fraction(2, 3).denominate)
        self.assertEqual(test_fract.numerator, Fraction(2, 3).numerator)

    def test__mul__(self):
        test_fract = Fraction(4, 3) * Fraction(4, 6)
        self.assertEqual(test_fract.denominate, Fraction(8, 9).denominate)
        self.assertEqual(test_fract.numerator, Fraction(8, 9).numerator)

    def test__truediv__(self):
        test_fract = Fraction(4, 3) / Fraction(4, 6)
        self.assertEqual(test_fract.denominate, Fraction(2, 1).denominate)
        self.assertEqual(test_fract.numerator, Fraction(2, 1).numerator)

    def test_cmp(self):
        test_fract = Fraction(4, 3)
        test_num2 = Fraction(4, 6)
        self.assertEqual(test_fract.cmp(test_num2), 1)
        self.assertEqual(test_num2.cmp(test_fract), -1)
        self.assertEqual(test_num2.cmp(test_num2), 0)

    def test_exept(self):
        with self.assertRaises(TypeError):
            Fraction(1.5, 1.7)
            Fraction(1, '1')
        with self.assertRaises(ZeroDivisionError):
            Fraction(2, 0)


if __name__ == '__main__':
    unittest.main()
