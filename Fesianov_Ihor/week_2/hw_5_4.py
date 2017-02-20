__author__ = 'Ihor'

import unittest


class TestFibonacci(unittest.TestCase):
    def test_fibo(self):
        with self.assertRaises(TypeError):
            fibo(1.5)
            fibo([1, 3.2, '15'])
            fibo('1')
        self.assertEqual(fibo(8), 21)
        self.assertEqual(fibo(4), 3)


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n_1 = 0
    n_2 = 1
    for i in range(1, n + 1):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result


if __name__ == '__main__':
    print(fibo(10))

if __name__ == '__main__':
    unittest.main()
