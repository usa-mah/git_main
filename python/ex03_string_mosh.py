
course0 = 'Python for Beginners'

course = '''
Hi John,

This is all taken care of. 
Eat the zebra now!


Regards,
John Boom

'''
print (course)

another = course0[1:-1]
print(another)



'''
EXERCISE 03 - String / Formatted String / String method
------------ ----------------- --------- ----------------
Exercise 03 asks
'''
first = 'John'
last = 'Smith'
message  = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder'

print(message)
print(msg)

print(len(course0))

print(course0.capitalize())
print(course0.upper())
print(course0.lower())
print(course0.find('o')) # finds the index of 'o' in course0
print(course0.find('Beginners')) # the starting index of Beginners is 11
print(course0.replace('Beginners', 'Absolute Beginners')) # replace Beginners with 'Absolute Beginners'
print(course0.replace('o', 'boom')) # replaces 'o' with 'boom'
print('Python' in course0) # returns TRUE if Python is there in the course0

print(course0) # despite course0.replace in above lines, the original course0 remains as it was at the start