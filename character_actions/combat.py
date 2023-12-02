"""
ADD A DOCSTRING
"""

import random
from save import save_data


def random_enemy():
    """
    Select a random enemy based on the current level.

    :precondition: function is called to select a random enemy; 'save_data' module is properly initialized
    and contains enemy data
    :postcondition: select a random enemy based on the current level
    :return: a dictionary representing the randomly selected enemy with its attributes
    """
    level_two_enemy = random.randrange(5)
    if level_two_enemy == 4:
        enemies = save_data.read_enemy()
        enemies_list = ['Royal Guard', 'Bounty Hunters', 'Mandalorian', 'Sith Troopers']
        random_number = random.randrange(4)
        enemy = enemies[enemies_list[random_number]]

    else:
        enemies = save_data.read_enemy()
        enemies_list = ['Clone Trooper', 'Battle Droids', 'Tusken Raiders']
        random_number = random.randrange(3)
        enemy = enemies[enemies_list[random_number]]

    return enemy


def is_valid_choice(value):
    """
    Determine if the provided value is a valid choice for a battle.

    :param value: a string the user input to be checked for validity
    :precondition: value must be a string
    :postcondition: determine if the provided value is a valid choice for a battle
    :return: a Boolean, True if the input is a valid whole number 1, 2, or 3; False otherwise
    >>> is_valid_choice('2')
    True
    >>> is_valid_choice('1.5')
    False
    >>> is_valid_choice('attack')
    False
    """
    try:
        float_value = float(value)
        return float_value.is_integer() and int(float_value) in [1, 2, 3]
    except ValueError:
        return False


def combat_choice():
    """
    Get the user's choice for a battle.

    :precondition: function is called to get the user's choice for a battle
    :postcondition: get the user's choice for a battle
    :return: an int, the user's valid choice for the battle (1 for attack, 2 for force, 3 for run)
    """
    while True:
        user_input = input('Battle initiated: (1): attack, (2): force, (3): run: ')
        if is_valid_choice(user_input):
            return int(user_input)
        else:
            print('Invalid input! You must input a number 1, 2, or 3. Try again.')


def combat_selection(user_choice, character):
    """
    Execute a combat function based on the user's choice.

    :param user_choice: an int, user's choice for the combat action (1 for attack, 2 for force, 3 for running away)
    :param character: a dict representing the character's attributes
    :precondition: user_choice must be an int, 1, 2 or 3
    :precondition: character must be a dict representing the character's attributes
    :postcondition: execute a combat function based on the user's choice
    :return: The result of the chosen combat function
    """
    if user_choice == 1:
        return attack_lightsaber(character)
    elif user_choice == 2:
        return attack_force(character)
    else:
        return run_away()


def random_calculate_generator():
    """
    Generate a random mathematical calculation.

    :precondition: function is called to generate a random mathematical calculation
    :postcondition: generates two random numbers and performs addition or subtraction based on the result of dice
    roll
    :return: a list containing a string representation of the mathematical calculation and the result
    """
    number_one = random.randrange(0, 50)
    number_two = random.randrange(-10, 30)
    dice = random.randrange(0, 6)
    if dice % 2 == 0:
        random_result = number_one + number_two
        operation = '+'
    else:
        random_result = number_one - number_two
        operation = '-'
    return [f'{number_one} {operation} {number_two} = ', random_result]


def random_product_generator():
    number_one = random.randrange(-5, 15)
    number_two = random.randrange(-5, 15)
    random_result = number_one * number_two
    return [f'{number_one} * {number_two} = ', random_result]


def run_away():
    dice = random.randrange(0, 6)
    player_guess = int(input('Guess a number between 1-6 inclusive: '))
    if player_guess == dice:
        return 0
    else:
        return -1


def attack_lightsaber(character):
    question = random_calculate_generator()
    user_answer = int(input(f'{question[0]}'))
    damage = 1
    if user_answer == question[1]:
        damage += character['str']
        return damage
    else:
        return damage


def attack_force(character):
    question = random_calculate_generator()
    user_answer = int(input(f'{question[0]}'))
    damage = 1
    if user_answer == question[1]:
        damage += character['int']
        return damage
    else:
        return damage


def experience_up(character, enemy):
    character['experience'] += enemy['experience']


def register_damage_outgoing(enemy, output_damage):
    enemy['hp'] -= output_damage
    if enemy['hp'] <= 0:
        print(f'You slayed {enemy["name"]}')
        return True
    else:
        print(f'You delt {output_damage} to {enemy["name"]}')
        return False


def register_damage_incoming(character, enemy):
    character['hp'] -= enemy['str']
    if character['hp'] <= 0:
        print('Your HP has fallen to 0, you have died...')
        return False
    else:
        print(f'You took {enemy["str"]} damage')
        return True
    # relate this to player_alive = boolean


def main():
    name = 'Thor'
    enemy = random_enemy()
    character = save_data.read_character(name)
    battle_status = True
    while battle_status:
        user_choice = combat_choice()
        damage = combat_selection(user_choice, character)
        if damage and damage != -1:
            print('dmg delt =', damage)
            # damage enemy
            register_damage_outgoing(enemy, damage)

            # if enemy not dead, they attack you
            if enemy['hp'] > 0:
                register_damage_incoming(character, enemy)
            else:
                experience_up(character, enemy)
                save_data.write_json(character)
                battle_status = False
        else:
            if damage == 0:
                print('You escaped successfully')
                return
            else:
                print('ran away but took dmg of', damage)
                character['hp'] -= damage


if __name__ == "__main__":
    main()
