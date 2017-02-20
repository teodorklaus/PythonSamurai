__author__ = 'Ihor'

import unittest

from Fesianov_Ihor.week_3.Task_6 import String


class TestString(unittest.TestCase):
    def test_concat(self):
        test_str1 = String([4, 2, 6, 5])
        test_str2 = String(['N', ' ', 'A'])
        self.assertEqual(test_str1.concat(test_str2).represent, String([4, 2, 6, 5, 'N', ' ', 'A']).represent)

    def test___str__(self):
        test_str1 = String([4, 2, 6, 5])
        self.assertEqual(test_str1.represent, '4265')

    def test_lower(self):
        test_str = String(['N', ' ', 'A', 'i', 3, 5, ' ', 5, ' '])
        self.assertEqual(test_str.lower().represent, 'n ai35 5 ')

    def test_upper(self):
        test_str = String(['S', 'o', 'M', 'e', ' ', 5])
        self.assertEqual(test_str.upper().represent, 'SOME 5')

    def test_del_space(self):
        test_str = String(['N', ' ', 'A', 'i', 3, 5, ' ', 5, ' '])
        self.assertEqual(test_str.del_space().represent, 'NAi355')

    def test_find(self):
        test_str1 = String(list('spagmeggg,ga   smas  jjhjh'))
        test_str2 = String(list('mas'))
        test_str3 = String(list('why'))
        self.assertEqual(test_str1.find(test_str2), 16)
        self.assertEqual(test_str1.find(test_str3), -1)

    def test_cmp(self):
        test_sample = String([8, 4, 2, 6, 9, 188, -67])
        test_sample2 = String([8, 4, 2, 5, 8, 2000, 11, 34, 5])
        self.assertEqual(test_sample.cmp(test_sample2), 1)

        test_sample3 = String([8, 4, 2, 10, 8, 2000, 11, 34, 5])
        self.assertEqual(test_sample.cmp(test_sample3), -1)

        test_sample4 = String([8, 4, 2, 6, 9, 188, -67, 0])
        self.assertEqual(test_sample.cmp(test_sample4), -1)


if __name__ == '__main__':
    unittest.main()
