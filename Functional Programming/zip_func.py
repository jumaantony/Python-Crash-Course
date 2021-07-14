my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
your_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
their_list = [5, 8, 9, 7, 5, 6]


def multipliy_by_2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


print(list(zip(your_list, my_list, their_list)))
