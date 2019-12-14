


import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


class Tabela_Classe_Agressividade(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('class_agres.ui',self)
		self.setWindowTitle('Navier - Classes de Agressividade e Cobrimentos Mínimos')
		self.show()
	def load_signals(self):
		print('inicializado')
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		

		self.tableWidget.setSpan(0, 0, 1, 4)
		#self.tableWidget.horizontalHeader().setVisible(False) //QtWidgets.QHeaderView.ResizeToContents

		header_2 = self.tableWidget_2.horizontalHeader()
		header_2.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header_2.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header_2.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header_2.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

		self.tableWidget_2.setSpan(0, 0, 2, 1)
		self.tableWidget_2.setSpan(0, 1, 2, 1)
		self.tableWidget_2.setSpan(0, 3, 2, 1)

		self.tableWidget_2.setSpan(3, 0, 2, 1)
		self.tableWidget_2.setSpan(3, 1, 2, 1)
		self.tableWidget_2.setSpan(3, 3, 2, 1)

		self.tableWidget_2.setSpan(5, 0, 2, 1)
		self.tableWidget_2.setSpan(5, 1, 2, 1)
		self.tableWidget_2.setSpan(5, 3, 2, 1)



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	aplicacao = Tabela_Classe_Agressividade()
	app.exec_()
