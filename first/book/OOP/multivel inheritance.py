class Animal:
    def __init__(self, nutrition):
        self.nutrition = nutrition


class Dog(Animal):
    def __init__(self, sound, nutrition):
        super().__init__(nutrition)
        self.sound = sound


class BabyDog(Dog):
    def __init__(self, sleep, sound, nutrition):
        super().__init__(sound, nutrition)
        self.sleep = sleep

    def display(self):
        print("My puppy sleeps", self.sleep, "a day. It usually",
              self.sound, "in order to be fed", self.nutrition)


d = BabyDog("8 hours", "barking", "biscuits")
d.display()
