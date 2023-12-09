"""
This module interacts with data stored in JSON files.
"""

import json


def save_game(character):

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
    try:
        with open(file_location, 'r') as file:
            output_file = json.load(file)
            return output_file
    except FileNotFoundError:
        with open('../game_data/trivia.json', 'r') as file:
            output_file = json.load(file)
            return output_file


def update_enemies(data):
    file_location = 'game_data/enemy.json'
    try:
        with open(file_location, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open('../game_data/enemy.json', 'w') as file:
            json.dump(data, file, indent=4)


def main():
    pass


if __name__ == "__main__":
    main()
