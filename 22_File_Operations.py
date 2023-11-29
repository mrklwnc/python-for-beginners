# Lesson 22: File Operations

import os

# REMEMBER THESE ACRONYMS
# r = Read
# a = Append (Update)
# w = Write
# x = Create

# * Read - error if it doesn't exist

f = open("txt/names.txt")

# print(f.read())
# print(f.read(4))  # Read the first 4 characters
# print(f.readline())

for line in f:
    print(line)

f.close()  # ? Always remember to close the file

try:
    # f = open("txt/some_names.txt")
    f = open("txt/names.txt")
    print(f.read())
except:
    print("This file doesn't exist")
finally:
    f.close()

# * Append - creates the file if it doesn't exist
f = open(
    "txt/names.txt", "a"
)  # "a" means 'append', by default it is "r" which is 'read'
f.write("Mary\n")
f.close()

f = open("txt/names.txt")
print(f.read())
f.close()

# * Write (Overwrite)
f = open("txt/context.txt", "w")
f.write("I deleted all of the context.")

f = open("txt/context.txt")
print(f.read())
f.close()

# * Create a File (In Two Ways)

# ? Opens a file for writing, if file doesn't exist, create it.
f = open("txt/name_list.txt", "w")
f.close()

# ? Creates the file, but returns an error if the file exists
if not os.path.exists("txt/mark.txt"):
    f = open("txt/mark.txt", "x")
    f.close()

# * Delete a File

# ? Avoid an error if it doesn't exist
if os.path.exists("txt/mark.txt"):
    os.remove("txt/mark.txt")
else:
    print("The file does not exist!")

# Get all contents from this file
with open("txt/more_names.txt") as f:
    content = f.read()

# And overwrite the contents of this
# file with the content from the file above ⬆
with open("txt/names.txt", "w") as f:
    f.write(content)
