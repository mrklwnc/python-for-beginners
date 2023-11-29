# Lesson 9: Functions


# * Creating a function
def my_first_function():
    print("Hello World!")


my_first_function()  # Call it


# Function with arguments
def my_fullname(fname, lname):
    print(fname + " " + lname)


my_fullname("Mark Lewence", "Endrano")


# ? Arbitrary Arguments - If you don't know how many arguments you'll expect
def list_ingredients(*ingredients):  # ? ingredients parameter becomes a TUPLE
    print("Food Ingredient/s: ", ingredients)  # ? Can access items using index

    for ingredient in ingredients:  # ! Just a test
        print(ingredient)


list_ingredients("Tomatoes", "Potatoes", "Onions", "Garlic")


# Keyword Arguments
def my_children(child3, child2, child1):
    print("The eldest child is " + child1)
    print("The middle child is " + child2)
    print("The youngest child is " + child3)


# ? The keys used here reference the parameter names inside the function
my_children(child1="Emil", child2="Tobias", child3="Linus")  # Output: Linus
my_children(child3="Emil", child2="Tobias", child1="Linus")  # Output: Emil


# Arbitrary Keyword Arguments - see Arbitrary Arguments for the definition
def my_kid(**kid):
    print("His last name is " + kid["lname"])  # Output: Endrano


my_kid(fname="Mark", lname="Endrano", age=20)


# Default Parameter Value
def my_country(country="Philippines"):
    print("His country is in " + country)


my_country("Canada")

# ? You can pass a list, tuple, dictionary, or a set as an argument


# Return Values
def my_sum(*numbers):
    return sum(numbers)


print(my_sum(1, 2, 3, 4, 5))


# PASS statement
def empty_function():
    # ? NOTE: Function definition cannot be empty, to avoid error, use PASS statement

    # To be filled with logic later on
    pass
