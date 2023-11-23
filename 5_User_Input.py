# Lesson 5: User Input
import sys
import random
from enum import Enum


# Using Enum (This is a Data type too)
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))  # Outputs RPS.PAPER
# print(RPS.ROCK)  # Outputs RPS.ROCK
# print(RPS["ROCK"])  # Outputs RPS.ROCK
# print(RPS.ROCK.value)  # Outputs 1

# sys.exit()

# User choose a number between 1,2, and 3
playerChoice = input("Choose a number:\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

# Cast it into an integer value because initially the value is a string
choice = int(playerChoice)

# Guard
if choice < 1 or choice > 3:
    sys.exit("Choice must be between 1,2, and 3")

# Computer randomly select a number between 1,2, and 3
computerChoice = random.choice("123")

# Cast it into an integer value
compChoice = int(computerChoice)

print("")
print("You chose", RPS(choice).name)  # Display your choice
print("Computer chose", RPS(compChoice).name)  # Display the computer's choice

# The Logic
if choice == 1 and compChoice == 2:
    print("You lose, 💻 Computer wins! Paper beats Rock")
elif choice == 2 and compChoice == 3:
    print("You lose, 💻 Computer wins! Scissors beats Paper")
elif choice == 3 and compChoice == 1:
    print("You lose, 💻 Computer wins! Rock beats Scissors")
elif choice == compChoice:
    print("It's a tie 🤝")
else:
    print("You win! 🎉🎉🎉")
