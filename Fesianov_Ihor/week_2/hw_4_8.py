__author__ = 'Ihor'

import unittest
import random


class TestGenerateSpecRandList(unittest.TestCase):
    def test_generate_specific_random_list(self):
        with self.assertRaises(TypeError):
            generate_specific_random_list(1.5)
            generate_specific_random_list([1, 3.2, '15'])
            generate_specific_random_list('1')
        self.assertIsNotNone(generate_specific_random_list())


def generate_specific_random_list(length=random.randint(1, 10)):
    def adder(var):
        el = random.randint(0, 100)
        while el % 2 == var:
            el = random.randint(0, 100)
        rand_list.append(el)

    rand_list = []
    for i in range(length):
        if i % 2 == 0:
            adder(1)
        else:
            adder(0)
    return rand_list


if __name__ == '__main__':
    mass = generate_specific_random_list()
    print(mass)

if __name__ == '__main__':
    unittest.main()
