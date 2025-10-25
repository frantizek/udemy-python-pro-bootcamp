"""
Day 3
Control Flow
Logical Operators

Treasure Island 🏝️
Adventurer’s Edition - Enhanced Story!
"""


def main():
    # Treasure Island 🏝️ Adventure Game
    print(
        "🏴‍☠️ Welcome to Treasure Island! 🏝️\n"
        "Legend has it that the lost Ruby of the Ancients is hidden somewhere on this mysterious island...\n"
        "Your quest: brave the trials and claim the treasure!"
    )

    # First choice (crossroad)
    choice1 = input(
        "🌄 You stand at a fork in the overgrown jungle trail. "
        "To your left, twisted vines lead into the shadowy forest. "
        "To your right, a rickety wooden bridge crosses a bubbling ravine.\n"
        "Where do you want to go? Type 'left' or 'right' >>> "
    )

    if choice1.lower() == "left":
        # Second choice (lake)
        choice2 = input(
            "\n🌊 After hacking through vines, you arrive at a shimmering lake. "
            "A ghostly mist dances above the water.\n"
            "A battered rowboat is tied to a rotting dock. "
            "Do you 'wait' for the boat to drift closer, or 'swim' through the fog to the island? >>> "
        )

        if choice2.lower() == "wait":
            # Third choice (doors)
            choice3 = input(
                "\n🏠 The boat drifts you safely to the island. You find an eerie cottage with three ancient doors:\n"
                "      🔴 One red, with fiery claw marks.\n"
                "      🟡 One yellow, glowing faintly.\n"
                "      🔵 One blue, cold with a mysterious mist seeping out.\n"
                "Which door do you choose? Type 'red', 'yellow', or 'blue' >>> "
            )

            if choice3.lower() == "red":
                print(
                    "\n🔥 You open the red door—suddenly, the room fills with flames!\n"
                    "A fire-breathing dragon awakens and chases you back to the jungle.\n"
                    "Game Over - Roasted by the dragon!"
                )
            elif choice3.lower() == "blue":
                print(
                    "\n👻 The blue door swings open to reveal a swirling vortex!\n"
                    "Spectral pirates pull you into the cold abyss beyond.\n"
                    "Game Over - Lost forever in the ghostly realm!"
                )
            elif choice3.lower() == "yellow":
                print(
                    "\n✨ The yellow door creaks open, revealing a chamber bathed in golden light.\n"
                    "On a pedestal sits the fabled Ruby of the Ancients!\n"
                    "Congratulations, brave adventurer—YOU WIN! 🏆"
                )
            else:
                print(
                    "\nYou hesitate and pick a door that doesn’t exist...\n"
                    "A hidden trapdoor opens beneath you and you tumble into darkness!\n"
                    "Game Over - The island’s magic claims another wanderer."
                )
        else:
            print(
                "\n🐍 You dive into the misty lake, but the water churns!\n"
                "A giant serpent wraps around you, dragging you to the depths.\n"
                "Game Over - Claimed by the lake beast."
            )

    else:
        print(
            "\n🌪️ You cross the rickety bridge, but it collapses behind you!\n"
            "You tumble into the ravine, surrounded by strange glowing eyes...\n"
            "Game Over - The shadows of the jungle take you."
        )


if __name__ == "__main__":
    main()
