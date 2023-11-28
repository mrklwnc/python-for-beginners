# Challenge: Rock, Paper, Scissors

import sys
import random
from enum import Enum


def rps(name="Player One"):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tie = 0

    def start_game():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tie

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Ask the player a number
        player_choice = input(
            f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        # Check if number is within the choices
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please choose a number between 1 to 3 only.")
            return start_game()

        # Cast Choices
        player = int(player_choice)
        computer = random.randint(1, 3)

        print(f"You chose {RPS(player).name}.")
        print(f"Computer chose {RPS(computer).name}.")

        # Logic
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tie

            if player == 1 and computer == 2:
                computer_wins += 1
                return f"💻 Computer wins! Paper beats Rock"
            elif player == 2 and computer == 3:
                computer_wins += 1
                return f"💻 Computer wins! Scissors beats Paper"
            elif player == 3 and computer == 1:
                computer_wins += 1
                return f"💻 Computer wins! Rock beats Scissors"
            elif player == computer:
                tie += 1
                return f"It's a tie 🤝"
            else:
                player_wins += 1
                return f"{name} win! 🎉🎉🎉"

        result = decide_winner(player, computer)

        print(result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")
        print(f"\nTies: {tie}")

        # Ask if the player wants to continue playing
        while True:
            decision = input(
                "\nDo you want to continue playing? \n'C' to Continue, 'Q' to Quit.\n"
            )

            if decision.lower() not in ["c", "q"]:
                continue
            else:
                break

        if decision.lower() == "c":
            return start_game()
        else:
            print("\nThank you for playing!")
            if __name__ == "__main__":
                sys.exit("Bye! 👋")
            else:
                return

    return start_game


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a game experience in a form of Rock, Paper, and Scissors."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="Your player name.",
    )

    args = parser.parse_args()

    game = rps(args.name)
    game()
