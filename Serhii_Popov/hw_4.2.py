import unittest

class testarf(unittest.TestCase):
    def test_arf(self):
        with self.assertRaises(TypeError):
            arifmeticmean (1.2)
        self.assertEqual(arifmeticmean([100, 15, 45, 5, 10]), 35)



def arifmeticmean(list1):
    return float(sum(list1) / len(list1))