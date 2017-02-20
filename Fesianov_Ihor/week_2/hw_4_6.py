__author__ = 'Ihor'

import unittest
import myfunc


class TestCounterNumderInList(unittest.TestCase):
    def test_bigger_lists_half(self):
        with self.assertRaises(TypeError):
            bigger_lists_half(1.5)
            bigger_lists_half([1, 3.2, '15'])
            bigger_lists_half('1')
        test_list = [0, 4, 5, 4, 8, 4]
        self.assertEqual(bigger_lists_half([1, 2, 3, 3, 2, 1]), 'arithmetic mean of lists half is the same')
        self.assertEqual(bigger_lists_half(test_list), [4, 8, 4])
        self.assertEqual(bigger_lists_half([1, 2, 3, 3, 2, 1, 0]), 'lists length is odd')


def bigger_lists_half(mass):
    if len(mass) % 2 == 0:
        half1 = mass[:int(len(mass) / 2)]
        half2 = mass[int(len(mass) / 2):]
        if myfunc.arithmetic_mean(half1) == myfunc.arithmetic_mean(half2):
            return 'arithmetic mean of lists half is the same'
        else:
            return (half2, half1)[myfunc.arithmetic_mean(half1) > myfunc.arithmetic_mean(half2)]
    else:
        return 'lists length is odd'


if __name__ == '__main__':
    print(bigger_lists_half(myfunc.input_list()))

if __name__ == '__main__':
    unittest.main()
