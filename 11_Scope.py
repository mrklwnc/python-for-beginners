# Lesson 11: Scope


# ? A scope is a variable avaialable only in the place it is created.


# Global Scope - created in the main body
x = 100  # ? This is a global scope


def my_otherfunction():
    print(x)  # I am used inside this function but still, I am a global scope


my_otherfunction()


# Local Scope - created inside a function
def my_function():
    x = 300  # ? This is a local scope
    print(x)

    def my_innerfunction():  # ? I am also a local scope
        print("I am an inner function!")

    my_innerfunction()


my_function()
# ? Functions can also be a local scope


# ? Can you see the variable x?
# ? x is used as a global and a local variable, local scope's are priority to be printed even though they are the same variable name


# Global Keyword
def my_lastfunction():
    global x
    x = "I am a Global Keyword inside a function"


my_lastfunction()

print(x)


# Change the Value of a Global variable/scope inside a function
x = "I am a Global scope"


def myfunc():
    global x  # ?If you comment this, the global scope will get printed instead
    x = "Just changed the global scope by refering to it as a global keyword"


myfunc()

print(x)
