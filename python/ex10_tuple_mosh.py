# declare a tuple
# Tuple is different from the list in the sense that it cannot be changed.
# No new value can be added or existing value can be removed. Once a tuple is declared it's immutable.

# Tuple only has 2 methods: count() and index()
# count() --> counts number of occurances of an item
# index() --> finds index of the first occurance of an item

numbers = (1, 4, 2, 6)
print(numbers[0])

# Mostly you wouuld use list, but a tuple is useful when you don't want to accidentally modify a list


# Unpacking of Tuple
# UNPACKINGcan be used with LIST as well
coordinates = (1, 2, 3)

# If wanted to do this calculation
mul_coord = coordinates[0] * coordinates[1] * coordinates[2]
# instead of doing this complex calculation --> coordinates[0] * coordinates[1] * coordinates[2], this is better
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

mul_coord1 = x * y * z

# Even better approach is to do "Unpacking"
a, b, c = coordinates

mul_coord2 = a * b * c

print(mul_coord)
print(mul_coord1)
print(mul_coord2)
