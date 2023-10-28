import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
import numpy as np

r_spacing = 10
c_spacing = 5
magic = 9
ico = 250
jokes = [
"Why do Minesweeper players make great detectives? Because they can spot a mine from a mile away!",
"I tried to impress my crush with my Minesweeper skills, but it turns out they were more into 'mines' than 'sweeping'!",
"ARE YOU ENJOYING CHAT GPT's JOKES?",
"Why did the Minesweeper player break up with their partner? Because they were tired of sweeping things under the rug!",
"What do you call a successful Minesweeper player? A real 'mine'field expert!",
"Minesweeper taught me one thing: Always check your surroundings for 'explosive' surprises!",
"My friend asked me to explain Minesweeper, so I just 'cleared the air' for them!",
"Why was the Minesweeper player always the life of the party? Because they knew how to 'defuse' any situation!",
"Minesweeper is like life: Sometimes you're just one wrong move away from disaster!",
"Minesweeper is a game of strategy, patience, and the occasional explosive surprise.",
"The key to winning Minesweeper is to approach it like life – one step at a time and always prepared for the unexpected!"
]

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

    def dig(self, x, y):             
        if self.grid[y][x] > 8:
            self.boom()
            self.banter.setText('Awww try again!')
            self.banter.setStyleSheet(
                f"""
                background-color: rgba(0, 0, 0, 0);
                color: {'pink'}; 
                """
                ) 
        else:
            self.board[y][x] = 1
            self.update()
            self.count += 1
            # print(self.count, int(self.w*(self.index/10)))
            if self.count == int(self.w*(self.index/10)):
                self.banter.setText(jokes[self.index])
                self.banter.setStyleSheet(
                f"""
                background-color: rgba(0, 0, 0, 0);
                color: {'pink'}; 
                """
                ) 
                self.index += 1
            if self.count == self.w:
                self.win()
        return 0
    
    def win(self):
        self.banter.setText('YOU WIN!')
        self.banter.setStyleSheet(
            f"""
            background-color: rgba(0, 0, 0, 0);
            color: {'pink'}; 
            """
        ) 
    def boom(self):
        self.board = [[1] * (self.columns) for _ in range(self.rows)]
        self.update()
        return 0
    
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
        self.cell_size = 30
        self.bombs = 100
        self.w = (self.rows*self.columns)-self.bombs
        self.count = 0
        self.grid = create_random_grid(self.rows, self.columns, self.bombs)
        self.index = 1

        self.icon = QLabel(self)
        self.cat = QPixmap('./cat.png')
        self.cat = self.cat.scaled(ico, ico)
        self.icon.setPixmap(self.cat)
        self.icon.move(800, 0)

        self.xbomb = QPixmap('./x.png')
        self.xbomb = self.xbomb.scaled(self.cell_size, self.cell_size)
        self.l_flag = 0
        # Initialize the game board
        self.board = [[0] * (self.columns) for _ in range(self.rows)]
        self.setWindowTitle("Minesweeper")
        self.setStyleSheet(
            """
            background: black;
            """
        )
        self.setMinimumSize(QSize(1400, 900))  
        self.reset = self.create_button("Reset the Game!", 100,100,550,100,'System',60,self.reset_game)
        self.banter = self.create_label("Don't Go BOOM!!", 180,200,1000,100,'System',20)
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
        size =  self.cell_size*0.7
        font = QFont('System', int(size))
        painter.setFont(font)

        for row in range(self.rows):
            for col in range(self.columns):
                
                painter.setBrush(QColor(255, 255, 255)) 
                cell_x = (col + c_spacing) * self.cell_size
                cell_y = (row + r_spacing) * self.cell_size
                painter.setPen(QColor(0, 0, 0)) 
                painter.drawRect(cell_x, cell_y, self.cell_size, self.cell_size)

                # painter.setBrush(cell_color)
                # painter.drawEllipse((col+c_spacing) * self.cell_size, (row + r_spacing) * self.cell_size, self.cell_size, self.cell_size)
                if self.board[row][col] == 1:
                    if self.grid[row][col] > 8:
                        painter.drawImage(cell_x, cell_y, self.xbomb.toImage())
                    else:
                        c = self.grid[row][col]
                        painter.setPen(QColor(255*(c%2), 75*(c%3), 50*(c%4)))
                        painter.drawText(cell_x, cell_y-(int)(self.cell_size*0.2)+self.cell_size, '  '+str(self.grid[row][col]))
                        painter.setPen(QColor(0,0,0))

    def reset_game(self):
        self.banter.setText('DONT GO BOOM!!')
        self.banter.setStyleSheet(
            f"""
            background-color: rgba(0, 0, 0, 0);
            color: {'white'}; 
            """
        ) 
        self.index = 1
        self.grid = create_random_grid(self.rows, self.columns, self.bombs)
        self.count = 0
        self.board = [[0] * (self.columns) for _ in range(self.rows)]
        self.update()
        return 0 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.pos().x()
            y = event.pos().y()
            # Check which circle was clicked
            s_x = (c_spacing) * self.cell_size
            s_y = self.cell_size*r_spacing
            if x > s_x and x < s_x + self.cell_size*self.columns and y > s_y and y < s_y+ self.cell_size*self.rows:
                xx = int((x-s_x)/self.cell_size)
                yy = int((y-s_y)/self.cell_size)
                self.dig(xx, yy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = minesweeper()
    game.show()
    sys.exit(app.exec_())