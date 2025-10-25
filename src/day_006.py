#!/usr/bin/env python3
"""
Day 6: Python Functions & Karel the Robot
100 Days of Code - Python Pro Bootcamp

Challenge:
Learn and practice Python functions by solving Karel the Robot problems.
Karel is an educational programming language that teaches fundamental
programming concepts through robot navigation.

In this exercise, you'll create functions to make Karel:
1. Move around a grid world
2. Turn left/right
3. Interact with beepers
4. Solve maze-like problems

Key Concepts:
- Function definition and calling
- Parameters and arguments
- Return values
- Code reusability
- Problem decomposition

Note: We'll simulate Karel's world using text-based representation
since we don't have the actual Karel environment.
"""

# TODO: Import any necessary modules
# Consider what might help with grid simulation or visualization

# --- Karel World Constants ---
GRID_SIZE = 10  # 10x10 grid world
WALL = "▓"
EMPTY = "·"
KAREL_NORTH = "↑"
KAREL_EAST = "→"
KAREL_SOUTH = "↓"
KAREL_WEST = "←"
BEEPER = "○"


# --- Karel State ---
class KarelWorld:
    """
    Simulates Karel's world with position, direction, and beepers.
    """

    def __init__(self):
        # TODO: Initialize Karel's world state
        # - Position (x, y)
        # - Direction (north, east, south, west)
        # - Beeper locations
        # - Wall locations
        # - Grid representation
        pass

    def display_world(self):
        """
        Display the current state of Karel's world.

        Shows:
        - Karel's position and direction
        - Walls
        - Beepers
        - Empty spaces
        """
        # TODO: Create a visual representation of the grid
        # Print the grid with Karel, walls, and beepers
        print("Karel's World:")
        print("=" * 30)
        # Implementation needed
        print("World display not yet implemented")
        print("=" * 30)


# Global world instance
world = KarelWorld()


def move():
    """
    Move Karel forward one space in the direction it's facing.

    Conditions:
    - Cannot move through walls
    - Cannot move outside grid boundaries

    Returns:
        bool: True if movement was successful, False if blocked
    """
    # TODO: Implement movement logic
    # Check if front is clear (no wall and within bounds)
    # Update Karel's position if movement is possible
    # Return success status
    print("Karel attempts to move...")
    return False


def turn_left():
    """
    Turn Karel 90 degrees to the left.

    Example:
    - Facing North → turns to face West
    - Facing East → turns to face North
    """
    # TODO: Implement turning logic
    # Update Karel's direction counter-clockwise
    print("Karel turns left")


def turn_right():
    """
    Turn Karel 90 degrees to the right.

    This is not a primitive Karel command, so you'll need to
    implement it using turn_left() or direct direction change.
    """
    # TODO: Implement right turn using left turns or direct change
    # Hint: Three left turns = one right turn
    print("Karel turns right")


def front_is_clear():
    """
    Check if there's no wall in front of Karel.

    Returns:
        bool: True if Karel can move forward, False if blocked
    """
    # TODO: Check the cell in front of Karel
    # Consider direction and grid boundaries
    return True


def left_is_clear():
    """
    Check if there's no wall to Karel's left.

    Returns:
        bool: True if left side is clear, False if blocked
    """
    # TODO: Check the cell to Karel's left
    return True


def right_is_clear():
    """
    Check if there's no wall to Karel's right.

    Returns:
        bool: True if right side is clear, False if blocked
    """
    # TODO: Check the cell to Karel's right
    return True


def facing_north():
    """
    Check if Karel is facing north.

    Returns:
        bool: True if facing north, False otherwise
    """
    # TODO: Check Karel's current direction
    return False


def facing_east():
    """
    Check if Karel is facing east.

    Returns:
        bool: True if facing east, False otherwise
    """
    # TODO: Check Karel's current direction
    return False


def facing_south():
    """
    Check if Karel is facing south.

    Returns:
        bool: True if facing south, False otherwise
    """
    # TODO: Check Karel's current direction
    return False


def facing_west():
    """
    Check if Karel is facing west.

    Returns:
        bool: True if facing west, False otherwise
    """
    # TODO: Check Karel's current direction
    return False


def put_beeper():
    """
    Place a beeper at Karel's current location.

    Karel can carry infinite beepers in this simulation.
    """
    # TODO: Add a beeper to Karel's current position
    print("Karel puts down a beeper")


def pick_beeper():
    """
    Pick up a beeper from Karel's current location.

    Returns:
        bool: True if beeper was picked up, False if no beeper present
    """
    # TODO: Remove a beeper from current position if available
    print("Karel picks up a beeper")
    return True


def beepers_present():
    """
    Check if there are any beepers at Karel's current location.

    Returns:
        bool: True if beepers are present, False otherwise
    """
    # TODO: Check current cell for beepers
    return False


# --- Challenge Functions ---
def draw_square():
    """
    Challenge 1: Make Karel draw a square pattern.

    Karel should:
    1. Move in a square pattern
    2. Possibly place beepers at corners
    3. Return to starting position

    This teaches:
    - Function sequencing
    - Repetitive patterns
    """
    # TODO: Implement square drawing logic
    # Use move(), turn_left(), and put_beeper() as needed
    print("Drawing square...")


def navigate_maze():
    """
    Challenge 2: Navigate Karel through a simple maze.

    Karel should find its way from start to finish
    using wall detection and strategic turning.

    This teaches:
    - Conditional logic
    - Problem-solving strategies
    - Function composition
    """
    # TODO: Implement maze navigation logic
    # Use front_is_clear(), left_is_clear(), right_is_clear()
    # Use turn_left(), turn_right(), and move()
    print("Navigating maze...")


def climb_mountain():
    """
    Challenge 3: Make Karel climb a 'mountain' of beepers.

    Karel should:
    1. Approach a staircase-like pattern
    2. Climb up by moving and turning
    3. Possibly collect or place beepers along the way

    This teaches:
    - Complex movement patterns
    - State management
    - Algorithmic thinking
    """
    # TODO: Implement mountain climbing logic
    print("Climbing mountain...")


def solve_harvest_problem():
    """
    Challenge 4: Harvest a field of beepers.

    Karel should:
    1. Move through a field
    2. Pick up all beepers in its path
    3. Return to start with collected beepers

    This teaches:
    - Looping patterns
    - Resource collection
    - Complete coverage algorithms
    """
    # TODO: Implement beeper harvesting logic
    print("Harvesting beepers...")


def create_custom_function(pattern_name):
    """
    Challenge 5: Create a custom function for a specific pattern.

    Args:
        pattern_name (str): Name of the pattern to create

    This teaches:
    - Function design
    - Parameter usage
    - Creative problem solving
    """
    # TODO: Design and implement a custom Karel function
    # Examples: spiral, zigzag, circle, etc.
    print(f"Creating {pattern_name} pattern...")


def demonstrate_functions():
    """
    Demonstrate all the Karel functions working together.

    This function should showcase:
    - Basic movement
    - Turning
    - Beeper interaction
    - World state changes
    """
    print("🚀 Karel Function Demonstration")
    print("=" * 40)

    # Display initial world state
    world.display_world()

    # TODO: Add demonstration sequence
    # Show various functions in action
    # Create an engaging demonstration

    print("Demonstration completed!")


def main():
    """
    Main function to run Karel programming challenges.

    Provides a menu for selecting which challenge to attempt.
    """
    print("🤖 Welcome to Karel the Robot Simulator!")
    print("=" * 50)
    print("Learn Python Functions through Robot Programming")
    print("=" * 50)

    challenges = {
        "1": ("Draw a Square", draw_square),
        "2": ("Navigate a Maze", navigate_maze),
        "3": ("Climb a Mountain", climb_mountain),
        "4": ("Harvest Beepers", solve_harvest_problem),
        "5": ("Custom Pattern", lambda: create_custom_function("spiral")),
        "6": ("Function Demonstration", demonstrate_functions),
        "q": ("Quit", None),
    }

    while True:
        print("\nAvailable Challenges:")
        print("-" * 30)
        for key, (description, _) in challenges.items():
            print(f"{key}. {description}")

        choice = input("\nSelect a challenge (1-6) or 'q' to quit: ").strip().lower()

        if choice == "q":
            print("Thanks for programming with Karel! 👋")
            break

        if choice in challenges:
            challenge_name, challenge_func = challenges[choice]
            if challenge_func:
                print(f"\n🎯 Starting: {challenge_name}")
                print("=" * 40)
                challenge_func()
            else:
                break
        else:
            print("❌ Invalid choice. Please select 1-6 or 'q'.")


# TODO: Additional features for enhancement
# - Save/Load world state
# - Step-by-step execution
# - Visual animation
# - Multiple Karel instances
# - Complex obstacle courses
# - Timing and scoring system

if __name__ == "__main__":
    """
    Karel the Robot Programming Environment

    This simulation helps you understand:
    - Function definition and calling
    - Parameter passing
    - Return values
    - Program flow control
    - Problem decomposition

    Remember: The key to solving Karel problems is breaking
    them down into smaller, manageable functions!
    """
    main()
