import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x450")
        self.root.configure(bg="#2c3e50")

        self.moves = {"Rock": "🪨", "Paper": "📃", "Scissors": "✂️"}
        self.valid_choices = list(self.moves.keys())
        self.scores = {"user": 0, "computer": 0}

        self.setup_ui()

    def setup_ui(self):
        self.title_label = tk.Label(self.root, text="Choose Your Weapon", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="You: 0  |  Computer: 0", font=("Helvetica", 14), bg="#2c3e50", fg="#f1c40f")
        self.score_label.pack(pady=10)

        self.result_label = tk.Label(self.root, text="Let's Play!", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1", wraplength=350)
        self.result_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="#2c3e50")
        self.button_frame.pack(pady=20)

        for move, emoji in self.moves.items():
            btn = tk.Button(self.button_frame, text=f"{move}\n{emoji}", font=("Helvetica", 12), width=8, height=3, bg="#ecf0f1", command=lambda m=move: self.play_round(m))
            btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(self.root, text="Reset Score", command=self.reset_game, bg="#e74c3c", fg="white")
        self.reset_btn.pack(pady=20)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.valid_choices)
        winner = self.determine_winner(user_choice, computer_choice)
        self.update_display(user_choice, computer_choice, winner)

    def determine_winner(self, user, computer):
        if user == computer: return "tie"
        if ((user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock")):
            self.scores["user"] += 1
            return "user"
        self.scores["computer"] += 1
        return "computer"

    def update_display(self, user, computer, winner):
        user_emoji = self.moves[user]
        comp_emoji = self.moves[computer]
        result_text = f"You: {user_emoji} vs Comp: {comp_emoji}\n"
        if winner == "tie":
            result_text += "It's a Tie!"
            color = "#f1c40f"
        elif winner == "user":
            result_text += "You Win!"
            color = "#2ecc71"
        else:
            result_text += "Computer Wins!"
            color = "#e74c3c"
        self.result_label.config(text=result_text, fg=color, font=("Helvetica", 16, "bold"))
        self.score_label.config(text=f"You: {self.scores['user']}  |  Computer: {self.scores['computer']}")

    def reset_game(self):
        self.scores = {"user": 0, "computer": 0}
        self.score_label.config(text="You: 0  |  Computer: 0")
        self.result_label.config(text="Game Reset!", fg="#ecf0f1")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()