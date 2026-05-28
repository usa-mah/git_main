
# We cannot modify a tuple, but we can create a new tuple by concatenating two tuples together
# We can also use the built-in sorted() function to sort a tuple, which returns a new sorted list (since tuples are immutable)
# We can also use the built-in min(), max(), and sum() functions to find the minimum, maximum, and sum of the elements in a tuple
# We can also use the built-in index() and count() methods to find the index of the first occurrence of an element and count the number of occurrences of an element in a tuple
# We can also use the in and not in operators to check if an element is in a tuple or not in a tuple

courses = ("CompSci", "Physics", "History", "Math", "Art")
print(courses)  # Output: ('CompSci', 'Physics', 'History', 'Math', 'Art')
print(courses[0])  # Output: 'CompSci'
print(courses[1])  # Output: 'Physics'
print(courses[-1]) # Output: 'Art'
print(courses[-2]) # Output: 'Math'
print(courses[0:3])  # Output: ('CompSci', 'Physics', 'History')
print(courses[3:])   # Output: ('Math', 'Art')
print(courses[:3])   # Output: ('CompSci', 'Physics', 'History')
print(courses[-3:])  # Output: ('History', 'Math', 'Art')
print(courses[:-3])  # Output: ('CompSci', 'Physics')
print("\n")

courses1 = courses

# courses[0] = "Biology"  # This will raise a TypeError since tuples are immutable

print(courses)
print(courses1)

courses2 = courses + ("Biology",)  # Concatenate the original tuple with a new tuple containing "Biology"
print(courses2)  # Output: ('CompSci', 'Physics', 'History', 'Math', 'Art', 'Biology')

courses3 = ("Biology",) + courses[1:]  # Concatenate a new tuple containing "Biology" with the original tuple
print(courses3)  # Output: ('Biology', 'Physics', 'History', 'Math', 'Art')

# Empty tuple
empty_tuple = ()  # We can also use the built-in tuple() constructor to create an empty tuple
print(empty_tuple)  # Output: ()
empty_tuple2 = tuple()  # Create an empty tuple using the tuple() constructor
print(empty_tuple2)  # Output: ()