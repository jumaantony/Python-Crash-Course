# list comprehension
my_list = [char.upper() for char in 'hello juma']
my_list2 = [number for number in range(0, 100)]

my_list3 = [num ** 2 for num in range(0, 100)]

print(my_list)
print(my_list2)
print(my_list3)

# set comprehension
my_set = {char.upper() for char in 'hello juma'}
my_set2 = {number for number in range(0, 100)}

my_set3 = {num ** 2 for num in range(0, 100)}

print(my_set)
print(my_set2)
print(my_set3)

# dict comprehension
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
my_dict = {
    key: value ** 2 for key, value in simple_dict.items()
}

my_dict2 = {
    num: num ** 2 for num in [1, 2, 3, 4, 5]
}

print(my_dict)
print(my_dict2)

# exercise
some_list = ['a', 'b', 'c', 'a', 'd', 'e', 'd', 'e', 'c', 'f', 'g', 'h']

duplicates = {char for char in some_list if some_list.count(char) > 1}

print(duplicates)
