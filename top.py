import scanSettings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

# import matplotlib

# matplotlib.use('QT5Agg')
import pyqtgraph as pg
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
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.setupUi(self)

	#	#slots
	def browseSlot(self):
		self.debugPrint("clicked on load file")
		ftype = "Scans (*.bin)"
		qfd = QFileDialog()
		path = "./"
		title = "Open File"
		browse = QFileDialog.getOpenFileName(qfd, title, path, ftype)
		self.debugPrint("Loading file: " + str(browse[0]))
		fname = str(browse[0])
		#self.scrdraw(fname)

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

	# def scrdraw(self, fname):
	# 	matplotlib.interactive(False)
	# 	fig, ax, cs = spectr.render(fname)	
	# 	self.screen.canvas.figure = fig
	# 	self.screen.canvas.draw()
		

def main():
	app = QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
