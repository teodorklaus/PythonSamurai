import unittest
import random


class test_arifm_part(unittest.TestCase):
    def test_bigeest_mass_part(self):
        with self.assertRaises(TypeError):
            bigeest_mass_part (1)
        test_list = [1, 2, 5, 8, 7, 4, 6, 9, 3, 10]
        self.assertEqual(bigeest_mass_part([1, 2, 3, 4, 5, 2, 1, 3, 4, 5]), 'part1 = part2')
        self.assertTrue(bigeest_mass_part(test_list), [4, 6, 9, 3, 10])
        self.assertEqual(bigeest_mass_part([1, 2, 3]), 'Length is not / 2')



def bigeest_mass_part(mass):
    if len(mass) % 2 == 0:
        part1 = mass[:int(len(mass) / 2)]
        part2 = mass[int(len(mass) / 2):]
        if float(sum(part1) / len(part1)) == float(sum(part2) / len(part2)):
            return 'part1 = part2'
        else:
            return (part1, part2)[float(sum(part1) / len(part1)) > float(sum(part2) / len(part2))]
    else:
        return 'Length is not / 2'

