# Use python built in module --> random

import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))


# Randomly pick an item from a list

members = ["Kaka", "Tua", "Joma", "Vua", "Patrik"]
leader = random.choice(members)
print(leader)


# Exercise -- Roll the dice
# -------------------------


class Dice:
    def roll(self):
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        tupl = (first, second)
        return tupl


dice1 = Dice()
my_dice = dice1.roll()
print(my_dice)
