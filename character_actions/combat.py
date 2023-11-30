"""
ADD A DOCSTRING
"""

import random


def random_sum_generator():
    number_one = random.randrange(0, 500)
    number_two = random.randrange(-100, 300)
    dice = random.randrange(0, 6)
    if dice % 2 == 0:
        random_result = number_one + number_two
        operation = '+'
    else:
        random_result = number_one - number_two
        operation = '-'
    return [f'({number_one} {operation} {number_two} = ? )', random_result]


def run_away():
    dice = random.randrange(0, 6)
    player_guess = int(input('Guess a number between 1-6 inclusive: '))
    if player_guess == dice:
        return True
    else:
        return False


def main():
    pass


if __name__ == "__main__":
    main()
