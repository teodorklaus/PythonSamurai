__author__ = 'Ihor'


class Calc:
    actions = {0: '+', 1: '-', 2: '*', 3: '/'}

    def get_key(self, value):
        for key in self.actions:
            if self.actions[key] == value:
                return key

    def __init__(self):
        self.first_num = 0
        self.second_num = 0
        self.result = 0
        self.action = 0

    def addition(self):
        self.result = self.first_num + self.second_num

    def subtraction(self):
        self.result = self.first_num - self.second_num

    def multiplication(self):
        self.result = self.first_num * self.second_num

    def division(self):
        self.result = self.first_num / self.second_num

    def calculation(self):
        if self.action == 0:
            self.addition()
        elif self.action == 1:
            self.subtraction()
        elif self.action == 2:
            self.multiplication()
        elif self.action == 3:
            self.division()
        else:
            print('action was entered incorrectly')

    @staticmethod
    def is_exit():
        flag = input('''Enter 'ex' to exit ''')
        return (False, True)[flag == 'ex']

    def running(self):
        while not self.is_exit():
            self.first_num = int(input('enter the first number:\n'))
            self.action = self.get_key(input('enter action: +, -, *, /\n'))
            self.second_num = int(input('enter the second number:\n'))
            self.calculation()
            print('{} {} {} = {}'.format(self.first_num, self.actions[self.action], self.second_num, self.result))

