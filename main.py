from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QWidget)


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.resize(400, 400)

        # LAYOUT
        self.main = QWidget(self)
        self.setCentralWidget(self.main)

        calcLayout = QGridLayout()
        display_calc = QLineEdit()
        calcLayout.addWidget(display_calc, 0, 0)

        btn_0 = QPushButton('0')
        btn_sum = QPushButton('+')
        btn_something = QPushButton('')
        btn_dot = QPushButton('.')
        btn_subtract = QPushButton('-')
        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_3 = QPushButton('3')
        btn_4 = QPushButton('4')
        btn_5 = QPushButton('5')
        btn_6 = QPushButton('6')
        btn_7 = QPushButton('7')
        btn_8 = QPushButton('8')
        btn_9 = QPushButton('9')

        calcLayout.addWidget(btn_7, 1, 0)
        calcLayout.addWidget(btn_8, 1, 1)
        calcLayout.addWidget(btn_9, 1, 2)
        calcLayout.addWidget(btn_4, 2, 0)
        calcLayout.addWidget(btn_5, 2, 1)
        calcLayout.addWidget(btn_6, 2, 2)
        calcLayout.addWidget(btn_1, 3, 0)
        calcLayout.addWidget(btn_2, 3, 1)
        calcLayout.addWidget(btn_3, 3, 2)
        calcLayout.addWidget(btn_0, 4, 1)
        calcLayout.addWidget(btn_something, 4, 0)
        calcLayout.addWidget(btn_dot, 4, 2)

        self.main.setLayout(calcLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    app.exec()
