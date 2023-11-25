"""
ADD A DOCSTRING
"""


def adjust_to_difficulty(enemy_info, difficulty):
    stats = {'easy': 1, 'medium': 2, 'hard': 3}
    for stat in ['hp', 'str', 'int', 'dex']:
        enemy_info[stat] *= stats[difficulty]
    return


def create_enemy(enemy_names, difficulty):
    """
    Create an enemy with specified attributes.
    """
    enemy_info = {
        'name': enemy_names,
        'hp': 50,
        'str': 5,
        'int': 5,
        'dex': 5,
    }
    adjust_to_difficulty(enemy_info, difficulty)


    return enemy_info

def create_vader(difficulty):
    enemy_info = {
        'name': 'darth vader',
        'hp': 50,
        'str': 15,
        'int': 15,
        'dex': 15,
        "combat_moves":
            {
            'slash': 20,
            'plunge': 30,
            'choke': 50,
            'force': 10,
            },
        "battle_dialogue":
            {
            'text_one': 'Luke I am your farther',
            'text_two': 'Placeholder',
            }
    }
    adjust_to_difficulty(enemy_info, difficulty)
    return enemy_info


def create_emperor():
    enemy_info = {
        'name': 'palpatine',
        'hp': 50,
        'str': 15,
        'int': 15,
        'dex': 15,
        "combat_moves":
            {
                'slash': 20,
                'choke': 50,
                'thunder': 15,
                'force': 10
            },
        "battle_dialogue":
            {
                'text_one': 'Luke I am your farther',
                'text_two': 'Placeholder',
            }
    }
    return enemy_info


def main():
    # only call this function once at the beginning
    # should pull data from JSON with enemy names and difficulty rating
    # should create all possible enemies based on difficulty level chosen
    # store all these info in JSON eventually


if __name__ == "__main__":
    main()
