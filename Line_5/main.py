import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize

w = 5
class Line5(QWidget):
    whos_turn = 1
    temp_string = ''
    temp_color = ''
    start = 1
    player1 = {
         1: 0,  2: 0,  3: 0,  4: 0,  5: 0,
         6: 0,  7: 0,  8: 0,  9: 0, 10: 0,
        11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
        16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
        21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
    }
    player2 = {
         1: 0,  2: 0,  3: 0,  4: 0,  5: 0,
         6: 0,  7: 0,  8: 0,  9: 0, 10: 0,
        11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
        16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
        21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
    }
    main_c = {
        'row1': 1, 'row2': 2, 'row3': 3, 'row4': 4, 'row5': 5, 'row6': 6,
        'col1': 7, 'col2': 8, 'col3': 9, 'col4': 10, 'col5': 11, 'col6': 12, 'col7': 13,
        'lef1': 14, 'lef2': 15, 'lef3': 16, 'lef4': 17, 'lef5': 18, 'lef6': 19,
        'rig1': 20, 'rig1': 21, 'rig1': 22, 'rig1': 23, 'rig1': 24, 'rig1': 25,
    }


    def add_score(self, p, x, y):
        if p == 1:
            self.player1[x+1] += 1
            if self.player1[x+1] == w:
                self.winner(1)
            self.player1[6+y] += 1
            if self.player1[6+y] == w:
                self.winner(1)
            
            if (x, y) in [(3, 1),(2,2),(1,3), (4,0)]:
                self.player1[14] += 1
                if self.player1[14] == w:
                    self.winner(1)
            if (x, y) in [(4,1),(3,2),(2,3),(1,4),(0,5)]:
                self.player1[15] += 1
                if self.player1[15] == w:
                    self.winner(1)
            if (x, y) in [(5,1),(4,2),(3,3),(2,4),(1,5),(0,6)]:
                self.player1[16] += 1
                if self.player1[16] == w:
                    self.winner(1)
            if (x, y) in [(5,2),(4,3),(3,4),(2,5),(1,6),(0,7)]:
                self.player1[17] += 1
                if self.player1[17] == w:
                    self.winner(1)
            if (x, y) in [(5,3),(4,4),(3,5),(2,6),(1,7)]:
                self.player1[18] += 1
                if self.player1[18] == w:
                    self.winner(1)
            if (x, y) in [(5, 4),(4,5),(3,6), (2,7)]:
                self.player1[19] += 1
                if self.player1[19] == w:
                    self.winner(1)
            
            if (x, y) in [(3, 7),(2,6),(1,5), (0,4)]:
                self.player1[20] += 1
                if self.player1[20] == w:
                    self.winner(1)
            if (x, y) in [(4,7),(3,6),(2,5),(1,4),(0,3)]:
                self.player1[21] += 1
                if self.player1[21] == w:
                    self.winner(1)
            if (x, y) in [(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)]:
                self.player1[22] += 1
                if self.player1[22] == w:
                    self.winner(1)
            if (x, y) in [(5,6),(4,5),(3,4),(2,3),(1,2),(0,1)]:
                self.player1[23] += 1
                if self.player1[23] == w:
                    self.winner(1)
            if (x, y) in [(5,5),(4,4),(3,3),(2,2),(1,1)]:
                self.player1[24] += 1
                if self.player1[24] == w:
                    self.winner(1)
            if (x, y) in [(5, 4),(4,3),(3,2), (2,1)]:
                self.player1[25] += 1
                if self.player1[25] == w:
                    self.winner(1)
        else:
            self.player2[x+1] += 1
            if self.player2[x+1] == w:
                self.winner(2)
            self.player2[6+y] += 1
            if self.player2[6+y] == w:
                self.winner(2)
            
            if (x, y) in [(3, 1),(2,2),(1,3), (4,0)]:
                self.player2[14] += 1
                if self.player2[14] == w:
                    self.winner(2)
            if (x, y) in [(4,1),(3,2),(2,3),(1,4),(0,5)]:
                self.player2[15] += 1
                if self.player2[15] == w:
                    self.winner(2)
            if (x, y) in [(5,1),(4,2),(3,3),(2,4),(1,5),(0,6)]:
                self.player2[16] += 1
                if self.player2[16] == w:
                    self.winner(2)
            if (x, y) in [(5,2),(4,3),(3,4),(2,5),(1,6),(0,7)]:
                self.player2[17] += 1
                if self.player2[17] == w:
                    self.winner(2)
            if (x, y) in [(5,3),(4,4),(3,5),(2,6),(1,7)]:
                self.player2[18] += 1
                if self.player2[18] == w:
                    self.winner(2)
            if (x, y) in [(5, 4),(4,5),(3,6), (2,7)]:
                self.player2[19] += 1
                if self.player2[19] == w:
                    self.winner(2)
            
            if (x, y) in [(3, 7),(2,6),(1,5), (0,4)]:
                self.player2[20] += 1
                if self.player2[20] == w:
                    self.winner(2)
            if (x, y) in [(4,7),(3,6),(2,5),(1,4),(0,3)]:
                self.player2[21] += 1
                if self.player2[21] == w:
                    self.winner(2)
            if (x, y) in [(5,7),(4,6),(3,5),(2,4),(1,3),(0,2)]:
                self.player2[22] += 1
                if self.player2[22] == w:
                    self.winner(2)
            if (x, y) in [(5,6),(4,5),(3,4),(2,3),(1,2),(0,1)]:
                self.player2[23] += 1
                if self.player2[23] == w:
                    self.winner(2)
            if (x, y) in [(5,5),(4,4),(3,3),(2,2),(1,1)]:
                self.player2[24] += 1
                if self.player2[24] == w:
                    self.winner(2)
            if (x, y) in [(5, 4),(4,3),(3,2), (2,1)]:
                self.player2[25] += 1
                if self.player2[25] == w:
                    self.winner(2)

    def winner(self, n):
        if n == 1:
            self.temp_color = 'red'
            self.temp_string = 'Congratz Player 1'
            self.change_label()

        else:
            self.temp_color = 'blue'
            self.temp_string = 'Congratz Player 2'
            self.change_label()

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
    
    def update_turn(self):
        if self.whos_turn == 1:
            self.whos_turn = 2
        else:
            self.whos_turn = 1

    def __init__(self):
        super().__init__()
        # Define the board size
        self.rows = 6
        self.columns = 7
        self.cell_size = 100

        # Initialize the game board
        self.board = [[0] * (self.columns+1) for _ in range(self.rows)]
        self.setWindowTitle("Line 5")
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
        # Reset the game board
        self.board = [[0] * (self.columns+1) for _ in range(self.rows)]
        self.player1 = {
            1: 0,  2: 0,  3: 0,  4: 0,  5: 0,
            6: 0,  7: 0,  8: 0,  9: 0, 10: 0,
            11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
            16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
            21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
        }
        self.player2 = {
            1: 0,  2: 0,  3: 0,  4: 0,  5: 0,
            6: 0,  7: 0,  8: 0,  9: 0, 10: 0,
            11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
            16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
            21: 0, 22: 0, 23: 0, 24: 0, 25: 0,
        }
        self.whos_turn = 1
        self.update()
        self.start = 1
        self.temp_string = "Make a Line of 5!"
        self.temp_color = 'pink'
        self.change_label()


    def mousePressEvent(self, event):
        if self.start == 1:
            self.temp_color = 'rgba(0, 0, 0, 0)'
            self.change_label()

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

    def change_label(self):
        self.banter.setText(self.temp_string)
        self.banter.setStyleSheet(
            f"""
            background-color: rgba(0, 0, 0, 0);
            color: {self.temp_color}; 
            """
        ) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Line5()
    game.show()
    sys.exit(app.exec_())
