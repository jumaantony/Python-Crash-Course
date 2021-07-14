class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age


action_figure = Toy('red', 0)
print(action_figure.__str__())

# execise 

class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))

super_list1.append(5)

print(super_list1[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))