from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import spectr
import gui

class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
	def __init__ (self, parent=None):
		super(App, self).__init__(parent)
		self.setupUi(self)

def main():
	app = QApplication(sys.argv)
	form = App()
	form.show()
	app.exec_()

if __name__ == '__main__':
	main()