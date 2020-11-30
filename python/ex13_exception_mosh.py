# Exception
# ----------
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Value')


# Comments
# ---------

# --> This is single line comment

'''
This is multiple lines
comment
'''

"""
This is also multiple line
comment
"""
