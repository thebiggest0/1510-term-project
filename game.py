"""
Play the game.
"""
from save import save_data
from enemy import enemy
from character import character
from character_actions import combat
from character_actions import move
from character_actions import trivia
from introduction import game_start
from conclusion import conclusion


def main():
    """
    Run the game.
    """
    name = game_start.name_entry()
    players = save_data.read_all_characters()
    if name not in players:
        game_start.intro_text()
        player_data = character_status.create_character(name)
        save_data.save_game(player_data)
        difficulty = game_start.select_difficulty()
        game_start.warm_up_question(name)
        enemy.create_enemy(difficulty)

    player = save_data.read_character(name)
    player_current_position = [player['x-coordinate'], player['y-coordinate']]
    game_map = move.initialize_map()
    map_size = 14
    move.print_map(game_map, player_current_position)
    game_play = True

    while game_play:
        game_end = False
        player = save_data.read_character(name)
        player_current_position = [player['x-coordinate'], player['y-coordinate']]
        command = input("Enter move ('w', 's', 'a' or 'd') to move (up, down, left or right): ")
        if command in ['w', 's', 'a', 'd']:
            player_pos = move.move_player(player_current_position, command, map_size, game_map)

            player['x-coordinate'] = player_pos[0]
            player['y-coordinate'] = player_pos[1]

            move.print_map(game_map, player_pos)

            current_spot = game_map[player_pos[1]][player_pos[0]]
            enemy_checker = combat.event_checker(current_spot)
            if enemy_checker:
                game_end = combat.fight_enemy(player, enemy_checker)
                character_status.level_up(player)
            else:
                if current_spot == 'J':
                    trivia.jedi_interaction(player['name'])
                else:
                    save_data.save_game(player)

        else:
            print("Invalid command")

        if game_end:
            game_play = False

    if player['hp'] <= 0:
        conclusion.game_lose()
    else:
        conclusion.game_win()


if __name__ == "__main__":
    main()
