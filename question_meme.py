import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
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

        self.setMinimumSize(QSize(1500, 900))    
        self.setWindowTitle("Playing Around") 

        self.label = self.create_label(">> >>> >>>> >>>", 300,200,900,200,'System',90)
        self.pybutton = self.create_button('Yes', 300,500,200,100,'System',90,self.clickMethod)
        self.pys = 200
        self.pys2 = 100
        self.pybutton2 = self.create_button('No', 900,500,200,100,'System',90,self.clickMethod2)

    def clickMethod(self):
        self.label.setText("OK NICE")
        self.pybutton.resize(0,0)
        self.pybutton2.resize(0,0)
        
    def clickMethod2(self):
        if self.pys + 400 > 900:
            self.pybutton2.resize(0,0)
        self.pybutton2.move(random.randrange(0,1250),random.randrange(0,600))
        self.label.setText("WRONG ANSWER")
        self.pybutton2.setText("sorry")
        self.pybutton2.setFont(QFont('System', 32))
        self.pys += 20
        self.pys2 += 20
        self.pybutton.resize(self.pys,self.pys2)
        self.pybutton.move(300, 400)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )