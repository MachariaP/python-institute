#!/usr/bin/env python3
"""
Demonstrates Boolean values and relational operators in python.

Uses variables to compare numbers with relational operators (==. !=, >, <, >=, <=)
and prints the resulting Boolean values (True or False)>
"""


def main():
    """
    Performs comparisons using relational operators and prints Boolean results.

    Compares two numbers and checks a variable against zero, showing how
    relational operators produce True or False.
    """
    # Define variables
    x = 5
    y = 3

    # Demonstrate relational operators
    print(f"{x} == {y}:", x == y)   # Equal
    print(f"{x} != {y}:", x != y)   # Not Equal
    print(f"{x} > {y}:", x > y)   # Greater than
    print(f"{x} < {y}:", x < y)   # Less than
    print(f"{x} >= {y}:", x >= y)   # Greater or equal
    print(f"{x} <= {y}:", x <= y)   # Less or equal

    # Practical example: Check if x is positive
    print(f"Is {x} positive?", x > 0)



if __name__ == "__main__":
    main()
