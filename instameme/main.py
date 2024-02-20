import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtCore import QSize, Qt

# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    # Variable Controls

    '''
    Change the following parameters to create your own unique meme question.
    '''

    #### Pre - Built && 
    question = "Will You be my Valentine?" # by default
    title = "Playing Around"
    positive_feedback = "Now what...?" # response if user picks button 1, default = yes
    negative_feedback = ["WRONG ANSWER", "Please?", "Why so mean...?"] # response if user picks button 2, default = no
    button_1 = "Yes"
    button_2 = "No"
    button_2_alter = "No (DONT)" #what button 2 will change to after user declines

    def create_label(self, name, movex, movey, rex, rey, fonttype, fontsize):
        l = QLabel(name, self)
        l.move(movex, movey)
        l.resize(rex, rey)
        l.setFont(QFont(fonttype, fontsize))
        return l
    def create_button(self, name, movex, movey, rex, rey, fonttype, fontsize, func):
        b = QPushButton(name, self)
        b.move(movex, movey)
        b.resize(rex, rey)
        b.setFont(QFont(fonttype, fontsize))
        b.clicked.connect(func)
        return b
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet(
            """
            background: black;
            """
        )

        self.setMinimumSize(QSize(1500, 900))    
        self.setWindowTitle(self.title) 

        self.label = self.create_label(self.question, 300,200,900,200,'System',75)
        self.label.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0);
            color: white; 
            """
        )
        self.pybutton = self.create_button(self.button_1, 300,500,200,100,'System',75,self.clickMethod)
        self.pybutton.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0);
            color: white; 
            """
        )
        self.pys = 200
        self.pys2 = 100
        self.pybutton2 = self.create_button(self.button_2, 900,500,200,100,'System',75,self.clickMethod2)
        self.pybutton2.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0);
            color: white; 
            """
        )
        
        self.initUI()

    def initUI(self):
       
        # Create a QLabel widget
        self.gif = QLabel(self)
        self.gif.setAlignment(Qt.AlignCenter)
        self.set_gif('heart.gif')  # Set the path to your GIF file
        self.gif.resize(0,0)

    def set_gif(self, path):
        # Create a QMovie object with the GIF file
        movie = QMovie(path)

        # Set the movie on the QLabel widget
        self.gif.setMovie(movie)

        # Start the movie
        movie.start()

    def clickMethod(self):
        self.label.setText(self.positive_feedback)
        self.pybutton.resize(0,0)
        self.pybutton2.resize(0,0)

        self.gif.resize(200,200)
        self.gif.move(400,400)


    def clickMethod2(self):
        if self.pys + 400 > 900:
            self.pybutton2.resize(0,0)
        self.pybutton2.move(random.randrange(0,1250),random.randrange(0,600))
        r = random.randint(0,len(self.negative_feedback)-1)
        self.label.setText(self.negative_feedback[r])
        self.pybutton2.setText(self.button_2_alter)
        self.pybutton2.setFont(QFont('System', 32))
        self.pys += 20
        self.pys2 += 20
        self.pybutton.resize(self.pys,self.pys2)
        self.pybutton.move(300, 400)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
