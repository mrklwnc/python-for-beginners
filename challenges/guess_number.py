# Challenge: Rock, Paper, Scissors

import sys
import random


def guess_number(name="Player One"):
    game_count = 0
    player_wins = 0

    def start_game():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins

        # Ask the player a number
        player_choice = input(f"\n{name}, please choose a number between 1 to 3: ")

        # Check if number is within the choices
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please choose a number between 1 to 3 only.")
            return start_game()

        # Cast Choices
        player = int(player_choice)
        computer = random.randint(1, 3)

        print(f"You chose the number {player}.")
        print(f"Computer chose the number {computer}.")

        # Logic
        def decide_winner(player, computer):
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name}, you win! 🎉🎉🎉"
            else:
                return f"Sorry {name}, better luck next time! 😢"

        result = decide_winner(player, computer)

        print(result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nYour winrate is: {player_wins/game_count:.2%}")

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

    game = guess_number(args.name)
    game()
