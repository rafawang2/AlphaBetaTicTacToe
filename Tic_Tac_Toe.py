from Tic_Tac_Toe_utils import *
from Bots import *

class TicTacToe():
    def __init__(self, player1:BOT, player2:BOT):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = -1
        self.player1 = player1
        self.player2 = player2
        self.player1.symbol = -1
        self.player2.symbol = 1

    def play(self):
        self.current_player = -1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # reset
        while True:
            if self.current_player == -1:   # player 1's turn
                print("Player 1's turn")
                r, c = self.player1.make_move(self.board)
                self.board[r][c] = self.player1.symbol
                self.current_player*=-1
            else:
                print("Player 2's turn")
                r, c = self.player2.make_move(self.board)
                self.board[r][c] = self.player2.symbol
                self.current_player*=-1
            print_board(self.board)

            if isWinner(self.board, 1):
                print("(O) wins!")
                break
            elif isWinner(self.board, -1):
                print("(X) wins!")
                break
            elif isTie(self.board):
                print("It's a tie!")
                break

game = TicTacToe(player1=Player(-1), player2=AlphaBetaBot(1))
print_board(game.board)
game.play()