from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()

window = QtWidgets.QWidget(windowTitle='FYP Shamus')

window.setWindowTitle('FYP Shamus window title')

print(window.windowTitle())

window.show()

app.exec()
