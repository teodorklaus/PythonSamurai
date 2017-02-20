import unittest
#sum_list1 = 0
#a = [50, 30, 's', 'sos']
#b = [4, 'end', 'start', '4']

class TestCopyList(unittest.TestCase):
    def test_copy_list(self):
        with self.assertRaises(TypeError):
            sum_list(1.5)
        a = [5, '523asd', 23, 'Error', 12]
        b = ['asd', 'dsa', 'destroy', 1, 18]
        self.assertEqual(sum_list(a, b), None)


def sum_list(list1, list2):
    list2 = list1 + list2
    return list2

#print (sum_list(sum_list1))