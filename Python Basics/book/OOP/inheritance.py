class Parent:
    parentAttr = 100

    def __init__(self):
        print("calling parent constructor")

    def parentMethod(self):
        print('calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent Attribute: ', Parent.parentAttr)


class Child(Parent):  # defining the child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('calling child method')


c = Child()  # instance of a child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again cal parent's method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("hello ", self.name, "your are", self.age, "years old")


p1 = Person("Antony", 34)
p1.display()


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


s1 = Student("Juma", 25)
s1.display()