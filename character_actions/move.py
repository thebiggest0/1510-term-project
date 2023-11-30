"""
Move the character.
"""
from save import save_data
from character import character
import json


def initialize_map():
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
    for index_row in range(len(game_map)):
        print('|', end=' ')
        for index_column in range(len(game_map[index_row])):
            if [index_column, index_row] == player_position:
                print('X', end=' ')
            else:
                print(game_map[index_row][index_column], end=' ')
        print('|')


def check_valid_move(position, check_map):
    if check_map[position[1]][position[0]] in ['_', 'O', '*', 'J']:
        # call battle against level 3 enemy
        # call enter jedi temple
        # call talk to jedi ghost
        # battle: +/-, x
        # intro
        # level up

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
