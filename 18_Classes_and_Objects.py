# Lesson 18: Classes and Objects


class MyFirstClass:
    x = 5


first = MyFirstClass
print(first.x)


# The __init__() function
class Person:
    # ? NOTE: The "self" parameter does not have to be named "self"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def introduction(self):
        return f"Hello! I'm {self.name}, and I am {self.age} years old."


mark = Person("Mark", 22)

print(mark.name, mark.age)
# ? NOTE: Without the def __str__() method, this will return an error since by default. A class only returns a string, and since age is not defined as a string, it returns an error.

john = Person("John", 28)

print(john)

# The __str__() function
print(mark)

# Object Methods
print(mark.introduction())

# Modify Object Properties
mark.age = 28

# Delete Object Properties
# del mark.age

print(mark)

# Delete Objects
print(john)

# del john


# The "pass" statement
class Cars:
    pass


# Creating a Child Class
class Student(Person):
    def __init__(self, name, age, year, course):
        super().__init__(
            name, age
        )  # Using the super() method instead of using the Parent's name which is the class "Person"
        self.year = year
        self.course = course

    def __str__(self):
        return f"My name is {self.name}, a {self.year} student taking {self.course}."

    def welcome(self):
        return f"Welcome {self.name} to the {self.course} as a {self.year} student."


jane = Student("Jane", 23, "1st Year", "Bachelor of Science in Information Technology")

print(jane)

# Accessing a method from the parent class
print(jane.introduction())

# Accessing a method from as the child class of Person
print(jane.welcome())
