__author__ = 'Ihor'

import unittest


class TestsCopyList(unittest.TestCase):
    def test_list_copy(self):
        with self.assertRaises(TypeError):
            list_copy(1.5)
            list_copy(5)
            list_copy('1kjndfkjnv')
        test_list_1 = [2, 3, 5, 7, 11, 13]
        test_list_2 = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
        list_copy(test_list_1, 2, test_list_2, 3, 3)
        self.assertEqual(test_list_2, [1001, 1002, 1003, 5, 7, 11, 1007])


def list_copy(from_list, from_index, to_list, to_index, count):
    range_list = from_list[from_index:from_index + count]
    to_list[to_index:to_index + count] = range_list[:]


if __name__ == '__main__':
    list1 = [2, 3, 5, 7, 11, 13]
    list2 = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
    list_copy(list1, 2, list2, 3, 3)
    print(list2)


'''
if __name__ == '__main__':
    unittest.main()
'''