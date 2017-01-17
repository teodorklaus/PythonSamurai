__author__ = 'Ihor'

import myfunc
import unittest

class TestArithmeticMean(unittest.TestCase):
    def test_arithmetic_mean(self):
        with self.assertRaises(TypeError):
            arithmetic_mean(1.5)
        self.assertEqual(arithmetic_mean([1.0, 4, 12.8, -40]), -5.55)
        self.assertTrue(arithmetic_mean([1.0, 4, 12.8, -40]), func_arithmetic_mean([1.0, 4, 12.8, -40]))


def arithmetic_mean(lis):
    summ = 0
    for el in lis:
        summ += float(el)
    return summ / len(lis)


def func_arithmetic_mean(lis):
    return sum(lis) / len(lis)


if __name__ == '__main__':
    list1 = myfunc.input_list()
    print(arithmetic_mean(list1))
    print(func_arithmetic_mean(list1))

if __name__ == '__main__':
    unittest.main()
