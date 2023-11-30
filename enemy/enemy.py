"""
ADD A DOCSTRING
"""
import json


def create_enemy(difficulty):
    """
    Create an enemy with specified attributes.
    """
    stats = {'easy': 1, 'medium': 2, 'hard': 3}
    enemy_data = '../game_data/enemy.json'
    with open(enemy_data, 'r') as output_data:
        data = json.load(output_data)

        for name in data:
            for key in data[name]:
                if key in ['hp', 'str', 'int', 'dex']:
                    data[name][key] *= stats[difficulty]

            # update json file with new updated data
            with open('../game_data/enemy.json', 'w') as file:
                json.dump(data, file, indent=4)


def main():
    # only call this function once at the beginning
    # should pull data from JSON with enemy names and difficulty rating
    # should create all possible enemies based on difficulty level chosen
    # store all these info in JSON eventually


if __name__ == "__main__":
    main()
