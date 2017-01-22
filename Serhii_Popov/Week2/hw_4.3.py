import unittest

class testreplace(unittest.TestCase):
    def test_replace(self):
        with self.assertRaises(TypeError):
           replacemaxmin ('2')
           replacemaxmin(print([10, 20, 30, 40, 50, 100, 150]))
#arr = [10, 20, 30, 150, 40, 50, 100]



def replacemaxmin(arr):
    top = (arr.index(max(arr)))
    bot = (arr.index(min(arr)))
    for el in range(len(arr)):
        el = arr[top]
        arr[top] = arr[bot]
        arr[bot] = el
        return arr

#print (replacemaxmin(arr))

