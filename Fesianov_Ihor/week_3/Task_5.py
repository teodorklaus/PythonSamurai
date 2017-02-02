__author__ = 'Ihor'

import Fesianov_Ihor.week_2.my_list_functions as my


class List:
    def __init__(self, *elements):
        self.elements = list(elements)

    def __str__(self):
        label = '{'
        for el in self.elements:
            label += str(el) + ' '
        label = label[:-1] + '}'
        return label

    def minimum(self):
        return my.list_max_min(self.elements)[1]

    def maximum(self):
        return my.list_max_min(self.elements)[0]

    def filling_random(self, minim=0, maxim=9):
        self.elements = my.gererate_random_list(len(self.elements), minim, maxim)

    def increase(self, num=1):
        self.elements.extend(num * [0])

    def print_list(self):
        print(self.__str__())

    def sort_list(self):
        my.select_sort(self.elements)

    def cmp(self, other):
        for i in range(min(len(self.elements), len(other.elements))):
            if self.elements[i] != other.elements[i]:
                return (1, -1)[self.elements[i] < other.elements[i]]
        return 0 if len(self.elements) == len(other.elements) else (1, -1)[len(self.elements) < len(other.elements)]


