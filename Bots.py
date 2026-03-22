from Tic_Tac_Toe_utils import *
import random

class BOT:
    def __init__(self, symbol):
        self.symbol = symbol
    def make_move(board):
        raise NotImplementedError( "virtualMethod is virutal! Must be overwrited and return a tuple with (r, c) format." )

class Player(BOT):
    def __init__(self, symbol):
        super().__init__(symbol)
    def make_move(self, board):
        while True:
            pos = str(input()).split(' ')
            r = int(pos[0])
            c = int(pos[1])
            if r>=3 or c >=3 or r<0 or c<0 or not is_ValidMove(board, r, c):
                print("Wrong Input")
                continue
            return r, c

class RandomBot(BOT):
    def __init__(self, symbol):
        super().__init__(symbol)
    def make_move(self, board):
        return random.choice(get_ValidMoves(board))

class AlphaBetaBot(BOT):
    def __init__(self, symbol):
        super().__init__(symbol)

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        # leaf node's score
        if isWinner(board, self.symbol): # win
            return 1
        elif isWinner(board, -self.symbol): # lose
            return -1
        elif isTie(board):  #平手
            return 0

        # AI's turn
        if maximizingPlayer:
            max_eval = float('-inf')
            for r in range(3):
                for c in range(3):
                    if is_ValidMove(board, r, c):
                        board[r][c] = self.symbol
                        eval = self.minimax(board, depth - 1, alpha, beta, False)   # go to min layer
                        board[r][c] = 0
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:  # Beta pruning
                            break
            return max_eval

        # Enemy's turn
        else:
            min_eval = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = -self.symbol
                        eval = self.minimax(board, depth - 1, alpha, beta, True)
                        board[r][c] = 0  #回復棋盤
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval  #回傳最小化玩家的最佳評估值

    def make_move(self, board):
        best_val = float('-inf')
        move = None  #儲存最佳移動的位置
        for r in range(3):
            for c in range(3):
                if is_ValidMove(board, r, c):
                    board[r][c] = self.symbol
                    move_val = self.minimax(board, 0, float('-inf'), float('inf'), False)   # go to min layer
                    board[r][c] = 0
                    if move_val > best_val:     # update best move
                        best_val = move_val
                        move = (r, c)
        return move  #回傳最佳移動的位置