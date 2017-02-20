import unittest
#import random



class test_cut_gl(unittest.TestCase):
    def test_cut(self):
        with self.assertRaises(TypeError):
            cut_massive(1,5)
            cut_massive(1, 2,3, '23')
            cut_massive(1, 2)
        test_list1 = [1, 4, 5, 6, 8, 7, 5, 5, 6, 3, 1]
        test_list2 = [1, 4, 5, 6, 8, 7, 5, 5, 6, 3, 1]
        #test_list3 = [0]
        cut_massive(test_list1, 2, 8)
        cut_massive2(test_list2, 4, 2)
        self.assertEqual(test_list1, [5, 6, 8, 7, 5, 5])
        self.assertEqual(test_list2, [5, 6, 8, 7, 5, 5, 6]) #

def cut_massive2(massive, start, end):
    for i in range(start):                      #Help with this logic, what is wrong?
        massive = list(reversed(massive))
        del massive[0]
    print (massive)
    #return massive
    #massive1 = list(reversed(massive))
    #print(massive)
    #for i in range(end):
    #    del massive1[0]
        #print(massive)
    #massive = list(reversed(massive1))
    #print (massive)
    #return massive

def cut_massive(massive, start, end):
    for i in range(len(massive) - end):
        del massive[len(massive) - 1]
    for i in range(start):
        del massive[0]
    #print (massive)





