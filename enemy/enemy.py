"""
Create enemy.
"""
import json
from save import save_data


def create_enemy(difficulty):
    """
    Create an enemy with specified attributes.
    """
    enemy_data = '../game_data/enemy_template.json'
    with open(enemy_data, 'r') as output_data:
        data = json.load(output_data)

        for name in data:
            for key in data[name]:
                if key in ['hp', 'str', 'int', 'dex']:
                    data[name][key] *= difficulty
                    int(data[name][key])

            with open('../game_data/enemy.json', 'w') as file:
                json.dump(data, file, indent=4)


def main():
    create_enemy('easy')


if __name__ == "__main__":
    main()
