import csv
import sys

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from morse.models.morse_experiment import scan
from morse.ui_mainwindow import Ui_MainWindow

testtext = "se"


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.text_message.setPlaceholderText("Write your message here")
        self.ui.send_button.clicked.connect(self.send_signal)

    def send_signal(self):
        input = self.ui.text_message.toPlainText()
        print(input)
        scan(text=input)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
