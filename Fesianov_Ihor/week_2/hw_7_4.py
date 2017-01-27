__author__ = 'Ihor'

import unittest


class TestsShiftList(unittest.TestCase):
    def test_shift(self):
        with self.assertRaises(TypeError):
            shift(1.5, 2)
            shift([1, 3.2, '15'])
            shift('1', 1)
        test_list_1 = [11, 13, 2, 3, 5, 7]
        shift(test_list_1, 4)
        self.assertEqual(test_list_1, [2, 3, 5, 7, 11, 13])
        test_list_2 = [1, 2, 3, 4]
        shift(test_list_2, 3)
        self.assertEqual(test_list_2, [2, 3, 4, 1])


def shift(mass, m):
    n = m % len(mass)
    mass_copy = mass[:]
    for i in range(len(mass)):
        if i < n:
            mass[i] = mass[i + len(mass) - n]
        else:
            mass[i] = mass_copy[i - n]


if __name__ == '__main__':
    list1 = [0, 1, 2, 3, 4]
    shift(list1, 2)
    print(list1)

if __name__ == '__main__':
    unittest.main()
