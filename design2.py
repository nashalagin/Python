# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designExecut.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 871, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(710, 410, 75, 23))
        self.updateButton.setObjectName("updateButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 410, 411, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineName.setObjectName("lineName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineName)
        self.linePhone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.linePhone.setObjectName("linePhone")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePhone)
        self.addUserButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.addUserButton.setObjectName("addUserButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addUserButton)
        self.addAdmButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.addAdmButton.setObjectName("addAdmButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addAdmButton)
        self.numReqBox = QtWidgets.QSpinBox(self.centralwidget)
        self.numReqBox.setGeometry(QtCore.QRect(650, 520, 42, 22))
        self.numReqBox.setObjectName("numReqBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 520, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 520, 71, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата рег."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Инициатор"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Статус"))
        self.updateButton.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "ФИО"))
        self.label_2.setText(_translate("MainWindow", "телефон"))
        self.addUserButton.setText(_translate("MainWindow", "Добавить как инициатора"))
        self.addAdmButton.setText(_translate("MainWindow", "Добавить как исполнителя"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))
        self.label_3.setText(_translate("MainWindow", "Номер заявки"))
