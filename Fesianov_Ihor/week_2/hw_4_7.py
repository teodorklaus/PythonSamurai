__author__ = 'Ihor'

import unittest
import myfunc


class TestCounterNumderInList(unittest.TestCase):
    def test_bigger_lists_half(self):
        with self.assertRaises(TypeError):
            sum_list(1.5)
            sum_list([1, 3.2, '15'])
            sum_list('1')
        test_list1 = [0, 4, 5, 4, 8, 4]
        test_list2 = [1, 2, 3, 3, 2, 1]
        test_sumlist = [1, 6, 8, 7, 10, 5]
        self.assertEqual(sum_list(test_list1, test_list2), test_sumlist)
        self.assertEqual(sum_list(test_list1, test_list2), sum_list_2(test_list1, test_list2))
        self.assertEqual(sum_list(test_list1, test_list2[1:]), 'length of list must be the same')

def is_len_the_same(list1,list2):
    return (False, True)[len(list1) == len(list2)]

def sum_list(list1, list2):
    if not is_len_the_same(list1, list2):
        return 'length of list must be the same'
    output = []
    for i in range(len(list1)):
        output.append(list1[i] + list2[i])
    return output

def sum_list_2(list1, list2):
    if not is_len_the_same(list1, list2):
        return 'length of list must be the same'
    return list(map((lambda x, y: x + y), list1, list2))


if __name__ == '__main__':
    list1 = [2, 3, 5, 0]
    list2 = [4, 6, 20, 140]
    print(sum_list(list1, list2))
    print(sum_list_2(list1, list2))

if __name__ == '__main__':
    unittest.main()
