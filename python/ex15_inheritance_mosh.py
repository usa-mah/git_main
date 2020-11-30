# Inheritance
# -----------

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): # inheritance .. Dog inherites from Mammal
    def bark(self):
        print("Woof Woof")


class Cat(Mammal): # inheritance .. Cat inherites from Mammal
    def mew(self):
        print("Mew Mew")


dog1 = Dog()
dog1.walk()
dog1.bark()
