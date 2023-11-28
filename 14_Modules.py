# Lesson 14: Modules

# Import the module
# Syntax for importing: from folder_name import function_name

# If inside a folder: Add a period (.) like the one below
# ? See the imported files for more information
from modules.greetings import greetings_module
from modules.others import variables_module
from modules import operators


greetings_module.greeting("Mark")

print("")

# Access variables in a module
print(variables_module.my_info)
print(variables_module.my_info["name"])
print(variables_module.my_info["age"])
print(variables_module.my_info["hobbies"])
print(variables_module.my_info["hobbies"][0])

# Can be used since they are not inside the if __name__ == __main__ code block
print(operators.add_numbers(6, 9))
print(operators.multiply_numbers(4, 20))

# Can't be used since they are inside the if __main__ code block which are only accessible if the file they are defined is the one that was executed
# ! NOTE: Code below will return an error
print(operators.result_sum)
print(operators.result_product)
