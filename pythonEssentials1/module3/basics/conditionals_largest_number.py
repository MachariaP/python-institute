#!/usr/bin/env python3
"""
Demonstrates conditional execution to find the largest of three numbers.

Reads three integer from user input, uses if statements to determine the largest,
and print the result. Includes error handling for invalid inputs.
"""


def get_integer(prompt):
    """
    Prompts for an integer input with error handling.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def find_largest(number1, number2, number3):
    """
    Find the largest of three numbers using if statements.

    Args:
        number1 (int): First number.
        number2 (int): Second number.
        number3 (int): Third number.

    Returns:
        int: The largest number.
    """
    largest_number = number1
    if number2 > largest_number:
        largest_number = number2
    if number3 > largest_number:
        largest_number = number3
    return largest_number

def main():
    """
    Reads three numbers and prints the largest.

    Uses get_integer() for input and find_largest() for comparison.
    """
    # Read three numbers
    number1 = get_integer("Enter the first number: ")
    number2 = get_integer("Enter the second number: ")
    number3 = get_integer("Enter the third number: ")

    # Find and print the largest
    largest = find_largest(number1, number2, number3)
    print("The largest number is:", largest)


if __name__ == "__main__":
    main()

