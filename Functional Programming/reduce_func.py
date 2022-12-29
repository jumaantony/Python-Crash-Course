"""The reduce(fun,seq) function is used to apply a particular function passed in 
its argument to all of the list elements mentioned in the sequence passed 
along.This function is defined in “functools” module."""

from functools import reduce

my_list = [2, 3, 4, 5]


"""def multipliy_by_2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0"""


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 5))
