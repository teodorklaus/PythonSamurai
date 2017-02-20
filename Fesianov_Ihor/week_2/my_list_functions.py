__author__ = 'Ihor'

import random


def input_list():
    n = int(input('enter lists size:\n'))
    print('enter lists elements')
    list1 = []
    for i in range(n):
        list1.append(float(input()))
    print(list1)
    return list1


def list_max_min(lis):
    max = lis[0]
    min = lis[0]
    for el in lis:
        if el > max:
            max = el
        if el < min:
            min = el
    return (max, min)


def arithmetic_mean(lis):
    summ = 0
    for el in lis:
        summ += float(el)
    return summ / len(lis)


def replace_max_min(ar):
    maxx = list_max_min(ar)[0]
    minn = list_max_min(ar)[1]
    for i in range(len(ar)):
        if ar[i] == maxx:
            ar[i] = minn
        elif ar[i] == minn:
            ar[i] = maxx


def gererate_random_list(length=random.randint(1, 10), mini=0, maxi=9):
    rand_list = []
    for i in range(length):
        rand_list.append(random.randint(mini, maxi))
    return rand_list


def bigger_lists_half(mass):
    if len(mass) % 2 == 0:
        half1 = mass[:int(len(mass) / 2)]
        half2 = mass[int(len(mass) / 2):]
        if arithmetic_mean(half1) == arithmetic_mean(half2):
            return 'arithmetic mean of lists half is the same'
        else:
            return (half2, half1)[arithmetic_mean(half1) > arithmetic_mean(half2)]
    else:
        return 'lists length is odd'


def is_len_the_same(list1, list2):
    return (False, True)[len(list1) == len(list2)]


def sum_list(list1, list2):
    if not is_len_the_same(list1, list2):
        return 'length of list must be the same'
    output = []
    for i in range(len(list1)):
        output.append(list1[i] + list2[i])
    return output


def generate_specific_random_list(length=random.randint(1, 10)):
    def adder(var):
        el = random.randint(0, 100)
        while el % 2 == var:
            el = random.randint(0, 100)
        rand_list.append(el)

    rand_list = []
    for i in range(length):
        if i % 2 == 0:
            adder(1)
        else:
            adder(0)
    return rand_list


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n_1 = 0
    n_2 = 1
    for i in range(1, n + 1):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result


def list_copy(from_list, from_index, to_list, to_index, count):
    range_list = from_list[from_index:from_index + count]
    to_list[to_index:to_index + count] = range_list[:]


def shift(mass, m):
    n = m % len(mass)
    mass_copy = mass[:]
    for i in range(len(mass)):
        if i < n:
            mass[i] = mass[i + len(mass) - n]
        else:
            mass[i] = mass_copy[i - n]


def select_sort(mass):
    for i in range(len(mass)):
        ind = i + mass[i:].index(min(mass[i:]))
        t = mass[ind]
        mass[ind] = mass[i]
        mass[i] = t


def insert_sort(mass):
    for i in range(1, len(mass)):
        j = i
        el = mass.pop(j)
        while el < mass[j - 1] and j > 0:
            j -= 1
        mass.insert(j, el)


def find(ar, subar, start=0):
    if subar[0] in ar[start:]:
        first_index = start + ar[start:].index(subar[0])
        for i in range(1, len(subar)):
            if subar[i] != ar[first_index + i]:
                return find(ar, subar, first_index + 1)
        return first_index
    return -1


def cmp(list1, list2):
    for i in range(min(len(list1), len(list2))):
        if list1[i] != list2[i]:
            return (1, -1)[list1[i] < list2[i]]
    return 0 if len(list1) == len(list2) else (1, -1)[len(list1) < len(list2)]
