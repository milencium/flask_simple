import enum
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout
import requests


class FlaskyFrontEnd(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 800
        self.top = 400
        self.width = 400
        self.height = 140
        self.initUI()
        self.json = None
        self.channels = []
        self.channelsL = 0
        self.data_table = None
        self.data_tableL = 0

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QtWidgets.QPushButton('Load data', self)
        self.button.move(150, 35)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        url = "http://localhost:5000/data"
        r = requests.get(url)
        self.json = r.json()
        self.channels = self.json[0]
        self.channelsL = len(self.channels)
        self.data_table = self.json[1]
        self.data_tableL = len(self.data_table)
        self.headers = []
        print(self.data_tableL)
        print(self.channelsL)
        QtWidgets.QMessageBox.question(
            self,
            "Message",
            "THIS IS LOADED CHANNELS DATA: {}".format(str(self.channels)),
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )
        self.createTable()

    def createTable(self):
        self.vbox = QVBoxLayout()
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(len(self.data_table[0]))
        self.tableWidget.setRowCount(len(self.channels))
        for i, row in enumerate(self.data_table):
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        for i, channel in enumerate(self.channels):
            self.headers.append(channel)
        self.tableWidget.setVerticalHeaderLabels(self.headers)
        self.vbox.addWidget(self.tableWidget)
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = FlaskyFrontEnd()
    sys.exit(app.exec_())
