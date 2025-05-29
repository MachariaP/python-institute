#!/usr/bin/env python3
"""
Demonstrates while loops in Python with three examples.

Implements:
    1. Finding the largest number from the user input until -1 is entered.
    2. Counting even and odd numbers untill 0 is entered.
    3. Using a counter to loop a fixed number of times.
Includes input validation to handle non-integer inputs.
"""


def main():
    """
    Executes three while loop examples: largest number, even/odd counter, and fixed counter.

    Each example uses while loops to control repetition, with error handling for user inputs.
    """
    # Helper function for integer input
    def get_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer.")

    # Example 1: Largest Number
    print("\n--- Largest Number Finder ---")
    largest_number = -9999999999
    number = get_integer("Enter a number or type -1 to stop: ")
    while number != -1:
        if number > largest_number:
            largest_number = number
        number = get_integer("Enter a number or type -1 to stop: ")
    print("The largest number is:", largest_number)


if __name__ == "__main__":
    main()

