"""
ADD A DOCSTRING
"""

import json


# def save_game(character):
#     write_json(character)


def save_game(character):

    # stores all data in json file as 'data'
    with open('../game_data/character.json', 'r') as file:
        data = json.load(file)

    # add character name as key with entire dictionary as value to data
    # if existing data, it will override, if it does not exist it will add as new
    data.update({character['name']: character})

    # update json file with new updated data
    with open('../game_data/character.json', 'w') as file:
        json.dump(data, file, indent=4)


def read_character(name):
    file_location = '../game_data/character.json'
    with open(file_location, 'r') as file:
        output_file = json.load(file)
        return output_file[name]


def read_all_characters():
    file_location = '../game_data/character.json'
    with open(file_location, 'r') as file:
        output_file = json.load(file)
        return output_file


def read_enemy():
    file_location = '../game_data/enemy.json'
    with open(file_location, 'r') as file:
        output_file = json.load(file)
        return output_file


def read_trivia(file_location):
    with open(file_location, 'r') as file:
        output_file = json.load(file)
        return output_file


def update_enemies(data):
    file_location = '../game_data/enemy.json'
    with open(file_location, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    pass


if __name__ == "__main__":
    main()
