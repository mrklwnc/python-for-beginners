# Lesson 12: Closures

# Closure is a function having access to the scope of its parent function after the parent function has returned


def parent_function(person):
    coins = 3

    # play_game() function have access to its parent function scope such as "coins"
    def play_game():
        # ? nonlocal means it is inside its parent function
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game
    # adding parentheses in the function calls it, we are just returning it so we remove the parentheses


mark = parent_function("Mark")
ricci = parent_function("Ricci")

mark()
mark()

ricci()

mark()
