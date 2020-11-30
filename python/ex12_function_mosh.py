
# Function
#-------------------
def greet_user():
    print('Hi there')
    print('Welcome aboard')


#after Function define must add 2 empty lines

print("Start")
greet_user()
print("Finish")



# Function parameter
#--------------------
def greet_newuser(name = "Usama"): # Here name is parameter, "Usama" is default
    print(f'Hi {name}')
    print('Welcome aboard')



print("Start")
greet_newuser("John") # Here "John" is the argument
greet_newuser("Mary")
greet_newuser()
print("Finish")



# Function with 2 parameters
#-----------------------------
def greet_newuser(first_name = "Usama", last_name = "Mahboob"):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')



print("Start")
greet_newuser("John", "Stewart")
greet_newuser("Mary", "Mitchel")
greet_newuser()
print("Finish")
print("\n\n")


# Keyword Argument
#------------------
# If you explicitly specify aan argument for a parameter, then position of 
# that argument don't matter

# ^ this is called Keyword Argument

greet_newuser(last_name="Stewart", first_name="John")

# if you are going to use one positional argument and one keyword argument
# then use the positional argument first
# eg., greet_newuser("John", last_name="Stewart")
# ^ this is valid.. but the following is invalid
# eg., greet_newuser(first_name = "John", "Stewart")



# Return Statement
#-------------------

def square(number):
    return number*number

print(square(3))


def square(number):
    print(number*number)
    return None # by default a function returns None anyway


square(3)
