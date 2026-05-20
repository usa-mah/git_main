
message = "Hello World!"
message1 = 'Halo, Walt!'
multi_line_message = """This is a multi-line string.
It can span multiple lines.
Like this."""

print('Hello, World')
print(message)
print(message1)
print('Bobby\'s World!')
print("Bobby's World!")
print("Happy \"World\"")
print(multi_line_message)

print("\n")

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

print("\n")

# String repetition
echo = "Echo! " * 3
print(echo)
print("\n")

# String indexing
word = "Python"
print(word[0])  # Print the first character
print(word[1])  # Print the second character
print(word[-1]) # Print the last character
print(word[-2]) # Print the second to last character
print("\n")
# String slicing
print(word[0:3])  # Print the first three characters
print(word[3:])   # Print from the fourth character to the end
print(word[:3])   # Print the first three characters
print(word[-3:])  # Print the last three characters
print(word[:-3])  # Print all but the last three characters
print("\n")


# String methods
print(word.upper())  # Convert to uppercase
print(word.lower())  # Convert to lowercase
print(word.capitalize())  # Capitalize the first letter
print(word.replace("o", "0"))  # Replace 'o' with '0'
print(word.split("t"))  # Split the string at 't'
print(word.find("h"))  # Find the index of 'h' (= 3)
print(message.find("World"))  # Find the index of 'World' in the message (= 6)
print(message.find("Universe"))  # Find the index of 'Universe' in the message (not found, returns -1)
print(message.replace("World", "Universe"))  # Replace 'World' with 'Universe' in the message
print(word.count("o"))  # Count the occurrences of 'o'
print(word.startswith("Py"))  # Check if the string starts with "Py"
print(word.endswith("on"))  # Check if the string ends with "on"
print(word.isalpha())  # Check if the string contains only letters
print(word.isdigit())  # Check if the string contains only digits
print(word.islower())  # Check if the string is in lowercase
print(word.isupper())  # Check if the string is in uppercase
print(word.strip())  # Remove leading and trailing whitespace
print(word.center(20))  # Center the string within a width of 20 characters
print(word.ljust(20))  # Left-justify the string within a width of 20 characters
print(word.rjust(20))  # Right-justify the string within a width of 20 characters
print(word.zfill(10))  # Pad the string with zeros on the left to a total width of 10 characters
print(word.swapcase())  # Swap the case of each character
print(word.title())  # Convert the string to title case
print(word.isalnum())  # Check if the string is alphanumeric
print(word.isascii())  # Check if the string contains only ASCII characters
print(word.isprintable())  # Check if the string is printable
print("\n")


# String formatting
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)
print("\n")
michael = "Michael"
language = "Python"
formatted_string1 = f"{michael} is learning {language}."
formatted_string2 = "{} is learning {}.".format(michael, language)
formatted_string3 = f"{michael} is learning {language.upper()}."
print(formatted_string1)
print(formatted_string2)
print(formatted_string3)
print("\n")
# String length
print(len(word))  # Print the length of the string





print("\n")
print("\n")
print("\n")
print(dir(str))  # Print all the attributes and methods of the str class
# print(help(str.upper))  # Print the documentation for the upper() method of the str class
# print(help(str))  # Print the documentation for the str class