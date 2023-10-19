import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
import numpy as np
import pandas as pd

magic = 9
def create_random_grid(m, n, s):
    grid = np.zeros((m, n), dtype=int)  # Create an m x n grid of zeros
    if s > m * n:
        raise ValueError("s should be less than or equal to m * n")

    ones_indices = np.random.choice(m * n, s, replace=False)
    for idx in ones_indices:
        row, col = divmod(idx, n)
        grid[row, col] = magic

    # Initialize neighbor_counts to keep track of boom booms
    neighbor_counts = grid.copy()

    for i in range(m):
        for j in range(n):
            if grid[i, j] == magic:
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        neighbor_counts[x, y] += 1

    return neighbor_counts

class minesweeper(QWidget):

    def create_button(self, name, movex, movey, rex, rey, fonttype, fontsize, func):
        b = QPushButton(name, self)
        b.move(movex, movey)
        b.resize(rex, rey)
        b.setFont(QFont(fonttype, fontsize))
        b.clicked.connect(func)
        return b
    
    def create_label(self, name, movex, movey, rex, rey, fonttype, fontsize):
        l = QLabel(name, self)
        l.move(movex, movey)
        l.resize(rex, rey)
        l.setFont(QFont(fonttype, fontsize))
        return l
    
    def __init__(self):
        super().__init__()
        # Define the board size
        self.rows = 16
        self.columns = 30
        self.cell_size = 20
        self.bombs = 100
        self.grid = create_random_grid(self.rows, self.columns, self.bombs)

        # gridi = pd.DataFrame(self.grid)
        # print(gridi)

        # Initialize the game board
        self.board = [[0] * (self.columns+1) for _ in range(self.rows)]
        self.setWindowTitle("Minesweeper")
        self.setStyleSheet(
            """
            background: black;
            """
        )
        self.setMinimumSize(QSize(1400, 900))  
        self.reset = self.create_button("Reset the Game!", 850,200,550,100,'System',60,self.reset_game)
        self.banter = self.create_label("Make a Line of 5!", 1000,400,550,100,'System',32)
        self.reset.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0);
            color: white; 
            """
        ) 
        self.banter.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0);
            color: white; 
            """
        )  

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother edges

        for row in range(self.rows):
            for col in range(self.columns):
                col += 1
                cell_color = QColor(255, 255, 255)  # Default cell color (white)
                if self.board[row][col] == 1:
                    cell_color = QColor(255, 0, 0)  # Red
                elif self.board[row][col] == 2:
                    cell_color = QColor(0, 0, 255)  # Blue
                
                painter.setBrush(QColor(255, 255, 255)) 
                painter.drawRect(col * self.cell_size, (row + 1) * self.cell_size, self.cell_size, self.cell_size)

                painter.setBrush(cell_color)
                painter.drawEllipse(col * self.cell_size, (row + 1) * self.cell_size, self.cell_size, self.cell_size)

    def reset_game(self):
        return 0 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            # Check which circle was clicked
            for col in range(self.columns):
                col += 1
                s_x = col * self.cell_size
                s_y = self.cell_size  # Offset for the row
                if x > s_x and x < s_x + self.cell_size and y > s_y and y < s_y*(self.rows+1):
                    # Calculate the row where the piece will be placed
                    for row in range(self.rows - 1, -1, -1):
                        if self.board[row][col] == 0:
                            # Place a piece (1 for red) and update the board
                            self.board[row][col] = self.whos_turn
                            self.update()
                            self.add_score(self.whos_turn, row, col)
                            self.update_turn()
                            self.start = 0
                            break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = minesweeper()
    game.show()
    sys.exit(app.exec_())
