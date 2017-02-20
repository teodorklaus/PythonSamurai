import unittest
import random

class test_random_odd_pairs(unittest.TestCase):
    def test_random(self):
        with self.assertRaises(TypeError):
            random_mass_generator(1,5)
        self.assertNotEqual(random_mass_generator(), 'None')

def random_mass_generator(lenght = random.randint(1,10)):
    random_mass = []
    def random1(now):
        el = random.randint(1, 100)
        while el % 2 == now:
            el = random.randint(1,100)
        random_mass.append(el)


    for i in range(lenght):
        if i % 2 == 0:
            random1(1)
        else:
            random1(0)
    return random_mass
