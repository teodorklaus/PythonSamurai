__author__ = 'Ihor'

import unittest
import math


class TestPrimeNums(unittest.TestCase):
    def test_prime_nums(self):
        with self.assertRaises(TypeError):
            prime_nums(1.5)
            prime_nums([1, 3.2, '15'])
            prime_nums('1')
        self.assertEqual(prime_nums(15), [2, 3, 5, 7, 11, 13])
        test_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(prime_nums(100), test_list)

    def test_is_prime(self):
        with self.assertRaises(TypeError):
            is_prime_1(1.5)
            is_prime_1([1, 3.2, '15'])
            is_prime_1('1')
        self.assertEqual(is_prime_1(40), False)
        self.assertEqual(is_prime_1(79), True)
        self.assertEqual(is_prime_1(3491), True)
        self.assertEqual(is_prime_1(3491), is_prime_2(3491))


def prime_nums(n):
    '''
    Sieve of Eratosthenes.

    :param n: integer number
    :return: list of prime numbers less, then 'n'
    '''
    n += 1
    all_num = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i * 2, n, i):
            all_num[j] = False
    return [i for i in range(2, n) if all_num[i]]


def is_prime_1(num):
    if num < 2:
        return False
    for ch in range(2, num):
        if num % ch == 0:
            return False
    return True


def is_prime_2(num):
    if prime_nums(num)[len(prime_nums(num)) - 1] == num:
        return True
    return False


if __name__ == '__main__':
    print(prime_nums(100))
    print(is_prime_1(5039))
    print(is_prime_2(5039))

if __name__ == '__main__':
    unittest.main()
