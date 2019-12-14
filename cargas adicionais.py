


import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


class Carga_Adicional(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = loadUi('lajes_carg_adicional_atualizada.ui',self)
		#self.tableWidget.setRowCount(linhas)
		#self.tableWidget.setColumnCount(colunas)
		#table = self.tableWidget()
		#header = self.tableWidget.horizontalHeader()
		#header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
		#header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

		self.tableWidget.resizeRowsToContents()

		self.setWindowTitle('Navier - Cargas Adicionais')
		self.show()
		



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	aplicacao = Carga_Adicional()
	app.exec_()
