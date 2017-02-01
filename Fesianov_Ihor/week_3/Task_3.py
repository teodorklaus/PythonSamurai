__author__ = 'Ihor'


def gcd(num1, num2):
    """
    Euclidean algorithm.
    Method for computing the greatest common divisor
    """
    return num2 if num1 % num2 == 0 else gcd(num2, num1 % num2)


def lcm(num1, num2):
    """
    Least common multiple.
    Method for computing the least common multiple
    """
    return num1 * num2 // gcd(num1, num2)


class Fraction:
    def __init__(self, numerator=1, denominate=1):
        if numerator < 0 and denominate < 0:
            numerator = abs(numerator)
            denominate = abs(denominate)
        elif denominate < 0:
            numerator *= -1
            denominate = abs(denominate)
        self.numerator = numerator
        self.denominate = denominate
        self.value = self.numerator / self.denominate

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominate)

    def __sub__(self, other):
        new_first_numerator = lcm(self.denominate, other.denominate) * self.numerator // self.denominate
        new_second_numerator = lcm(self.denominate, other.denominate) * other.numerator // other.denominate
        new_num = new_first_numerator - new_second_numerator
        new_den = lcm(self.denominate, other.denominate)
        return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

    def __add__(self, other):
        return self - (Fraction(0, 1) - other)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominate * other.denominate
        return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

    def __truediv__(self, other):
        new_num = self.numerator * other.denominate
        new_den = self.denominate * other.numerator
        return Fraction(new_num // gcd(new_num, new_den), new_den // gcd(new_num, new_den))

    def show(self):
        print('{}/{}'.format(self.numerator, self.denominate))

    def cmp(self, other):
        eps = 0.000001
        return 0 if abs(self.value - other.value) < eps else (1, -1)[self.value < other.value]


a = Fraction(4, 3)
b = Fraction(4, 6)
c = a / b
print(c)
