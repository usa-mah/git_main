
student = {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'CompSci']}
print(student)  # Output: {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'CompSci']}
print(len(student))  # Output: 3
print(student.keys())  # Output: dict_keys(['name', 'age', 'courses'])
print(student.values())  # Output: dict_values(['John Doe', 20, ['Math, 'CompSci']])
print(student.items())  # Output: dict_items([('name', 'John Doe'), ('age', 20), ('courses', ['Math', 'CompSci'])
print(student['name'])  # Output: 'John Doe'
print(student['age'])  # Output: 20
print(student['courses'])  # Output: ['Math', 'CompSci']
print(student.get('name'))  # Output: 'John Doe'
print(student.get('phone'))  # Output: None
print(student.get('phone', 'Not Found'))  # Output: 'Not Found'
student['phone'] = '555-5555'  # Add a new key-value pair
print(student)  # Output: {'name': 'John Doe', 'age': 20, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
print(student.get('phone', 'Not Found'))  # Output: '555-5555'
student['name'] = 'Jane Doe'  # Update the value of an existing key
print(student)  # Output: {'name': 'Jane Doe', 'age': 20, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
student.update({'name': 'John Doe', 'age': 21})  # Update multiple key-value pairs
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
del student['phone']  # Remove a key-value pair
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'courses': ['Math', 'CompSci']}
print(student.pop('age'))  # Output: 21
print(student)  # Output: {'name': 'John Doe', 'courses': ['Math', 'CompSci']}
print(student.popitem())  # Output: ('courses', ['Math', 'CompSci'])
print(student)  # Output: {'name': 'John Doe'}
print(student.keys())  # Output: dict_keys(['name'])
print(student.values())  # Output: dict_values(['John Doe'])
print(student.items())  # Output: dict_items([('name', 'John Doe')])
print('name' in student)  # Output: True
print('age' in student)  # Output: False
print('age' not in student)  # Output: True
student['age'] = 22  # Add a new key-value pair
student['courses'] = ['Math', 'CompSci']  # Add a new key-value pair

for key, value in student.items():
    print(f"{key}: {value}")  # Output: 'name: John Doe', 'age: 22', 'courses: ['Math', 'CompSci']' (each on a new line)
    print(key, value)  # Output: 'name John Doe', 'age 22', 'courses ['Math', 'CompSci']' (each on a new line)