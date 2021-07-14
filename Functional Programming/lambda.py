# lambda expressions are one time anonymous functions
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def multipliy_by_2(item):
    return item * 2


print(list(map(lambda item: item*2, my_list)))
