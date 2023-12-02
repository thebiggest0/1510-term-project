def is_valid_choice(value):
    try:
        float_value = float(value)
        return float_value.is_integer() and int(float_value) in [1, 2, 3]
    except ValueError:
        return False


def combat_choice():
    while True:
        user_input = input('Battle initiated: (1): attack, (2): force, (3): run: ')
        if is_valid_choice(user_input):
            return int(user_input)
        else:
            print('Invalid input! You must input a whole number 1, 2, or 3. Try again.')


def main():
    choice = combat_choice()
    print(f'User chose: {choice}')


if __name__ == "__main__":
    main()
