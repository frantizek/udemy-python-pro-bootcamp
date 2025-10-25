"""
Day 4
Randomisation and Lists

Project: Rock Paper Scissors
"""

import random


def main():
    print("Welcome to Rock Paper Scissors!")

    # Player choice input
    player_choice = input("What do you choose? Type Rock, Paper or Scissors: ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win! 🎉"
    else:
        result = "Computer wins! 🤖"

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    print(result)


if __name__ == "__main__":
    main()
