"""
ADD A DOCSTRING
"""


def intro_text():
    print("""It is an era of dire betrayal across the Republic. The once noble Jedi Order has collapsed under a 
    shocking act of treachery from within. In a single, calculated strike, the clone troopers, loyal soldiers of the 
    Republic, have turned on their Jedi commanders, executing the infamous Order 66.

    Hiding in the sprawling metropolis of Coruscant, a planet teeming with a trillion souls, you stand as the last 
    surviving Jedi, a lone beacon of hope amidst the chaos. The very forces you once fought alongside have become 
    relentless hunters, sworn to your extinction.
    
    The Galactic Republic, under the shadow of manipulation, fears the return of the Jedi might inspire a wave of 
    resistance, and the newly anointed Galactic Empire's dominion would be threatened.
    
    To preserve your legacy and unravel the truth, your mission is clear: you must brave the dangers of a city turned 
    hostile, infiltrate the besieged Jedi Temple, and uncover the machinations behind this devastating turn of events. 
    Survival is your first challenge, but the secrets within the hallowed halls of the Temple may hold the key to the 
    fate of the Force itself.""")


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
