"""
ADD A DOCSTRING
"""


def run_away():
    dice = random.randrange(0, 6)
    player_guess = int(input('Guess a number between 1-6 inclusive: '))
    if player_guess == dice:
        return True
    else:
        return False


def main():


if __name__ == "__main__":
    main()
