from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QWidget, QSizePolicy)


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(400, 400)
        self.main = QWidget()
        self.calcLayout = QGridLayout(self.main)
        self.setCentralWidget(self.main)

        # layout

        self.display_calc = QLineEdit()
        self.display_calc.setDisabled(True)
        self.calcLayout.addWidget(self.display_calc, 0, 0, 1, 5)
        self.display_calc.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.main.setLayout(self.calcLayout)

        # numbers buttons
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)

        # operations mathematics
        self.add_btn(QPushButton('x'), 1, 3, 1, 1)
        self.add_btn(QPushButton('+'), 2, 3, 1, 1)
        self.add_btn(QPushButton('-'), 3, 3, 1, 1)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.calcLayout.addWidget(btn, row, col, rowspan, colspan)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    app.exec()
