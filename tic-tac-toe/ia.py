import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text='', width=10, height=3, command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            
            if self.check_winner():
                self.show_winner()
                self.reset_game()
            elif self.check_draw():
                self.show_draw()
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)
        
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True  # Horizontal
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True  # Vertical
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True  # Diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True  # Diagonal

        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def show_winner(self):
        winner = f"Player {self.current_player} wins!"
        messagebox.showinfo("Game Over", winner)

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")

    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.config(text='', state=tk.NORMAL)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()