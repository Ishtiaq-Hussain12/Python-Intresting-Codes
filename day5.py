import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initializing variables & missing constants visible in snippets
        self.human = "X"
        self.bot = "O"
        self.current_player = self.human
        self.board = [""] * 9
        self.buttons = []
        self.MISTAKE_CHANCE = 0.2  # Defined based on bot_move logic
        
        # Color settings from WhatsApp Image 2026-06-30 at 11.44.56 AM.jpeg
        self.BG_COLOR = "#2c1d47"
        self.BTN_COLOR = "#4a2c72"
        self.HOVER_COLOR = "#5c388c"
        self.X_COLOR = "#e0b0ff"
        self.O_COLOR = "#da70d6"
        
        self.root.config(bg=self.BG_COLOR)
        self.create_widgets()

    def create_widgets(self):
        # Snippet from WhatsApp Image 2026-06-30 at 11.44.56 AM.jpeg
        self.title_label = tk.Label(
            self.root,
            text="Your Turn (X)",
            font=("Helvetica", 16, "bold"),
            bg=self.BG_COLOR,
            fg="#ffffff"
        )
        self.title_label.pack(pady=15)
        
        self.grid_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.grid_frame.pack()
        
        for i in range(9):
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=("Helvetica", 24, "bold"),
                width=5,
                height=2,
                bg=self.BTN_COLOR,
                fg="#ffffff",
                activebackground=self.HOVER_COLOR,
                activeforeground="#ffffff",
                relief="flat",
                command=lambda idx=i: self.on_click(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Snippet transitions from Image 3 to WhatsApp Image 2026-06-30 at 11.44.50 AM.jpeg
        self.reset_btn = tk.Button(
            self.root,
            text="Reset Game",
            font=("Helvetica", 12, "bold"),
            bg="#8a2be2",
            fg="#ffffff",
            activebackground="#9932cc",
            activeforeground="#ffffff",
            relief="flat",
            command=self.reset_game
        )
        self.reset_btn.pack(pady=20)

    # Snippet from WhatsApp Image 2026-06-30 at 11.44.50 AM.jpeg
    def on_click(self, idx):
        if self.board[idx] == "" and self.current_player == self.human:
            self.make_move(idx, self.human, self.X_COLOR)
            
            if self.check_game_over():
                return
                
            self.current_player = self.bot
            self.title_label.config(text="Bot is thinking...")
            self.root.after(400, self.bot_move)

    def make_move(self, idx, player, color):
        self.board[idx] = player
        self.buttons[idx].config(text=player, fg=color)

    def bot_move(self):
        move = None
        empty_spots = [i for i, spot in enumerate(self.board) if spot == ""]
        
        # Roll the dice: Does the bot make a mistake?
        if random.random() < self.MISTAKE_CHANCE:
            if empty_spots:
                move = random.choice(empty_spots)  # Pure random move
        else:
            # 1. Try to win
            move = self.find_winning_move(self.bot)
            # 2. Block the player
            if move is None:
                move = self.find_winning_move(self.human)
                
            if move is None and empty_spots:
                move = random.choice(empty_spots)
                
        if move is not None:
            self.make_move(move, self.bot, self.O_COLOR)
            if self.check_game_over():
                return
            self.current_player = self.human
            self.title_label.config(text="Your Turn (X)")

    # Snippet from jh.jpeg
    def find_winning_move(self, player):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for c1, c2, c3 in win_coords:
            # Checking for a line where 2 are filled by the player and 1 is empty
            if self.board[c1] == player and self.board[c2] == player and self.board[c3] == "":
                return c3
            if self.board[c1] == player and self.board[c3] == player and self.board[c2] == "":
                return c2
            if self.board[c2] == player and self.board[c3] == player and self.board[c1] == "":
                return c1
        return None

    def check_game_over(self):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for coord in win_coords:
            if self.board[coord[0]] == self.board[coord[1]] == self.board[coord[2]] != "":
                winner = "Fuck Bro!" if self.board[coord[0]] == self.human else "Oh My Yes!"
                messagebox.showinfo("OHHHHH", winner)
                self.reset_game()
                return True
                
        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return True
            
        return False

    def reset_game(self):
        self.current_player = self.human
        self.board = [""] * 9
        self.title_label.config(text="Your Turn (X)")
        for btn in self.buttons:
            btn.config(text="", bg=self.BTN_COLOR)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x450")
    game = TicTacToeBot(root)
    root.mainloop()