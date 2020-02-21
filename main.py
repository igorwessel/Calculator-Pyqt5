from PyQt5 import QtWidgets


class Calculator(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.resize(400, 500)
        self.centralWidget = self


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    app.exec()
