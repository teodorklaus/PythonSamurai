import unittest
import math
#from operator import add
#from itertools import starmap, zip_longest



class test_list_sum(unittest.TestCase):
    def test_sum(self):
        with self.assertRaises(TypeError):
            lists_sum(1.5)
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        self.assertEqual(lists_sum2(list1, list2), lists_sum(list1, list2))
        self.assertTrue(lists_sum(list1, list2), [7, 9, 11, 13, 15])
        self.assertTrue(lists_sum2(list1, list2), [7, 9, 11, 13, 15])

def check_len(list1, list2):
    if len(list1) == len(list2):
        return True
    else:
        return False


def lists_sum(list1, list2):
    if check_len(list1, list2) == False:
        return 'len(list1) != len(list2)'
    sum_lists = []
    for i in range(len(list1)):
        sum_lists.append(list1[i] + list2[i])
    return sum_lists

def lists_sum2(list1, list2):
    if check_len(list1, list2) == False:
        return 'len(list1) != len(list2)'
    #return list(add(list1[i],list2[i]))
    return list(map((lambda x, y: x + y), list1, list2))
    #return list(map(add(list1, list2, failvalue = 0)))




