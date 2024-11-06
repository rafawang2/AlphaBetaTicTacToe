class TicTacToe():
    def __init__(self, ai_symbol=1):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.ai_symbol = ai_symbol  #AI的符號，1代表O，-1代表 X
        self.player_symbol = -ai_symbol  #玩家符號為AI的反轉
        self.current_player = -1
        
        
    def isWinner(self,player):  #回傳player是否為贏家
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False
    
    def isTie(self):
        return all([cell != 0 for row in self.board for cell in row])
    
    def print_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    print('.', end=' ')
                elif self.board[i][j] == -1:
                    print('X', end=' ')
                elif self.board[i][j] == 1:
                    print('O', end=' ')
            print()
        
    def is_ValidMove(self,r,c):
        if r<0 or c<0 or r>2 or c>2:
            return False
        
        return True if self.board[r][c] == 0 else False
    
    def player_make_move(self):
        pos = str(input()).split(' ')
        r = int(pos[0])
        c = int(pos[1])
        if r>=3 or c >=3 or r<0 or c<0:
            print("Wrong Input")
            return None    
        return r, c
    
    def minimax(self, depth, alpha, beta, maximizingPlayer):
        # 檢查是否有勝利者或和局
        if self.isWinner(self.ai_symbol):  #AI獲勝
            return 1
        elif self.isWinner(self.player_symbol):  #玩家獲勝
            return -1
        elif self.isTie():  #平手
            return 0

        #AI回合(最大化玩家)
        if maximizingPlayer:
            max_eval = float('-inf')  #初始最大值為負無限大
            #遍歷棋盤
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == 0:  #若格子為空
                        self.board[r][c] = self.ai_symbol  #AI嘗試在此位置下子
                        #計算玩家的評估值
                        eval = self.minimax(depth - 1, alpha, beta, False)  #跳至計算玩家回合
                        self.board[r][c] = 0  #回復棋盤
                        max_eval = max(max_eval, eval)  #更新當前最大評估值
                        alpha = max(alpha, eval)  # 更新alpha值(最大邊界)
                        if beta <= alpha:  #若beta<=alpha，停止搜尋(beta剪枝)
                            break
            return max_eval  #回傳最大化玩家的最佳評估值

        #若輪到玩家(最小化玩家)的回合
        else:
            min_eval = float('inf')  #初始化最小值為正無限大

            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == 0:
                        self.board[r][c] = self.player_symbol  #玩家在此位置下子
                        #計算AI的評估值
                        eval = self.minimax(depth - 1, alpha, beta, True)   #跳至計算AI回合
                        self.board[r][c] = 0  #回復棋盤
                        min_eval = min(min_eval, eval)  #更新當前最小評估值
                        beta = min(beta, eval)  # 更新beta值(最小邊界)
                        if beta <= alpha:  #若beta<=alpha，停止搜尋 (alpha剪枝)
                            break
            return min_eval  #回傳最小化玩家的最佳評估值

    def best_move(self, player):
        best_val = float('-inf')  #設定初始最佳分數為負無限大
        move = None  #儲存最佳移動的位置
        #遍歷棋盤
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    
                    if player == self.ai_symbol:
                        self.board[r][c] = self.ai_symbol  #AI嘗試在此位置下子
                        #使用minimax函數計算此移動的評估值(玩家下一步)
                        move_val = self.minimax(0, float('-inf'), float('inf'), False)
                        self.board[r][c] = 0  #回復棋盤
                        if move_val > best_val:  #若此移動評估值優於目前最佳值
                            best_val = move_val  #更新最佳值
                            move = (r, c)  #儲存最佳位置
                    else:
                        self.board[r][c] = -self.ai_symbol  #AI對手嘗試在此位置下子
                        #使用minimax函數計算此移動的評估值(玩家下一步)
                        move_val = self.minimax(0, float('-inf'), float('inf'), True)
                        self.board[r][c] = 0  #回復棋盤
                        if move_val > best_val:  #若此移動評估值優於目前最佳值
                            best_val = move_val  #更新最佳值
                            move = (r, c)  #儲存最佳位置
                            
        return move  #回傳最佳移動的位置


    def self_play(self, games):
        print(f"AI is {self.ai_symbol}")
        results = {'win': 0, 'loss': 0, 'tie': 0}
        for _ in range(games):
            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            current_player = -1
            game_over = False
            self.print_board()
            while not game_over:
                if current_player == self.ai_symbol:
                    move = self.best_move(self.ai_symbol)
                else:
                    move = self.best_move(-self.ai_symbol)
                if move:
                    r, c = move
                    self.board[r][c] = current_player
                self.print_board()
                if self.isWinner(self.ai_symbol):
                    results['win'] += 1
                    game_over = True
                    print('AI win')
                elif self.isWinner(-self.ai_symbol):
                    results['loss'] += 1
                    game_over = True
                    print('Human win')
                elif self.isTie():
                    results['tie'] += 1
                    game_over = True
                    print('Tie')
                else:
                    current_player *= -1
            print("--------------")
        print(f"贏: {results['win']} 輸: {results['loss']} 平手: {results['tie']}")

    
    def play(self):
        self.current_player = -1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #重置棋盤
        while True:
            if self.current_player == -1:
                r, c = self.player_make_move()
                if self.is_ValidMove(r,c):
                    self.board[r][c] = -1
                    self.current_player = 1
            else:
                print("AI is making a move...")
                move = self.best_move(self.ai_symbol)
                if move:
                    r, c = move
                    self.board[r][c] = 1
                    self.current_player = -1
            self.print_board()

            if self.isWinner(1):
                print("AI (O) wins!")
                break
            elif self.isWinner(-1):
                print("Player (X) wins!")
                break
            elif self.isTie():
                print("It's a tie!")
                break
            
        
    
# game = TicTacToe()
# game.print_board()
# game.play()