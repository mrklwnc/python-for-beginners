# Lesson 4: Data Types
# * String Data Type

# ? Literal Assignment
first = "Mark Lewence"
last = "Endrano"

# ? use type() to check for the data type of a variable
print(type(first))

# ? Checks if the variable "first" is a string
print(type(first) == str)

# ? Checks if the variable is an instance of a string (or whatever data type you put as the 2nd parameter inside the isinstance() function) and then returns a boolean
print(isinstance(first, str))

# ? Constructor function (str(), int(), bool(), list(), tuple(), dict(), set())
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# ? Concatenation
fullname = first + " " + last
print(fullname)

# ? Casting (Example: Changing an int to a string vice-versa)
decade = str(2001)
print(decade)
print(type(decade))

zipcode = "10001"
zip_value = int(zipcode)
print(zipcode)
print(type(zip_value))

statement = "I was born in the year " + decade + "."
print(statement)

# ? Multiline
multiline = """
    Welcome to the world of Python.

I hope you will be able to continue your experiment with this experiment and continue to learn more about Python.

                                Thank you!
"""

print(multiline)

# ? Escaping special characters
sentence = "I'm escaped!\tI am tabbed right now!\nThis is a new line."
print(sentence)

# ? String Methods
print(first)
print(first.upper())  # Uppercase
print(first.lower())  # Lowercase
print(multiline.title())  # Capitalize every first letter of each word
print(multiline.replace("Thank you!", "Goodbye!"))
print(multiline.strip())  # Remove whitespace
print(multiline.lstrip())  # Remove whitespace on the left side
print(multiline.rstrip())  # Remove whitespace on the right side

# ? Build a Menu
title = "menu".title()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$5".rjust(4))
print("Muffin".ljust(16, ".") + "$3.5".rjust(4))
print("Cheesecake".ljust(16, ".") + "$9.5".rjust(4))

# ? Index
print(first[1])  # Get value at the given index, in this case "1"
print(first[-1])  # Get the last value
print(first[5:-1])  # Get the range [startingIndex:endIndex]
print(first[3:])  # Get the range until the end

# ? Some methods that return boolean data
print(first.startswith("M"))
print(first.endswith("A"))

import math

print(math.pi)  # Pi value
print(math.sqrt(64))  # Square Root
print(math.ceil(3.25))  # Round up
print(math.floor(3.25))  # Round down
