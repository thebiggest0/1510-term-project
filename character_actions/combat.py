"""
ADD A DOCSTRING
"""

import random


def random_sum_generator():
    number_one = random.randrange(0, 500)
    number_two = random.randrange(-100, 300)
    dice = random.randrange(0, 6)
    if dice % 2 == 0:
        random_result = number_one + number_two
        operation = '+'
    else:
        random_result = number_one - number_two
        operation = '-'
    return [f'({number_one} {operation} {number_two} = ? )', random_result]


def random_product_generator():
    number_one = random.randrange(-100, 500)
    number_two = random.randrange(-100, 300)
    random_result = number_one * number_two
    return [f'({number_one} * {number_two} = ? )', random_result]


def run_away():
    dice = random.randrange(0, 6)
    player_guess = int(input('Guess a number between 1-6 inclusive: '))
    if player_guess == dice:
        return True
    else:
        return False


def attack_lightsaber(character, enemy):
    question = random_sum_generator()
    user_answer = int(input())
    damage = 0
    if user_answer == question:
        damage += character['str']
        return damage
    else:
        return damage


def attack_force(character):
    question = random_sum_generator()
    user_answer = int(input())
    damage = 0
    if user_answer == question:
        damage += character['int']
        return damage
    else:
        return damage


def experience_up(character, enemy):
    character['experience'] += enemy['experience']


def register_damage_outgoing(character, enemy, output_damage):
    enemy['hp'] -= output_damage
    if enemy['hp'] <= 0:
        print(f'You slayed {enemy["name"]}')
        return True
    else:
        print(f'You delt {output_damage} to {enemy["name"]}')
        return False


def register_damage_incoming(character, enemy, incoming_damage):
    character['hp'] -= incoming_damage
    if character['hp'] <= 0:
        print('Your HP has fallen to 0, you have died...')
        return False
    else:
        print(f'You took {incoming_damage} damage')
        return True
    # relate this to player_alive = boolean

def main():
    pass


if __name__ == "__main__":
    main()
