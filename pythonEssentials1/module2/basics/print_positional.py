#!/usr/bin/env python3
"""
Demonstrates the positional way of passing arguments to the print() function
with the end parameter.

This script shows how the order of arguments in print() determines the output
sequence and how the end parameter modifies the default newline behavior. The
print() function accepts the following parameters:
    - sep:
        Controls the separator between arguments (default: ' '). 
        E.g., sep='-' joins arguments with a hyphen.
    - end:
        Controls what is printed after arguments (default: '\n').
        E.g., end=' ' adds a space instead of a newline.
"""

def main():
    """
    Main function to demonstrate positional arguments and the end parameter in print().

    Prints two strings with a space separator and modifies the end parameter
    to keep the next print on the same line.
    """
    print("My name is","Python.", end=" ")
    print("Monty Python.")


if __name__ == "__main__":
    main()
