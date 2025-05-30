#!/usr/bin/env python3
"""
Implements a Guess the secret Number game using a while loop.

Prompts the user to guess a secret number, continues untill the correct number is
guessed, and provides feedback, Uses multi-line printing for a welcome message
and includes input validation.
"""

def get_integer(prompt):
    """
    Prompts for a valid integer input

    Args:
        prompt (str): The prompt to display.

    Returns:
        int: The valid integer entered.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    """
    Runs the Guess the Secret Number game.

    Uses a while loop to prompt for guesses until the secret number is matched.
    Prints a multi-line welcome message and specific feedback.
    """
    secret_number = 777  # The magician's secret number

    # Welcome message with ASCII art
    print(
            """
            +================================+
            | Welcome to my game, muggle!    |
            | Enter an integer number        |
            | and guess what number I've     |
            | picked for you.                |
            | So, what is the secret number? |
            +================================+
            """
            )
    # Get initial guess
    guess = get_integer("Guess the secret number: ")

    # Game loop
    while guess != secret_number:
        print("Ha ha! You're stuck in my loop!")
        guess = get_integer("Guess the secret number: ")

    # Success output
    print(guess)
    print("Well done, muggle! You are free now.")


if __name__ == "__main__":
    main()


    
