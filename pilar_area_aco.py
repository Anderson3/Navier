
import sys, os

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import pyqtgraph as pg

file = 'file:///C:/Users/Acer/Desktop/tessssst/sample.pdf'


global pilares_info_aco
pilares_info_aco = [1.4,0.5,1.0,0.1,20,0.4,1000]

class Pilar_area_aco(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('pilares_areas_aco.ui',self)
		self.setWindowTitle('Navier - Pilares - Áreas de Aço')

		self.pushButton_4.setIcon(QtGui.QIcon('btn_flexaosimples.png'))
		self.pushButton_4.setIconSize(QtCore.QSize(50,60))
		self.pushButton_5.setIcon(QtGui.QIcon('btn_flexaocomposta.png'))
		self.pushButton_5.setIconSize(QtCore.QSize(50,60))

		self.show()

	def load_signals(self):
		print('inicializado')
		self.pushButton_2.clicked.connect(self.calcular_area_aco)
		self.pushButton.clicked.connect(self.recuperar_dados)
		self.pushButton_3.clicked.connect(self.limpar)
		self.pushButton_4.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))
		self.pushButton_5.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))

	def recuperar_dados(self):
		self.lineEdit_2.setText(str(pilares_info_aco[0]))
		self.lineEdit_3.setText(str(pilares_info_aco[1]))
		self.lineEdit_5.setText(str(pilares_info_aco[2]))
		self.lineEdit_6.setText(str(pilares_info_aco[3]))
		self.lineEdit_12.setText(str(pilares_info_aco[4]))
		self.lineEdit_13.setText(str(pilares_info_aco[5]))
		self.lineEdit_14.setText(str(pilares_info_aco[6]))

	def calcular_area_aco(self):
		fck = float(self.lineEdit_12.text())
		fcd = fck/1.4
		fyd = 500/1.15
		area_concreto = float(self.lineEdit_13.text())
		nk = float(self.lineEdit_14.text())
		nd = 1.4 * nk

		mi_x = float(self.lineEdit_2.text())
		delta_x = float(self.lineEdit_3.text())

		mi_y = float(self.lineEdit_5.text())
		delta_y = float(self.lineEdit_6.text())

		omega_x = float(self.lineEdit_4.text())
		omega_y = float(self.lineEdit_7.text())

		as_x = (omega_x * (area_concreto*1000000) * fcd)/fyd
		as_y = (omega_y * (area_concreto*1000000) * fcd)/fyd

		as_x = round(as_x, ndigits=3)
		as_y = round(as_y, ndigits=3)

		as_pilar_min = 0.15 * (nd/fyd)
		if as_pilar_min < (0.004*area_concreto*100000):
			as_pilar_min = round((0.004*area_concreto*100000), ndigits=3)

		as_pilar_max = round((0.08*area_concreto*1000000), ndigits=3)

		#-------------------------------------- saída de dados ----------------------------------------------------
		self.lineEdit_8.setText(str(as_x))
		self.lineEdit_9.setText(str(as_y))
		self.lineEdit_10.setText(str(as_pilar_max))
		self.lineEdit_11.setText(str(as_pilar_min))

	def teste(self):
		print('teste')
	
	def limpar(self):
		self.lineEdit_2.setText('0')
		self.lineEdit_3.setText('0')
		self.lineEdit_4.setText('1')
		self.lineEdit_5.setText('0')
		self.lineEdit_6.setText('0')
		self.lineEdit_7.setText('1')
		self.lineEdit_8.setText('0')
		self.lineEdit_9.setText('0')
		self.lineEdit_10.setText('0')
		self.lineEdit_11.setText('0')
		self.lineEdit_12.setText('0')
		self.lineEdit_13.setText('0')
		self.lineEdit_14.setText('0')

	def abrirTabelaAuxiliar(self,file):
	    if sys.platform == 'linux2':
	        subprocess.call(["xdg-open", file])
	    else:
	        os.startfile(file)



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	inicio = Pilar_area_aco()
	app.exec_()
