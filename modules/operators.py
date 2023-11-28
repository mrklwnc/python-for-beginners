# Example usage 'if __name__ == __main__:' for me to understand
def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


# ? The following block will only be executed if this script is run directly, but not as an import
if __name__ == "__main__":
    # ! NOTE: Variables inside here cannot be imported in the 14_Modules.py since it is inside this if statement which prevents it from being imported to other files.

    # Such as these two variables below
    result_sum = add_numbers(2, 3)
    result_product = multiply_numbers(4, 5)

    print("Sum:", result_sum)
    print("Product:", result_product)
