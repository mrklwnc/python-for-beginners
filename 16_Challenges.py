# Lesson 16: Challenges

import sys
from challenges.rps import rps
from challenges.guess_number import guess_number


def arcade_games(name="Player 1"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, Welcome back to the Arcade menu.")
        else:
            print(f"\n{name}, Welcome to the Arcade.")

        game_choice = input(
            "Please choose a game:\n1 = Rock Paper Scissors\n2 = Number Guessing\n0 = Exit the Arcade\n"
        )

        game = int(game_choice)

        welcome_back = True

        if game not in range(0, 3):
            print(f"{name}, please choose between the given choices.")
            return arcade_games(name)

        if game == 1:
            rockpaperscissors = rps(name)
            rockpaperscissors()
        elif game == 2:
            gn = guess_number(name)
            gn()
        else:
            sys.exit(f"Bye {name} 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a game experience in a form of Rock, Paper, and Scissors."
    )

    parser.add_argument(
        "-n",
        "--name",
        required=True,
        metavar="name",
        help="Your player name.",
    )

    args = parser.parse_args()

    arcade_games(args.name)
