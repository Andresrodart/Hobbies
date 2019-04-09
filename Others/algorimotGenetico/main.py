from PyQt5.QtWidgets import *
from algoGen import *

class MainWindow(QMainWindow):										#Ventana principal que hereda de QMainWindow
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setWindowTitle("Algoritmo Genético")
		windw = Window(self)
		windw.setMinimumSize(1,1)
		self.setCentralWidget(windw)
		self.miMetodo = None
	
	def on_button_archivo(self):
		fnme =  QFileDialog.getOpenFileName(self, 'Selecciona el archivo de reglas', 'c:\\',"Json Files (*.json)")	
		rules = {}
		with open(fnme[0], 'r') as inputFile:
			rules = json.load(inputFile)
		self.miMetodo = AlgoGen(rules)
		Res = ResultadoArchivo(self) 
		self.setCentralWidget(Res) 
	
	def on_button_salir(self):
		windw = Window(self)
		windw.setMinimumSize(1,1)
		self.setCentralWidget(windw)

class Window(QWidget):
	def __init__(self, parent):        
		super(Window, self).__init__(parent)
		self.parent().resize(250,100)
		self.layout = QVBoxLayout(self)
		self.button_archivo = QPushButton('Cargar Archivo')
		self.button_carga = QPushButton('Ingresar datos')
		self.layout.addWidget(self.button_archivo)
		self.layout.addWidget(self.button_carga)
		self.button_archivo.clicked.connect(self.parent().on_button_archivo)
		#self.button_carga.clicked.connect(self.parent().on_button_clicked_maestro)
		self.setLayout(self.layout)

class ResultadoArchivo(QWidget):
	def __init__(self, parent):        
		super(ResultadoArchivo, self).__init__(parent)
		self.__clean__()
		layoutRes = QWidget() 
		layoutRes.layout = QVBoxLayout(self)
		self.parent().resize(520 + 150,500)
		
		UpPanel = QWidget() 
		UpPanel.layout = QHBoxLayout(self) 
		
		ResRul = QWidget()
		ResRul.layout = QVBoxLayout(self)
		for item in self.parent().miMetodo.rules:
			ResRul.layout.addWidget(QLabel(item + ' = ' + str(self.parent().miMetodo.rules[item]), self))
		ResRul.setLayout(ResRul.layout)

		ResWid = QWidget()
		ResWid.layout = QVBoxLayout(self)
		LabelRes = QLabel('Resultado:', self)
		ResWid.layout.addWidget(LabelRes)
		ResWid.layout.addWidget(QLabel(''.join(self.parent().miMetodo.resultado[0]), self))
		for item in self.parent().miMetodo.resultado[1]:
			ResWid.layout.addWidget(QLabel(item + ' = ' + str(self.parent().miMetodo.resultado[1][item]), self))
		ResWid.setLayout(ResWid.layout)
		
		UpPanel.layout.addWidget(ResWid)
		UpPanel.layout.addWidget(ResRul)
		UpPanel.setLayout(UpPanel.layout)

		tableWidget = QTableWidget()
		tableWidget.setColumnCount(len(self.parent().miMetodo.iterations[0][0]))
		tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		
		for i, each in zip( range(len(self.parent().miMetodo.iterations)), self.parent().miMetodo.iterations):
			for one in each:
				rowPosition = tableWidget.rowCount()
				tableWidget.insertRow(rowPosition)
				for j, cell in zip(range(len(one)), one):
					try:
						tableWidget.setItem(rowPosition, j, QTableWidgetItem("{0:.4f}".format(cell)))
					except:
						tableWidget.setItem(rowPosition, j, QTableWidgetItem(cell))
			rowPosition = tableWidget.rowCount()
			tableWidget.insertRow(rowPosition)
		tableWidget.resizeColumnsToContents()
		
		rtrn = QPushButton("Regresar")
		rtrn.clicked.connect(self.parent().on_button_salir)
		
		layoutRes.layout.addWidget(UpPanel)
		layoutRes.layout.addWidget(tableWidget)
		layoutRes.layout.addWidget(rtrn)
		

		self.parent().setCentralWidget(layoutRes)
	
	def __clean__(self):
		try:
			for i in reversed(range(self.layout.count())): 
				self.layout.itemAt(i).widget().setParent(None)
		except:
			pass

if __name__ == '__main__':
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()
