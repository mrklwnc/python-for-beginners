# Lesson 6: Lists and Tuples

#             Mutable | Ordered | Indexing | Duplicate Data
# LIST           ✔        ✔        ✔             ✔
# TUPLE          ❌       ✔        ✔             ✔
# SET            ✔        ❌       ❌            ❌
# DICTIONARY     ✔        ✔        ✔             ❌

# * Lists
letters = ["a", "b", "c", "d", "e"]
words = ["One", "Two", "Three", "Four", "Five"]

# ? Add a data into the list

# Using append
letters.append("f")

#  Using +=
letters += ["g", "h", "i", "j", "k"]

# Using extend()
letters.extend(["l", "m", "n", "o", "p"])

# Using an existing list
letters.extend(words)

# Adding into a controlled position
letters.insert(0, "Z")

# Using range
letters[2:2] = ["Six", "Seven"]

# Replacing data from the list (also known as splice() method)
letters[1:3] = ["Eight", "Nine"]

# Removing data from the list
letters.remove("Z")

# Removing the last data from the list
letters.pop()

# Using "del" to delete a data inside the list (NOTE: You can also use it to delete the whole list)
# del letters[8]

# Delete the whole "letters" list
# del letters

# Clear the list
# letters.clear()

# When sorting, lowercase comes last
letters.sort()

print(letters)

nums = [48, 5, 63, 72, 28, 19]

nums.reverse()

# nums.sort(reverse=True)  # Sorted Descending
# print(nums)

# Global Sort
print(sorted(nums, reverse=True))

# Making a copy of the list
firstCopy = nums.copy()
secondCopy = list(nums)
thirdCopy = nums[:]

# * Tuples

myTuple = tuple((1, "Mark", {"hobbies": ["Coding", "Video Games", "Singing"]}))
anotherTuple = (
    2,
    "Ronald",
    {"hobbies": ["Coding", "Video Games", "Dancing"]},
    23,
    "Philippines",
    "Philippines",
    "Philippines",
    "Philippines",
    "Philippines",
)

print(myTuple)
print(anotherTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append("Lewence")
newTuple = tuple(newList)
print(newTuple)

# Unpacking tuples
(one, *two, three) = anotherTuple
print(one)
print(two)
print(three)
# The one with the asterisk holds the remaining data inside the tuple
# Those without the asterish holds 1 data from the tuple

# Count the number of times the data has been repeated inside the tuple
print(anotherTuple.count("Philippines"))
