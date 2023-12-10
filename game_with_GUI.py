import tkinter as tk
from tkinter import messagebox
from save import save_data
from enemy import enemy
from character import character
from character_actions import combat
from character_actions import move
from character_actions import trivia
from introduction import game_start
from conclusion import conclusion


class GameGUI:
    def __init__(self, master, player_name):
        self.master = master
        self.master.title("Game GUI")

        self.player_name = player_name
        self.player = save_data.read_character(player_name)
        self.player_current_position = [self.player['x-coordinate'], self.player['y-coordinate']]
        self.game_map = move.initialize_map()
        self.map_size = 14

        self.label = tk.Label(master, text=f"Welcome, {self.player_name}!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.move_button = tk.Button(master, text="Move", command=self.process_move)
        self.move_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        move.print_map(self.game_map, self.player_current_position)

    def process_move(self):
        command = self.entry.get().lower()
        game_end = False

        if command in ['w', 's', 'a', 'd']:
            player_pos = move.move_player(self.player_current_position, command, self.map_size, self.game_map)
            self.player['x-coordinate'] = player_pos[0]
            self.player['y-coordinate'] = player_pos[1]
            move.print_map(self.game_map, player_pos)

            current_spot = self.game_map[player_pos[1]][player_pos[0]]
            enemy_checker = combat.event_checker(current_spot)

            if enemy_checker:
                game_end = combat.fight_enemy(self.player, enemy_checker)
                character.level_up(self.player)
            else:
                if current_spot == 'J':
                    trivia.jedi_interaction(self.player['name'])
                else:
                    save_data.save_game(self.player)

        else:
            messagebox.showinfo("Invalid Command", "Please enter 'w', 's', 'a', or 'd'.")

        if game_end:
            self.end_game()

    def end_game(self):
        if self.player['hp'] <= 0:
            conclusion.game_lose()
        else:
            conclusion.game_win()


def main():
    name = game_start.name_entry()
    players = save_data.read_all_characters()

    if name not in players:
        game_start.intro_text()
        player_data = character.create_character(name)
        save_data.save_game(player_data)
        difficulty = game_start.select_difficulty()
        game_start.warm_up_question(name)
        enemy.create_enemy(difficulty)

    root = tk.Tk()
    game_gui = GameGUI(root, name)
    root.mainloop()


if __name__ == "__main__":
    main()
