import tkinter as tk
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=' ', font=('normal', 40, 'normal'), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner() is None:
                self.current_player = 'O'
                self.ai_move()
                self.current_player = 'X'
            self.check_winner()

    def ai_move(self):
        move = self.best_move()
        self.board[move[0]][move[1]] = 'O'
        self.buttons[move[0]][move[1]].config(text='O')

    def check_winner(self):
        winner = None
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                winner = row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                winner = self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            winner = self.board[0][2]

        if winner:
            self.show_winner(winner)
            return winner

        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            self.show_winner('Tie')
            return 'Tie'

        return None

    def show_winner(self, winner):
        if winner == 'Tie':
            result_text = "It's a tie!"
        else:
            result_text = f"{winner} wins!"

        result_label = tk.Label(self.root, text=result_text, font=('normal', 20, 'normal'))
        result_label.grid(row=3, column=0, columnspan=3)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner_state(board)
        if winner == 'X':
            return -1
        if winner == 'O':
            return 1
        if winner == 'Tie':
            return 0

        if is_maximizing:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move

    def check_winner_state(self, board):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return board[0][2]

        if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
            return 'Tie'

        return None

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
