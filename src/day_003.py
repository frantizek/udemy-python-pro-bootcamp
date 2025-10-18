"""
Day 3
Control Flow
Logical Operators

Treasure Island 🏝️
"""

def main():
    # Treasure Island 🏝️ Adventure Game
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # First choice (crossroad)
    choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right' >>> ")
    if choice1.lower() == "left":

        # Second choice (lake)
        choice2 = input(
            "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat or 'swim' to swim across >>> ")
        if choice2.lower() == "wait":
            # Third choice (doors)
            choice3 = input(
                "You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which colour do you choose? >>> ")
            if choice3.lower() == "red":
                print("Game Over - The monster from the island has found you.")
            elif choice3.lower() == "blue":
                print("Game Over - You have been captured by the evil witch.")
            elif choice3.lower() == "yellow":
                print("You Win! You have found the treasure.")
            else:
                print("Game Over - door doesn't exist.")
        else:
            print("Game Over - attacked by a trout.")

    else:
        print("Game Over - you fell into a hole.")


if __name__ == "__main__":
    main()
