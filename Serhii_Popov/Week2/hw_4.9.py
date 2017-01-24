import unittest
import random


class comparsion_test_gl(unittest.TestCase):
    def coparsion_test(self):
        with self.assertRaises(TypeError):
            comparison(1.5)
            comparison(1, 2,5, '2')
            comparison('1')
        test_list1 = [26, 48, 27, 33, 46, 73]
        test_list2 = [41, 43, 33, 55, 62, 26]
        self.assertEqual(comparison(test_list1, test_list2), 'Sum pair elements Mass1 > Mass2')

#list1 = []
#list2 = []
def comparison(list1, list2):
    lenght = random.randint(5, 25)
    for i in range(lenght):
        list1.append(random.randint(25, 75))
        list2.append(random.randint(25, 75))


    def list1_sum_f(list1):
        list1_sum = 0
        for el in list1:
            if el % 2 == 0:
                #el = random.randint(25, 75)
                list1_sum += 1
        return list1_sum

    def list2_sum_f(list2):
        list2_sum = 0
        for el in list2:
            if el % 2 == 0:
                # el = random.randint(25, 75)
                list2_sum += 1
        return list2_sum



    if list1_sum_f(list1) > list2_sum_f(list2):
        return 'Sum pair elements Mass1 > Mass2' #list1_sum_f(sum1)
    else:
        return 'Sum pair elements Mass1 < Mass2' #list2_sum_f(sum2)


#print (comparison(list1, list2))

