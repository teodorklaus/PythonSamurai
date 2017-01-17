__author__ = 'Ihor'
import unittest


@unittest.skip("seek problem")
class TestListMinMax(unittest.TestCase):
    def test_list_min_max(self):
        with self.assertRaises(TypeError):
            list_min_max(1.5)
        self.assertEqual(list_min_max([1.0, 4, 12.8, -40]), (12.8, -40))
        self.assertTrue(list_min_max([1.0, 4, 12.8, -40]), list_func_min_max([1.0, 4, 12.8, -40]))


def input_list():
    n = int(input('enter lists size:\n'))
    print('enter lists elements')
    list1 = []
    for i in range(n):
        list1.append(float(input()))
    print(list1)
    return list1


def list_min_max(lis):
    max = lis[0]
    min = lis[0]
    for el in lis:
        if el > max:
            max = el
        if el < min:
            min = el
    return (max, min)


def list_func_min_max(lis):
    return (max(lis), min(lis))


if __name__ == '__main__':
    listik = input_list()
    print(list_min_max(listik))
    print(list_func_min_max(listik))

if __name__ == '__main__':
    unittest.main()
