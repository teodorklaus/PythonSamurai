__author__ = 'Ihor'

import unittest
import myfunc


class TestsSort(unittest.TestCase):
    def select_sort(self):
        with self.assertRaises(TypeError):
            select_sort(1.5, 10)
            select_sort(['15', 100])
            select_sort('lknawd')
        test_list = [8, 2, 5, 4, 0, 6, 4, 7]
        select_sort(test_list)
        self.assertEqual(test_list, [0, 2, 4, 4, 5, 6, 7, 8])

    def insert_sort(self):
        with self.assertRaises(TypeError):
            insert_sort(1.5, 10)
            insert_sort(['15', 100])
            insert_sort('lknawd')
        test_list = [8, 2, 5, 4, 0, 6, 4, 7]
        insert_sort(test_list)
        self.assertEqual(test_list, [0, 2, 4, 4, 5, 6, 7, 8])


def select_sort(mass):
    for i in range(len(mass)):
        ind = i + mass[i:].index(min(mass[i:]))
        t = mass[ind]
        mass[ind] = mass[i]
        mass[i] = t


def insert_sort(mass):
    for i in range(1, len(mass)):
        j = i
        el = mass.pop(j)
        while el < mass[j - 1] and j > 0:
            j -= 1
        mass.insert(j, el)


if __name__ == '__main__':
    list1 = myfunc.gererate_random_list()
    print(list1)
    select_sort(list1)
    print(list1)

    list2 = myfunc.gererate_random_list()
    print(list2)
    insert_sort(list2)
    print(list2)

if __name__ == '__main__':
    unittest.main()

