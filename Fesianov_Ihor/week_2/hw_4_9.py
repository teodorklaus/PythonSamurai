__author__ = 'Ihor'

import unittest
import random
import myfunc


class TestComparison(unittest.TestCase):
    def test_count_even_number(self):
        with self.assertRaises(TypeError):
            count_even_number(1.5)
            count_even_number([1, 3.2, '15'])
            count_even_number('1')
        test_list = [8, 5, 2, 7 , 25, 6, 5]
        self.assertEqual(count_even_number(test_list), 3)
    def test_comparison(self):
        test_list1 = [8, 5, 2, 7 , 25, 6, 5]
        test_list2 = [9, 4, 35, 37, 38, 48, 36, 90]
        self.assertEqual(comparison_amount_even_number(test_list1, test_list2), 'more in second list')

def count_even_number(mass):
    count = 0
    for el in mass:
        if el % 2 == 0:
            count +=1
    return count

def count_even_number_2(mass):
    return len(list(filter(lambda x: x % 2 == 0, mass)))

def comparison_amount_even_number(list1, list2):
    if count_even_number(list1) == count_even_number(list2):
        return 'amount of even numbers is the same'
    return ('more in first list', 'more in second list')[count_even_number(list1) < count_even_number(list2)]


if __name__ == '__main__':
    list1 = myfunc.gererate_random_list(mini=25, maxi=75)
    list2 = myfunc.gererate_random_list(len(list1), 25, 75)
    print(list1, list2)
    print(count_even_number(list1), count_even_number_2(list2))
    print(comparison_amount_even_number(list1, list2))

if __name__ == '__main__':
    unittest.main()
