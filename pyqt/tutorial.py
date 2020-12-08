import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import center
from PyQt5.QtWidgets import QApplication, QMainWindow

X_POSITION = 300
Y_POSITION = 300
WIDTH = 500
HEIGHT = 500


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(X_POSITION, Y_POSITION, WIDTH, HEIGHT)
        self.setWindowTitle("Test window")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel("This is label", self)
        self.label.move(100, 100)
        self.button = QtWidgets.QPushButton("Click me!", self)
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Clicked")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
