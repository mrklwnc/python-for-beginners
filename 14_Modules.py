# Lesson 14: Modules

# Import the module
# Syntax for importing: from folder_name import function_name

# If inside a folder: Add a period (.) like the one below
from modules.greetings import greetings_module
from modules.others import variables_module

greetings_module.greeting("Mark")

print("")

# Access variables in a module
print(variables_module.my_info)
