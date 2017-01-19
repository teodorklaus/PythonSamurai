__author__ = 'Ihor'

import unittest


class TestCopyList(unittest.TestCase):
    def test_copy_list(self):
        with self.assertRaises(TypeError):
            copy_list(1.5)
        a = [1, 'pro0', 8, 1000, 451.1555, ('sos', 3)]
        b = [0, 2, 3, 5, 3, 'system']
        self.assertEqual(copy_list(a, b), None)


def copy_list(list_orig, list_for_copy):
    for i in range(len(list_orig)):
        list_orig[i] = list_for_copy[i]


if __name__ == '__main__':
    list1 = [0, 4, 5, -1.5, 98]
    list2 = [0, 7, 'd', False, -3, 14]
    copy_list(list1, list2)
    print(list1, list2)

if __name__ == '__main__':
    unittest.main()
