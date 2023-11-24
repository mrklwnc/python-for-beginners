# Lesson 8: For and While Loops

# * For Loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping through a string
for x in "Hello":
    print(x)

# The BREAK statement
for x in fruits:
    print(x)
    if x == "banana":
        break
# ? NOTE: It breaks the loop when "banana" is found

#  The CONTINUE statement
for x in fruits:
    print(x)
    if x == "banana":
        continue
# ? NOTE: It repeats the loop once again once "banana" is found

# The RANGE Function
for x in range(
    5
):  # ? Starts by 0 by default and stops before hitting the specified value
    print(x)

for x in range(2, 30, 3):  # ? Syntax: range(start, end, increment)
    print(x)

# Else in For Loop
for x in range(5):
    print(x)
else:
    print("Finished!")
# ? NOTE: Else block will not execute if the loop is stopped by a "break" statement

adj = ["red", "big", "tasty"]

# Nested For Loop
for x in adj:
    for y in fruits:
        print(x, y)

# The PASS statement
for x in [0, 1, 2, 3, 4, 5]:
    pass


# * While Loop

i = 1
while i < 6:
    print(i)
    i += 1

# The BREAK and CONTINUE statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # ? Just change this to "continue" for the CONTINUE statement
    i += 1

# The ELSE statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
