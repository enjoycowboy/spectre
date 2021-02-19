# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectr.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(721, 721)
        MainWindow.setMinimumSize(QtCore.QSize(721, 721))
        MainWindow.setMaximumSize(QtCore.QSize(721, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 610, 701, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 590, 59, 16))
        self.label.setObjectName("label")
        self.screen = MplWidget(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(0, 0, 721, 551))
        self.screen.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.screen.setMouseTracking(True)
        self.screen.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.screen.setAutoFillBackground(False)
        self.screen.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.screen.setObjectName("screen")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 560, 701, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scan = QtWidgets.QPushButton(self.layoutWidget)
        self.scan.setObjectName("scan")
        self.horizontalLayout.addWidget(self.scan)
        self.load = QtWidgets.QPushButton(self.layoutWidget)
        self.load.setObjectName("load")
        self.horizontalLayout.addWidget(self.load)
        self.slice = QtWidgets.QPushButton(self.layoutWidget)
        self.slice.setObjectName("slice")
        self.horizontalLayout.addWidget(self.slice)
        self.measure = QtWidgets.QPushButton(self.layoutWidget)
        self.measure.setObjectName("measure")
        self.horizontalLayout.addWidget(self.measure)
        self.report = QtWidgets.QPushButton(self.layoutWidget)
        self.report.setAutoDefault(False)
        self.report.setDefault(False)
        self.report.setFlat(False)
        self.report.setObjectName("report")
        self.horizontalLayout.addWidget(self.report)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.slice.clicked.connect(MainWindow.invokeSlicer)
        self.measure.clicked.connect(MainWindow.measureMode)
        self.scan.clicked.connect(MainWindow.spawnOptions)
        self.load.clicked.connect(MainWindow.browseSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectrox"))
        self.label.setText(_translate("MainWindow", "Debugger"))
        self.scan.setText(_translate("MainWindow", "Scan Now"))
        self.load.setText(_translate("MainWindow", "Load Scan"))
        self.slice.setText(_translate("MainWindow", "Slice"))
        self.measure.setText(_translate("MainWindow", "Measure"))
        self.report.setText(_translate("MainWindow", "Report"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())