__author__ = 'Ihor'
import math

class Number:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __pow__(self, other):
        exponent = other.value if isinstance(other, Number) else other
        return Number(self.value ** exponent)

    def factorial(self):
        return Number(math.factorial(self.value))

    def __mod__(self, other):
        divider = other.value if isinstance(other, Number) else other
        return Number(self.value % divider)

    def cmp(self, other):
        return 0 if self.value == other.value else (1, -1)[self.value < other.value]
