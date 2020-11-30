# Class
# ------


# Naming convension for class
# always start with Capital letter .. e.g, class Email
# if multi word then capitalize each word .. e.g, EmailClient

class Point:   # First letter of the class name is Capitalized
    # Here define all the functions/methods belong to that class
    def move(self):
        print("move")

        
    def draw(self):
        print("draw")


point1 = Point()

point1.draw()

# you can have attributes that belong to a particular object
# attribute is basically variable
point1.x = 10 # no need to have x or y declared beforehand
point1.y = 20

print(point1.x)
print(point1.y)


# Constructor
# ------------
class NewPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
    def move(self):
        print("move")

        
    def draw(self):
        print("draw")


point2 = NewPoint(25, 30)
print(point2.x)
print(point2.y)
point2.x = 30
print(point2.x)



# Exercise
# ---------
class Person:
    def __init__(self, name):
        self.name = name

        
    def talk(self):
        print(f"{self.name}, keep talking")

john = Person("John")
john.talk()
