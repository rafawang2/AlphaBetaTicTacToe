from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QSlider, QPushButton
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen ,QFont,QPixmap
from PyQt5.QtCore import Qt, QTimer
from Tic_Tac_Toe import TicTacToe
import sys, os

class GameWindow(QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.game = TicTacToe()
        self.setGeometry(500, 200, 400, 600)
        self.setWindowTitle('Sudoku Solver Visualization')
        mainWindow_styleSheet = """
            QMainWindow {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6C6C6C, stop: 1 #5B5B5B);
            }
        """
        self.setStyleSheet(mainWindow_styleSheet)
        self.gap = 100
        self.BoardStart_pos = [50,50]
        self.mouse_events_enabled = False
        self.game.print_board()
        self.init_ui()
    def init_ui(self):
        self.startButton = QPushButton(self)
        self.startButton.setGeometry(100,400,200,50)
        button_styleSheet = """
        QPushButton
        {
            color: white;
            background-color: #27a9e3;
            border-width: 0px;
            border-radius: 3px;
        }
        
        QPushButton:hover
        {
            color: white;
            background-color: #66c011;
            border-width: 0px;
            border-radius: 3px;
        }
        
        QPushButton:pressed
        {
            color: white;
            background-color: yellow;
            border-width: 0px;
            border-radius: 3px;
        }
        
        
        QPushButton[pagematches=true]
        {
            color: white;
            background-color: red;
            border-width: 0px;
            border-radius: 3px;
        }
        """
        self.startButton.setStyleSheet(button_styleSheet)
        self.startButton.setText("Start!")
        self.startButton.clicked.connect(self.StartGame)
    
    def StartGame(self):
        print("Game Start!")
        if self.mouse_events_enabled:
            self.game.__init__()
            self.update()
        else:
            self.mouse_events_enabled = True
            self.game.__init__()
            self.update()
    
    
    def mousePressEvent(self, event):
        if not self.mouse_events_enabled:
            return  # 如果滑鼠事件未啟用，則直接返回
        if event.button() == Qt.LeftButton:  # 確保是左鍵點擊
            x = event.x() - self.BoardStart_pos[0] + self.gap
            y = event.y() - self.BoardStart_pos[1] + self.gap
            
            # 計算點擊的行和列
            row = y // self.gap - 1
            col = x // self.gap - 1
            print(f"{row} {col}")
            if self.game.current_player == -1:
                self.mouse_events_enabled = True
                if self.game.is_ValidMove(r=row,c=col):
                    self.game.board[row][col] = self.game.current_player
                    self.game.print_board()
                    self.game.current_player *= -1
            if self.game.current_player == 1:
                self.mouse_events_enabled = False
                move = self.game.best_move(1)
                if move:
                    r, c = move
                    self.game.board[r][c] = 1
                    self.game.current_player *= -1
                self.mouse_events_enabled = True
            
            if self.game.isWinner(-1):
                self.mouse_events_enabled = False
                print("Player X win!")
            elif self.game.isWinner(1):
                self.mouse_events_enabled = False
                print("Player O win!")
            elif self.game.isTie():
                self.mouse_events_enabled = False
                print("Tie!")
                
            
            self.update()
                                
        
        
    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_board(painter)
    
    def draw_board(self, painter):
        black_pen = QPen(QColor('#000000'), 3)
        red_pen = QPen(QColor('#EA0000'), 3)
        blue_pen = QPen(QColor('#0000E3'), 3)
        # 畫格線
        length = self.gap * 3
        painter.setPen(black_pen)
        for i in range(4):
            y = self.BoardStart_pos[1] + i * self.gap
            painter.drawLine(self.BoardStart_pos[0], y, 
                           self.BoardStart_pos[0] + length, y)
            
            x = self.BoardStart_pos[0] + i * self.gap
            painter.drawLine(x, self.BoardStart_pos[1], 
                           x, self.BoardStart_pos[1] + length)
        
        x = self.BoardStart_pos[0] + self.gap//4
        y = self.BoardStart_pos[1] + self.gap//4
        
        for i in range(3):
            x = self.BoardStart_pos[0] + self.gap//4
            for j in range(3):
                if self.game.board[i][j] == -1:
                    painter.drawLine(x, y,x+self.gap//2,y+self.gap//2)
                    painter.drawLine(x+self.gap//2, y,x,y+self.gap//2)
                elif self.game.board[i][j] == 1:
                    painter.drawEllipse(x, y,self.gap//2,self.gap//2)
                x += self.gap
            y += self.gap

def window():
    app = QApplication(sys.argv)
    win = GameWindow()
    win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    window()
    