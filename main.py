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

        # LAYOUT

        self.display_calc = QLineEdit()
        self.display_calc.setDisabled(True)
        self.calcLayout.addWidget(self.display_calc, 0, 0, 1, 5)
        self.display_calc.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.main.setLayout(self.calcLayout)

        def add_btn(self, btn, row, col, rowspan, colspan):
            pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    app.exec()
