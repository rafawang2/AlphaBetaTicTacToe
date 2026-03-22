def isWinner(board, player):  #回傳player是否為贏家
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def isTie(board):
    return all([cell != 0 for row in board for cell in row])

def print_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print('.', end=' ')
            elif board[i][j] == -1:
                print('X', end=' ')
            elif board[i][j] == 1:
                print('O', end=' ')
        print()

def is_ValidMove(board, r,c):
    if r<0 or c<0 or r>2 or c>2:
        return False
    return True if board[r][c] == 0 else False

def get_ValidMoves(board):
    validmoves = []
    for r in range(3):
        for c in range(3):
            if is_ValidMove(board,r,c):
                validmoves.append((r,c))
    return validmoves