#!/usr/bin/env python3
"""
Demonstrates the effect of an empty print() function invocation.

The script prints two lines of nursery rhyme with an empty print() call
between them, resulting in a blank line in the output.
"""

def main():
    """
    Main function to print a nursery rhyme with an empty print() call.

    The empty print() adds a newline, creating a blank line between outputs.
    """
    print("The itsy bitsy spider climbed up the waterspout.")
    print()
    print("Down came the rain and washed the spider out.")

if __name__ == "__main__":
    main()
