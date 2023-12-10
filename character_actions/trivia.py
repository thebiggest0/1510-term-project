"""
Ask trivia questions.
"""

from save import save_data
import random


def jedi_dialogue():
    """
    Print dialogue for Jedi interaction.

    :precondition: function is called to print a dialogue
    :postcondition: print something to the screen
    """
    print('You spot a fallen Jedi master and their force ghost waving you to come closer')
    print('To deem you worthy, you are asked a question.')


def star_wars_trivia():
    """
    Return a random trivia question from trivia.json.

    :precondition: function is called to return a random trivia question
    :postcondition: return a dict with random trivia question
    :return: a dict, with a random trivia question
    """
    file = 'game_data/trivia.json'
    data = save_data.read_trivia(file)
    number = random.randrange(1, 36)
    question = data[f'question_{number}']
    return question


def ask_trivia(question):
    """
    Ask the player a trivia question.

    :param question: a dict, with a random trivia question
    :precondition: function is called to ask a trivia question
    :postcondition: print a trivia question to the screen
    """
    print(question['question'])
    print(1, question['option_one'])
    print(2, question['option_two'])
    print(3, question['option_three'])
    print(4, question['option_four'])

    while True:
        try:
            answer = int(input('Answer: '))
            if answer in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    while answer != question['answer']:
        try:
            answer = int(input('Wrong answer! The force ghost says try again: '))
            if answer in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    print('Correct!')


def player_choice():
    """
    Ask the player to choose between strength or health.

    :precondition: function is called to ask the player to choose between strength or health
    :postcondition: return the player's choice as an integer
    :postcondition: print something to screen
    :return: an int, the player's choice
    """
    print('The force ghost asks you to choose between strength or health')

    while True:
        try:
            answer = int(input('Enter (1) for STAT increase or (2) for healing: '))
            if answer in [1, 2]:
                return answer
            else:
                print('Invalid choice. Please enter either (1) for strength or (2) for healing.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def player_heal(name):
    """
    Heal the player to full health.

    :param name: a str, the player's name
    :precondition: function is called to heal the player to full health
    :postcondition: print something to the screen
    """
    player_data = save_data.read_character(name)
    healing = {1: 50, 2: 100, 3: 150}
    player_data['hp'] = healing[player_data['level']]
    print(f'You have been healed! hp: {player_data["hp"]}')
    save_data.save_game(player_data)


def player_stat_increase(name):
    """
    Increase the player's strength or intelligence by 5.

    :param name: a str, the player's name
    :precondition: function is called to increase the player's strength or intelligence by 5
    :postcondition: increase the player's strength or intelligence by 5
    :postcondition: prints something to the screen
    """
    number = random.randrange(2)
    stats = ['str', 'int']
    stat = stats[number]
    print(f'Your {stat} has increased by 5!')
    player_data = save_data.read_character(name)

    player_data[stat] += 5
    save_data.save_game(player_data)


def jedi_interaction(name):
    """
    Run the Jedi interaction.

    :param name: a str, the player's name
    :precondition: function is called to run the Jedi interaction
    :postcondition: run the Jedi interaction
    """
    jedi_dialogue()
    question = star_wars_trivia()
    ask_trivia(question)
    choice = player_choice()
    if choice == 1:
        player_stat_increase(name)
    else:
        player_heal(name)


def main():
    """
    Drive the program.
    """
    name = 'Thor'

    jedi_dialogue()
    question = star_wars_trivia()
    ask_trivia(question)
    choice = player_choice()
    if choice == 1:
        player_stat_increase(name)
    else:
        player_heal(name)


if __name__ == "__main__":
    main()
