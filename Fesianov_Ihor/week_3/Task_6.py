__author__ = 'Ihor'

import Fesianov_Ihor.week_2.my_list_functions as my


class String:
    __low_alphabet = list('abcdefghijklmnopqrstuvwxyz')
    __cap_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self, symbols):
        self.symbols_list = symbols
        self.__make_represent()

    def __make_represent(self):
        self.represent = ''
        for el in self.symbols_list:
            self.represent += str(el)

    def __str__(self):
        return self.represent

    def concat(self, other):
        return String(self.symbols_list + other.symbols_list)

    def print(self):
        print(self.__str__())

    def __replace_symbol(self, from_alph, to_alph):
        new_list = []
        for i in range(len(self.symbols_list)):
            if self.symbols_list[i] in from_alph:
                new_list.append(to_alph[from_alph.index(self.symbols_list[i])])
            else:
                new_list.append(self.symbols_list[i])
        return String(new_list)

    def lower(self):
        return self.__replace_symbol(self.__cap_alphabet, self.__low_alphabet)

    def upper(self):
        return self.__replace_symbol(self.__low_alphabet, self.__cap_alphabet)

    def del_space(self):
        return self.__replace_symbol([' '], [''])

    def find(self, other, start=0):
        if other.symbols_list[0] in self.symbols_list[start:]:
            first_index = start + self.symbols_list[start:].index(other.symbols_list[0])
            for i in range(1, len(other.symbols_list)):
                if other.symbols_list[i] != self.symbols_list[first_index + i]:
                    return self.find(other, first_index + 1)
            return first_index
        return -1

    def substring(self, start=0, end=1):
        return String(self.symbols_list[start:end])

    def cmp(self, other):
        return my.cmp(self.symbols_list, other.symbols_list)

a = String([4, 2, 6, 5, 'a', 'f', 'f', 'a'])
b = String(['N', ' ', 'A', 'i', 3, 5, ' ', 5, ' '])
c = String(list('spagmeggg,ga   sgas  jjhjh'))
d = String(list('gas'))

print(c.find(d))
