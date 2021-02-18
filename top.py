import scanSettings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog


import sys
import spectr
import mainWindow


class settingsDialog(QtWidgets.QDialog, scanSettings.Ui_ScanSettings):

	
	def __init__(self, parent=None):
		super(settingsDialog, self).__init__(parent)
		self.setupUi(self)
		self.values = []

	def getValues(self):
		return self.values
	def okay(self):
		self.values = [self.timeSlider.value(), self.gainSlider.value() * 10,
			int(str(self.comboBox.currentText()))]
		self.accept()

	def cancel(self):
		self.close()

class App(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
	def __init__ (self, parent=None):
		super(App, self).__init__(parent)
		self.setupUi(self)
		
		#slots
	def browseSlot(self):
		self.debugPrint("clicked on load file")
		fname = QFileDialog.getOpenFileName()
		self.debugPrint("file to be loaded: " + str(fname))

	def invokeSlicer(self):
		self.debugPrint("slicer invoked")

	def spawnOptions(self):
		self.debugPrint("options spawned")
		self.dialog = settingsDialog()
		self.dialog.show()
		if (self.dialog.exec_()):
			self.debugPrint(str(self.dialog.values))

		
		

	def debugPrint(self, msg):
		self.textBrowser.append(msg)

	def measureMode(self):
		self.debugPrint("measure moded")



#metodo pra instanciar a classe da janela de configuração





def main():
	app = QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
