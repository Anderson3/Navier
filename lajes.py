


import sys
import math

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import pyqtgraph as pg

import marcus 

class Lajes(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = loadUi('lajes.ui',self)

		self.lado1 = 'livre'
		self.lado2 = 'livre'
		self.lado3 = 'livre'
		self.lado4 = 'livre'
		self.label_37.hide()
		self.label_38.hide()
		self.label_40.hide()
		self.label_41.hide()
		global caso
		caso = '1'
		global lx_lage
		lx_lage = 'l_menor'
		self.lineEdit.setReadOnly(True)

		self.load_signals()

		self.setWindowTitle('Navier - Lajes')
		self.show()

	def load_signals(self):
		print('lajes iniciado')
		self.pushButton.clicked.connect(self.estado_l1)
		self.pushButton_2.clicked.connect(self.estado_l2)
		self.pushButton_3.clicked.connect(self.estado_l3)
		self.pushButton_4.clicked.connect(self.estado_l4)
		self.pushButton.clicked.connect(self.situacao_laje)
		self.pushButton_2.clicked.connect(self.situacao_laje)
		self.pushButton_3.clicked.connect(self.situacao_laje)
		self.pushButton_4.clicked.connect(self.situacao_laje)

		self.pushButton_5.clicked.connect(self.teste)
		self.pushButton_6.clicked.connect(self.calcular_laje)

		self.toolButton.clicked.connect(self.revelar_carg_acidental)

	def teste(self):
		lado1 = float(self.lineEdit_3.text())
		lado2 = float(self.lineEdit_4.text())
		espes = float(self.lineEdit_5.text())


		pp = (espes * 25)/100
		self.lineEdit.setText(str(pp))

	def revelar_carg_acidental(self):
		print('oi--')
		carga_adicional.show()

	def estado_l1(self):
		if self.lado1 == 'livre':
			self.lado1 = 'engastado'
			pixmap = QPixmap('engv.png')
			self.pushButton.setIcon(QIcon(pixmap))
		else:
			self.lado1 = 'livre'
			pixmap = QPixmap('livv.png')
			self.pushButton.setIcon(QIcon(pixmap))

	def estado_l2(self):
		if self.lado2 == 'livre':
			self.lado2 = 'engastado'
			pixmap = QPixmap('engh.png')
			self.pushButton_2.setIcon(QIcon(pixmap))
		else:
			self.lado2 = 'livre'
			pixmap = QPixmap('livh.png')
			self.pushButton_2.setIcon(QIcon(pixmap))

	def estado_l3(self):
		if self.lado3 == 'livre':
			self.lado3 = 'engastado'
			pixmap = QPixmap('engh.png')
			self.pushButton_3.setIcon(QIcon(pixmap))
		else:
			self.lado3 = 'livre'
			pixmap = QPixmap('livh.png')
			self.pushButton_3.setIcon(QIcon(pixmap))

	def estado_l4(self):
		if self.lado4 == 'livre':
			self.lado4 = 'engastado'
			pixmap = QPixmap('engv.png')
			self.pushButton_4.setIcon(QIcon(pixmap))
		else:
			self.lado4 = 'livre'
			pixmap = QPixmap('livv.png')
			self.pushButton_4.setIcon(QIcon(pixmap))

	def situacao_laje(self):
		l1 = self.lado1
		l2 = self.lado2
		l3 = self.lado3
		l4 = self.lado4

		cota_v1 = self.label_37
		cota_v2 = self.label_40
		cota_h1 = self.label_38
		cota_h2 = self.label_41

		if (l1 == 'livre' and l2 == 'livre' and l3 == 'livre' and l4 == 'livre'):
			global caso
			caso = '1'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			global lx_lage
			lx_lage = 'l_menor'
		elif (l1 == 'engastado' and l2 == 'livre' and l3 == 'livre' and l4 == 'livre') or (l1 == 'livre' and l2 == 'livre' and l3 == 'livre' and l4 == 'engastado'):
			caso = '2'

			cota_v1.hide()
			cota_v2.hide()
			cota_h1.show()
			cota_h2.show()

			lx_lage = 'l_maior'
		elif (l1 == 'livre' and l2 == 'engastado' and l3 == 'livre' and l4 == 'livre') or (l1 == 'livre' and l2 == 'livre' and l3 == 'engastado' and l4 == 'livre') :
			caso = '2'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			lx_lage = 'l_menor'
		elif (l1 == 'engastado' and l2 == 'engastado' and l3 == 'livre' and l4 == 'livre') or (l1 == 'engastado' and l2 == 'livre' and l3 == 'engastado' and l4 == 'livre') or (l1 == 'livre' and l2 == 'engastado' and l3 == 'livre' and l4 == 'engastado') or (l1 == 'livre' and l2 == 'livre' and l3 == 'engastado' and l4 == 'engastado'):
			caso = '3'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			lx_lage = 'l_menor'
		elif (l1 == 'engastado' and l2 == 'livre' and l3 == 'livre' and l4 == 'engastado'):
			caso = '4'

			cota_v1.hide()
			cota_v2.hide()
			cota_h1.show()
			cota_h2.show()

			lx_lage = 'l_maior'
		elif (l1 == 'livre' and l2 == 'engastado' and l3 == 'engastado' and l4 == 'livre'):
			caso = '4'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			lx_lage = 'l_menor'
		elif (l1 == 'engastado' and l2 == 'livre' and l3 == 'engastado' and l4 == 'engastado') or (l1 == 'engastado' and l2 == 'engastado' and l3 == 'livre' and l4 == 'engastado'):
			caso = '5'

			cota_v1.hide()
			cota_v2.hide()
			cota_h1.show()
			cota_h2.show()

			lx_lage = 'l_maior'
		elif (l1 == 'livre' and l2 == 'engastado' and l3 == 'engastado' and l4 == 'engastado') or (l1 == 'engastado' and l2 == 'engastado' and l3 == 'engastado' and l4 == 'livre'):
			caso = '5'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			lx_lage = 'l_menor'
		elif (l1 == 'engastado' and l2 == 'engastado' and l3 == 'engastado' and l4 == 'engastado'):
			caso = '6'

			cota_v1.show()
			cota_v2.show()
			cota_h1.hide()
			cota_h2.hide()

			lx_lage = 'l_menor'
		else:
			caso='ainda não existe, não sei como você chegou até aqui srsrrsrsrsrsrs'


		print(caso)
		self.lineEdit_6.setText(str(caso))

	def calcular_laje(self):
		lado_maior = float(self.lineEdit_3.text())
		lado_menor = float(self.lineEdit_4.text())
		espes = float(self.lineEdit_5.text())
		d = float(self.lineEdit_27.text())

		self.lineEdit_7.setText('')
		self.lineEdit_9.setText('')
		self.lineEdit_8.setText('')
		self.lineEdit_10.setText('')
		self.lineEdit_16.setText('')
		self.lineEdit_14.setText('')
		self.lineEdit_15.setText('')
		self.lineEdit_16.setText('')
		
		if lado_maior != 0 and lado_menor != 0 and espes != 0 and d != 0:
			lado1 = float(self.lineEdit_3.text())
			lado2 = float(self.lineEdit_4.text())
			espes = float(self.lineEdit_5.text())
			d = float(self.lineEdit_27.text())
			carreg_adicional = float(self.lineEdit_2.text())

			pp = (espes * 25)/100
			self.lineEdit.setText(str(pp))

			carreg_total = pp + carreg_adicional
			#print(caso)
			#print(lx_lage)
			#---------------------------------- cálculo do Lx baseado no caso do tipo de situação da laje -----------------
			global lx
			global lambda_laje
			if lx_lage == 'l_menor':
				lx = lado2
				lambda_laje = round((lado1/lado2),ndigits=2)
			elif lx_lage == 'l_maior':
				lx = lado1
				lambda_laje = round((lado2/lado1),ndigits=2)
			print(lx_lage)

			#---------------------------------- definição se a laje é unidirecional ou bidirecional baseado no lambda  -----------------
			global tipo_laje
			if float(lambda_laje) > 2.001:
				tipo_laje = 'UNIDIRECIONAL'
				self.laje_unidirecional(carreg_total)
			else:
				tipo_laje = 'BIDIRECIONAL'
				self.label_43.setStyleSheet("Background: url('laje_unidirecional_modelo.png') no-repeat")
			
				mx = my = nx = ny = ''
				
				if caso == '1':
					caso1 = marcus.caso1
					linhas = len(caso1)
					colunas = len(caso1[0])

					for i in range(linhas):
						aux = caso1[i][0]
						if lambda_laje == aux:
							print(caso1[i])
							mx = caso1[i][2]
							my = caso1[i][3]

					print('mx: ',mx)
					print('my: ',my)

				if caso == '2':
					caso2 = marcus.caso2
					linhas = len(caso2)
					colunas = len(caso2[0])

					for i in range(linhas):
						aux = caso2[i][0]
						if lambda_laje == aux:
							print(caso2[i])
							mx = caso2[i][2]
							nx = caso2[i][3]
							my = caso2[i][4]

					print('mx: ',mx)
					print('nx: ',nx)
					print('my: ',my)

				if caso == '3':
					caso3 = marcus.caso3
					linhas = len(caso3)
					colunas = len(caso3[0])

					for i in range(linhas):
						aux = caso3[i][0]
						if lambda_laje == aux:
							print(caso3[i])
							mx = caso3[i][2]
							nx = caso3[i][3]
							my = caso3[i][4]
							ny = caso3[i][5]

					print('mx: ',mx)
					print('nx: ',nx)
					print('my: ',my)
					print('ny: ',ny)

				if caso == '4':
					caso4 = marcus.caso4
					linhas = len(caso4)
					colunas = len(caso4[0])

					for i in range(linhas):
						aux = caso4[i][0]
						if lambda_laje == aux:
							print(caso4[i])
							mx = caso4[i][2]
							nx = caso4[i][3]
							my = caso4[i][4]

					print('mx: ',mx)
					print('nx: ',nx)
					print('my: ',my)

				if caso == '5':
					caso5 = marcus.caso5
					linhas = len(caso5)
					colunas = len(caso5[0])

					for i in range(linhas):
						aux = caso5[i][0]
						if lambda_laje == aux:
							print(caso5[i])
							mx = caso5[i][2]
							nx = caso5[i][3]
							my = caso5[i][4]
							ny = caso5[i][5]

					print('mx: ',mx)
					print('nx: ',nx)
					print('my: ',my)
					print('ny: ',ny)

				if caso == '6':
					caso6 = marcus.caso6
					linhas = len(caso6)
					colunas = len(caso6[0])

					for i in range(linhas):
						aux = caso6[i][0]
						if lambda_laje == aux:
							print(caso6[i])
							mx = caso6[i][2]
							nx = caso6[i][3]
							my = caso6[i][4]
							ny = caso6[i][5]

					print('mx: ',mx)
					print('nx: ',nx)
					print('my: ',my)
					print('ny: ',ny)

				print(lx)
				if mx != '':
					self.lineEdit_7.setText(str(mx))
					momento_pos_x = ((carreg_total * (lx**2))/mx)
					momento_pos_x = round(momento_pos_x,ndigits=4)
					self.lineEdit_13.setText(str(momento_pos_x))
				#else:
				#	self.lineEdit_13.setText('0')
				if nx != '':
					self.lineEdit_9.setText(str(nx))
					momento_neg_x = round(((carreg_total * (lx**2))/nx),ndigits=4)
					self.lineEdit_14.setText(str(momento_neg_x))
					#momento_neg_x = round(momento_neg_x,ndigits=2)
				#else:
				#	self.lineEdit_14.setText('0')
				if my != '':
					self.lineEdit_8.setText(str(my))
					momento_pos_y = ((carreg_total * (lx**2))/my)
					momento_pos_y = round(momento_pos_y,ndigits=4)
					self.lineEdit_15.setText(str(momento_pos_y))
				#else:
				#	self.lineEdit_15.setText('0')
				if ny != '':
					self.lineEdit_10.setText(str(ny))
					momento_neg_y = round(((carreg_total * (lx**2))/ny),ndigits=4)
					self.lineEdit_16.setText(str(momento_neg_y))
					#momento_neg_y = round(momento_neg_y,ndigits=2)
				#else:
				#	self.lineEdit_16.setText('0')


				#----------------------------------- enviar resultados de saida ao programa ---------------------------------------
				self.lineEdit_11.setText(str(lambda_laje))
				self.label_16.setText(str(tipo_laje))
				self.lineEdit_12.setText(str(carreg_total))

				self.resultados_laje()
		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes")
		

	def laje_unidirecional(self,carreg_total):

		#self.lineEdit_7.setText('')
		#self.lineEdit_9.setText('')
		#self.lineEdit_8.setText('')
		#self.lineEdit_10.setText('')
		#self.lineEdit_16.setText('')
		#self.lineEdit_13.setText('')
		#self.lineEdit_14.setText('')
		#self.lineEdit_15.setText('')
		#self.lineEdit_16.setText('')

		print('unidirecional')
		#l1 = self.lado1
		l2 = self.lado2
		l3 = self.lado3
		#l4 = self.lado4
		print(carreg_total)
		if (l2 == 'livre' and l3 == 'livre'):
			self.label_43.setStyleSheet("Background: url('laje_unidirecional_ll2.png') no-repeat")
			momento_pos_y = (carreg_total * (lx**2))/8
			momento_neg_y = 0
		elif (l2 == 'engastado' and l3 == 'engastado'):
			self.label_43.setStyleSheet("Background: url('laje_unidirecional_ee2.png') no-repeat")
			momento_pos_y = (carreg_total * (lx**2))/24
			momento_neg_y = (carreg_total * (lx**2))/12
		elif (l2 == 'engastado' and l3 == 'livre') or (l2 == 'livre' and l3 == 'engastado'):
			self.label_43.setStyleSheet("Background: url('laje_unidirecional_le2.png') no-repeat")
			momento_pos_y = (carreg_total * (lx**2))/14.2
			momento_neg_y = (carreg_total * (lx**2))/8

		print('momento_pos_y: ',momento_pos_y)
		print('momento_neg_y: ',momento_neg_y)

		#----------------------------------- enviar resultados de saida ao programa ---------------------------------------
		momento_pos_y = round(momento_pos_y,ndigits=4)
		self.lineEdit_15.setText(str(momento_pos_y))
		momento_neg_y = round(momento_neg_y,ndigits=4)
		self.lineEdit_16.setText(str(momento_neg_y))

		self.lineEdit_13.setText('0')
		self.lineEdit_14.setText('0')

		self.lineEdit_11.setText(str(lambda_laje))
		self.label_16.setText(str(tipo_laje))
		self.lineEdit_12.setText(str(carreg_total))

		self.resultados_laje()

	def truncar(self,x):
		aux = '{:.9f}'.format(x)
		return aux

	def resultados_laje(self):

		mx = self.lineEdit_13.text()
		if mx == '':
			self.lineEdit_13.setText('0')

		my = self.lineEdit_15.text()
		if my == '':
			self.lineEdit_15.setText('0')

		nx = self.lineEdit_14.text()
		if nx == '':
			self.lineEdit_14.setText('0')

		ny = self.lineEdit_16.text()
		if ny == '':
			self.lineEdit_16.setText('0')

		fck_laje = float(self.comboBox.currentText())
		fyk_laje = float(self.comboBox_2.currentText())
		fcd_laje = fck_laje * 1.4 * 1000000
		fyd_laje = fyk_laje * 1.4 * 1000000
		d_laje = float(self.lineEdit_27.text())

		mx = float(self.lineEdit_13.text())
		my = float(self.lineEdit_15.text())
		nx = float(self.lineEdit_14.text())
		ny = float(self.lineEdit_16.text())
		#print('mx: ',mx)
		#print('nx: ',nx)
		#print('my: ',my)
		#print('ny: ',ny)
		if mx > nx:
			mk_x = mx
		else:
			mk_x = nx
		if my > ny:
			mk_y = my
		else:
			mk_y = ny

		#print('mkx: ',mk_x)
		#print('mky: ',mk_y)
		md_x = round(1.4 * mk_x, ndigits = 4)
		kmd_x_laje = (md_x * 1000)/(1 * ((d_laje/100)**2) * 0.85 * (fcd_laje))
		print('kmd_x_laje-',kmd_x_laje)
		kx_x_laje = (1 - math.sqrt(1 - 2*kmd_x_laje))/0.8
		kz_x_laje = 1 - 0.4 * kx_x_laje

		as_x_laje = (md_x * 1000/ (kz_x_laje * (d_laje/100) * fyd_laje))*100000

		print('md_x: ', md_x)
		print('kmd_x_laje: ', kmd_x_laje)
		print('kx_x_laje: ', kx_x_laje)
		print('kz_x_laje: ', kz_x_laje)
		print('as_x_laje: ', as_x_laje)

		md_y = round(1.4 * mk_y, ndigits = 4)
		kmd_y_laje = (md_y * 1000)/(1 * ((d_laje/100)**2) * 0.85 * (fcd_laje))
		kx_y_laje = (1 - math.sqrt(1 - 2*kmd_y_laje))/0.8
		kz_y_laje = 1 - 0.4 * kx_y_laje

		as_y_laje = (md_y * 1000/ (kz_y_laje * (d_laje/100) * fyd_laje))*100000

		print('md_y: ', md_y)
		print('kmd_y_laje: ', kmd_y_laje)
		print('kx_y_laje: ', kx_y_laje)
		print('kz_y_laje: ', kz_y_laje)
		print('as_y_laje: ', as_y_laje)

		#------------------------------------------ saida de dados ------------------------------------
		kmd_x_laje = self.truncar(kmd_x_laje)
		kx_x_laje = self.truncar(kx_x_laje)
		kz_x_laje = self.truncar(kz_x_laje)
		as_x_laje = self.truncar(as_x_laje)

		kmd_y_laje = self.truncar(kmd_y_laje)
		kx_y_laje = self.truncar(kx_y_laje)
		kz_y_laje = self.truncar(kz_y_laje)
		as_y_laje = self.truncar(as_y_laje)

		self.lineEdit_17.setText(str(md_x))
		self.lineEdit_18.setText(str(kmd_x_laje))
		self.lineEdit_19.setText(str(kx_x_laje))
		self.lineEdit_20.setText(str(kz_x_laje))
		self.lineEdit_21.setText(str(as_x_laje))

		self.lineEdit_22.setText(str(md_y))
		self.lineEdit_24.setText(str(kmd_y_laje))
		self.lineEdit_25.setText(str(kx_y_laje))
		self.lineEdit_26.setText(str(kz_y_laje))
		self.lineEdit_23.setText(str(as_y_laje))





if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	inicio = Lajes()

	app.exec_()
