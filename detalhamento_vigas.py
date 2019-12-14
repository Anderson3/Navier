


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
info_viga = ['95','12','45','40','1.9']

class Detalhar_viga(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('detalhamento_vigas_alt.ui',self)
		self.setWindowTitle('Navier - Vigas - Detalhamento')
		self.show()
	def load_signals(self):
		print('inicializado')
		self.pushButton.clicked.connect(self.calcular_area)
		#self.pushButton.clicked.connect(self.calcular_estribos)
		self.pushButton_2.clicked.connect(self.limpar_detalhamento)
		self.pushButton_3.clicked.connect(self.recuperarValores)


		#pg.plot(x=[0,1,2,3,4], y=[0,1,2,3,4]**2 )
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

		self.widget.setTitle('nº barras/Bitola')
		self.widget.showGrid(x=True,y=True,alpha=1)

		#if '0' not in info_viga:
		#	self.recuperarValores()

	def calcular_estribos(self):
		vsw = self.lineEdit_14.text()
		fyk_estribo = self.comboBox_2.currentText()
		tramos = self.lineEdit_15.text()

		if (vsw != '0' and tramos != '0'):
			vsw = float(self.lineEdit_14.text())
			bitola_estribo = float(self.comboBox.currentText())
			fyk_estribo = float(self.comboBox_2.currentText())
			tramos = float(self.lineEdit_15.text())
			d = float(self.lineEdit_13.text())

			area_bitola = (3.14*((bitola_estribo/1000)**2)/4)

			print(vsw)
			print(bitola_estribo)
			print(tramos)
			print(fyk_estribo)
			print(area_bitola)


			s_estribo = ((tramos * area_bitola * 0.9 * (d/100) * (fyk_estribo*100000/1.15))/vsw*1000)/100
			s_estribo = round(s_estribo, ndigits=3)

			self.lineEdit.setText(str(s_estribo))
		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes para o cálculo dos Estribos!")


	def recuperarValores(self):
		area_aco = info_viga[0]
		base = info_viga[1]
		altura = info_viga[2]
		d = info_viga[3]
		d_agreg = info_viga[4]

		self.lineEdit_11.setText(area_aco)
		self.lineEdit_10.setText(base)
		self.lineEdit_9.setText(altura)
		self.lineEdit_12.setText(d_agreg)
		self.lineEdit_13.setText(d)

	def calcular_area(self):
		area_aco = self.lineEdit_11.text()
		base = self.lineEdit_10.text()
		altura = self.lineEdit_9.text()
		d_agreg = self.lineEdit_12.text()
		d = self.lineEdit_13.text()

		if (area_aco != '0' and base != '0' and altura != '0' and d_agreg != '0' and d != '0'):

			self.widget.clear()
			area_aco = float(self.lineEdit_11.text())
			base = float(self.lineEdit_10.text())
			altura = float(self.lineEdit_9.text())
			cobrimento = float(self.comboBox_3.currentText())
			bitola_estribo = float(self.comboBox.currentText())
			x = []
			y = []
			z = []
			cont = 0
			for i in tabela_bitolas:
				n_barras = float(area_aco/i[1])
				print('bitola: ',i[0],' - nº barras: ',n_barras)

				self.tableWidget.setItem(cont,2, QTableWidgetItem(str(round(n_barras, ndigits=2))))
				self.tableWidget.setItem(cont,3, QTableWidgetItem(str(round(n_barras +0.5)+1)))

				x.append(i[0])
				y.append(round(n_barras +0.5)+1)

				bitola = x[cont]
				n_barras = (round(n_barras +0.5)+1)

				espass_horizontal = (round(base - 2*(cobrimento+bitola_estribo/10) - n_barras*(bitola/10), ndigits=2))/(n_barras-1)
				
				z.append(round(espass_horizontal,ndigits=2))
				self.tableWidget.setItem(cont,4, QTableWidgetItem(str(espass_horizontal)))

				print('base:',base)
				print('cobrimento:',cobrimento)
				print('bitola_estribo:',bitola_estribo)
				print('n_barras:',n_barras)

				cont +=1

			#print(x)
			#print(y)
			#print(z)
			
			self.widget.plot(x=x,y=y,pen=(3))

			self.calcular_espacamentos()
			self.calcular_estribos()

		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes!")


	def calcular_espacamentos(self):
		bitola = float(self.comboBox_4.currentText())
		d_agreg = float(self.lineEdit_12.text())

		s_horizontal = max(2, (bitola/10), 1.2*d_agreg)
		s_vertical = max(2, (bitola/10), 0.5*d_agreg)

		#------------------------------- saida de dados ----------------------------------
		self.lineEdit_7.setText(str(s_horizontal))
		self.lineEdit_8.setText(str(s_vertical))

	def limpar_detalhamento(self):
		self.widget.clear()
		self.lineEdit_11.setText(str('0'))
		self.lineEdit_9.setText(str('0'))
		self.lineEdit_10.setText(str('0'))
		self.lineEdit_7.setText(str('0'))
		self.lineEdit_8.setText(str('0'))






if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	inicio = Detalhar_viga()
	app.exec_()
