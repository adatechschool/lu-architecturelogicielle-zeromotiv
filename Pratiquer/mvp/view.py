from __future__ import (absolute_import,division,print_function)
from PyQt5 import QtWidgets, QtCore, QtGui


class View(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(View, self).__init__(parent)

         grid = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(4)
        self.table.setColumnCount(2)
        grid.addWidget(self.table)

        self.colours = QtWidgets.QComboBox()
        options = ["Blue", "Green", "Red"]
        self.colours.addItems(options)

        self.grid_lines = QtWidgets.QTableWidgetItem()
        self.grid_lines.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.grid_lines.setCheckState(QtCore.Qt.Unchecked)
        self.addItemToTable("Show grid lines", self.grid_lines, 1)

        self.freq = QtWidgets.QTableWidgetItem("1.0")
        self.phi = QtWidgets.QTableWidgetItem("0.0")

        self.addWidgetToTable("Colour", self.colours, 0)
        self.addItemToTable("Frequency", self.freq, 2)
        self.addItemToTable("Phase", self.phi, 3)

        self.plot = QtWidgets.QPushButton('Add', self)
        self.plot.setStyleSheet("background-color:lightgrey")

        grid.addWidget(self.plot)

        self.setLayout(grid)

 def setTableRow(self, name, row):
        text = QtWidgets.QTableWidgetItem(name)
        text.setFlags(QtCore.Qt.ItemIsEnabled)
        col = 0
        self.table.setItem(row, col, text)

 def addWidgetToTable(self, name, widget, row):
        self.setTableRow(name,row)
        col = 1
        self.table.setCellWidget(row, col, widget)

 def addItemToTable(self, name, widget, row):
        self.setTableRow(name, row)
        col = 1
        self.table.setItem(row, col, widget)




    def btn_click(self):
        print("Hello world")
