"""
ADD A DOCSTRING
"""


def intro_text():
    pass


def name_entry():
    """
    Return user's name.

    :precondition: function is called when the program requires the user's name for player identification
    :postcondition: return user's name after successful entry and confirmation
    :return: a string that user inputs
    """
    name = ''
    while not name:
        name = input('Please enter your player name: ')
        if name:
            final_confirm = input(f'Hello {name}, please confirm your game name: \n Enter "y" or "n" to '
                                  f'complete entry: ')
            if final_confirm.strip().lower() == 'y':
                return name
            else:
                name = ''


def instructions():
    pass


def difficulty_checker():
    number_input = int(input('Select difficulty: Enter (1):easy, (2):medium, (3):hard:'))
    if type(number_input) != int:
        raise ValueError
    elif number_input not in [1, 2, 3]:
        raise IndexError
    else:
        return number_input


def select_difficulty():
    print('Please select difficulty of game')
    print('Easy: For beginners, enemies will be lower hp and do less damage.')
    print('Medium: For casuals, enemies will be higher hp and do more damage')
    print('Hard: For experts, enemies will be----- classified data')

    try:
        user_difficulty = difficulty_checker()
    except ValueError:
        print('Please input an integer between 1-3 inclusive')
    except IndexError:
        print('Please input an integer between 1-3 inclusive')
    else:
        return user_difficulty


def main():
    pass


if __name__ == "__main__":
    main()
