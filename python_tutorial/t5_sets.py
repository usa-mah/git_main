
# Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor.
# Sets do not allow duplicate elements, and they are mutable, meaning we can add or remove elements from a set after it has been created.
# Sets are useful for performing mathematical set operations like union, intersection, difference, and symmetric difference.


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)  # Output: {'History', 'Math', 'Physics', 'CompSci'}
print('Math' in cs_courses)  # Output: True
print('Art' in cs_courses)  # Output: False
print('Art' not in cs_courses)  # Output: True

art_courses = {'History', 'Math', 'Art', 'Design'}
print(art_courses)  # Output: {'History', 'Math', 'Art', 'Design'}

# Set operations
print(cs_courses.intersection(art_courses))  # Output: {'History', 'Math'}
print(cs_courses.union(art_courses))  # Output: {'History', 'Math', 'Physics', 'CompSci', 'Art', 'Design'}
print(cs_courses.difference(art_courses))  # Output: {'Physics', 'CompSci'}
print(art_courses.difference(cs_courses))  # Output: {'Art', 'Design'}
print(cs_courses.symmetric_difference(art_courses))  # Output: {'Physics', 'CompSci', 'Art', 'Design'}

cs_courses.add('Data Science')  # Add a new course to the set
print(cs_courses)  # Output: {'History', 'Math', 'Physics', 'CompSci', 'Data Science'}
cs_courses.remove('Math')  # Remove a course from the set
print(cs_courses)  # Output: {'History', 'Physics', 'CompSci', 'Data Science'}
cs_courses.discard('Art')  # Remove 'Art' from the set if it exists, do nothing if it doesn't exist
print(cs_courses)  # Output: {'History', 'Physics', 'CompSci', 'Data Science'}
cs_courses.discard('Math')  # Remove 'Math' from the set if it exists, do nothing if it doesn't exist ('Math' has already been removed)
print(cs_courses)  # Output: {'History', 'Physics', 'CompSci', 'Data Science'}
cs_courses.clear()  # Remove all elements from the set
print(cs_courses)  # Output: set()

# We can also use the built-in len() function to find the number of elements in a set, and the built-in sorted() function to sort a set (which returns a new sorted list since sets are unordered).
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(len(cs_courses))  # Output: 4
print(sorted(cs_courses))  # Output: ['CompSci', 'History', 'Math', 'Physics']

# We can also use the built-in min() and max() functions to find the minimum and maximum elements in a set (based on alphabetical order for strings).
print(min(cs_courses))  # Output: 'CompSci'
print(max(cs_courses))  # Output: 'Physics'

# Empty set
empty_set = set()  # We cannot use {} to create an empty set since it creates an empty dictionary instead
print(empty_set)  # Output: set()
