"""
ADD A DOCSTRING
"""
from save import save_data
from enemy import enemy
from character import character
from character_actions import combat
from character_actions import move
from character_actions import trivia


def main():
    name = 'Thor'
    difficulty = 'easy'
    enemy.create_enemy(difficulty)
    player = save_data.read_character(name)
    player_current_position = [player['x-coordinate'], player['y-coordinate']]
    game_map = move.initialize_map()
    map_size = 10
    move.print_map(game_map, player_current_position)
    game_play = True

    while game_play:
        game_end = False
        player = save_data.read_character(name)
        command = input("Enter move (up, down, left, right): ")
        if command in ['w', 's', 'a', 'd']:
            player_pos = move.move_player(player_current_position, command, map_size, game_map)

            # update player position
            player['x-coordinate'] = player_pos[0]
            player['y-coordinate'] = player_pos[1]

            move.print_map(game_map, player_pos)

            current_spot = game_map[player_pos[1]][player_pos[0]]
            # initiate the events!!!
            enemy_checker = combat.event_checker(current_spot)
            if enemy_checker:
                game_end = combat.fight_enemy(player, enemy_checker)
                character.level_up(player) # test level up system
            else:
                if current_spot == 'J':
                    trivia.jedi_interaction(player['name'])
                else:
                    save_data.save_game(player)

        else:
            print("Invalid command")

        if game_end:
            game_play = False

    print('Congratulations you won!')


if __name__ == "__main__":
    main()
