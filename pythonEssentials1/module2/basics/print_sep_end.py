#!/usr/bin/env python3
"""
Demonstrates the sep and end keyword arguments in the print() function.

This script shows how sep customizes the separator between arguments and how
end modifies the default newline behavior. Parameters:
    - sep: Sets the separator between arguments (default: ' ').
           E.g., sep='_' joins arguments with an underscore.
    - end: Sets what is printed after arguments (default: '\n').
           E.g., end='*' adds an asterisk instead of a newline.
"""


def main():
    """
    Prints strings using sep and end parameters to customize output.

    Uses underscores and asterisks as separators and end characters to
    demonstrate their combined effect in print().
    """
    print("My", "name","is", sep="_", end="*")
    print("Monty","Python.", sep="*", end="*\n")


if __name__ == "__main__":
    main()
