"""

"""


def check_valid_move(position, game_map):
    pass


def move_player(position, direction, map_size, game_map):
    x, y = position
    a, b = 0, 0
    if direction == 'a' and x > 0:
        a = -1
    elif direction == 'd' and x < map_size - 1:
        a = 1
    elif direction == 'w' and y > 0:
        b = -1
    elif direction == 's' and y < map_size - 1:
        b = 1

    position[0] += a
    position[1] += b
    if check_valid_move(position, game_map):
        return position
    else:
        print('You can not go there, it is a wall')
        return [position[0] - a, position[1] - b]


def print_map(game_map, player_position):
    for index_row in range(len(game_map)):
        print('|', end=' ')
        for index_column in range(len(game_map[index_row])):
            if [index_column, index_row] == player_position:
                print('X', end=' ')
            else:
                print(game_map[index_row][index_column], end=' ')
        print('|')


def main():
    pass


if __name__ == "__main__":
    main()
