from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QWidget, QSizePolicy)


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(320, 400)
        self.main = QWidget()
        self.calcLayout = QGridLayout(self.main)
        self.setCentralWidget(self.main)

        self._old_number = ''
        self._current_number = ''
        self._operator = ''
        self._result_number = 0

        # layout

        self.display_calc = QLineEdit()
        self.display_calc.setDisabled(True)
        self.calcLayout.addWidget(self.display_calc, 0, 0, 1, 5)
        self.display_calc.setFixedHeight(120)
        self.display_calc.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.main.setLayout(self.calcLayout)

        # numbers buttons

        # first row
        self.add_btn(QPushButton('AC'), 1, 0, 1, 3,)

        # second row
        self.add_btn(QPushButton('7'), 2, 0, 1, 1)
        self.add_btn(QPushButton('8'), 2, 1, 1, 1)
        self.add_btn(QPushButton('9'), 2, 2, 1, 1)

        # third row
        self.add_btn(QPushButton('4'), 3, 0, 1, 1)
        self.add_btn(QPushButton('5'), 3, 1, 1, 1)
        self.add_btn(QPushButton('6'), 3, 2, 1, 1)

        # four row
        self.add_btn(QPushButton('1'), 4, 0, 1, 1)
        self.add_btn(QPushButton('2'), 4, 1, 1, 1)
        self.add_btn(QPushButton('3'), 4, 2, 1, 1)

        # five row
        self.add_btn(QPushButton('0'), 5, 0, 1, 1)
        self.add_btn(QPushButton('.'), 5, 1, 1, 1)
        self.add_btn(QPushButton('C'), 5, 2, 1, 1)

        # operations mathematics
        self.add_btn(QPushButton('÷'), 1, 3, 1, 2)
        self.add_btn(QPushButton('x'), 2, 3, 1, 2)
        self.add_btn(QPushButton('-'), 3, 3, 1, 2)
        self.add_btn(QPushButton('+'), 4, 3, 1, 2)
        self.add_btn(QPushButton('='), 5, 3, 1, 2,)

    def operate(self, button_txt):
        """
        This function have responsibility for effectuate all the logic of calculator.
        :param button_txt: receive button_txt.
        :return: don't return anything.
        """
        if button_txt.isdigit():  # checking if button is a number.
            if len(str(self._current_number)) <= 8:
                self._current_number += button_txt
        else:  # otherwise is a operator
            if button_txt in ('÷', 'x', '-', '+'):
                # have a responsibility insert in old number the current number and salve the operator.
                self._operator = button_txt
                self._old_number = self._current_number
                self._current_number = ''
            elif button_txt == '.':
                self._current_number += button_txt
            elif button_txt == 'AC':  # reset operation.
                self._current_number, self._old_number, self._operator, self._result_number = '', '', '', ''
            elif button_txt == 'C':  # reset the current number
                self._current_number = ''
            else:
                # in this stage operator is '=', have a responsibility to perform a operate in old number and
                # current number using o operator salved.
                if isinstance(float(self._old_number), float):
                    if self._operator == '÷':
                        self._result_number = float(self._old_number) / float(self._current_number)
                    if self._operator == 'x':
                        self._result_number = float(self._old_number) * float(self._current_number)
                    if self._operator == '-':
                        self._result_number = float(self._old_number) - float(self._current_number)
                    if self._operator == '+':
                        self._result_number = float(self._old_number) + float(self._current_number)
                else:
                    if self._operator == '÷':
                        self._result_number = round(int(self._old_number) / int(self._current_number), 2)
                    if self._operator == 'x':
                        self._result_number = int(self._old_number) * int(self._current_number)
                    if self._operator == '-':
                        self._result_number = int(self._old_number) - int(self._current_number)
                    if self._operator == '+':
                        self._result_number = int(self._old_number) + int(self._current_number)
                self._current_number = str(self._result_number)

    def insert_in_display(self, button_txt):
        """
        This function have a responsability for insert the values in display.
        :param button_txt: receive the button_text
        :return: don't return anything.
        """

        self.operate(button_txt)  # This function have a responsibility for effectuate all logic of calculator.
        if button_txt.isdigit():  # If button is a number insert in display.
            if len(str(self._current_number)) <= 8:
                self.display_calc.setText(str(self._current_number))
        else:  # If button not is a number is a operator
            if button_txt == '=':
                if len(str(self._result_number)) >= 8:
                    self.display_calc.setText('ERR')
                else:
                    self.display_calc.setText(str(self._result_number))
            elif button_txt == 'C':
                self.display_calc.setText('')
            elif button_txt == 'AC':
                self.display_calc.setText('0')
            elif button_txt == '.':
                self.display_calc.setText(str(self._current_number))

    def add_btn(self, btn, row, col, rowspan=0, colspan=0, function=None, style=None):
        """
        Insert button in grid layout.
        :param btn: text in button.
        :param row: row in grid layout.
        :param col: column in grid layout.
        :param rowspan: default value is 0.
        :param colspan: default value is 0
        :param function: in case want add custom function for button.
        :param style: in case want add custom style for button.
        :return: don't return anything.
        """

        self.calcLayout.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect(
                lambda: self.insert_in_display(btn.text())
            )
        else:
            btn.clicked.connect(function)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    app.exec()
