"""
Combat with enemies.
"""

import random
from save import save_data


def random_enemy():
    """
    Select a random enemy.

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
    """
    Generate a random mathematical product.

    :precondition: function is called to generate a random mathematical product
    :postcondition: generates two random numbers and performs multiplication to calculate the product
    :return: a list containing a string representation of the mathematical product and the result
    """
    number_one = random.randrange(-5, 15)
    number_two = random.randrange(-5, 15)
    random_result = number_one * number_two
    return [f'{number_one} * {number_two} = ', random_result]


def run_away():
    """
    Determine if the user can run away.

    :precondition: function is called to simulate a player attempting to run away
    :postcondition: generates a random dice roll between 1 and 6, and compares it to the player's guess;
                   returns 0 if the guess matches the dice roll, and -1 otherwise;
                   if the player enters a non-integer guess, returns -1
    :return: an int, 0 if the player's guess matches the dice roll, -1 otherwise
    """
    dice = random.randrange(1, 7)
    try:
        player_guess = int(input('Guess a number between 1-6 inclusive: '))
    except ValueError:
        return -1
    if player_guess == dice:
        return 0
    else:
        return -1


def attack_lightsaber(character):
    """
    Simulate a lightsaber attack in a combat scenario.

    :param character: a dictionary representing the character's attributes, including strength ('str')
    :precondition: function is called to simulate a lightsaber attack
    :postcondition: generates a random calculation question using the `random_calculate_generator` function
                   if the user's answer matches the correct result, increases the damage dealt by the character's
                   strength
    :return: an int, damage based on the user's answer and the character's strength
    """
    damage = 1
    question = random_calculate_generator()
    try:
        user_answer = int(input(f'{question[0]}'))
    except ValueError:
        return damage
    if user_answer == question[1]:
        damage += character['str']
        return damage
    else:
        return damage


def attack_force(character):
    """
    Simulate a force attack in a combat scenario.

    :param character: a dictionary representing the character's attributes, including strength ('str')
    :precondition: function is called to simulate a force attack
    :postcondition: generates a random calculation question using the `random_calculate_generator` function
                   if the user's answer matches the correct result, increases the damage dealt by the character's
                   strength
    :return: an int, damage based on the user's answer and the character's strength
    """
    damage = 1
    question = random_calculate_generator()
    try:
        user_answer = int(input(f'{question[0]}'))
    except ValueError:
        return damage
    if user_answer == question[1]:
        damage += character['str']
        return damage
    else:
        return damage


def experience_up(character, enemy):
    """
    Increase the character's experience points based on defeating an enemy.

    :param character: a dict representing the character's attributes, with a key 'experience'
    :param enemy: a dict representing the defeated enemy's attributes, with a key 'experience'
    :precondition: character must be a dict representing the character's attributes, with a key 'experience'
    :precondition: enemy  must be a dict representing the defeated enemy's attributes, with a key 'experience'
    :postcondition: increase the character's experience points based on defeating an enemy
    >>> character_data = {'name': 'Jedi Knight', 'experience': 50}
    >>> enemy_data = {'name': 'Sith Lord', 'experience': 30}
    >>> experience_up(character_data, enemy_data)
    >>> character_data['experience']
    80

    >>> character_data = {'name': 'Thor', 'experience': 10}
    >>> enemy_data = {'name': 'Loki', 'experience': 10}
    >>> experience_up(character_data, enemy_data)
    >>> character_data['experience']
    20
    """
    character['experience'] += enemy['experience']


def register_damage_outgoing(enemy, output_damage):
    """
    Register outgoing damage to an enemy during a combat scenario.

    :param enemy: a dict representing the enemy's attributes, including keys 'name' and 'hp'
    :param output_damage: an int representing amount of damage dealt to the enemy
    :precondition: enemy must be a dict representing the enemy's attributes, including keys 'name' and 'hp'
    :precondition: output_damage must be an int representing amount of damage dealt to the enemy
    :postcondition: deduct the output damage from the enemy's hit points; if the enemy's hit points fall to or below
    0, prints a message indicating the enemy has been slain and returns True; otherwise, prints a message indicating
    the damage dealt to the enemy and returns False
    :return: a Boolean, True if the enemy is slain, False otherwise
    """
    enemy['hp'] -= output_damage
    if enemy['hp'] <= 0:
        print(f'You slain {enemy["name"]}')
        return True
    else:
        print(f'You dealt {output_damage} to {enemy["name"]}')
        return False


def register_damage_incoming(character, enemy):
    """
    Register incoming damage to the character during a combat scenario.

    :param character: a dict representing the character's attributes, with key 'hp'
    :param enemy: a dict representing the attacking enemy's attributes, with key 'str'
    :precondition: character must be a dict representing the character's attributes, with key 'hp'
    :precondition: enemy must be a dict representing the attacking enemy's attributes, with key 'str'
    :postcondition: deducts the enemy's strength from the character's hit points, if the character's hit points fall
    to or below 0, prints a message indicating the character has died and returns False, otherwise, prints a message
    indicating the damage taken and returns True
    :return: a Boolean, False if the character has died, True otherwise
    """
    character['hp'] -= enemy['str']
    save_data.save_game(character)
    if character['hp'] <= 0:
        print('Your HP has fallen to 0, you have died...')
        return False
    else:
        print(f'You took {enemy["str"]} damage')
        return True
    # relate this to player_alive = boolean


def fight_vader():
    """
    Fight Darth Vader.

    :precondition: function is called to fight Darth Vader
    :postcondition: return Darth Vader's attributes
    :return: a dict representing Darth Vader's attributes
    >>> fight_vader()
    {'name': 'Darth Vader', 'difficulty': 4, 'hp': 200, 'str': 20, 'experience': 500}
    """
    enemies = save_data.read_enemy()
    boss = enemies['Darth Vader']
    return boss


def fight_emperor():
    """
    Fight Emperor Palpatine.

    :precondition: function is called to fight Emperor Palpatine
    :postcondition: return Emperor Palpatine's attributes
    :return: a dict representing Emperor Palpatine's attributes
    >>> fight_emperor()
    {'name': 'Palpatine', 'difficulty': 4, 'hp': 300, 'str': 25, 'experience': 0}
    """
    enemies = save_data.read_enemy()
    boss = enemies['Emperor']
    return boss


def fight_mini_boss():
    """
    Fight a mini boss.

    :precondition: function is called to fight a mini boss
    :postcondition: return the mini boss's attributes
    :return: a dict representing the mini boss's attributes
    """
    enemies = save_data.read_enemy()
    for enemy in enemies:
        if enemies[enemy]['difficulty'] == 3:
            mini_boss = enemies.pop(enemy)
            save_data.update_enemies(enemies)
            return mini_boss


def event_checker(coordinates):
    """
    Check if the user has encountered an event.

    :param coordinates: a string representing the coordinates of the player's current location
    :precondition: coordinates must be a string representing the coordinates of the player's current location
    :postcondition: check if the player has encountered an event
    :return: a Boolean, True if the player has encountered an event, False otherwise
    """
    print(coordinates)
    if coordinates == '_' or coordinates == ' ':
        # number = random.randrange(2)
        # if number == 1:
        #     return random_enemy()
        # else:
        #     return False
        return False
    elif coordinates == 'J':
        return False
    elif coordinates == 'O':
        return fight_mini_boss()
    elif coordinates == 'V':
        return fight_vader()
    elif coordinates == 'P':
        return fight_emperor()


def fight_enemy(character, enemy):
    """
    Fight an enemy.

    :param character: a dict representing the character's attributes
    :param enemy: a dict representing the enemy's attributes
    :precondition: character must be a dict representing the character's attributes
    :precondition: enemy must be a dict representing the enemy's attributes
    :postcondition: fight an enemy
    :return: a Boolean, True if the player has died, False otherwise
    """
    print(enemy)
    battle_status = True
    character_status = True
    while battle_status:
        user_choice = combat_choice()
        damage = combat_selection(user_choice, character)
        if damage and damage != -1:
            print('dmg delt =', damage)
            # damage enemy
            register_damage_outgoing(enemy, damage)

            # if enemy not dead, they attack you
            if enemy['hp'] > 0:
                character_status = register_damage_incoming(character, enemy)
                battle_status = False
            else:
                experience_up(character, enemy)
                save_data.save_game(character)
                battle_status = False
        else:
            if damage == 0:
                print('You escaped successfully')
                return
            else:
                print('ran away but took dmg of', damage)
                character['hp'] -= damage
    if not character_status:
        return True
    if enemy['name'] == 'Palpatine':
        return True


def main():
    """
    Drive the program.
    """
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
                save_data.save_game(character)
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
