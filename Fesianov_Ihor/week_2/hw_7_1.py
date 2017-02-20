__author__ = 'Ihor'

import unittest


class TestInvert(unittest.TestCase):
    def test_invert_list(self):
        with self.assertRaises(TypeError):
            invert_list(1.5)
            invert_list([1, 3.2, '15'])
            invert_list('1')
        test_list = [-1, 1, 66.6, 333, 333, 1234.5, 38, 100, 98.5]
        invert_num_list(test_list)
        self.assertEqual(test_list, [98.5, 100, 38, 1234.5, 333, 333, 66.6, 1, -1])
        invert_list(test_list)
        self.assertEqual(test_list, [-1, 1, 66.6, 333, 333, 1234.5, 38, 100, 98.5])


def invert_num_list(mass):
    for i in range(len(mass) // 2):
        mass[i] = mass[i] + mass[len(mass) - 1 - i]
        mass[len(mass) - 1 - i] = mass[i] - mass[len(mass) - 1 - i]
        mass[i] = mass[i] - mass[len(mass) - 1 - i]


def invert_list(mass):
    for i in range(len(mass) // 2):
        t = mass[i]
        mass[i] = mass[len(mass) - 1 - i]
        mass[len(mass) - 1 - i] = t


if __name__ == '__main__':
    list1 = [-1, 1, 66.6, 333, 333, 1234.5, 38, 100, 98.5]
    invert_list(list1)
    print(list1)

if __name__ == '__main__':
    unittest.main()
