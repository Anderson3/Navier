

import sys
import os
import math

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtWidgets, QtGui, QtCore
import pyqtgraph as pg


import marcus

file = 'file:///C:/Users/Acer/Desktop/tessssst/sample.pdf'

class Inicio(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = None
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('inicio_alt.ui',self)
		self.label.setStyleSheet("Background-Color: #ddebff;")

		self.setWindowTitle('Navier - inicio')

		self.pushButton.setIcon(QtGui.QIcon('btn_inicio_vigas.png'))
		self.pushButton.setIconSize(QtCore.QSize(52,52))
		self.pushButton_3.setIcon(QtGui.QIcon('btn_inicio_pilares.png'))
		self.pushButton_3.setIconSize(QtCore.QSize(42,42))
		self.pushButton_9.setIcon(QtGui.QIcon('btn_inicio_lajes.png'))
		self.pushButton_9.setIconSize(QtCore.QSize(42,42))
		self.pushButton_11.setIcon(QtGui.QIcon('btn_inicio_fundacoes.png'))
		self.pushButton_11.setIconSize(QtCore.QSize(45,45))

		#self.tab_2.setStyleSheet("background: url('navier_logo.png') no-repeat contain")
		#self.tab_2.setStyleSheet("background-image: url(navier_logo.png); background-repeat: no-repeat; background-position: right bottom")

		self.label_5.setStyleSheet("Background-Color: #ddebff;")
		self.label_10.setStyleSheet("Background-Color: #ddebff;")
		self.label_9.setStyleSheet("Background-Color: #ddebff;")
		self.label_11.setStyleSheet("Background-Color: #ddebff;")
		
		self.pushButton_2.setIcon(QtGui.QIcon('btn_caa.png'))
		self.pushButton_2.setIconSize(QtCore.QSize(45,45))
		self.pushButton_5.setIcon(QtGui.QIcon('btn_cadicional.png'))
		self.pushButton_5.setIconSize(QtCore.QSize(45,45))
		self.pushButton_6.setIcon(QtGui.QIcon('btn_tabbitolas.png'))
		self.pushButton_6.setIconSize(QtCore.QSize(45,45))
		self.pushButton_7.setIcon(QtGui.QIcon('btn_tabmarcus.png'))
		self.pushButton_7.setIconSize(QtCore.QSize(45,45))
		self.pushButton_8.setIcon(QtGui.QIcon('btn_flexaosimples.png'))
		self.pushButton_8.setIconSize(QtCore.QSize(45,45))
		self.pushButton_23.setIcon(QtGui.QIcon('btn_flexaocomposta.png'))
		self.pushButton_23.setIconSize(QtCore.QSize(45,45))

		#self.textBrowser_14.hide()
		self.label_21.setToolTip('Brunel - programa de cálculo e verificação de perfis metálicos para perfis brasileiros')
		self.label_22.setToolTip('EngTool - aplicação mobile para cálculo de vigas de concreto armado')

		#self.scrollArea.setStyleSheet("background-color:transparent;")
		#self.scrollArea.setStyleSheet("QScrollArea {background-color:transparent;}");
		#self.scrollAreaContents.setStyleSheet("background-color:transparent;");
		
		self.setFixedSize(570, 450)
		self.show()


	def load_signals(self):
		self.pushButton.clicked.connect(self.iniciar_vigas)
		self.pushButton_3.clicked.connect(self.iniciar_pilares)
		self.pushButton_9.clicked.connect(self.iniciar_lajes)
		self.pushButton_11.clicked.connect(self.iniciar_fundacoes)

		self.pushButton_2.clicked.connect(self.iniciar_classe_agressividade)
		self.pushButton_5.clicked.connect(self.iniciar_carga_adicional)
		self.pushButton_6.clicked.connect(self.iniciar_tabela_bitolas)

		self.pushButton_7.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))
		self.pushButton_8.clicked.connect(lambda: self.abrirTabelaAuxiliar(file))


	def abrirTabelaAuxiliar(self,file):
	    if sys.platform == 'linux2':
	        subprocess.call(["xdg-open", file])
	    else:
	        os.startfile(file)

	def iniciar_vigas(self):
		print('vigas')
		vigas.show()
	def iniciar_pilares(self):
		print('pilares')
		pilares.show()
	def iniciar_lajes(self):
		print('lajes')
		lajes.show()
	def iniciar_fundacoes(self):
		print('fundações')
		sapatas.show()
	#--------------------------- forms complementares -----------------------------
	def iniciar_carga_adicional(self):
		print('carga adicional')
		carga_adicional.show()
	def iniciar_tabela_bitolas(self):
		print('carga adicional')
		tabela_bitolas.show()
	def iniciar_classe_agressividade(self):
		print('classe de agressividade')
		tabela_classe_agressividade.show()

	'''def abrir_segunda(self):
		print('oi')
		gui2.hide()
		time.sleep(0.5)
		gui2.show()
	'''



class Vigas(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = loadUi('vigas_alt.ui',self)
		self.load_signals()

		self.setWindowTitle('Navier - Vigas')

	def load_signals(self):
		print('viga carregado')
		self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
		self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
		self.pushButton_3.clicked.connect(lambda: detalhar_vigas.show())

		self.pushButton_6.clicked.connect(self.calcular_viga_index)

		self.radioButton.clicked.connect(lambda: self.lineEdit_35.setText('0.450'))
		self.radioButton_2.clicked.connect(lambda: self.lineEdit_35.setText('0.628'))


	def calcular_viga_index(self):
		aux = self.stackedWidget.currentIndex() #retorn o indice do stackedwidget e indica se o cálculo é de simples ou dupla
		#aux == 0 (Simples), aux == 1 (Dupla)
		if aux == 1:
			self.calcular_viga_simples()
		else:
			self.calcular_viga_dupla()

	def truncar(self,x):
		aux = '{:.9f}'.format(x)
		return aux

	def calcular_viga_cortante(self):
		aux = self.stackedWidget.currentIndex()
		fck_viga = float(self.comboBox.currentText())
		fcd_viga = fck_viga/1.4
		fyk_viga = float(self.comboBox_2.currentText())
		fyd_viga = fyk_viga/1.15

		mk_viga = float(self.lineEdit.text())
		vk_viga = float(self.lineEdit_2.text())

		if aux == 1:
			bw_viga = float(self.lineEdit_3.text())
			h_viga = float(self.lineEdit_4.text())
			d_viga = float(self.lineEdit_5.text())

		else:
			bw_viga = float(self.lineEdit_15.text())
			h_viga = float(self.lineEdit_16.text())
			d_viga = float(self.lineEdit_17.text())


		theta_transversal = 45
		alfa_transversal = 90
		if self.radioButton_4.isChecked():
			theta_transversal = self.spinBox.value()
		
		theta_transversal = (theta_transversal/180)*math.pi
		alfa_transversal = (alfa_transversal/180)*math.pi

		fator_cotangentes_transversal = ((math.cos(alfa_transversal)/math.sin(alfa_transversal))) + ((math.cos(theta_transversal)/math.sin(theta_transversal)))
		fator_cotangentes_transversal = 1

		vsd = vk_viga * 1.4
		vrd2 = 0.27 * (1-(fck_viga/250)) * (bw_viga/100) * fcd_viga * (d_viga/100) *(math.sin(2*theta_transversal))*fator_cotangentes_transversal * 1000
		print('VSD: ',vsd)
		print('VRD2: ',vrd2)

		if vrd2 < vsd:
			QMessageBox.about(self, "Alerta", "A seção de concreto não permite gerar bielas resistentes à compressão. Reveja as dimensões da viga ou esforços de cálculo para a estrutura.")
		else:
			vc_0 = 0.09*(fck_viga**(2/3))*(bw_viga/100)*(d_viga/100)*1000
			if self.radioButton_4.isChecked():
				vc_0 = vc_0*((vrd2 - vsd)/(vrd2 - vc_0))

			vsw = vsd - vc_0

			#as_transversal = (vsw/(0.9*(d_viga/100)*fyd_viga*fator_cotangentes_transversal*math.sin(alfa_transversal)))*1000
			as_transversal = (vsw/(0.9*(d_viga/100)*fyd_viga)*math.tan(theta_transversal))*1000

			taxa_aco_cortante_retangular = 0.2*(0.3*fck_viga**(2/3))/fyk_viga

			as_min_transversal = ((bw_viga*10)*taxa_aco_cortante_retangular)*1000 # para deixar em mm²

			print('vk_viga: ',vk_viga)
			print('vsd: ',vsd)
			print('vrd2: ',vrd2)
			print('vc_0: ',vc_0)
			print('vsw: ',vsw)
			print('as_transversal: ',as_transversal)
			print('taxa_aco_cortante_retangular: ',taxa_aco_cortante_retangular)
			print('as_min_transversal',as_min_transversal)

			#------------------------------------------- saida de dados --------------------------------------------------
			self.lineEdit_30.setText(str(round(vk_viga*1.4, ndigits=4)))
			self.lineEdit_31.setText(str(round(vrd2, ndigits=4)))
			self.lineEdit_32.setText(str(round(vc_0, ndigits=4)))
			self.lineEdit_33.setText(str(round(vsw, ndigits=4)))

			self.lineEdit_34.setText(str(round(as_transversal, ndigits=4)))
			self.lineEdit_37.setText(str(round(as_min_transversal, ndigits=4)))


	def calcular_viga_simples(self):
		mk_viga = self.lineEdit.text()
		vk_viga = self.lineEdit_2.text()
		bw_viga = self.lineEdit_3.text()
		h_viga = self.lineEdit_4.text()
		d_viga = self.lineEdit_5.text()

		if (mk_viga != '0' and vk_viga != '0' and bw_viga != '0' and h_viga != '0' and d_viga != '0'):
			fck_viga = float(self.comboBox.currentText())
			fcd_viga = fck_viga/1.4
			fyk_viga = float(self.comboBox_2.currentText())
			fyd_viga = fyk_viga/1.15

			mk_viga = float(self.lineEdit.text())
			vk_viga = float(self.lineEdit_2.text())
			bw_viga = float(self.lineEdit_3.text())
			h_viga = float(self.lineEdit_4.text())
			d_viga = float(self.lineEdit_5.text())

			d_linha_viga = h_viga - d_viga
			self.lineEdit_21.setText(str(round(d_linha_viga, ndigits=2)))
			area_secao_viga = bw_viga * h_viga

			kmd_viga = (mk_viga * 1.4 * 1000)/((bw_viga/100) * ((d_viga/100)**2) * (0.85*fcd_viga*1000000))
			if kmd_viga >0.5:
				QMessageBox.about(self, "Alerta", "Os esforços especificados não são suportados pela seção de concreto analisada. Por favor altera as dimensões da seção da viga ou reveja os esforços de cálculo para a estrutura.")
			else:
				kx_viga = (1 - math.sqrt(1 - 2*kmd_viga))/0.8
				kz_viga = 1 - 0.4*kx_viga
				as_viga = (mk_viga * 1.4 * 1000)/(kz_viga * (d_viga/100) * fyd_viga)

				as_sobre_apoio_viga = as_viga/3
				if h_viga >= 60:
					as_pele = (0.1/100)*area_secao_viga*100
				else:
					as_pele = 0

				as_max_viga = (4/100)*area_secao_viga*100

				if fck_viga == 20:
					taxa_aco_viga_retangular = 0.15/100
				elif fck_viga == 25:
					taxa_aco_viga_retangular = 0.15/100
				elif fck_viga == 30:
					taxa_aco_viga_retangular = 0.173/100
				elif fck_viga == 35:
					taxa_aco_viga_retangular = 0.201/100
				elif fck_viga == 40:
					taxa_aco_viga_retangular = 0.203/100
				elif fck_viga == 45:
					taxa_aco_viga_retangular = 0.259/100
				elif fck_viga == 50:
					taxa_aco_viga_retangular = 0.288/100

				as_min_viga = taxa_aco_viga_retangular * area_secao_viga*100


				if kx_viga < 0:
					dominio_viga = 'Domínio 1'
				elif kx_viga > 0 and kx_viga <0.259:
					dominio_viga = 'Domínio 2'
				elif kx_viga > 0.259 and kx_viga <0.45:
					dominio_viga = 'Domínio 3 - Dúctil'
				elif kx_viga > 0.45 and kx_viga <0.63:
					dominio_viga = 'Domínio 3 - Não Dúctil'
				elif (kx_viga > 0.628 and kx_viga <1):
					dominio_viga = 'Domínio 4a'
				elif (kx_viga > 0.438 and kx_viga <1) and (fyk_viga == 600):
					dominio_viga = 'Domínio 4a'
				else:
					dominio_viga = 'Domínio 4b'

				kmd_viga = self.truncar(kmd_viga)
				kx_viga = self.truncar(kx_viga)
				kz_viga = self.truncar(kz_viga)

				print('kmd_viga: ',kmd_viga)
				print('kx_viga: ',kx_viga)
				print('kz_viga: ',kz_viga)
				print('as_viga: ',as_viga)
				print('as_sobre_apoio_viga: ',as_sobre_apoio_viga)
				print('as_max_viga: ',as_max_viga)
				print('as_min_viga',as_min_viga)

				#-------------------------------------- saida de dados ------------------------------------------------
				self.lineEdit_6.setText(str(round(mk_viga*1.4,ndigits=4)))
				self.lineEdit_13.setText(dominio_viga)
				self.lineEdit_7.setText(str(kmd_viga))
				self.lineEdit_8.setText(str(kx_viga))
				self.lineEdit_9.setText(str(kz_viga))

				self.lineEdit_10.setText(str(round(as_viga,ndigits=4)))
				self.lineEdit_11.setText(str(round(as_sobre_apoio_viga,ndigits=4)))
				self.lineEdit_12.setText(str(round(as_pele,ndigits=4)))
				self.lineEdit_14.setText(str(round(as_max_viga,ndigits=4)))
				self.lineEdit_20.setText(str(round(as_min_viga,ndigits=4)))

				#-------------------------------------------------------------------------------------------------
				if (dominio_viga == 'Domínio 4a') or (dominio_viga == 'Domínio 4b'):
					QMessageBox.about(self, "Atenção", "Domínio de cálculo 4, recomenda-se utilizar, em seção retangular, armadura dupla ou seção tê para contenção dos esforços de compressão do concreto.")

				if as_viga > as_max_viga:
					QMessageBox.about(self, "Atenção", "Área Total calculada superior a Área Máxima especificada para a seção da viga.")
				if as_viga < as_min_viga:
					QMessageBox.about(self, "Atenção", "Área Total calculada inferior a Área Mínima especificada para a seção da viga.")

				self.calcular_viga_cortante()


		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes!")

	

	def calcular_viga_dupla(self):
		mk_viga = self.lineEdit.text()
		vk_viga = self.lineEdit_2.text()
		bw_viga = self.lineEdit_15.text()
		h_viga = self.lineEdit_16.text()
		d_viga = self.lineEdit_17.text()

		if (mk_viga != '0' and vk_viga != '0' and bw_viga != '0' and h_viga != '0' and d_viga != '0'):
			fck_viga = float(self.comboBox.currentText())
			fcd_viga = fck_viga/1.4
			fyk_viga = float(self.comboBox_2.currentText())
			fyd_viga = fyk_viga/1.15

			mk_viga = float(self.lineEdit.text())
			vk_viga = float(self.lineEdit_2.text())
			bw_viga = float(self.lineEdit_15.text())
			h_viga = float(self.lineEdit_16.text())
			d_viga = float(self.lineEdit_17.text())

			d_linha_viga = h_viga - d_viga
			self.lineEdit_27.setText(str(round(d_linha_viga, ndigits=4)))

			xis_dominio = float(self.lineEdit_35.text())

			d_min_viga = math.sqrt((mk_viga*1.4*1000)/((bw_viga/100) * (fcd_viga*1000000) * (0.68*xis_dominio - 0.272*(xis_dominio**2))))

			x_lim_viga = xis_dominio * (d_viga/100)

			momento_lim_viga = 0.68 * (bw_viga/100) * (fcd_viga*1000) * x_lim_viga*((d_viga/100) - 0.4*x_lim_viga)

			print('d_min_viga: ',d_min_viga)
			print('x_lim_viga: ',x_lim_viga)
			print('momento_lim_viga: ',momento_lim_viga)

			if d_min_viga < (h_viga/100):
				self.lineEdit_36.setText(str(round(d_min_viga, ndigits=5)))
				self.lineEdit_18.setText(str(round(x_lim_viga, ndigits=5)))
				QMessageBox.about(self, "Observação", "A altura atual da viga é maior que a altura útil mínima, calcule como simplesmente armada")

			else:

				momento_lim_viga = 0.68 * (bw_viga/100) * (fcd_viga*1000) * x_lim_viga*((d_viga/100) - 0.4*x_lim_viga)
				momento_2_viga = (mk_viga*1.4) - momento_lim_viga

				as_compressao_viga = (momento_2_viga * 1000)/(((d_viga/100) - (d_linha_viga/100))*(fyd_viga))
				#as_tracao_viga = ((momento_lim_viga * 1000)/((1 - 0.4*x_lim_viga)*(d_viga/100)*fyd_viga))
				as_tracao_viga = ((momento_lim_viga * 1000)/((1 - 0.4*xis_dominio)*(d_viga/100)*fyd_viga))

				as_tracao_viga = as_tracao_viga + as_compressao_viga

				as_total_viga = as_tracao_viga + as_compressao_viga

				as_sobre_apoio_viga = as_tracao_viga/3

				area_secao_viga = bw_viga * h_viga
				if h_viga >= 60:
					as_pele = (0.1/100)*area_secao_viga*100
				else:
					as_pele = 0

				if fck_viga == 20:
					taxa_aco_viga_retangular = 0.15/100
				elif fck_viga == 25:
					taxa_aco_viga_retangular = 0.15/100
				elif fck_viga == 30:
					taxa_aco_viga_retangular = 0.173/100
				elif fck_viga == 35:
					taxa_aco_viga_retangular = 0.201/100
				elif fck_viga == 40:
					taxa_aco_viga_retangular = 0.203/100
				elif fck_viga == 45:
					taxa_aco_viga_retangular = 0.259/100
				elif fck_viga == 50:
					taxa_aco_viga_retangular = 0.288/100

				as_max_viga = (4/100)*area_secao_viga*100
				as_min_viga = taxa_aco_viga_retangular * area_secao_viga*100


				print('momento_lim_viga: ',momento_lim_viga)
				print('momento_2_viga: ',momento_2_viga)
				print('as_compressao_viga: ',as_compressao_viga)
				print('as_tracao_viga: ',as_tracao_viga)


				#------------------------------------------ saida de dados --------------------------------------------------
				self.lineEdit_36.setText(str(round(d_min_viga, ndigits=5)))
				self.lineEdit_18.setText(str(round(x_lim_viga, ndigits=5)))
				self.lineEdit_26.setText(str(round(momento_lim_viga, ndigits=5)))
				self.lineEdit_19.setText(str(round(momento_2_viga, ndigits=5)))

				self.lineEdit_22.setText(str(round(as_compressao_viga, ndigits=5)))
				self.lineEdit_28.setText(str(round(as_tracao_viga, ndigits=5)))
				self.lineEdit_23.setText(str(round(as_sobre_apoio_viga, ndigits=5)))
				self.lineEdit_24.setText(str(round(as_pele, ndigits=5)))
				self.lineEdit_38.setText(str(round(as_total_viga, ndigits=2)))
				self.lineEdit_25.setText(str(round(as_max_viga, ndigits=2)))
				self.lineEdit_29.setText(str(round(as_min_viga, ndigits=2)))
				#------------------------------------------ ------------- --------------------------------------------------
				
				if as_total_viga > as_max_viga:
					QMessageBox.about(self, "Atenção", "Área Total calculada superior a Área Máxima especificada para a seção da viga.")
				if as_total_viga < as_min_viga:
					QMessageBox.about(self, "Atenção", "Área Total calculada inferior a Área Mínima especificada para a seção da viga.")

				self.calcular_viga_cortante()
				
		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes!")




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



class Carga_Adicional(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = loadUi('lajes_carg_adicional.ui',self)
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

class Sapatas(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = loadUi('sapatas_alt.ui',self)
		self.load_signals()
		self.setWindowTitle('Navier - Sapatas')

	def load_signals(self):
		print('sapatas carregado')
		self.pushButton_6.clicked.connect(self.calcular_sapata)
		self.pushButton.clicked.connect(self.gerar_dim_sapata)

	def arredondar_cinco(self, numero):
		numero = round(numero, ndigits=2)
		numero = 100*numero
		resto = numero%5
		while resto != 0:
		    numero += 1
		    resto = numero%5
		    print('numero:',numero,' - resto: ',resto)

		numero = numero/100
		return numero

	def calcular_sapata(self):

		nk = float(self.lineEdit_3.text())
		momento_x_sapata = float(self.lineEdit_4.text())
		momento_y_sapata = float(self.lineEdit_5.text())
		x_pilar = float(self.lineEdit.text())
		y_pilar = float(self.lineEdit_2.text())
		tensao_adm_solo = float(self.lineEdit_35.text())
		fator_solo = float(self.lineEdit_13.text())

		base_y_sapata = float(self.lineEdit_10.text())
		base_x_sapata = float(self.lineEdit_9.text())
		h_total = float(self.lineEdit_11.text())
		h_0 = float(self.lineEdit_12.text())

		y_sapata = float(self.lineEdit_9.text())
		x_sapata = float(self.lineEdit_10.text())
		h_total = float(self.lineEdit_11.text())
		h_0 = float(self.lineEdit_12.text())

		if (nk != 0 and x_pilar != 0 and y_pilar != 0 and tensao_adm_solo != 0 and fator_solo != 0 and base_y_sapata != 0 and base_x_sapata != 0 and h_total != 0 and h_0 != 0):
			if (x_sapata < 0.6 or y_sapata < 0.6):
				QMessageBox.about(self, "Erro de Entrada", "As sapatas não podem apresentar lados menores de 60 cm, conforme a NBR 6122")
			else:
				fck_sapata = float(self.comboBox.currentText())
				fcd_sapata = fck_sapata / 1.4
				fyk_sapata = float(self.comboBox_2.currentText())
				fyd_sapata = fyk_sapata / 1.15
				nk = float(self.lineEdit_3.text())
				momento_x_sapata = float(self.lineEdit_4.text())
				momento_y_sapata = float(self.lineEdit_5.text())
				tensao_adm_solo = float(self.lineEdit_35.text())
				fator_solo = float(self.lineEdit_13.text())
				angulo_dissp_sapata = float(self.spinBox.value())

				angulo_dissp_sapata = (angulo_dissp_sapata / 180)* 3.14

				x_pilar = float(self.lineEdit.text())/100
				y_pilar = float(self.lineEdit_2.text())/100

				y_sapata = float(self.lineEdit_9.text())
				x_sapata = float(self.lineEdit_10.text())
				h_total = float(self.lineEdit_11.text())
				h_0 = float(self.lineEdit_12.text())

				if (momento_x_sapata != 0 and momento_y_sapata == 0) or (momento_x_sapata == 0 and momento_y_sapata != 0):
					fator_acrescimo_dimensoes = 1.05
				elif (momento_x_sapata != 0 and momento_y_sapata != 0):
					fator_acrescimo_dimensoes = 1.103
				else:
					fator_acrescimo_dimensoes = 1.0

				x_sapata = round(x_sapata * fator_acrescimo_dimensoes, ndigits=4)
				y_sapata = round(y_sapata * fator_acrescimo_dimensoes, ndigits=4)

				wx = x_sapata * (y_sapata**2)/6
				wy = y_sapata * (x_sapata**2)/6

				mw_x = (momento_x_sapata/wx)*1000
				mw_y = (momento_y_sapata/wy)*1000

				tensao_sapata = (fator_solo*nk*1000)/(x_sapata*y_sapata)
				tensao_max_sapata = tensao_sapata + mw_x + mw_y
				tensao_min_sapata = tensao_sapata - mw_x - mw_y

				nk_equiv = (x_sapata * y_sapata * tensao_max_sapata)/fator_solo
				area_sapata = round(fator_solo * ((nk*1000)/(tensao_adm_solo*1000000)),ndigits=6)

				ca_sapata = (x_sapata - x_pilar)/2
				cb_sapata = (y_sapata - y_pilar)/2
				h_rig_x = 2/3 * ca_sapata
				h_rig_y = 2/3 * cb_sapata

				h_mincis = (1.4 * nk_equiv)/(2*(x_pilar+y_pilar)*0.27*(1-(fck_sapata/250))*(fcd_sapata*1000000))
				if h_mincis < 0.40:
					h_mincis = 0.40
				if h_total < h_mincis:
					h_total = h_mincis

				braco_alavanca_sapata = h_total - 0.05

				h0a = h_total - ca_sapata * math.tan(angulo_dissp_sapata)
				h0b = h_total - cb_sapata * math.tan(angulo_dissp_sapata)

				#h0 = round(h0a, ndigits=2)
				#if h0a < h0b:
				#	h0 = round(h0b, ndigits=2)

				volume_concreto_sapata = (h_total-h_0)/(3*(x_sapata*y_sapata+x_pilar*y_pilar+math.sqrt(x_sapata*y_sapata*x_pilar*y_pilar))+x_sapata*y_sapata*h_0)

				tracao_x_sapata = 1.1 * nk_equiv * (x_sapata - x_pilar)/(8 * braco_alavanca_sapata)
				tracao_y_sapata = 1.1 * nk_equiv * (y_sapata - y_pilar)/(8 * braco_alavanca_sapata)
				as_x_sapata = (1.4 * tracao_x_sapata)/(fyd_sapata)
				as_y_sapata = (1.4 * tracao_y_sapata)/fyd_sapata

				taxa_aco_sapata = (0.078 * (fck_sapata)**(2/3))/fyd_sapata
				
				if taxa_aco_sapata <= 0.0015:
					taxa_aco_sapata = 0.0015

				as_x_min_laje = 0.67 * taxa_aco_sapata * h_mincis * x_sapata
				as_y_min_laje = 0.67 * taxa_aco_sapata * h_mincis * y_sapata

				print('x_sapata: ',x_sapata)
				print('y_sapata: ',y_sapata)

				print('wx: ',wx)
				print('wy: ',wy)
				print('mw_x: ',mw_x)
				print('mw_y: ',mw_y)
				print('tensao_max_sapata: ',tensao_max_sapata)
				print('tensao_min_sapata: ',tensao_min_sapata)
				print('nk_equiv: ',nk_equiv)
				print('ca_sapata: ',ca_sapata)
				print('cb_sapata: ',cb_sapata)
				print('h0a: ',h0a)
				print('h0b: ',h0b)
				print('h_mincis: ',h_mincis)
				#print('h0: ',h0)
				print('h_total',h_total)
				print('-------------------------------------\n')

				#-------------------------------------- saida dos dados --------------------------------------------------
				self.lineEdit_11.setText(str(h_total))
				#self.lineEdit_12.setText(str(h0))

				self.lineEdit_15.setText(str(area_sapata))
				self.lineEdit_16.setText(str(round(wx, ndigits=6)))
				self.lineEdit_17.setText(str(round(wy, ndigits=6)))
				self.lineEdit_18.setText(str(round(nk_equiv, ndigits=4)))
				self.lineEdit_19.setText(str(round(tensao_max_sapata/1000000, ndigits=4)))
				self.lineEdit_20.setText(str(round(tensao_min_sapata/1000000, ndigits=4)))
				self.lineEdit_21.setText(str(round(ca_sapata*100, ndigits=4)))
				self.lineEdit_22.setText(str(round(cb_sapata*100, ndigits=4)))

				self.lineEdit_23.setText(str(round(h_rig_x*100, ndigits=4)))
				self.lineEdit_24.setText(str(round(h_rig_y*100, ndigits=4)))
				self.lineEdit_25.setText(str(round(h_mincis*100, ndigits=4)))
				self.lineEdit_26.setText(str(round(h0a*100, ndigits=4)))
				self.lineEdit_28.setText(str(round(h0b*100, ndigits=4)))
				self.lineEdit_27.setText(str(round(volume_concreto_sapata, ndigits=4)))

				self.lineEdit_14.setText(str(round(tracao_x_sapata/1000, ndigits=4)))
				self.lineEdit_29.setText(str(round(tracao_y_sapata/1000, ndigits=4)))
				self.lineEdit_30.setText(str(round(as_x_sapata, ndigits=4)))
				self.lineEdit_31.setText(str(round(as_y_sapata, ndigits=4)))

				self.lineEdit_32.setText(str(round(taxa_aco_sapata, ndigits=7)))
				self.lineEdit_33.setText(str(round(as_x_min_laje*1000000, ndigits=4)))
				self.lineEdit_34.setText(str(round(as_y_min_laje*1000000, ndigits=4)))

		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes")



	def gerar_dim_sapata(self):

		nk = float(self.lineEdit_3.text())
		momento_x_sapata = float(self.lineEdit_4.text())
		momento_y_sapata = float(self.lineEdit_5.text())
		x_pilar = float(self.lineEdit.text())
		y_pilar = float(self.lineEdit_2.text())
		tensao_adm_solo = float(self.lineEdit_35.text())
		fator_solo = float(self.lineEdit_13.text())


		if (nk != 0 and x_pilar != 0 and y_pilar != 0 and tensao_adm_solo != 0 and fator_solo != 0):
		
			fck_sapata = float(self.comboBox.currentText())
			fcd_sapata = fck_sapata / 1.4
			fyk_sapata = float(self.comboBox_2.currentText())
			fyd_sapata = fyk_sapata / 1.15
			nk = float(self.lineEdit_3.text())
			momento_x_sapata = float(self.lineEdit_4.text())
			momento_y_sapata = float(self.lineEdit_5.text())
			tensao_adm_solo = float(self.lineEdit_35.text())
			fator_solo = float(self.lineEdit_13.text())
			angulo_dissp_sapata = float(self.spinBox.value())

			angulo_dissp_sapata = (angulo_dissp_sapata / 180)* 3.14

			x_pilar = float(self.lineEdit.text())/100
			y_pilar = float(self.lineEdit_2.text())/100

			area_sapata = round(fator_solo * ((nk*1000)/(tensao_adm_solo*1000000)),ndigits=6)

			y_sapata = 0.5*(y_pilar - x_pilar) + math.sqrt(0.25*((y_pilar - x_pilar)**2)+area_sapata)

			x_sapata = area_sapata/y_sapata

			if (momento_x_sapata != 0 and momento_y_sapata == 0) or (momento_x_sapata == 0 and momento_y_sapata != 0):
				fator_acrescimo_dimensoes = 1.05
			elif (momento_x_sapata != 0 and momento_y_sapata != 0):
				fator_acrescimo_dimensoes = 1.103
			else:
				fator_acrescimo_dimensoes = 1.0

			x_sapata = round(x_sapata * fator_acrescimo_dimensoes, ndigits=4)
			y_sapata = round(y_sapata * fator_acrescimo_dimensoes, ndigits=4)

			if x_sapata < 0.6:
				x_sapata = 0.6
			if y_sapata < 0.6:
				y_sapata = 0.6
			print(x_sapata,'<--------------------------------------------------')
			wx = x_sapata * (y_sapata**2)/6
			wy = y_sapata * (x_sapata**2)/6

			mw_x = (momento_x_sapata/wx)*1000
			mw_y = (momento_y_sapata/wy)*1000

			tensao_sapata = (fator_solo*nk*1000)/(x_sapata*y_sapata)
			tensao_max_sapata = tensao_sapata + mw_x + mw_y
			tensao_min_sapata = tensao_sapata - mw_x - mw_y

			x_sapata = self.arredondar_cinco(x_sapata)
			y_sapata = self.arredondar_cinco(y_sapata)
			if x_sapata < 0.6:
				x_sapata = 0.6
			if y_sapata < 0.6:
				y_sapata = 0.6

			nk_equiv = (x_sapata * y_sapata * tensao_max_sapata)/fator_solo

			ca_sapata = (x_sapata - x_pilar)/2
			cb_sapata = (y_sapata - y_pilar)/2
			h_rig_x = 2/3 * ca_sapata
			h_rig_y = 2/3 * cb_sapata

			h_total = h_rig_x
			if h_total < h_rig_y:
				h_total = h_rig_y

			h_mincis = (1.4 * nk_equiv)/(2*(x_pilar+y_pilar)*0.27*(1-(fck_sapata/250))*(fcd_sapata*1000000))
			if h_mincis < 0.40:
				h_mincis = 0.40
			h_mincis = round(h_mincis, ndigits=4)

			if h_total < h_mincis:
				h_total = h_mincis

			h_total = self.arredondar_cinco(h_total)

			h0a = h_total - ca_sapata * math.tan(angulo_dissp_sapata)
			h0b = h_total - cb_sapata * math.tan(angulo_dissp_sapata)
			h0_prerrogativo = h_total/3
			tangente_angulo = math.tan(angulo_dissp_sapata)
			h0 = round(h0a, ndigits=2)
			if h0a < h0b:
				h0 = round(h0b, ndigits=2)
			elif h0b < h0_prerrogativo:
				h0 = h0_prerrogativo
			if h0 < 0.25:
				h0 = 0.25
			h0 = self.arredondar_cinco(h0)

			volume_concreto_sapata = ((h_total-h0)/3*(x_sapata*y_sapata+x_pilar*y_pilar+math.sqrt(x_sapata*y_sapata*x_pilar*y_pilar)))+(x_sapata*y_sapata*h0)

			braco_alavanca_sapata = h_total - 0.05

			tracao_x_sapata = 1.1 * nk_equiv * (x_sapata - x_pilar)/(8 * braco_alavanca_sapata)
			tracao_y_sapata = 1.1 * nk_equiv * (y_sapata - y_pilar)/(8 * braco_alavanca_sapata)
			as_x_sapata = (1.4 * tracao_x_sapata)/(fyd_sapata)
			as_y_sapata = (1.4 * tracao_y_sapata)/fyd_sapata

			taxa_aco_sapata = (0.078 * (fck_sapata)**(2/3))/fyd_sapata

			if taxa_aco_sapata <= 0.0015:
				taxa_aco_sapata = 0.0015

			as_x_min_laje = 0.67 * taxa_aco_sapata * h_total * x_sapata
			as_y_min_laje = 0.67 * taxa_aco_sapata * h_total * y_sapata

			print('x_sapata: ',x_sapata)
			print('y_sapata: ',y_sapata)

			print('wx: ',wx)
			print('wy: ',wy)
			print('mw_x: ',mw_x)
			print('mw_y: ',mw_y)
			print('tensao_max_sapata: ',tensao_max_sapata)
			print('tensao_min_sapata: ',tensao_min_sapata)
			print('nk_equiv: ',nk_equiv)
			print('ca_sapata: ',ca_sapata)
			print('cb_sapata: ',cb_sapata)
			print('h0a: ',h0a)
			print('h0b: ',h0b)
			print('h_mincis: ',h_mincis)
			print('h0: ',h0)
			print('tangente_angulo: ',tangente_angulo)
			print('----------')
			print('h_total: ',h_total)
			print('tracao_x_sapata: ',tracao_x_sapata)
			print('tracao_y_sapata: ',tracao_y_sapata)
			print('as_x_sapata: ',as_x_sapata)
			print('as_y_sapata: ',as_y_sapata)
			print('taxa_aco_sapata: ',taxa_aco_sapata)
			print('as_x_min_laje: ',as_x_min_laje)
			print('as_y_min_laje: ',as_y_min_laje)
			print('-------------------------------------\n')
			#------------------------------ saida de dados ---------------------------------------------
			self.lineEdit_9.setText(str(y_sapata))
			self.lineEdit_10.setText(str(x_sapata))
			self.lineEdit_15.setText(str(area_sapata))

			self.lineEdit_11.setText(str(round(h_total, ndigits=4)))
			self.lineEdit_12.setText(str(round(h0, ndigits=4)))


			self.lineEdit_15.setText(str(area_sapata))
			self.lineEdit_16.setText(str(round(wx, ndigits=6)))
			self.lineEdit_17.setText(str(round(wy, ndigits=6)))
			self.lineEdit_18.setText(str(round(nk_equiv, ndigits=4)))
			self.lineEdit_19.setText(str(round(tensao_max_sapata/1000000, ndigits=4)))
			self.lineEdit_20.setText(str(round(tensao_min_sapata/1000000, ndigits=4)))
			self.lineEdit_21.setText(str(round(ca_sapata*100, ndigits=4)))
			self.lineEdit_22.setText(str(round(cb_sapata*100, ndigits=4)))

			self.lineEdit_23.setText(str(round(h_rig_x*100, ndigits=4)))
			self.lineEdit_24.setText(str(round(h_rig_y*100, ndigits=4)))
			self.lineEdit_25.setText(str(round(h_mincis*100, ndigits=4)))
			self.lineEdit_26.setText(str(round(h0a*100, ndigits=4)))
			self.lineEdit_28.setText(str(round(h0b*100, ndigits=4)))
			self.lineEdit_27.setText(str(round(volume_concreto_sapata, ndigits=4)))

			self.lineEdit_14.setText(str(round(tracao_x_sapata/1000, ndigits=4)))
			self.lineEdit_29.setText(str(round(tracao_y_sapata/1000, ndigits=4)))
			self.lineEdit_30.setText(str(round(as_x_sapata, ndigits=4)))
			self.lineEdit_31.setText(str(round(as_y_sapata, ndigits=4)))

			self.lineEdit_32.setText(str(round(taxa_aco_sapata, ndigits=7)))
			self.lineEdit_33.setText(str(round(as_x_min_laje*1000000, ndigits=4)))
			self.lineEdit_34.setText(str(round(as_y_min_laje*1000000, ndigits=4)))

		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes")


class App2(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(400, 100, 200, 200)
		self.editor = QtWidgets.QTextEdit('Achou', self)
		self.editor.setGeometry(20, 20, 160, 160)

#---------------------------------------------- Janelas de Detalhamento ----------------------------------------------------
tabela_bitolas_ferro = [
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

'''class Detalhar_viga(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('detalhamento_vigas.ui',self)
		self.setWindowTitle('Navier - Vigas - Detalhamento')
	def load_signals(self):
		print('inicializado')
		self.pushButton.clicked.connect(self.calcular_area)
		self.pushButton_2.clicked.connect(self.limpar_detalhamento)
		
		#pg.plot(x=[0,1,2,3,4], y=[0,1,2,3,4]**2 )
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

		self.widget.setTitle('Nº barras/Bitola')
		self.widget.showGrid(x=True,y=True,alpha=1)


	def calcular_area(self):
		area_aco = self.lineEdit.text()
		base = self.lineEdit_2.text()
		altura = self.lineEdit_3.text()
		d_agreg = self.lineEdit_4.text()

		if (area_aco != '0' and base != '0' and altura != '0' and d_agreg != '0'):

			self.widget.clear()
			area_aco = float(self.lineEdit.text())
			base = float(self.lineEdit_2.text())
			altura = float(self.lineEdit_3.text())
			cobrimento = float(self.comboBox.currentText())
			x = []
			y = []
			z = []
			cont = 0
			for i in tabela_bitolas_ferro:
				n_barras = float(area_aco/i[1])
				print('bitola: ',i[0],' - nº barras: ',n_barras)

				self.tableWidget.setItem(cont,2, QTableWidgetItem(str(round(n_barras, ndigits=2))))
				self.tableWidget.setItem(cont,3, QTableWidgetItem(str(round(n_barras +0.5)+1)))

				x.append(i[0])
				y.append(round(n_barras +0.5)+1)

				bitola = x[cont]
				n_barras = (round(n_barras +0.5)+1)

				espass_horizontal = (round(base - 2*(cobrimento+0.5) - n_barras*(bitola/10), ndigits=2))/(n_barras-1)
				z.append(round(espass_horizontal,ndigits=2))
				self.tableWidget.setItem(cont,4, QTableWidgetItem(str(espass_horizontal)))

				cont +=1

			print(x)
			print(y)
			print(z)
			
			self.widget.plot(x=x,y=y,pen=(3))

			self.calcular_espacamentos()

		else:
			QMessageBox.about(self, "Falta de Dados", "Por favor insira dados consistentes!")


	def calcular_espacamentos(self):
		bitola = float(self.comboBox_2.currentText())
		d_agreg = float(self.lineEdit_4.text())

		s_horizontal = max(2, (bitola/10), 1.2*d_agreg)
		s_vertical = max(2, (bitola/10), 0.5*d_agreg)

		#------------------------------- saida de dados ----------------------------------
		self.lineEdit_5.setText(str(s_horizontal))
		self.lineEdit_6.setText(str(s_vertical))

	def limpar_detalhamento(self):
		self.widget.clear()
		self.lineEdit.setText(str('0'))
		self.lineEdit_2.setText(str('0'))
		self.lineEdit_3.setText(str('0'))
		self.lineEdit_5.setText(str('0'))
		self.lineEdit_4.setText(str('0'))
'''

tabela_bitolas_ferro = [
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
		#self.show()
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
			for i in tabela_bitolas_ferro:
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



class Tabela_Bitolas(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = loadUi('bitolas_ferros.ui',self)
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		self.setWindowTitle('Navier - Tabela de Bitolas')

class Tabela_Classe_Agressividade(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.load_ui()
		self.load_signals()

	def load_ui(self):
		self.ui = loadUi('class_agres.ui',self)
		self.setWindowTitle('Navier - Classes de Agressividade e Cobrimentos Mínimos')
	def load_signals(self):
		print('inicializado')
		header = self.tableWidget.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

		self.tableWidget.setSpan(0, 0, 1, 4)

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
	inicio = Inicio()
	vigas = Vigas()
	detalhar_vigas = Detalhar_viga()
	pilares = Pilares()
	pilares_areas_aco = Pilar_area_aco()
	#pilares.show()
	#vigas.show()
	lajes = Lajes()
	#lajes.show()
	sapatas = Sapatas()
	#sapatas.show()
	carga_adicional = Carga_Adicional()
	tabela_classe_agressividade = Tabela_Classe_Agressividade()
	tabela_bitolas = Tabela_Bitolas()

	app.exec_()