"""
ADD A DOCSTRING
"""


def creat_character(name):
    """
    Create a character with specified attributes.
    """
    character_info = {
        'name': name,
        'level': 1,
        'experience': 100,
        'hp': 50,
        'str': 15,
        'int': 15,
        'dex': 15,
        'x-coordinate': 0,
        "y-coordinate": 0
    }
    return character_info


def level_up(character_info):
    """
    Increase level of the character.
    """
    experience_check = [100,200,300,500]
    if experience_check[character_info['level'] - 1] <= character_info['experience']:
        character_info['experience'] -= experience_check[character_info['level'] - 1]
        character_info['level'] += 1
        print(f'Congratulations {character_info["name"]}! you\'ve leveled up!')
        stat_increase(character_info)
    return character_info


def stat_increase(character_info):
    """
    Increase stats of the character.

    :postcondition: increase player hp by 10%
    :postcondition: increase player stats by 20%
    """
    character_info['hp'] = int(character_info['hp'] * 1.2)
    stats = ['str', 'int', 'dex']
    for stat in stats:
        character_info[stat] = int(character_info[stat] * 1.1)
    print('Your stats have increased!')
    print(f'HP: {character_info["hp"]} \nSTR: {character_info["str"]} \nINT: {character_info["int"]} '
          f'\nDEX: {character_info["dex"]}')

    # figure out how to update stats on GUI maybe?
    # figure out how to store changes to JSON, probably store it when save is called?
    return character_info


def main():
    name = 'Yoda'
    character = creat_character(name)
    level_up(character)
    # stat_increase(character)


if __name__ == "__main__":
    main()
