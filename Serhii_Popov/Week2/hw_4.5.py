import unittest
import random

random_list = []
numeric_count = 0

class test_random_sum(unittest.TestCase):
    def test_random(self):
        with self.assertRaises(TypeError):
            random_sum(5)
            numeric = 1
        test_list = [0, 1, 2, 3, 5, 1, 1, 2, 5, 5, 6, 1, 1]
        self.assertEqual(random_sum(1, test_list), 5)


def random_list_generator(random_list):
    length = random.randint(1, 100)
    for i in range(length):
        random_list.append(random.randint(0, 9))
    return random_list
#numeric = int(input('Plese enter numeric from 0 to 9: '))

def random_sum(numeric_count):
    numeric = int(input('Please Enter numeric from 0 to 9: '))
    for i in random_list_generator(random_list):
        numeric_count = 0
    numeric_count = random_list_generator(random_list).count(numeric)
    return numeric_count



#count_numeric = random_list_generator(random_list).count(numeric)

#print (random_list_generator(random_list))
#print (random_sum(numeric_count))



