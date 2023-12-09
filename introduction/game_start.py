"""
Start the game.
"""
import itertools
from save import save_data


def intro_text():
    """
    Print the game introduction.

    :precondition: function is called when the game begins
    :postcondition: print the game introduction
    """
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
        name = input('Welcome to the Star War game! Please enter your player name: ')
        if name:
            final_confirm = input(f'Hello {name}, please confirm your game name: \nEnter "y" to '
                                  f'complete entry: ')
            if final_confirm.strip().lower() == 'y':
                return name
            else:
                name = ''


def select_difficulty():
    """
    Display difficulty options and prompt the user to select a difficulty level.

    This function prints information about each difficulty level and then calls the `difficulty_checker` function to
    obtain the user's choice. It handles potential exceptions for invalid inputs and prints corresponding error
    messages.

    :precondition: function is called when the program requires the user to choose difficulty
    :postcondition: proceed with the chosen difficulty
    :return: an int representing the selected difficulty level (1 for easy, 2 for medium, 3 for hard)
    """
    while True:
        print('Please select the difficulty of the game:')
        print('Easy: For beginners, enemies will have lower HP and do less damage.')
        print('Medium: For casuals, enemies will have higher HP and do more damage.')
        print('Hard: For experts, enemies will be----- classified data.')

        try:
            user_difficulty = difficulty_checker()
        except (ValueError, IndexError):
            print('Invalid input! You must input an integer between 1-3 inclusive.')
        else:
            return user_difficulty


def difficulty_checker():
    """
    Check if the difficulty user entered is valid.

    :precondition: function is called when the program requires the user to choose difficulty
    :postcondition: check if the difficulty user entered is valid
    :return: an int representing the selected difficulty level, 1 for easy, 2 for medium and 3 for hard
    :raise ValueError: if user's input is not an int
    :raise IndexError: if user's input is not int 1, 2 or 3
    """
    number_input = int(input('Select difficulty: Enter (1):easy, (2):medium, (3):hard:'))
    if type(number_input) != int:
        raise ValueError
    elif number_input not in [1, 2, 3]:
        raise IndexError
    else:
        return number_input


def warm_up_question(name):
    """
    Conducts a warm-up question for the user.

    This function prompts the user with a warm-up question related to permutations of enemy encounters.
    If the user answers correctly, their character's strength is increased by 5.

    :param name: a string, name of the player's character
    :precondition: name must be a string
    :postcondition: print result to user, update character's strength in json file if the user answers correctly
    :raises ValueError: if the user's input is not an integer
    """
    print('Before we begin the game, let us have a warm-up question! If you answer correctly, '
          'your strength will increase 5.')
    print('Assume you will meet 3 enemies: Clone Trooper, Battle Droids, and Royal Guard, '
          'how many permutations will you have?')

    while True:
        try:
            user_input = int(input('Please enter your answer: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

    enemy_list = ['Clone Trooper', 'Battle Droids', 'Royal Guard']
    correct_answer = len(list(itertools.permutations(enemy_list)))

    if user_input == correct_answer:
        character_dict = save_data.read_character(name)
        character_dict['str'] += 5
        save_data.save_game(character_dict)
        print('Congratulations! Your answer is correct! Your strength increased by 5! Enjoy your game!')
    else:
        print(f'Sorry, wrong answer. The correct answer is {correct_answer}. Enjoy your game!')


def main():
    name = 'Thor'
    warm_up_question(name)


if __name__ == "__main__":
    main()
