"""
-generators are available in python and allows generation of a
sequence of values over time e.g range.
-they are useful when calculating large sets of data
-used when processing long loops that needs not to be stored in the memory
"""


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(50)
print(my_list)


# print(list(range(1000000)))


def generator_func(num):
    for i in range(num):
        yield i


"""for item in generator_func(1000):
    print(item)"""

g = generator_func(100)
next(g)
next(g)
print(next(g))


# creating our own range func
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0,100)
for i in gen:
    print(i)
