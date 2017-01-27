__author__ = 'Ihor'

import unittest
import random


class TestsGame(unittest.TestCase):
    def test_guess_the_number(self):
        with self.assertRaises(TypeError):
            guess_the_number(1.5, 10)
            guess_the_number(['15', 100])
            guess_the_number('lknawd')


def guess_the_number(n_min=25, n_max=125):
    win_num = random.randint(n_min, n_max)
    num = int(input('Enter number in range from 25 to 125, including both end points:\n'))
    i = 1
    while i < 5 and num != win_num:
        if num < n_min or num > n_max:
            print('Your number is not in the range.')
        else:
            state = ('higher', 'lower')[num > win_num]
            print('Enter %s number' % state)
            i += 1
        num = int(input('(%i/5)try again:\n' % i))
    print(('You lose\nRight number is ' + str(win_num), 'You win!')[num == win_num])


if __name__ == '__main__':
    guess_the_number()

if __name__ == '__main__':
    unittest.main()
