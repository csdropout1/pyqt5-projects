import sys
import random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPainter, QColor

class Snake(QFrame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.timer = QBasicTimer()
        self.snake = [(5, 5), (5, 4), (5, 3)]
        self.direction = 'Right'
        self.apple = self.createApple()

        self.timer.start(100, self)
        self.buffer = []
        self.setWindowTitle('Snake')
        self.show()

    def createApple(self):
        apple = (random.randint(0, self.width() // 20 - 1), random.randint(0, self.height() // 20 - 1))
        while apple in self.snake:
            apple = (random.randint(0, self.width() // 20 - 1), random.randint(0, self.height() // 20 - 1))
        return apple

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(0, 0, 0))
        painter.drawRect(0, 0, self.width(), self.height())

        painter.setBrush(QColor(255, 255, 255))
        for part in self.snake:
            painter.drawRect(part[0] * 20, part[1] * 20, 20, 20)

        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(self.apple[0] * 20, self.apple[1] * 20, 20, 20)

    def timerEvent(self, event):
        self.makeBuffer()
        self.moveSnake()
        self.checkCollision()

        self.update()

    def makeBuffer(self):
        if len(self.buffer) > 0:
            self.direction = self.buffer.pop(0)

    def moveSnake(self):
        head = list(self.snake[0])

        if self.direction == 'Right':
            head[0] += 1
        elif self.direction == 'Left':
            head[0] -= 1
        elif self.direction == 'Up':
            head[1] -= 1
        elif self.direction == 'Down':
            head[1] += 1

        self.snake.insert(0, tuple(head))

        if self.snake[0] == self.apple:
            self.apple = self.createApple()
        else:
            self.snake.pop()

    def checkCollision(self):
        head = self.snake[0]

        if head[0] < 0 or head[0] >= self.width() // 20 or head[1] < 0 or head[1] >= self.height() // 20:
            self.timer.stop()
        elif len(self.snake) != len(set(self.snake)):
            self.timer.stop()

class SnakeGame(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.insta = Snake()
        self.setCentralWidget(self.insta)
        self.lastpress = ''
        self.resize(800, 800)
        self.center()
        self.setWindowTitle('Snake Game')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def keyPressEvent(self, event):
        
        key = event.key()

        if key == Qt.Key_Left and self.insta.direction != 'Right' and self.lastpress != 'Left':
            # self.insta.direction = 'Left'      
            self.insta.buffer.append('Left')
            self.lastpress = 'Left'
        elif key == Qt.Key_Right and self.insta.direction != 'Left' and self.lastpress != 'Right':
            # self.insta.direction = 'Right'
            self.insta.buffer.append('Right')
            self.lastpress = 'Right'
        elif key == Qt.Key_Up and self.insta.direction != 'Down' and self.lastpress != 'Up':
            # self.insta.direction = 'Up'
            self.insta.buffer.append('Up')
            self.lastpress = 'Up'
        elif key == Qt.Key_Down and self.insta.direction != 'Up' and self.lastpress != 'Down':
            # self.insta.direction = 'Down'
            self.insta.buffer.append('Down')
            self.lastpress = 'Down'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SnakeGame()
    sys.exit(app.exec_())
