import sys
from PyQt5 import QtCore, QtWidgets


button_css = """
    background-color: #3C3C3C;
    color: #B98A5B;
    font-family: Magneto;
    font-size: 26px;
"""

buttons = {
    "9": (0, 80, 65, 65),
    "8": (65, 80, 65, 65),
    "7": (130, 80, 65, 65),
    "+": (195, 80, 65, 65),
    "6": (0, 145, 65, 65),
    "5": (65, 145, 65, 65),
    "4": (130, 145, 65, 65),
    "-": (195, 145, 65, 65),
    "3": (0, 210, 65, 65),
    "2": (65, 210, 65, 65),
    "1": (130, 210, 65, 65),
    "x": (195, 210, 65, 65),
    "0": (0, 275, 65, 65),
    "=": (65, 275, 65, 65),
    "C": (130, 275, 65, 65),
    "/": (195, 275, 65, 65),
}


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Set windows
        self.setFixedSize(QtCore.QSize(260, 340))
        self.setWindowTitle("Simple PyCalc")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        labelView = QtWidgets.QLabel(self, text="Python")
        labelView.setGeometry(QtCore.QRect(0, 0, 260, 80))
        labelView.setStyleSheet(
            """
            background-color:#C1C1C1;
            font-size: 32px;
            font-family: Magneto;
            font-weight: bold;
            """
        )
        for text, pos in buttons.items():
            buttons[text] = QtWidgets.QPushButton(text, self)
            buttons[text].setGeometry(QtCore.QRect(pos[0], pos[1], pos[2], pos[3]))
            buttons[text].setStyleSheet(button_css)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
