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
        i = random.randrange(4)
        enemy = enemies[enemies_list[i]]

    else:
        enemies = save_data.read_enemy()
        enemies_list = ['Clone Trooper', 'Battle Droids', 'Tusken Raiders']
        i = random.randrange(3)
        enemy = enemies[enemies_list[i]]

    return enemy


def combat_choice():
    while True:
        user_choice = int(input('Battle initiated: (1): attack, (2): force, (3): run: '))
        if user_choice in [1, 2, 3]:
            return user_choice


def combat_selection(user_choice, character):
    if user_choice == 1:
        return attack_lightsaber(character)
    elif user_choice == 2:
        return attack_force(character)
    else:
        return run_away()


def random_sum_generator():
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
    question = random_sum_generator()
    user_answer = int(input(f'{question[0]}'))
    damage = 1
    if user_answer == question[1]:
        damage += character['str']
        return damage
    else:
        return damage


def attack_force(character):
    question = random_sum_generator()
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
        # run away
            if damage == 0:
                print('You escaped successfully')
                return
            else:
                print('ran away but took dmg of', damage)
                character['hp'] -= damage


if __name__ == "__main__":
    main()
