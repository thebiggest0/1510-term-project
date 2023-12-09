"""
Create enemy.
"""
import json


def create_enemy(difficulty):
    """
    Create an enemy with specified attributes.
    """
    enemy_data_path = '../game_data/enemy_template.json'
    output_path = '../game_data/enemy.json'

    with open(enemy_data_path, 'r') as input_file:
        data = json.load(input_file)

        updated_data = {
            name: {key: value * difficulty if key in ['hp', 'str', 'int', 'dex'] else value
                   for key, value in attributes.items()}
            for name, attributes in data.items()
        }

    with open(output_path, 'w') as output_file:
        json.dump(updated_data, output_file, indent=4)


def main():
    create_enemy('easy')


if __name__ == "__main__":
    main()
