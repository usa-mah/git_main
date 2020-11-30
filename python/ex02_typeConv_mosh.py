#"""
birth_year = input('Birth Year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(f'your age is {age}')
#"""


'''
EXERCISE 02 - Type Conversion
------------ -----------------
Exercise 02 asks a user their weight (in pounds) convert it to kilograms and print on the terminal
'''

weight_pound = input('Hey what\'s your weight in pound? ')
weight_kg = 0.45 * float(weight_pound)
print(f'Oi, your weight in Kg is {weight_kg}')
