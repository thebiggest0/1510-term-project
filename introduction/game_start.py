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


def select_difficulty():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
