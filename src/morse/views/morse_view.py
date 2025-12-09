import csv
import sys
import time

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

from morse.models.morse_experiment import list_resources, scan
from morse.ui_mainwindow import Ui_MainWindow


class InvalidPortError(Exception):
    pass

class InvalidMessageError(Exception):
    pass

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.portlist = list_resources()
        self.ui.portBox.addItems(self.portlist)

        self.ui.text_message.setPlaceholderText("Write your message here")
        self.ui.send_button.clicked.connect(self.send_signal)

    @Slot()
    def send_signal(self):
        input = self.ui.text_message.toPlainText()
        portindex = self.ui.portBox.currentIndex()
        usb = self.portlist[portindex]
        print(input)

        if len(list(input)) == 0:
            raise InvalidMessageError("You must enter at least one character to continue")
        if portindex < 0:
            raise InvalidPortError("You must choose a port to continue")
        scan(text=input, port=usb)
        time.sleep(3)
        self.ui.text_message.clear() 


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
