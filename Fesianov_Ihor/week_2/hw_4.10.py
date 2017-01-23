__author__ = 'Ihor'

import unittest


class TestSplitList(unittest.TestCase):
    def test_split_list(self):
        with self.assertRaises(TypeError):
            split_list(1.5)
            split_list([1, 3.2, '15'])
            split_list(1, 2.4, 7)
        test_list = [-1, 1, 66.6, 333, 333, 1234.5, 38, 100]
        split_list(test_list, 2, 5)
        self.assertEqual(test_list, [66.6, 333, 333])


def split_list(mass, start, end):
    for i in range(len(mass) - end):
        del mass[len(mass) - 1]
    for i in range(start):
        del mass[0]


if __name__ == '__main__':
    list1 = [-1, 1, 66.6, 333, 333, 1234.5, 38, 100]
    list2 = [-1, 1, 66.6, 333, 333, 1234.5, 38, 100]
    split_list(list1, 2, 4)
    print(list1)
    print(list2[2:4])

if __name__ == '__main__':
    unittest.main()
