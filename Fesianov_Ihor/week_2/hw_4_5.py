__author__ = 'Ihor'

import unittest
import random


class TestCounterNumderInList(unittest.TestCase):
    def test_counter(self):
        with self.assertRaises(TypeError):
            counter(1.5)
            counter([1, 3.2, '15'])
            counter('1')
        test_list = [0, 4, 5, 4, 8, 4, 4]
        self.assertEqual(counter(4, test_list), 4, 'count problem')
        self.assertEqual(counter(0, test_list), counter_2(0, test_list))


def gererate_random_list(length=random.randint(1, 10)):
    rand_list = []
    for i in range(length):
        rand_list.append(random.randint(0, 9))
    return rand_list


def counter(num, ar):
    count = 0
    for el in ar:
        if el == num:
            count += 1
    return count


def counter_2(num, ar):
    return len(list(filter(lambda x: x == num, ar)))


if __name__ == '__main__':
    n = int(input('enter number:\n'))
    mass = gererate_random_list()
    print(mass)
    print(counter(n, mass))
    print(counter_2(n, mass))

if __name__ == '__main__':
    unittest.main()
