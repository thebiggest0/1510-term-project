"""
This module interacts with data stored in JSON files.
"""

import json


def save_game(character):
    """
    Save the game.

    :param character: a dict containing the character's attributes
    :precondition: character must be a dict containing the character's attributes
    :postcondition: save the game
    """
    # stores all data in json file as 'data'
    try:
        with open('game_data/character.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('../game_data/character.json', 'r') as file:
            data = json.load(file)

    # add character name as key with entire dictionary as value to data
    # if existing data, it will override, if it does not exist it will add as new
    data.update({character['name']: character})

    # update json file with new updated data
    try:
        with open('game_data/character.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('../game_data/character.json', 'w') as file:
            json.dump(data, file, indent=4)


def read_character(name):
    """
    Read the character from the game.

    :param name: a non-empty string, name of the character user entered
    :precondition: name must be a non-empty string
    :postcondition: read the character from the game
    :return: a dict containing the character's attributes
    """
    file_location = 'game_data/character.json'
    try:
        with open(file_location, 'r') as file:
            output_file = json.load(file)
            return output_file[name]
    except FileNotFoundError:
        with open('../game_data/character.json', 'r') as file:
            output_file = json.load(file)
            return output_file[name]


def read_all_characters():
    """
    Read all characters from the game.

    :precondition: function must be called
    :postcondition: read all characters from the game
    :return: a dict containing all characters' attributes
    """
    file_location = 'game_data/character.json'
    try:
        with open(file_location, 'r') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        with open('../game_data/character.json', 'r') as file:
            output_file = json.load(file)
            return output_file


def read_enemy():
    """
    Read the enemy from the game.

    :precondition: function must be called
    :postcondition: read the enemy from the game
    :return: a dict containing the enemy's attributes
    """
    file_location = 'game_data/enemy.json'
    try:
        with open(file_location, 'r') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        with open('../game_data/enemy.json', 'r') as file:
            output_file = json.load(file)
            return output_file


def read_trivia(file_location):
    """
    Read the trivia from the game.

    :param file_location: a non-empty string, location of the trivia file
    :precondition: file_location must be a non-empty string
    :postcondition: read the trivia from the game
    :return: a dict containing the trivia's attributes
    """
    try:
        with open(file_location, 'r') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        with open('../game_data/trivia.json', 'r') as file:
            output_file = json.load(file)
            return output_file


def update_enemies(data):
    """
    Update the enemies in the game.

    :param data: a dict containing the enemy's attributes
    :precondition: data must be a dict containing the enemy's attributes
    :postcondition: update the enemies in the game
    """
    file_location = 'game_data/enemy.json'
    try:
        with open(file_location, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('../game_data/enemy.json', 'w') as file:
            json.dump(data, file, indent=4)


def main():
    """
    Drive the program.
    """
    save_game({'name': 'T', 'level': 1, 'experience': 0, 'hp': 80, 'str': 15, 'int': 15, 'x-coordinate': 10, 'y-coordinate': 11})


if __name__ == "__main__":
    main()
