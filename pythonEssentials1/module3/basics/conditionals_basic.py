#!/usr/bin/env python3
"""
Demonstrates conditional execution in Python using if, if-else, and if-elif-else.

Implements examples of conditional statements to control program flow based on
Boolean conditions, including basic if, if-else, nested if-else, and if-elif-else.
"""


def main():
    """
    Executes examples of conditional statements.

    Demonstrates:
        - Basic if: Sheep counting to sleep.
        - if-else: Weather-based activity choice.
        - Nested if-else: Sunday plans with multiple conditions.
        - if-elif-else: Cascade of activity options.
    """
    # Basic if: Sheep counting
    sheep_counter = 120
    if sheep_counter >= 120:
        print("Time to sleep and dream!")

    # if-else: Weather- based plan
    the_weather_is_good = True
    if the_weather_is_good:
        print("Go for a walk.")
    else:
        print("Go to a theatre.")
    print("Have lunch.")

    # Nested if-else: Sunday plans
    nice_restaurant_is_found = False
    tickets_are_available = True
    if the_weather_is_good:
        if nice_restaurant_is_found:
            print("Have lunch at the restuarant.")
        else:
            print("Eat a sandwitch")
    else:
        if tickets_are_available:
            print("Go to the theater.")
        else:
            print("Go shopping at the mall")

    # if-elif-else: Activity cascade
    tickets_are_available = False
    table_is_available = True
    if the_weather_is_good:
        print("Go for a walk.")
    elif tickets_are_available:
        print("Go to the theatre.")
    elif table_is_available:
        print("Go for lunch at the restaurant.")
    else:
        print("Play chess at home.")


if __name__ == "__main__":
    main()
