import sys
import cmath
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('ui/main_0.ui', self)

        self.total = 0

        self.enter_button.clicked.connect(self.calculate)
        self.next_button.clicked.connect(self.go_next)
        self.show()

    def calculate(self):
        # Calculate
        input_1 = 0
        input_2 = 0
        input_3 = 0
        input_4 = 0
        input_5 = 0
        input_6 = 0

        try:
            input_1 = float(self.input_1.text())
            input_2 = float(self.input_2.text())
            input_3 = float(self.input_3.text())
            input_4 = float(self.input_4.text())
            input_5 = float(self.input_5.text())
            input_6 = float(self.input_6.text())
            self.total = sum([input_1, input_2, input_3, input_4, input_5, input_6])

        except ValueError:
            print('Conversion error')

        print(f'{input_1 = }')
        print(f'{input_2 = }')
        print(f'{input_3 = }')
        print(f'{input_4 = }')
        print(f'{input_5 = }')
        print(f'{input_6 = }')
        print(f'{self.total = }')
        self.output_1.setText(str(self.total))
        ####

    def go_next(self):
        widget.addWidget(Calculations(self))
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Calculations(QtWidgets.QMainWindow):

    def __init__(self, main_window):
        # Main window constructor
        super(Calculations, self).__init__()

        print(f'{main_window.total = }')
        # print(f'{main_window.input_1.text() = }')
        # print(f'{main_window.input_2.text() = }')
        # print(f'{main_window.input_3.text() = }')
        # print(f'{main_window.input_4.text() = }')
        # print(f'{main_window.input_5.text() = }')
        # print(f'{main_window.input_6.text() = }')

        # Main UI here
        loadUi('ui/main_1.ui', self)

        self.input_1_label.setText('TLOS Exponent:')
        self.input_2_label.setText('Crash Area (Ac):')
        self.input_3_label.setText('Population Density (Dp):')
        self.input_4_label.setText('Sheltering Factor (Fs):')
        self.input_5_label.setText('P3:')

        self.output_1_label.setText('Total Failures:')
        self.output_2_label.setText('P1,ua:')
        self.output_3_label.setText('P2:')
        self.output_4_label.setText('P1,1:')
        self.output_5_label.setText('P1,2:')
        self.output_6_label.setText('P1,3:')
        self.output_7_label.setText('P1,4:')
        self.output_8_label.setText('P1,5:')
        self.output_9_label.setText('P1,6:')
        self.output_10_label.setText('P1,ua_new:')

        self.button_calculate.clicked.connect(self.calculate)

        self.show()



    def calculate(self):
        input_1 = 0
        input_2 = 0
        input_3 = 0
        input_4 = 0
        input_5 = 0
        output_1 = 1000.0   # hard code placeholder
        total = 0

        try:
            input_1 = float(self.input_1.text())
            input_2 = float(self.input_2.text())
            input_3 = float(self.input_3.text())
            input_4 = float(self.input_4.text())
            input_5 = float(self.input_5.text())
            total = sum([input_1, input_2, input_3, input_4, input_5])

        except ValueError:
            print('Conversion error')

        print(f'{input_1 = }')
        print(f'{input_2 = }')
        print(f'{input_3 = }')
        print(f'{input_4 = }')
        print(f'{input_5 = }')
        print(f'{total = }')

        '''
        
        '''

        self.output_10.setText(str(total))
        self.output_1.setText(str(output_1)) # hard code placeholder


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mw)
    widget.setFixedWidth(1000)
    widget.setFixedHeight(1000)
    widget.show()
    app.exec()
