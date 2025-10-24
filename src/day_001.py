#!/usr/bin/env python3
"""
Day 1: Band Name Generator
100 Days of Code - Python Pro Bootcamp

Challenge:
Create a simple band name generator that:
1. Greets the user
2. Asks for the city they grew up in
3. Asks for the name of a pet
4. Combines them to show their band name

Example:
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
> New York
What's your pet's name?
> Rocket
Your band name could be New York Rocket

This exercise focuses on:
- Print statements
- Input functions
- String variables
- String concatenation
"""


# TODO: Import any necessary modules (if needed for future enhancements)
# Currently no imports needed for basic functionality

def display_welcome_message():
    """
    Display a welcome message to the user.

    This function introduces the program and explains what it does.
    """
    print("🎸 Welcome to the Band Name Generator! 🎸")
    print("=" * 50)
    print("I'll help you create an awesome band name by combining")
    print("the city you grew up in with the name of your pet.")
    print("=" * 50)
    print()  # Empty line for better readability


def get_user_city():
    """
    Prompt the user for the city they grew up in.

    Returns:
        str: The name of the city entered by the user
    """
    # TODO: Get user input for city name
    # Use input() function to prompt user
    # Consider adding input validation in future versions
    city = input("What's the name of the city you grew up in?\n> ")
    return city


def get_pet_name():
    """
    Prompt the user for their pet's name.

    Returns:
        str: The name of the pet entered by the user
    """
    # TODO: Get user input for pet name
    # Use input() function to prompt user
    # Consider adding input validation in future versions
    pet_name = input("What's your pet's name?\n> ")
    return pet_name


def generate_band_name(city, pet_name):
    """
    Generate a band name by combining city and pet name.

    Args:
        city (str): The city name
        pet_name (str): The pet name

    Returns:
        str: The generated band name
    """
    # TODO: Combine the city and pet name to create band name
    # Use string concatenation or f-string
    band_name = f"{city} {pet_name}"
    return band_name


def display_band_name(band_name):
    """
    Display the generated band name to the user.

    Args:
        band_name (str): The generated band name to display
    """
    print("\n" + "🎶" * 25)
    print(f"Your band name could be: {band_name}!")
    print("🎶" * 25)


def main():
    """
    Main function that orchestrates the band name generation process.

    This function follows the program flow:
    1. Display welcome message
    2. Get user inputs
    3. Generate band name
    4. Display result
    """
    try:
        # Step 1: Welcome the user
        display_welcome_message()

        # Step 2: Get user inputs
        # TODO: Call get_user_city() function and store result
        user_city = get_user_city()

        # TODO: Call get_pet_name() function and store result
        user_pet_name = get_pet_name()

        # Step 3: Generate band name
        # TODO: Call generate_band_name() with the collected inputs
        band_name = generate_band_name(user_city, user_pet_name)

        # Step 4: Display the result
        display_band_name(band_name)

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# TODO: Add additional features for future versions
# Feature ideas:
# - Input validation (empty strings, numbers, etc.)
# - Multiple band name suggestions
# - Save favorite band names to file
# - Random adjective generator
# - Band name style selection (rock, pop, jazz, etc.)

if __name__ == "__main__":
    """
    This block ensures the main function only runs when the script
    is executed directly, not when imported as a module.
    """
    main()
