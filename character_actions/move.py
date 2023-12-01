"""
Move the character.
"""
from save import save_data
from character import character
import json


def initialize_map():
    """
    NO DOCSTRING FOR NOW
    """
    # make base map with '_' for each block
    # map = [['_' for _ in range(size)] for _ in range(size)]
    game_map = [
           ['_', '_', '_', '_', '_', '_', '#', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', 'O', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
           ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
    return game_map


def move_player(position, direction, map_size, game_map):
    """
    Move the player's position on the game map based on the specified direction.

    :param position: A list representing the current position of the player
    :param direction: A string representing the direction in which the player wants to move ('a' for left,
    'd' for right, 'w' for up, 's' for down)
    :param map_size: An int representing the size of the game map
    :param game_map: A list of lists representing the game map

    :precondition: position must be a list representing the current position of the player.
    :precondition: direction must be a string representing a valid movement direction ('a', 'd', 'w', or 's').
    :precondition: map_size must be an int representing the size of the game map.
    :precondition: game_map must be a list of lists representing the game map.

    :postcondition: Move the player's position on the game map based on the specified direction.
                   If the move is valid, return the new position; otherwise, return the original position.
                   Print a message if the destination is a wall.

    :return: A list representing the new position of the player after the move if it is a valid move;
             otherwise, the original position.
    >>> move_player([1, 1], 'w', 3, [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']])
    [1, 0]
    >>> move_player([0, 0], 's', 3, [['X', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])
    [0, 1]
    """
    original_position = position[:]

    if direction == 'a' and position[0] > 0:
        position[0] -= 1
    elif direction == 'd' and position[0] < map_size - 1:
        position[0] += 1
    elif direction == 'w' and position[1] > 0:
        position[1] -= 1
    elif direction == 's' and position[1] < map_size - 1:
        position[1] += 1

    if check_valid_move(position, game_map):
        return position
    else:
        print('You can not go there, it is a wall')
        return original_position


def print_map(game_map, player_position):
    """
    Print the game map with the player's position marked by 'X'.

    :param game_map: A list of lists representing the game map
    :param player_position: A list representing the current position of the player
    :precondition: game_map must be a list of lists representing the game map
    :precondition: player_position must be a list representing the current position of the player
    :postcondition: Print the game map with the player's position marked by 'X'
    """
    for index_row in range(len(game_map)):
        print('|', end=' ')
        for index_column in range(len(game_map[index_row])):
            if [index_column, index_row] == player_position:
                print('X', end=' ')
            else:
                print(game_map[index_row][index_column], end=' ')
        print('|')


def check_valid_move(position, game_map):
    """
    Check if a move to the specified position is valid based on the game map.

    :param position: A list representing the target position
    :param game_map: A list of lists representing the game map
    :precondition: position must be a list representing the target position
    :precondition: check_map must be a list of lists representing the game map
    :postcondition: Return True if the move to the specified position is valid, otherwise return False
    :return: a Boolean, True if the move is valid, False otherwise
    >>> check_valid_move([0, 1], [['#', '_', '#'], ['_', 'X', '_'], ['#', '_', '#']])
    True
    >>> check_valid_move([0, 1], [['#', '_', '#'], ['#', 'X', '_'], ['#', '_', 'X']])
    False
    """
    if game_map[position[1]][position[0]] in ['_', 'O', '*', 'J']:
        return True
    else:
        return False


def main():
    name = input('What is your name: ')

    with open('../game_data/character.json', 'r') as file:
        data = json.load(file)
        if name not in data:
            player = character.creat_character(name)
            save_data.save_game(player)
            with open('game_data/character.json', 'r') as game_file:
                data = json.load(game_file)
        else:
            player = data[name]

    map_size = 10
    player_pos = [data[name]['x-coordinate'], data[name]['y-coordinate']]
    game_map = initialize_map()
    print_map(game_map, player_pos)
    while True:
        command = input("Enter 'w', 's', 'a', 'd' to move up, down, left or right: ")
        if command in ['w', 's', 'a', 'd']:
            player_pos = move_player(player_pos, command, map_size, game_map)

            # update player position
            player['x-coordinate'] = player_pos[0]
            player['y-coordinate'] = player_pos[1]

            print_map(game_map, player_pos)
            print(player)
            save_data.save_game(player)
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
