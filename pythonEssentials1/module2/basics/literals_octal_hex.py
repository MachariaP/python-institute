#!/usr/bin/env python3
"""
Demonstrates octal and hexadecimal integer literals in Python.

Shows how Python handles octal (base 8, 0o prefix) and hexadecimal (base 16,
0x prefix) literals, converting them to decimal when printed. Octal uses digits
0-7; hexadecimal uses 0-9 and A-F.
"""


def main():
    """
    Prints octal and hexadecimal literals to show their decimal equivalents.

    Display the decimal values of octal (0o123, 0o77) and hexadecimal (0x123,
    0xFF) literals using the print() function.
    """
    print(0o123)    # Octal: 1*8² + 2*8¹ + 3*8⁰ = 83
    print(0o77)     # Octal: 7*8¹ + 7*8⁰ = 63
    print(0x123)    # Hexadecimal: 1*16² + 2*16¹ + 3*16⁰ = 291
    print(0xFF)     # Hexadecimal: 15*16¹ + 15*16⁰ = 255


if __name__ == "__main__":
    main()
