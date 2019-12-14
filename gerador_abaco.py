


import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import pyqtgraph as pg

tabela_bitolas = [
	[6.3, 31.17],
	[8, 50.26],
	[10, 78.53],
	[12.5, 122.71],
	[16, 201.06],
	[20, 314.15],
	[25, 490.87],
	[32, 804.24],
	[40, 1256.63]
				]

class Detalhar_viga(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('scrollAreaTeste.ui',self)
		self.show()
	def load_signals(self):
		print('inicializado')
		self.pushButton.clicked.connect(self.calcular_area)
		
		#pg.plot(x=[0,1,2,3,4], y=[0,1,2,3,4]**2 )
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)


	def calcular_area(self):
		area_aco = float(self.lineEdit.text())
		x = []
		y = []
		cont = 0
		for i in tabela_bitolas:
			n_barras = float(area_aco/i[1])
			print('bitola: ',i[0],' - nº barras: ',n_barras)

			self.tableWidget.setItem(cont,2, QTableWidgetItem(str(round(n_barras, ndigits=2))))
			self.tableWidget.setItem(cont,3, QTableWidgetItem(str(round(n_barras +0.5)+1)))

			x.append(i[0])
			y.append(round(n_barras +0.5)+1)
			cont +=1

		print(x)
		print(y)
		
		self.widget.plot(x=x,y=y,pen=(3))


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	inicio = Detalhar_viga()
	app.exec_()
