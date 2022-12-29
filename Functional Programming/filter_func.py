# The filter() function returns an iterator where 
# the items are filtered through a function to test 
# if the item is accepted or not.

my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def multipliy_by_2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))
