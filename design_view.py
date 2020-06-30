# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(60, 20, 571, 371))
        self.tableView.setObjectName("tableView")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(650, 80, 41, 31))
        self.toolButton.setObjectName("toolButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 510, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineName.setGeometry(QtCore.QRect(60, 410, 431, 20))
        self.lineName.setObjectName("lineName")
        self.textDescription = QtWidgets.QTextEdit(self.centralwidget)
        self.textDescription.setGeometry(QtCore.QRect(60, 440, 431, 71))
        self.textDescription.setObjectName("textDescription")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 410, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 460, 51, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "@"))
        self.pushButton.setText(_translate("MainWindow", "Подать запрос"))
        self.label.setText(_translate("MainWindow", "ФИО"))
        self.label_2.setText(_translate("MainWindow", "Описание"))
