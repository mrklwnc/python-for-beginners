# Lesson 10: Recursion


# Example from w3schools
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


# Example for Chat-GPT
def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)

# ! NOTE: Let Chat-GPT explain this to you like you are a 5 years old


# Rock Paper Scissors Recursion (Advanced)
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def rockpaperscissors():
    player_choice = random.choice("123")
    computer_choice = random.choice("123")

    choice = int(player_choice)
    comp_choice = int(computer_choice)

    print(
        "You chose: " + RPS(choice).name, "\nComputer chose: " + RPS(comp_choice).name
    )

    if choice == 1 and comp_choice == 2:
        print("Result: You lose, 💻 Computer wins! Paper beats Rock")
        return rockpaperscissors()
    elif choice == 2 and comp_choice == 3:
        print("Result: You lose, 💻 Computer wins! Scissors beats Paper")
        return rockpaperscissors()
    elif choice == 3 and comp_choice == 1:
        print("Result: You lose, 💻 Computer wins! Rock beats Scissors")
        return rockpaperscissors()
    elif choice == comp_choice:
        print("Result: It's a tie 🤝")
        return rockpaperscissors()
    else:
        return "You win! 🎉🎉🎉"


# It doesn't stop until you win!
print(rockpaperscissors())
