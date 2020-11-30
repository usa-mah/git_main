# How to define a dictionary
# Key:Value pair, just like associative array
# NOTE: The Key must always be unique in a dictionary
customer = {
    "name": "John Smith",
    "email": "john.smith@gmail.com",
    "Phone": "1234"
}


print(customer["name"])

# Error if you try to print a key that doesn't exist in the dictionary
# print(customer["Name"])       --> ERROR
# print(customer["birthdate"])  --> ERROR


# you can use get() method to find if a key exists or not
# It won't error, rather it will give True or False

print(customer.get("birthdate"))

# You can get a default value instead of None if a key is absent
print(customer.get("birthdate", "15 July, 1986"))

# You can change the Value of a Key
customer["name"] = "Jack Smith"
print(customer["name"])


# -------------
# Exercise
# -------------
# Give number input, eg. 1234
# Output would be spelled words, eg, One Two Three Four

phone = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}

user_input = input("Phone: ")

for digit in user_input:
    print(phone.get(digit, "!"),end=" ")
print("\n")

# ------
# Emoji Converter -- revisit this, unable to bring in the emoji
# ------
#

message = input(">")
split_msg = message.split(' ')
# split method splits the string and create a list .. here ' ' is the separator
print(split_msg)

emojis = {
    ":)" : "",
    ":(" : ""
}
# Complete this exercise

