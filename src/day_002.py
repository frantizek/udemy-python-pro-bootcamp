#!/usr/bin/env python3
"""
Day 2: Tip Calculator
100 Days of Code - Python Pro Bootcamp

Challenge:
Create a tip calculator that:
1. Greets the user
2. Asks for the total bill amount
3. Asks for the tip percentage (10, 12, or 15)
4. Asks for the number of people to split the bill
5. Calculates how much each person should pay

Example:
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.6

This exercise focuses on:
- Basic arithmetic operations
- Type conversion (string to numbers)
- Float precision and rounding
- User input handling
- Formatted output
"""

from typing import Optional
from decimal import Decimal, InvalidOperation
import logging


def display_welcome_message():
    """
    Display a welcome message to the user.

    This function introduces the program and explains what it does.
    """
    print("💰 Welcome to the Tip Calculator! 💰")
    print("=" * 50)
    print("I'll help you calculate how much each person should pay")
    print("including the tip for your meal.")
    print("=" * 50)
    print()  # Empty line for better readability


def get_total_bill(
    min_amount: float = 0.01,
    max_amount: float = 100_000.0,
    allow_cancel: bool = True,
    logger: Optional[logging.Logger] = None
) -> Optional[Decimal]:
    """
    Robustly collect and validate bill amount.

    Returns Decimal for precise currency math.
    """
    while True:
        user_input = input("What was the total bill? $ ").strip()

        if allow_cancel and user_input.lower() in ('q', 'quit', 'exit'):
            if logger:
                logger.info("User cancelled bill input")
            return None

        try:
            # Decimal for currency precision
            amount = Decimal(user_input)

            if amount < Decimal(str(min_amount)):
                print(f"⚠️  Minimum: ${min_amount:.2f}")
            elif amount > Decimal(str(max_amount)):
                print(f"⚠️  Maximum: ${max_amount:,.2f}")
            else:
                return amount.quantize(Decimal('0.01'))  # Round to cents

        except (ValueError, InvalidOperation):
            print("❌ Invalid input. Enter a number like 42.50")
            if logger:
                logger.warning(f"Invalid bill input: {user_input}")


def get_tip_percentage(
    min_percentage: int = 0,
    max_percentage: int = 100,
    suggested_values: tuple[int, ...] = (10, 12, 15),
    allow_cancel: bool = True,
    logger: Optional[logging.Logger] = None
) -> Optional[int]:
    """
    Get tip percentage with validation and suggestions.

    Accepts any percentage within range but suggests common values.

    Args:
        min_percentage: Minimum acceptable tip percentage (default: 0)
        max_percentage: Maximum acceptable tip percentage (default: 100)
        suggested_values: Common tip percentages to display
        allow_cancel: Allow user to cancel input
        logger: Optional logger for tracking

    Returns:
        Validated tip percentage or None if cancelled

    Examples:
        get_tip_percentage()  # Interactive
        get_tip_percentage(min_percentage=10, max_percentage=25)
    """
    suggestions = ", ".join(map(str, suggested_values))
    prompt = f"What percentage tip would you like to give? ({suggestions}%) "

    while True:
        user_input = input(prompt).strip()

        # Handle cancellation
        if allow_cancel and user_input.lower() in ('q', 'quit', 'exit'):
            if logger:
                logger.info("User cancelled tip input")
            return None

        try:
            # Parse as float to accept decimals, then convert to int
            tip_value = float(user_input)
            tip_percentage = int(tip_value)  # Convert to int

            # Validate range
            if tip_percentage < min_percentage:
                print(f"⚠️  Minimum tip: {min_percentage}%")
            elif tip_percentage > max_percentage:
                print(f"⚠️  Maximum tip: {max_percentage}%")
            else:
                # Sanity check for unusual values
                if tip_percentage > 30:
                    confirm = input(f"💵 {tip_percentage}% is generous! Confirm? (y/n) ")
                    if confirm.lower() != 'y':
                        continue
                elif tip_percentage == 0:
                    confirm = input("🤔 No tip? Are you sure? (y/n) ")
                    if confirm.lower() != 'y':
                        continue

                if logger:
                    logger.info(f"Tip percentage selected: {tip_percentage}%")

                return tip_percentage

        except ValueError:
            print(f"❌ Invalid input. Enter a number like {suggestions}")
            if logger:
                logger.warning(f"Invalid tip input attempted: {user_input}")


def get_number_of_people(
    min_people: int = 1,
    max_people: int = 100,
    allow_cancel: bool = True,
    logger: Optional[logging.Logger] = None
) -> Optional[int]:
    """
    Robustly get number of people splitting the bill.

    Handles edge cases like solo diners and large groups.

    Args:
        min_people: Minimum people (default: 1)
        max_people: Maximum people (default: 100)
        allow_cancel: Enable cancellation (default: True)
        logger: Optional logger instance

    Returns:
        Number of people or None if cancelled

    Raises:
        ValueError: If min_people < 1 or min_people > max_people
    """
    if min_people < 1:
        raise ValueError("min_people must be at least 1")
    if min_people > max_people:
        raise ValueError(f"min_people ({min_people}) cannot exceed max_people ({max_people})")

    prompt = "How many people to split the bill? "

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("💡 Please enter the number of people.")
            continue

        if allow_cancel and user_input.lower() in ('q', 'quit', 'exit'):
            if logger:
                logger.info("User cancelled people count input")
            return None

        try:
            num_people_float = float(user_input)

            if num_people_float != int(num_people_float):
                print("❌ Number of people must be a whole number (no decimals).")
                continue

            num_people = int(num_people_float)

            # Validate range
            if num_people < min_people:
                if min_people == 1:
                    print(f"⚠️  Need at least {min_people} person!")
                else:
                    print(f"⚠️  Need at least {min_people} people!")
            elif num_people > max_people:
                print(f"⚠️  Maximum supported: {max_people} people")
            else:
                # Context-aware sanity checks
                if num_people == 1:
                    print("💡 Just you? The full bill is yours then!")
                    confirm = input("Continue without splitting? (y/n) ")
                    if confirm.lower() != 'y':
                        continue
                elif num_people > 20:
                    print(f"👥 Large party of {num_people}!")
                    confirm = input("Is this correct? (y/n) ")
                    if confirm.lower() != 'y':
                        continue
                elif num_people > 50:
                    print(f"🎉 That's a huge group of {num_people}!")
                    confirm = input("Double-check - is this right? (y/n) ")
                    if confirm.lower() != 'y':
                        continue

                if logger:
                    logger.info(f"Bill split among {num_people} people")

                return num_people

        except ValueError:
            print("❌ Invalid input. Enter a whole number like 2, 4, or 6.")
            if logger:
                logger.warning(f"Invalid people count: '{user_input}'")


def calculate_tip_amount(total_bill, tip_percentage):
    """
    Calculate the tip amount based on bill total and percentage.

    Args:
        total_bill (Decimal): The total bill amount
        tip_percentage (int): The tip percentage

    Returns:
        float: The calculated tip amount
    """
    tip_amount = float(total_bill) * float(tip_percentage / 100)
    return tip_amount


def calculate_total_with_tip(total_bill, tip_amount):
    """
    Calculate the total bill including tip.

    Args:
        total_bill (float): The original bill amount
        tip_amount (float): The calculated tip amount

    Returns:
        float: The total amount including tip
    """
    total_with_tip = total_bill + tip_amount
    return total_with_tip


def calculate_split_amount(total_with_tip, num_people):
    """
    Calculate how much each person should pay.

    Args:
        total_with_tip (float): The total bill including tip
        num_people (int): The number of people splitting the bill

    Returns:
        float: The amount each person should pay
    """
    split_amount = total_with_tip / num_people
    return round(split_amount, 2)


def format_currency(amount: float) -> str:
    """
    Format the amount as currency with proper rounding.

    Args:
        amount (float): The amount to format

    Returns:
        str: The formatted currency string with 2 decimal places
    """
    formatted_amount = f"${amount:.2f}"
    return formatted_amount


def display_results(split_amount, total_bill, tip_percentage, num_people):
    """
    Display the calculation results to the user.

    Args:
        split_amount (float): The amount each person should pay
        total_bill (Decimal): The original bill amount
        tip_percentage (int): The tip percentage used
        num_people (int): The number of people splitting
    """
    print("\n" + "🧾" * 25)
    print("CALCULATION RESULTS:")
    print(f"Total Bill: ${total_bill}")
    print(f"Tip Percentage: {tip_percentage}%")
    print(f"Number of People: {num_people}")
    print(f"Each person should pay: {format_currency(split_amount)}")
    print("🧾" * 25)


def main():
    """
    Main function that orchestrates the tip calculation process.

    This function follows the program flow:
    1. Display welcome message
    2. Get user inputs
    3. Perform calculations
    4. Display results
    """
    try:
        # Step 1: Welcome the user
        display_welcome_message()

        # Step 2: Get user inputs
        total_bill = get_total_bill()
        if total_bill is None:
            print("\n❌ Calculation cancelled - no bill amount provided.")
            print("👋 Thanks for using the Tip Calculator!")
            return

        tip_percentage = get_tip_percentage()
        if tip_percentage is None:
            print("\n❌ Calculation cancelled - no tip percentage provided.")
            print("👋 Thanks for using the Tip Calculator!")
            return

        num_people = get_number_of_people()
        if num_people is None:
            print("\n❌ Calculation cancelled - no split information provided.")
            print("👋 Thanks for using the Tip Calculator!")
            return

        # Step 3: Perform calculations
        tip_amount = calculate_tip_amount(total_bill, tip_percentage)
        total_with_tip = calculate_total_with_tip(float(total_bill), tip_amount)
        split_amount = calculate_split_amount(total_with_tip, num_people)

        # Step 4: Display results
        display_results(split_amount, total_bill, tip_percentage, num_people)

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# TODO: Add additional features for future versions
# Feature ideas:
# ✅ Input validation for all user inputs  # DONE!
# - Support for custom tip percentages
# - Different rounding strategies
# - Tax calculation inclusion
# - Multiple currency support
# - Bill splitting strategies (equal, weighted, etc.)
# - Save calculation history to file

if __name__ == "__main__":
    """
    This block ensures the main function only runs when the script
    is executed directly, not when imported as a module.
    """
    main()
