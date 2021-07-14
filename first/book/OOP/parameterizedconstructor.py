class Student:
    # constructor parameterized
    def __init__(self, name):
        print("This is a parameterized constructor")
        self.name = name

    def show(self):
        print("Hellow", self.name)


std = Student('Wicked')
std.show()
