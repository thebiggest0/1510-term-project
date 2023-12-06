"""
ADD A DOCSTRING
"""

from save import save_data
import random


def jedi_dialogue():
    print('You spot a fallen Jedi master and their force ghost waving you to come closer')
    print('To deem you worthy, you are asked a question.')


def star_wars_trivia():
    """
    Receive trivia questions from trivia.json.

    :return:
    """

    file = '../game_data/trivia.json'
    data = save_data.read_trivia(file)
    number = random.randrange(23)
    question = data[f'question_{number}']
    return question


def ask_trivia(question):
    """
    Ask player a trivia question.

    :param question:
    :return:
    """
    print(question['question'])
    print(1, question['option_one'])
    print(2, question['option_two'])
    print(3, question['option_three'])
    print(4, question['option_four'])

    answer = int(input('Answer: '))
    while answer != question['answer']:
        print(question['answer'])
        answer = int(input('The force ghost says try again: '))


def player_choice():
    print('The force ghost asks you to choose between strength or health')
    answer = int(input('Enter (1) for strength or (2) for healing: '))
    return answer


def player_heal(name):
    """
    Heal player to full hp.

    :param name:
    :return:
    """
    player_data = save_data.read_character(name)
    healing = {1: 50, 2: 100, 3: 150}
    player_data['hp'] = healing[player_data['level']]
    print(f'Your health is back to full! hp: {player_data["hp"]}')
    save_data.save_game(player_data)


def player_stat_increase(name):
    """
    Increase one player stat by 5.

    :param name:
    :param number:
    :return:
    """
    number = random.randrange(3)
    stats = ['str', 'int', 'dex']
    stat = stats[number]
    player_data = save_data.read_character(name)

    player_data[stat] += 5
    save_data.save_game(player_data)


def jedi_interaction(name):
    jedi_dialogue()
    question = star_wars_trivia()
    ask_trivia(question)
    choice = player_choice()
    if choice == 1:
        player_stat_increase(name)
    else:
        player_heal(name)

def main():
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
