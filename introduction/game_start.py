"""
ADD A DOCSTRING
"""


def intro_text():
    pass


def name_entry():
    name = ''
    while not name:
        name = input('Please enter your player name: ')
        if name:
            final_confirm = input(f'Hello {name} please confirm your game name: \n"y" or "n" to complete entry: ')
            if final_confirm == 'y':
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
