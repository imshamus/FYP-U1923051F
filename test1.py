import sys
import cmath
import re
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, calculations_page):
        super(MainWindow, self).__init__()

        self.calculations_page = calculations_page

        loadUi('ui/main_0.ui', self)

        self.input_1_label.setText('Ground Control Systems (GCS):')
        self.input_2_label.setText('Mainframe (MF):')
        self.input_3_label.setText('Power Plant (PP):')
        self.input_4_label.setText('Navigation Systems (NS):')
        self.input_5_label.setText('Electronic Systems (ES):')
        self.input_6_label.setText('Payload (PL):')

        self.output_1_label.setText('Total Failures:')

        self.total = 0
        self.fail_dist = []

        self.enter_button.clicked.connect(self.calculate)
        self.next_button.clicked.connect(self.go_calculate_page)
        self.next_button.setEnabled(False)

        self.show()

    def calculate(self):
        # Calculate
        # input_1 = 0
        # input_2 = 0
        # input_3 = 0
        # input_4 = 0
        # input_5 = 0
        # input_6 = 0

        try:
            input_1 = float(self.input_1.text())
            input_2 = float(self.input_2.text())
            input_3 = float(self.input_3.text())
            input_4 = float(self.input_4.text())
            input_5 = float(self.input_5.text())
            input_6 = float(self.input_6.text())
            self.fail_dist = [
                input_1,
                input_2,
                input_3,
                input_4,
                input_5,
                input_6,
            ]
            self.total = sum([input_1, input_2, input_3, input_4, input_5, input_6])
            self.next_button.setEnabled(True)
            self.error_message.setText('')
            self.output_1.setText(str(self.total))
        except ValueError:
            self.next_button.setEnabled(False)
            self.error_message.setText('Error: Invalid input. Must be float.')
            self.output_1.setText('')
            print('Conversion error')
            return

        # print(f'{input_1 = }')
        # print(f'{input_2 = }')
        # print(f'{input_3 = }')
        # print(f'{input_4 = }')
        # print(f'{input_5 = }')
        # print(f'{input_6 = }')
        # print(f'{self.total = }')

        ####

    def go_calculate_page(self):
        self.calculations_page.total_failures = self.total
        self.calculations_page.fail_dist = self.fail_dist
        print(f'{self.calculations_page.total_failures = }')
        print(f'{self.calculations_page.fail_dist = }')
        # if widget.count() < 2:
        #     widget.addWidget(Calculations(total_failures=self.total, fail_dist=self.fail_dist))     # can comma
        go_next()


class Calculations(QtWidgets.QMainWindow):

    def __init__(self, total_failures=0, fail_dist=None):
        # Calculation constructor
        super(Calculations, self).__init__()

        if fail_dist is None:
            fail_dist = []

        # UI here
        self.total_failures = total_failures
        self.fail_dist = fail_dist
        self.p1 = 0

        loadUi('ui/main_1.ui', self)

        self.input_1_label.setText('TLOS Exponent:')
        self.input_2_label.setText('Crash Area (Ac):')
        self.input_3_label.setText('Population Density (Dp):')
        self.input_4_label.setText('Sheltering Factor (Fs):')
        self.input_5_label.setText('P3:')

        self.output_1_label.setText('Total Failures:')
        self.output_2_label.setText('P1, ua:')
        self.output_3_label.setText('P2:')

        self.output_4_label.setText('Ground Control Systems (GCS):')
        self.output_5_label.setText('Mainframe (MF):')
        self.output_6_label.setText('Power Plant (PP):')
        self.output_7_label.setText('Navigation Systems (NS):')
        self.output_8_label.setText('Electronic Systems (ES):')
        self.output_9_label.setText('Payload (PL):')
        self.output_10_label.setText('P1, ua_new:')

        # self.output_1.setText(str(self.total_failures))
        # self.lineedit_1.setText(str(self.total_failures))

        self.button_calculate.clicked.connect(self.calculate)
        self.previous_button.clicked.connect(go_previous)

        self.show()

    def calculate(self):
        input_1 = 0
        input_2 = 0
        input_3 = 0
        input_4 = 0
        input_5 = 0
        # total = 0

        try:
            input_1 = float(self.input_1.text())
            input_2 = float(self.input_2.text())
            input_3 = float(self.input_3.text())
            input_4 = float(self.input_4.text())
            input_5 = float(self.input_5.text())

        except ValueError:
            print('Conversion error')

        # print(f'{input_1 = }')
        # print(f'{input_2 = }')
        # print(f'{input_3 = }')
        # print(f'{input_4 = }')
        # print(f'{input_5 = }')
        # print(f'{total = }')

        output_3 = input_2 * input_3 * input_4
        output_2 = (10 ** (-1 * input_1)) / (output_3 * input_5)
        self.p1 = output_2
        # self.individual_fail_dist()
        indi_rel_1 = self.p1_1()
        indi_rel_2 = self.p1_2()
        indi_rel_3 = self.p1_3()
        indi_rel_4 = self.p1_4()
        indi_rel_5 = self.p1_5()
        indi_rel_6 = self.p1_6()

        total_rel = sum([
            indi_rel_1,
            indi_rel_2,
            indi_rel_3,
            indi_rel_4,
            indi_rel_5,
            indi_rel_6
        ])

        print(self.fail_dist)
        print(self.total_failures)
        print(self.p1)

        self.output_3.setText(str(output_3))
        print(shorten(str(output_2)))
        self.output_2.setText(shorten(str(output_2)))
        self.output_10.setText(shorten(str(total_rel)))

    # def individual_fail_dist(self):
    #     output_fields = [
    #         self.output_4,
    #         self.output_5,
    #         self.output_6,
    #         self.output_7,
    #         self.output_8,
    #         self.output_9,
    #     ]
    #     outputs = []
    #     for i, value in enumerate(self.fail_dist):
    #         print(f'{i = }, {value = }')
    #         x = (value / self.total_failures) * self.p1
    #         outputs.append(x)
    #         # output_fields[i].setText(x)
    #         print(f'{x = }')


    def p1_1(self):
        output_4 = (self.fail_dist[0] / self.total_failures) * self.p1
        self.output_4.setText(shorten(str(output_4)))
        return output_4

    def p1_2(self):
        output_5 = (self.fail_dist[1] / self.total_failures) * self.p1
        self.output_5.setText(shorten(str(output_5)))
        return output_5

    def p1_3(self):
        output_6 = (self.fail_dist[2] / self.total_failures) * self.p1
        self.output_6.setText(shorten(str(output_6)))
        return output_6

    def p1_4(self):
        output_7 = (self.fail_dist[3] / self.total_failures) * self.p1
        self.output_7.setText(shorten(str(output_7)))
        return output_7

    def p1_5(self):
        output_8 = (self.fail_dist[4] / self.total_failures) * self.p1
        self.output_8.setText(shorten(str(output_8)))
        return output_8

    def p1_6(self):
        output_9 = (self.fail_dist[5] / self.total_failures) * self.p1
        self.output_9.setText(shorten(str(output_9)))
        return output_9


# Static functions
def go_next():
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_previous():
    widget.setCurrentIndex(widget.currentIndex() - 1)

# REFRESH CALCULATE PAGE

def shorten(num_str):
    print(f'{num_str = }')
    result = re.search(r'\.', num_str)
    print(f'{result = }')
    if len(num_str) > 8 and result is not None:
        x = re.split('e', num_str)
        print(f'{x = }')
        shortened = f'{num_str[:4]}e{x[1]}'
        print(f'{shortened = }')
        return shortened
    else:
        return num_str


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    calculations = Calculations()
    mw = MainWindow(calculations)
    widget.addWidget(mw)
    widget.addWidget(calculations)
    widget.setFixedWidth(1000)
    widget.setFixedHeight(1000)
    widget.show()
    app.exec()
