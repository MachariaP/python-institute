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

    # Example 2: Even/Odd Counter
    print("\n--- Even/Odd Number Counter ---")
    odd_numbers = 0
    even_numbers = 0
    number = get_integer("Enter a number or type 0 to stop: ")
    while number:   # Simplified: non-zero is True
        if number % 2:  # Simplified: non-zero remainder is odd
            odd_numbers += 1
        else:
            even_numbers +=1
        number = get_integer("Enter a number or type 0 to stop: ")
    print("Odd numbers count:", odd_numbers)
    print("Even numbers count:", even_numbers)

    # Example 3: Counter-Based Loop
    print("\n--- Counter-Based Loop ---")
    counter = 5
    while counter:
        print("Inside the loop.", counter)
        counter -=1
    print("Outside the loop.", counter)


if __name__ == "__main__":
    main()

