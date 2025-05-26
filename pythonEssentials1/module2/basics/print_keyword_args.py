#!/usr/bin/env python3
"""
Demonstrates the sep keyword argument in the print() function.

This script shows how the sep parameter customizes the separator between
positional arguments. It uses a dash separator and an empty separator to
illustrate different behaviors.
"""

def main():
    """
    Prints strings with a dash separator and an empty separator.

    Demonstrates how the sep parameter modifies the default space separation
    in the print() function.
    """
    print("My","name","is","Monty","Python.", sep="-")  # Dash separator
    print("My","name","is","Monty","Python.", sep="")   # Empty separator


if __name__ == "__main__":
    main()
