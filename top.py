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
import numpy as np
from pyqtgraph.Qt import QtCore,QtGui
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

	win = pg.GraphicsLayoutWidget()
	p1 = win.addPlot(title="")
	roi = pg.ROI([0,0],[3,3])
	data = np.zeros(2)
	img = pg.ImageItem()

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
		App.data = spectr.fileparse(fname)
		App.img.setImage(App.data)
		App.p1.addItem(App.img)
		App.p1.autoRange()
		App.updatePlot(self)
		self.debugPrint("reached end of function")
	

	def invokeSlicer(self):
		App.win.nextRow()
		App.p2 = App.win.addPlot(colspan=2)
		self.debugPrint("slicer invoked")
		App.roi.addScaleHandle([0.5, 1], [0.5, 0.5])
		App.roi.addScaleHandle([0, 0.5], [0.5, 0.5])
		App.p1.addItem(App.roi)
		App.roi.setZValue(10)  # make sure ROI is drawn above image

	def spawnOptions(self):
		
		App.p2.setMaximumHeight(250)
		App.win.resize(800,800)
		App.win.show()
		self.debugPrint("options spawned")
		self.dialog = settingsDialog()
		self.dialog.show()
		if (self.dialog.exec_()):
			self.debugPrint(str(self.dialog.values))

	def debugPrint(self, msg):
		self.textBrowser.append(msg)

	def measureMode(self,):
		self.debugPrint("measure mode")
		# """Show the position, pixel, and value under the mouse cursor.
		# """
		# if event.isExit():
		# 	App.p1.setTitle("")
		# 	return
		# pos = event.pos()
		# i, j = pos.y(), pos.x()
		# i = int(np.clip(i, 0, data.shape[0] - 1))
		# j = int(np.clip(j, 0, data.shape[1] - 1))
		# val = data[i, j]
		# ppos = img.mapToParent(pos)
		# x, y = ppos.x(), ppos.y()
		# p1.setTitle("pos: (%0.1f, %0.1f)  pixel: (%d, %d)  value: %g" %
		# 			(x, y, i, j, val))	

	def updatePlot(self):
		selected = App.roi.getArrayRegion(App.data, App.img)
		App.p2.plot(selected.mean(axis=0), clear=True)

def main():
	app = QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()
