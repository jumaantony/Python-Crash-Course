class Parent:
    def myMethod(self):
        print('calling parent method')


class Child:
    def myMethod(self):
        print("calling child method")


c = Child()  # instance of a child
c.myMethod()  # child calls overridden method
