# Lesson 19: Exceptions and Errors


class JustNotCoolException(Exception):
    pass


x = 2
try:
    # print(x / 1)

    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed!")

    # ? Custom Exception
    # raise Exception("I'm a custom exception!")

    # ? Extending Exception class
    raise JustNotCoolException("I'm an exception from an extended Exception class!")
except NameError:
    print("NameError means something probably is undefined.")
except ZeroDivisionError:
    print("Please don't divide by zero")
except Exception as error:
    print(error)
else:
    print("No Errors, congratulations!")
finally:
    print("I'm going to print with or without an error.")

# ? NOTE: https://www.w3schools.com/python/python_ref_exceptions.asp <-- Bunch of Built-in Exceptions here
