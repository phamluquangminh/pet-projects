from PyQt5 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.show()
        self.keypad()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        #! Button
        result_field = qtw.QColumnView()
        btn_result = qtw.QPushButton('=')
        btn_clear = qtw.QPushButton('C')
        btn_9 = qtw.QPushButton('9')
        btn_8 = qtw.QPushButton('8')
        btn_7 = qtw.QPushButton('7')
        btn_6 = qtw.QPushButton('6')
        btn_5 = qtw.QPushButton('5')
        btn_4 = qtw.QPushButton('4')
        btn_3 = qtw.QPushButton('3')
        btn_2 = qtw.QPushButton('2')
        btn_1 = qtw.QPushButton('1')
        btn_0 = qtw.QPushButton('0')
        btn_percent = qtw.QPushButton('%')
        btn_dot = qtw.QPushButton('.')
        btn_plus = qtw.QPushButton('+')
        btn_mins = qtw.QPushButton('-')
        btn_mult = qtw.QPushButton('*')
        btn_divd = qtw.QPushButton('÷')
        btn_1divd = qtw.QPushButton('1/x')
        btn_square = qtw.QPushButton('^2')

        #! Adding the buttons to the layout
        # * container.layout().addWidget(widget, row, column, rowSpan, columnSpan)
        container.layout().addWidget(result_field, 0, 0, 2, 4)
        container.layout().addWidget(btn_square, 3, 0, 1, 1)
        container.layout().addWidget(btn_percent, 3, 1, 1, 1)
        container.layout().addWidget(btn_1divd, 3, 2, 1, 1)
        container.layout().addWidget(btn_clear, 3, 3, 1, 1)
        container.layout().addWidget(btn_7, 4, 0, 1, 1)
        container.layout().addWidget(btn_8, 4, 1, 1, 1)
        container.layout().addWidget(btn_9, 4, 2, 1, 1)
        container.layout().addWidget(btn_plus, 4, 3, 1, 1)
        container.layout().addWidget(btn_4, 5, 0, 1, 1)
        container.layout().addWidget(btn_5, 5, 1, 1, 1)
        container.layout().addWidget(btn_6, 5, 2, 1, 1)
        container.layout().addWidget(btn_mins, 5, 3, 1, 1)
        container.layout().addWidget(btn_1, 6, 0, 1, 1)
        container.layout().addWidget(btn_2, 6, 1, 1, 1)
        container.layout().addWidget(btn_3, 6, 2, 1, 1)
        container.layout().addWidget(btn_mult, 6, 3, 1, 1)
        container.layout().addWidget(btn_dot, 7, 0, 1, 1)
        container.layout().addWidget(btn_0, 7, 1, 1, 1)
        container.layout().addWidget(btn_result, 7, 2, 1, 1)
        container.layout().addWidget(btn_divd, 7, 3, 1, 1)

        self.layout().addWidget(container)


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
