#names = ['John', 'Mosh', 'Bob', 'Sarah', 'Bulbul', 'Gulllu']
#print(names[1])
#print(names[-1])
#print(names[2:])
#print(names[:2])
#print(names[:])
#names[0] = 'Jon'
#print(names[0])


# Write a program to find the largest number in a list
"""
number = [5, 10, 43, 29, 39, 72, 22]

largest_num = number[0]

for i in number:
    if i > largest_num:
        largest_num = i
print(f"the largest number in the list is {largest_num}")
"""

# 2D List
'''
two_d = [
    [2,3,4],
    [5,6,7],
    [8,9,1]
]

print(two_d[0])
print(two_d[1])
print(two_d[2])
'''


# List Methods

numbers = [5, 2, 1, 7, 5, 4, 7, 5, 2]

# If you want to add or append a new value at the end of  the list
numbers.append(20)
print(numbers)

# If you want to insert a new value (30 and 40) at index (0 and 2 respectively)
numbers.insert(0,30)
numbers.insert(2,40)
print(numbers)

# If you want to remove the value 2 from the list --> it will remove all the 2 present in the list
numbers.remove(2)
print(numbers)
# Why is it only removing the first 2 ?????

# clear() methos will empty the list
temp = [10, 20, 30]
temp.clear()
print(temp)

# Pop the last item from the list
numbers.pop()
print(numbers)

# Pop value at index 3 from the list
numbers.pop(3)
print(numbers)

# Check the index of the value 7 in the list --> this will give an error if the value is not present in the list
print(numbers.index(7)) # To check the index of the value 7 in the list

# Check the index of the value 7 in the list --> this will return FALSE if the value is not present in the list
print(7 in numbers) # To check the index of the value 7 in the list

# Count how many copies of value 5 are present in the list
print(numbers.count(5))

# To sort the list
numbers.sort()
print(numbers)

# To sort the list in reverse order
# First sort the list  numbers.sort() as above
numbers.reverse()
print(numbers)

# To copy the list
numbers2 = numbers.copy()
print(numbers2)

# Anything I do to numbers after the above operation, it will have no impact on numbers2
numbers.append(50)
print(numbers2)
print(numbers)

# Clear the list
numbers.clear()
print(numbers)

# Bring back the numbers
numbers = numbers2.copy()
numbers.append(50)
print(numbers)

# Write a program to remove duplicates in a list
numbers3 = []
for item in numbers:
    if item not in numbers3:
        numbers3.append(item)

print(numbers3)
