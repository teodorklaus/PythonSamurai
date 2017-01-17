__author__ = 'Ihor'

import myfunc
import unittest


class TestReplaceMaxMin(unittest.TestCase):
    def test_replace_max_min(self):
        with self.assertRaises(TypeError):
            replace_max_min(1.5)
            replace_max_min([1, 3.2, '15'])


def replace_max_min(ar):
    maxx = myfunc.list_min_max(ar)[0]
    minn = myfunc.list_min_max(ar)[1]
    for i in range(len(ar)):
        if ar[i] == maxx:
            ar[i] = minn
        elif ar[i] == minn:
            ar[i] = maxx


def func_replace_max_min(ar):
    def is_maxmin(x, lis):
        if x == max(lis):
            return min(lis)
        elif x == min(lis):
            return max(lis)
        return x
    return list(map(lambda x: is_maxmin(x, ar), ar))


if __name__ == '__main__':
    list1 = myfunc.input_list()
    replace_max_min(list1)
    print(list1)
    list1 = func_replace_max_min(list1)
    print(list1)

if __name__ == '__main__':
    unittest.main()
