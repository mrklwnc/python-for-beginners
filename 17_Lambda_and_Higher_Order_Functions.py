# Lesson 17: Lambda & Higher-Order Functions

# * NOTE: Lambda is also known as anonymous function in Javascript

squared = lambda x: x * x

print(squared(2))

my_function = lambda x: print(x)

my_function(12)

# Multiple parameters
sum_total = lambda x, y: print(x + y)
sum_total(1, 2)


# Lambda Function
def sample_func(x):
    return lambda y: x * y


# Double the number
mydoubler = sample_func(2)
print(mydoubler(11))

# Triple the number
mytripler = sample_func(3)
print(mytripler(11))


# * Higher-Order Functions are functions that receives a function as an argument or if it returns a function

# Passing a lambda function as an argument
numbers = [3, 4, 5, 6, 7, 8]

# Map
squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

# Filter
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

from functools import reduce

# Using reduce(function, data, initial/starting value) function
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
# ? NOTE: Initial/Starting value is OPTIONAL for numbers

print(total)

# Using Sum
print(sum(numbers, 10))


# Using reduce in a list of strings
names = ["John", "Jacob", "Jane", "Mark", "Job"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
# ? NOTE: Initial/Starting value is REQUIRED for strings

print(char_count)
