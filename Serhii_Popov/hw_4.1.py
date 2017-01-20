import unittest


@unittest.skip("Goog test")
class TestProg(unittest.TestCase):
    def test_prog(self):
        with  self.assertRaises(TypeError):
            minmaxvalues(15.8,-600)
        self.assertEqual(minmaxvalues([2.0, 5, 15.8, -600]), (15.8, -600))
        self.assertTrue(minmaxvalues([2.0, 5, 15.8, -600]), func_minmax([2.0, 5, 15.8, -600]))

def input_values():
    n = int(input('Enter list range: '))
    print('enter elemts')
    inputrray = []
    for i in range(n):
        inputrray.append(float(input()))
    print(inputrray)
    return inputrray

def minmaxvalues(arr):
    max = arr[0]
    min = arr[0]
    for el in arr:
        if el > max:
            max = el
        if el < min:
            min = el
    return (max, min)


def func_minmax(arr):
    return (max(arr), min(arr))

