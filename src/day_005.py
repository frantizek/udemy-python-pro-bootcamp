"""
Day 5
- Create a Password Generator
"""
import string
import random
from typing import Optional
import logging

# --- Character Set Definitions ---
NUMBERS = string.digits                    # "0123456789"
UPPERCASE_LETTERS = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
SYMBOLS = "!#$%^&+=*()"                   # Required special characters


def generate_password(
    num_lowercase: int,
    num_uppercase: int,
    num_symbols: int,
    num_numbers: int
) -> str:
    """
    Generate a secure random password.

    Args:
        num_lowercase: Number of lowercase letters
        num_uppercase: Number of uppercase letters
        num_symbols: Number of special characters
        num_numbers: Number of digits

    Returns:
        Randomly generated password string
    """
    # Build password components
    password_chars = []

    # Add required lowercase letters
    password_chars.extend(random.choices(LOWERCASE_LETTERS, k=num_lowercase))

    # Add required uppercase letters
    password_chars.extend(random.choices(UPPERCASE_LETTERS, k=num_uppercase))

    # Add required symbols
    password_chars.extend(random.choices(SYMBOLS, k=num_symbols))

    # Add required numbers
    password_chars.extend(random.choices(NUMBERS, k=num_numbers))

    # Shuffle to randomize order
    random.shuffle(password_chars)

    # Convert list to string
    return ''.join(password_chars)


def validate_password_requirements(
    num_lowercase: int,
    num_uppercase: int,
    num_symbols: int,
    num_numbers: int
) -> tuple[bool, list[str], list[str]]:
    """
    Validate password requirements and provide feedback.

    Returns:
        Tuple of (is_valid, errors, suggestions)
    """
    errors = []
    suggestions = []
    total_length = num_lowercase + num_uppercase + num_symbols + num_numbers

    # Check total length
    if total_length < 8:
        missing = 8 - total_length
        errors.append(f"❌ Total: {total_length} characters (need at least 8)")
        suggestions.append(f"   💡 Add {missing} more character{'s' if missing > 1 else ''}")

    # Check numbers
    if num_numbers < 1:
        errors.append("❌ Numbers: 0 (need at least 1)")
        suggestions.append("   💡 Add at least 1 number")

    # Check lowercase letters
    if num_lowercase < 1:
        errors.append("❌ Lowercase Letters: 0 (need at least 1)")
        suggestions.append("   💡 Add at least 1 lowercase letter")

    # Check uppercase letters
    if num_uppercase < 1:
        errors.append("❌ Uppercase Letters: 0 (need at least 1)")
        suggestions.append("   💡 Add at least 1 uppercase letter")

    # Check symbols
    if num_symbols < 1:
        errors.append("❌ Symbols: 0 (need at least 1)")
        suggestions.append("   💡 Add at least 1 special character")

    return len(errors) == 0, errors, suggestions


def display_password_requirements():
    """Display password security requirements."""
    print("\n📋 Password Security Requirements:")
    print("=" * 50)
    print("   ✓ Minimum 8 characters total")
    print("   ✓ At least 1 lowercase letter (a-z)")
    print("   ✓ At least 1 uppercase letter (A-Z)")
    print("   ✓ At least 1 number (0-9)")
    print("   ✓ At least 1 special character (!#$%^&+=*())")
    print("=" * 50)
    print()


def display_current_status(num_lowercase: int, num_uppercase: int, num_symbols: int, num_numbers: int):
    """Show current component counts."""
    total = num_lowercase + num_uppercase + num_symbols + num_numbers
    print(f"\n📊 Current Configuration:")
    print(f"   Lowercase Letters: {num_lowercase}")
    print(f"   Uppercase Letters: {num_uppercase}")
    print(f"   Symbols: {num_symbols}")
    print(f"   Numbers: {num_numbers}")
    print(f"   Total: {total} characters")


def get_password_component_count(
    component_name: str,
    min_count: int = 0,
    max_count: int = 10,
    allow_cancel: bool = True,
    logger: Optional[logging.Logger] = None
) -> Optional[int]:
    """Get the count of password components with validation."""
    if min_count > max_count:
        raise ValueError(f"min_count ({min_count}) cannot exceed max_count ({max_count})")

    prompt = f"How many {component_name}? "

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print(f"💡 Please enter a number ({min_count}-{max_count}).")
            continue

        if allow_cancel and user_input.lower() in ('q', 'quit', 'exit'):
            if logger:
                logger.info(f"User cancelled {component_name} input")
            return None

        try:
            count = int(user_input)

            if count < min_count:
                print(f"⚠️  Minimum: {min_count}")
            elif count > max_count:
                print(f"⚠️  Maximum: {max_count}")
            else:
                if logger:
                    logger.info(f"{component_name} count: {count}")
                return count

        except ValueError:
            print(f"❌ Invalid input. Enter a whole number ({min_count}-{max_count}).")
            if logger:
                logger.warning(f"Invalid {component_name} input: {user_input}")


def main():
    """Main password generator function."""
    print("🔐 Secure Password Generator")
    print("=" * 50)

    # Display requirements
    display_password_requirements()

    max_attempts = 3
    attempt = 0

    while attempt < max_attempts:
        attempt += 1

        # Get inputs
        num_lowercase = get_password_component_count("lowercase letters")
        if num_lowercase is None:
            print("\n👋 Password generation cancelled!")
            return

        num_uppercase = get_password_component_count("uppercase letters")
        if num_uppercase is None:
            print("\n👋 Password generation cancelled!")
            return

        num_symbols = get_password_component_count("symbols")
        if num_symbols is None:
            print("\n👋 Password generation cancelled!")
            return

        num_numbers = get_password_component_count("numbers")
        if num_numbers is None:
            print("\n👋 Password generation cancelled!")
            return

        # Show what user selected
        display_current_status(num_lowercase, num_uppercase, num_symbols, num_numbers)

        # Validate requirements
        is_valid, errors, suggestions = validate_password_requirements(
            num_lowercase, num_uppercase, num_symbols, num_numbers
        )

        if is_valid:
            # Success!
            print("\n" + "=" * 50)
            print("✅ All Security Requirements Met!")
            print("=" * 50)
            print(f"   Total Password Length: {num_lowercase + num_uppercase + num_symbols + num_numbers}")
            print(f"   • {num_lowercase} lowercase letter{'s' if num_lowercase != 1 else ''}")
            print(f"   • {num_uppercase} uppercase letter{'s' if num_uppercase != 1 else ''}")
            print(f"   • {num_symbols} special character{'s' if num_symbols != 1 else ''}")
            print(f"   • {num_numbers} number{'s' if num_numbers != 1 else ''}")
            print()

            password = generate_password(num_lowercase, num_uppercase, num_symbols, num_numbers)

            print("\n" + "=" * 50)
            print("🔑 YOUR SECURE PASSWORD")
            print("=" * 50)
            print()
            print("   ┌" + "─" * (len(password) + 2) + "┐")
            print(f"   │ {password} │")
            print("   └" + "─" * (len(password) + 2) + "┘")
            print()
            print("=" * 50)
            print("⚠️  IMPORTANT:")
            print("   • Store this password securely")
            print("   • Don't share it with anyone")
            print("   • Use a password manager")
            print("=" * 50)
            return

        else:
            # Show errors and suggestions
            print("\n" + "=" * 50)
            print("⚠️  Requirements Not Met")
            print("=" * 50)
            for error in errors:
                print(f"   {error}")

            if suggestions:
                print("\n💡 Suggestions:")
                for suggestion in suggestions:
                    print(suggestion)

            if attempt < max_attempts:
                print(f"\n🔄 Let's try again... (Attempt {attempt + 1}/{max_attempts})\n")
            else:
                print("\n❌ Maximum attempts reached.")
                print("💡 Restart the program to try again.")


if __name__ == "__main__":
    main()
