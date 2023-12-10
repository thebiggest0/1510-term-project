"""
Move the character across the map.
"""
from save import save_data
from character import character
import json


def initialize_map():
    """
    Initialize the game map.

    :precondition: game is started
    :postcondition: return a list of lists representing the game map
    :return: a list of lists representing the game map
    """
    game_map = [
           ["J", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O", " ", "J"],
           ["#", "#", " ", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "O"],
           [" ", "#", " ", "#", "J", "#", " ", " ", " ", " ", " ", "#", " ", " "],
           [" ", " ", " ", "#", "O", " ", " ", " ", " ", " ", " ", " ", "#", " "],
           [" ", " ", " ", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
           [" ", "#", "J", " ", "#", " ", " ", " ", "#", "#", "#", "#", "#", " "],
           [" ", "#", "#", "#", "#", " ", "P", " ", "J", "V", " ", " ", " ", " "],
           [" ", " ", " ", " ", "#", " ", " ", " ", "#", "#", "#", "#", "#", "#"],
           [" ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
           [" ", " ", " ", "#", " ", "#", " ", " ", "J", " ", " ", " ", " ", " "],
           ["#", " ", "O", " ", " ", "#", " ", " ", " ", "#", "#", "#", " ", " "],
           ["J", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#", " ", " "],
           [" ", " ", " ", " ", "J", "O", " ", " ", " ", "#", " ", " ", "J", " "]]
    return game_map


def move_player(position, direction, map_size, game_map):
    """
    Move the player's position on the game map based on the specified direction.

    :param position: a list representing the current position of the player
    :param direction: a string representing the direction in which the player wants to move ('a' for left,
    'd' for right, 'w' for up, 's' for down)
    :param map_size: an int representing the size of the game map
    :param game_map: a list of lists representing the game map
    :precondition: position must be a list representing the current position of the player.
    :precondition: direction must be a string representing a valid movement direction ('a', 'd', 'w', or 's').
    :precondition: map_size must be an int representing the size of the game map.
    :precondition: game_map must be a list of lists representing the game map.
    :postcondition: move the player's position on the game map based on the specified direction.
                   If the move is valid, return the new position; otherwise, return the original position.
                   Print a message if the destination is a wall.

    :return: a list representing the new position of the player after the move if it is a valid move;
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
    elif direction == 's' and position[1] < map_size - 2:
        position[1] += 1

    if check_valid_move(position, game_map):
        return position
    else:
        print('You can not go there, it is a wall')
        return original_position


def print_map(game_map, player_position):
    """
    Print the game map with the player's position marked by 'X'.

    :param game_map: a list of lists representing the game map
    :param player_position: a list representing the current position of the player
    :precondition: game_map must be a list of lists representing the game map
    :precondition: player_position must be a list representing the current position of the player
    :postcondition: print the game map with the player's position marked by 'X'
    """
    print('_ ' + ' _ ' * len(game_map[0]) + ' _')
    for index_row in range(len(game_map)):
        print('|', end='  ')
        for index_column in range(len(game_map[index_row])):
            if [index_column, index_row] == player_position:
                print('\033[92m' + 'X' + '\033[0m', end='  ')
            else:
                print(game_map[index_row][index_column], end='  ')
        print('|')
    print('- ' + ' - ' * len(game_map[0]) + ' -')


def check_valid_move(position, game_map):
    """
    Check if a move to the specified position is valid based on the game map.

    :param position: a list representing the target position
    :param game_map: a list of lists representing the game map
    :precondition: position must be a list representing the target position
    :precondition: check_map must be a list of lists representing the game map
    :postcondition: return True if the move to the specified position is valid, otherwise return False
    :return: a Boolean, True if the move is valid, False otherwise
    >>> check_valid_move([0, 1], [['#', '_', '#'], ['_', 'X', '_'], ['#', '_', '#']])
    True
    >>> check_valid_move([0, 1], [['#', '_', '#'], ['#', 'X', '_'], ['#', '_', 'X']])
    False
    """
    if game_map[position[1]][position[0]] in (' ', '_', 'O', 'V', 'J', 'P'):
        return True
    else:
        return False


def main():
    """
    Drive the program.
    """
    name = input('What is your name: ')

    with open('../game_data/character.json', 'r') as file:
        data = json.load(file)
        if name not in data:
            player = character.create_character(name)
            save_data.save_game(player)
            with open('../game_data/character.json', 'r') as game_file:
                data = json.load(game_file)
        else:
            player = data[name]

    map_size = 14
    player_pos = [data[name]['x-coordinate'], data[name]['y-coordinate']]
    game_map = initialize_map()
    print_map(game_map, player_pos)
    while True:
        command = input("Enter move (up, down, left, right): ")
        if command in ['w', 's', 'a', 'd']:
            player_pos = move_player(player_pos, command, map_size, game_map)

            player['x-coordinate'] = player_pos[0]
            player['y-coordinate'] = player_pos[1]

            print_map(game_map, player_pos)
            print(player)
            save_data.save_game(player)
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
