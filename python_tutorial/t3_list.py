
courses = ["History", "Math", "Physics", "CompSci"]
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci']
print(courses[0])  # Output: 'History'
print(courses[1])  # Output: 'Math'
print(courses[2])  # Output: 'Physics'
print(courses[3])  # Output: 'CompSci'
print(courses[-1])  # Output: 'CompSci'
print(courses[0:2])  # Output: ['History', 'Math']
print(courses[2:])  # Output: ['Physics', 'CompSci']
print(courses[:2])  # Output: ['History', 'Math']
print(courses[:])  # Output: ['History', 'Math', 'Physics', 'CompSci']
print("\n")

courses.append("Art")  # Add 'Art' to the end of the list
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']
courses.insert(0, "Biology")  # Insert 'Biology' at index 0
print(courses)  # Output: ['Biology', 'History', 'Math', 'Physics', 'CompSci', 'Art']
courses.remove("Math")  # Remove 'Math' from the list
print(courses)  # Output: ['Biology', 'History', 'Physics', 'CompSci', 'Art']
courses.pop()  # Remove the last item
print(courses)  # Output: ['Biology', 'History', 'Physics', 'CompSci']
courses.pop(0)  # Remove the item at index 0
print(courses)  # Output: ['History', 'Physics', 'CompSci']
courses.reverse()  # Reverse the order of the list
print(courses)  # Output: ['CompSci', 'Physics', 'History']
courses.sort()  # Sort the list in alphabetical order
print(courses)  # Output: ['CompSci', 'History', 'Physics']
courses.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(courses)  # Output: ['Physics', 'History', 'CompSci']
print("\n")

courses_2 = ["Art", "Education"]
all_courses = courses + courses_2  # Concatenate the two lists
print(all_courses)  # Output: ['Physics', 'History', 'CompSci', 'Art', 'Education']
print(len(all_courses))  # Output: 5
courses.insert(0, courses_2)  # Insert the second list as a single element at index 0
print(courses)  # Output: [['Art', 'Education'], 'Physics', 'History', 'CompSci']
print(courses[0])  # Output: ['Art', 'Education']
print(courses[0][0])  # Output: 'Art'
print(courses[0][1])  # Output: 'Education'

courses.remove(courses_2)  # Remove the second list from the first list
print(courses)  # Output: ['Physics', 'History', 'CompSci']

courses.insert(0, courses_2)  # Insert the second list as a single element at index 0 again
courses.pop(0)  # Remove the first element (the second list)
print(courses)  # Output: ['Physics', 'History', 'CompSci']

courses.extend(courses_2)  # Extend the list by adding elements from the second list
print(courses)  # Output: ['Physics', 'History', 'CompSci', 'Art', 'Education']

new_courses = sorted(courses)  # Create a new sorted list without modifying the original
print(new_courses)  # Output: ['Art', 'CompSci', 'Education', 'History', 'Physics']
print(courses)  # Output: ['Physics', 'History', 'CompSci', 'Art', 'Education']


nums = [1, 6, 2, 5, 3]
print(nums)  # Output: [1, 6, 2, 5, 3]
print(min(nums))  # Output: 1
print(max(nums))  # Output: 6
print(sum(nums))  # Output: 17
nums.sort()  # Sort the list in ascending order
print(nums)  # Output: [1, 2, 3, 5, 6]
nums.sort(reverse=True)  # Sort the list in descending order
print(nums)  # Output: [6, 5, 3, 2, 1]

new_nums = sorted(nums)  # Create a new sorted list without modifying the original
print(new_nums)  # Output: [1, 2, 3, 5, 6]
print(nums)  # Output: [6, 5, 3, 2, 1]

print(min(nums)) # Output: 1
print(max(nums)) # Output: 6
print(sum(nums)) # Output: 17

print("\n")

print(courses.index("History"))  # Output: 1
print(courses.count("History"))  # Output: 1
print(courses.count("Math"))  # Output: 0

print('Art' in courses)  # Output: True
print('Math' in courses)  # Output: False
print('Math' not in courses)  # Output: True


print("\n")

for item in courses:
    print(item)    # Output: 'Physics', 'History', 'CompSci', 'Art', 'Education' (each on a new line)

# Using enumerate to get both index and value
# The enumerate function adds a counter to an iterable and returns it as an enumerate object.
# This allows you to loop through the items in a list while also keeping track of the index of each item.
for index, course in enumerate(courses):
    print(index, course)  # Output: 0 Physics, 1 History, 2 CompSci, 3 Art, 4 Education (each on a new line)

print("\n")

for index, course in enumerate(courses, start=1):  # Start counting from 1 instead of 0
    print(index, course)

course_str = ', '.join(courses)  # Join the list into a string with ', ' as the separator
print(course_str)  # Output: 'Physics, History, CompSci, Art, Education

course_str2 = ' - '.join(courses)  # Join the list into a string with ' - ' as the separator
print(course_str2)  # Output: 'Physics - History - CompSci - Art - Education'

new_list = course_str2.split(' - ') # Split the string back into a list using ' - ' as the separator
print(new_list)  # Output: ['Physics', 'History', 'CompSci', 'Art', 'Education']

# Empty list
empty_list = []  # We can also use the built-in list() constructor to create an empty list
print(empty_list)  # Output: []
empty_list2 = list()  # Create an empty list using the list() constructor
print(empty_list2)  # Output: []

