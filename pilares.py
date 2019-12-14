


import sys, os
import math

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import pyqtgraph as pg

global pilares_info
pilares_info = [0,0,0,0]

global pilares_info_aco
pilares_info_aco = [0, 0, 0, 0, 0, 0, 0]

class Pilares(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = loadUi('pilares_alt.ui',self)
		self.load_signals()

		self.setWindowTitle('Navier - Pilares')


	def load_signals(self):
		print('pilares carregado')
		self.cont_x = 0
		self.cont_y = 0
		#self.pushButton.clicked.connect(self.pilar_alterar_tipo_engaste_x)
		#self.pushButton_2.clicked.connect(self.pilar_alterar_tipo_engaste_y)
		self.pushButton_6.clicked.connect(self.calcular_pilares)
		self.pushButton.clicked.connect(self.gerar_envoltoria)
		self.pushButton_3.clicked.connect(lambda: pilares_areas_aco.show())

		self.show()


	def calcular_pilares(self):
		x_pilar = self.lineEdit.text()
		y_pilar = self.lineEdit_2.text()
		altura_pilar = self.lineEdit_3.text()
		altura_lance = self.lineEdit_4.text()

		nk_pilar = self.lineEdit_5.text()
		momento_x_topo = self.lineEdit_6.text()
		momento_x_base = self.lineEdit_7.text()
		momento_y_topo = self.lineEdit_8.text()
		momento_y_base = self.lineEdit_9.text()


		if (x_pilar != '0' and y_pilar != '0' and altura_pilar != '0' and altura_lance != '0' and nk_pilar != '0'):
			fck_pilar = float(self.comboBox_3.currentText())
			fcd_pilar = fck_pilar/1.4
			fyk_pilar = float(self.comboBox_4.currentText())
			fyd_pilar = fyk_pilar/1.15
			cobrimento_pilar = float(self.comboBox_5.currentText())

			x_pilar = float(self.lineEdit.text())
			y_pilar = float(self.lineEdit_2.text())
			altura_pilar = float(self.lineEdit_3.text())
			altura_lance = float(self.lineEdit_4.text())

			nk_pilar = float(self.lineEdit_5.text())
			momento_x_topo = float(self.lineEdit_6.text())
			momento_x_base = float(self.lineEdit_7.text())
			momento_y_topo = float(self.lineEdit_8.text())
			momento_y_base = float(self.lineEdit_9.text())

			area_secao_pilar = (x_pilar/100)*(y_pilar/100)

			#nd_pilar = (nk_pilar + ((x_pilar/100)*(y_pilar/100)*altura_pilar*25)) * 1.4
			nd_pilar = (nk_pilar) * 1.4
			md_x_topo = 1.4 * momento_x_topo
			md_x_base = 1.4 * momento_x_base
			md_y_topo = 1.4 * momento_y_topo
			md_y_base = 1.4 * momento_y_base

			'''apoio_x = self.stackedWidget.currentIndex()
			if apoio_x == 0:
				tipo_apoio_x = 'AA'
			elif apoio_x == 1:
				tipo_apoio_x = 'EA'
			elif apoio_x == 2:
				tipo_apoio_x = 'EE'
			'''

			tipo_apoio_x = 'AA'

			if momento_x_topo == 0 and momento_x_base == 0 and momento_y_topo == 0 and momento_y_base == 0:
				self.tipo_pilar = 'intermediario'
			elif momento_x_topo == 0 and momento_x_base == 0:
				self.tipo_pilar = 'extremidade-x'
			elif momento_y_topo == 0 and momento_y_base == 0:
				self.tipo_pilar = 'extremidade-y'
			else:
				self.tipo_pilar = 'canto'


			self.lineEdit_13.setText(str(round(md_x_topo, ndigits=5)))
			self.lineEdit_14.setText(str(round(md_x_base, ndigits=5)))
			self.lineEdit_22.setText(str(round(md_y_topo, ndigits=5)))
			self.lineEdit_28.setText(str(round(md_y_base, ndigits=5)))

			#-Eixo-X----------------------------------------------------------------------
			b = y_pilar
			h = x_pilar

			m_a = max(md_x_topo, md_x_base)
			m_b = min(md_x_topo, md_x_base)

			if self.tipo_pilar == 'intermediario' or self.tipo_pilar == 'extremidade-x':
				alfa_b_x = 1.0
			else:
				alfa_b_x = (0.6 + 0.4*(m_b/m_a))

			if alfa_b_x < 0.4:
				alfa_b_x = 0.4

			#excen_min_x = (1.5+0.03*h)
			momento_min_x = (nd_pilar *(1.5+0.03*h))/100
			excen_min_x = momento_min_x/nd_pilar

			if md_x_topo < momento_min_x:
				md_x_topo = momento_min_x
				print('momento topo - mínimo')
				alfa_b_x = 1.0
			if md_x_base < momento_min_x:
				md_x_base = momento_min_x
				print('momento base - mínimo')
				alfa_b_x = 1.0

			compr_efetivo_x = (altura_pilar*100) + h
			if (altura_lance*100 < compr_efetivo_x):
				compr_efetivo_x = altura_lance*100

			excen_x_acidental = compr_efetivo_x/400
			v_0 = (nd_pilar*1000)/(area_secao_pilar * fcd_pilar*1000000)

			excentricidade_relativa = (max(md_x_topo,md_x_base,momento_min_x)/nd_pilar)/h

			lambda_pilar_x = 3.46 * (compr_efetivo_x/h)
			lambda_pilar_x_limite = (25 + 12.5*(excentricidade_relativa))/alfa_b_x
			if lambda_pilar_x_limite < 35:
				lambda_pilar_x_limite = 35

			excen_2_x = (compr_efetivo_x**2)/10 *(0.005/((v_0+0.5)*h))

			md2_x = nd_pilar * (excen_2_x/100)

			if lambda_pilar_x > lambda_pilar_x_limite:
				print('efeitos de 2 ordem considerados')
				excen_2 = (compr_efetivo_x**2)/10 *(0.005/((v_0+0.5)*h))
				md2_x_relativo = nd_pilar * (excen_2/100)
			else:
				md2_x_relativo = 0
				print('efeitos de 2 ordem desconsiderados')

			msd_x_intermediario = alfa_b_x * max(abs(md_x_topo), abs(md_x_base), abs(momento_min_x)) + md2_x_relativo
			#msd_x_intermediario = alfa_b_x * abs(momento_min_x) + md2_x_relativo

			mi_x = msd_x_intermediario/(h * area_secao_pilar * fcd_pilar)/10
			delta_x = cobrimento_pilar/h


			#-Eixo-Y----------------------------------------------------------------------
			h = y_pilar
			b = x_pilar

			m_a = max(md_y_topo, md_y_base)
			m_b = min(md_y_topo, md_y_base)

			if self.tipo_pilar == 'intermediario' or self.tipo_pilar == 'extremidade-y':
				alfa_b_y = 1.0
			else:
				alfa_b_y = (0.6 + 0.4*(m_b/m_a))

			if alfa_b_y < 0.4:
				alfa_b_y = 0.4

			momento_min_y = (nd_pilar *(1.5+0.03*h))/100
			excen_min_y = momento_min_y/nd_pilar
			
			if md_y_topo < momento_min_y:
				md_y_topo = momento_min_y
				print('momento topo - mínimo')
				alfa_b_y = 1.0
			if md_y_base < momento_min_y:
				md_y_base = momento_min_y
				print('momento base - mínimo')
				alfa_b_y = 1.0

			compr_efetivo_y = (altura_pilar*100) + h
			if (altura_lance*100 < compr_efetivo_y):
				compr_efetivo_y = altura_lance*100

			excen_y_acidental = compr_efetivo_y/400
			v_0 = (nd_pilar*1000)/(area_secao_pilar * fcd_pilar*1000000)

			excentricidade_relativa = (max(md_y_topo,md_y_base,momento_min_y)/nd_pilar)/h

			lambda_pilar_y = 3.46 * (compr_efetivo_y/h)
			lambda_pilar_y_limite = (25 + 12.5*(excentricidade_relativa))/alfa_b_y
			if lambda_pilar_y_limite < 35:
				lambda_pilar_y_limite = 35

			excen_2_y = (compr_efetivo_y**2)/10 *(0.005/((v_0+0.5)*h))

			md2_y = nd_pilar * (excen_2_y/100)

			if lambda_pilar_y > lambda_pilar_y_limite:
				print('efeitos de 2 ordem considerados')
				excen_2 = (compr_efetivo_y**2)/10 *(0.005/((v_0+0.5)*h))
				md2_y_relativo = nd_pilar * (excen_2/100)
			else:
				md2_y_relativo = 0
				print('efeitos de 2 ordem desconsiderados')

			msd_y_intermediario = alfa_b_y * max(abs(md_y_topo), abs(md_y_base), abs(momento_min_y)) + md2_y_relativo
			#msd_y_intermediario = alfa_b_y * abs(momento_min_y) + md2_y_relativo

			mi_y = msd_y_intermediario/(h * area_secao_pilar * fcd_pilar)/10
			delta_y = cobrimento_pilar/h

			#print('v_0: ',v_0)
			#print('excen_2_x: ',excen_2_x)
			#print('compr_efetivo_x: ',compr_efetivo_x)
			#print('alfa_b_x: ',alfa_b_x)
			#print('lambda_pilar_x: ',lambda_pilar_x)
			#print('lambda_pilar_x_limite: ',lambda_pilar_x_limite)
			#print('momento_min_x: ',momento_min_x)
			#print('md_x_topo: ',md_x_topo)
			#print('md_x_base: ',md_x_base)
			#print('msd_x_intermediario: ',msd_x_intermediario)
			#print('md2_x: ',md2_x)
			#print('--------------------------------------------------')
			#print('lambda_pilar_y: ',lambda_pilar_y)
			#print('lambda_pilar_y_limite: ',lambda_pilar_y_limite)
			#print('momento_min_y: ',momento_min_y)
			#print('md_y_topo: ',md_y_topo)
			#print('md_y_base: ',md_y_base)
			#print('msd_y_intermediario: ',msd_y_intermediario)

			#--------------------------------------------- saida de dados ---------------------------------------------
			self.lineEdit_10.setText(str(round(nd_pilar, ndigits=4)))
			self.lineEdit_11.setText(str(round(area_secao_pilar, ndigits=4)))
			self.lineEdit_12.setText(str(round(v_0, ndigits=4)))

			self.lineEdit_15.setText(str(round(momento_min_x, ndigits=5)))
			self.lineEdit_16.setText(str(round(excen_min_x*100, ndigits=5)))
			self.lineEdit_17.setText(str(round(lambda_pilar_x, ndigits=5)))
			self.lineEdit_18.setText(str(round(lambda_pilar_x_limite, ndigits=5)))
			self.lineEdit_19.setText(str(round(excen_2_x, ndigits=5)))
			self.lineEdit_20.setText(str(round(md2_x, ndigits=5)))
			self.lineEdit_21.setText(str(round(msd_x_intermediario, ndigits=5)))

			self.lineEdit_24.setText(str(round(momento_min_y, ndigits=5)))
			self.lineEdit_25.setText(str(round(excen_min_y*100, ndigits=5)))
			self.lineEdit_26.setText(str(round(lambda_pilar_y, ndigits=5)))
			self.lineEdit_23.setText(str(round(lambda_pilar_y_limite, ndigits=5)))
			self.lineEdit_30.setText(str(round(excen_2_y, ndigits=5)))
			self.lineEdit_29.setText(str(round(md2_y, ndigits=5)))
			self.lineEdit_27.setText(str(round(msd_y_intermediario, ndigits=5)))

			self.lineEdit_31.setText(str(round(mi_x, ndigits=2)))
			self.lineEdit_32.setText(str(round(mi_y, ndigits=2)))
			self.lineEdit_33.setText(str(round(delta_x, ndigits=2)))
			self.lineEdit_34.setText(str(round(delta_y, ndigits=2)))

			global pilares_info
			pilares_info = [msd_x_intermediario, msd_y_intermediario, momento_min_x, momento_min_y]

			if md2_x_relativo == 0:
				self.label_39.setText('não considera 2º ordem')
			else:
				self.label_39.setText('considera 2º ordem')

			if md2_y_relativo == 0:
				self.label_44.setText('não considera 2º ordem')
			else:
				self.label_44.setText('considera 2º ordem')


			if self.tipo_pilar == 'intermediario':
				self.label.setText('PILAR INTERMEDIÁRIO')
			elif (self.tipo_pilar == 'extremidade-x') or (self.tipo_pilar == 'extremidade-y'):
				self.label.setText('PILAR DE EXTREMIDADE')
			else:
				self.label.setText('PILAR DE CANTO')
			
			global pilares_info_aco
			pilares_info_aco = [mi_x, delta_x, mi_y, delta_y, fck_pilar, area_secao_pilar, nk_pilar]

		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes!")

			

	def gerar_envoltoria(self):
		msd_x_intermediario = pilares_info[0]
		msd_y_intermediario = pilares_info[1]
		momento_min_x = pilares_info[2]
		momento_min_y = pilares_info[3]

		x = []
		y = []
		for i in range(360):
			theta = i
			theta_conv = (theta*math.pi)/180

			seno = math.sin(theta_conv)
			seno = momento_min_y * seno

			cosseno = math.cos(theta_conv)
			cosseno = momento_min_x * cosseno

			x.append(seno)
			y.append(cosseno)

		z = []
		w = []
		for j in range(360):
			theta = j
			theta_conv = (theta*math.pi)/180

			seno = math.sin(theta_conv)
			seno = msd_y_intermediario * seno

			cosseno = math.cos(theta_conv)
			cosseno = msd_x_intermediario * cosseno

			z.append(seno)
			w.append(cosseno)

		# create plot
		'''plt = pg.plot(x, y, title='theTitle', pen='r')
		plt.showGrid(x=True,y=True)
		'''
		# create plot
		plt = pg.plot()
		plt.clear()
		plt.showGrid(x=True,y=True)
		plt.addLegend()
		plt.setTitle('Envoltória de Momentos')
		

		# set properties
		plt.setLabel('left', 'Momentos Y', units='KN.m')
		plt.setLabel('bottom', 'Momentos X', units='KN.m')
		plt.setXRange(0,10)
		plt.setYRange(0,20)
		

		plt.enableAutoRange()
		plt.setWindowTitle('pyqtgraph plot')
		# plot
		c1 = plt.plot(x, y, pen='r', name='Envoltória Momentos min')
		c2 = plt.plot(z, w, pen='b', name='Envoltória Momentos máx')





file = 'file:///C:/Users/Acer/Desktop/tessssst/sample.pdf'

#global pilares_info_aco
#pilares_info_aco = [1.4,0.5,1.0,0.1,20,0.4,1000]

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

	def load_signals(self):
		print('inicializado')
		self.pushButton_2.clicked.connect(self.calcular_area_aco)
		self.pushButton.clicked.connect(self.recuperar_dados)
		self.pushButton_3.clicked.connect(self.limpar)
		self.pushButton_4.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))
		self.pushButton_5.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))

	def recuperar_dados(self):
		self.lineEdit_2.setText(str(round(pilares_info_aco[0], ndigits=2)))
		self.lineEdit_3.setText(str(round(pilares_info_aco[1], ndigits=2)))
		self.lineEdit_5.setText(str(round(pilares_info_aco[2], ndigits=2)))
		self.lineEdit_6.setText(str(round(pilares_info_aco[3], ndigits=2)))
		self.lineEdit_12.setText(str(round(pilares_info_aco[4], ndigits=2)))
		self.lineEdit_13.setText(str(round(pilares_info_aco[5], ndigits=2)))
		self.lineEdit_14.setText(str(round(pilares_info_aco[6], ndigits=2)))

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
	pilares = Pilares()
	pilares_areas_aco = Pilar_area_aco()

	app.exec_()
