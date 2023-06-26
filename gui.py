import tkinter as tk
import Minimax_game
import Alpha_Beta_game

"""
Very important!

After running the gui program and choosing the prefered algorithm and level of difficulty 
Before clicking on start game make sure that your opened window is the http://kevinshannon.com/connect4/ game

"""

class GameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Connect Four - AI")

        # Choose algorithm label
        self.choose_algo_label = tk.Label(master, text="Choose algorithm:")
        self.choose_algo_label.pack()

        # Choose algorithm radio buttons
        self.var_algo = tk.StringVar(value="minimax")
        self.minimax_radio = tk.Radiobutton(master, text="Minimax", variable=self.var_algo, value="minimax")
        self.minimax_radio.pack()
        self.alpha_beta_radio = tk.Radiobutton(master, text="Alpha-Beta", variable=self.var_algo, value="alpha_beta")
        self.alpha_beta_radio.pack()

        # Choose difficulty label
        self.choose_difficulty_label = tk.Label(master, text="Choose difficulty level (1-7):")
        self.choose_difficulty_label.pack()

        # Choose difficulty scale
        self.var_difficulty = tk.IntVar(value=4)
        self.difficulty_scale = tk.Scale(master, from_=1, to=7, orient=tk.HORIZONTAL, variable=self.var_difficulty)
        self.difficulty_scale.pack()

        # Start game button
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        # Get algorithm choice and difficulty level
        algo = self.var_algo.get()
        difficulty = self.var_difficulty.get()

        # Run selected algorithm with chosen difficulty level
        if algo == "minimax":
            Minimax_game.main(depth=difficulty)
        elif algo == "alpha_beta":
            Alpha_Beta_game.main(depth=difficulty)

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()