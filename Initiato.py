import socket


import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import design  # Это наш конвертированный файл дизайна

# SQL
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
#from base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import test_sqlAlchemy
#engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/tsrm', echo = True)
#print(engine)
#Base = declarative_base()


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.ui = design.Ui_MainWindow()
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.tableWidget.setColumnCount(5)
        self.updateButton.clicked.connect(self.getReqListServer)
        self.pushButton.clicked.connect(self.sendRequestServer)

    def test(self):
        data = []
        data.append(('Заполнить', 'QTableWidget'))
        data.append(('с данными', 'в Python'))
        data.append(('очень', 'просто'))
        self.tableWidget.setRowCount(4)
        self.ui = design.Ui_MainWindow()
        #self.textDescription.setText("TEST!!!")
        print(self.textDescription.toPlainText())# Получение текста из textEdit
        print(self.lineName.displayText())# Получение текста еиз lineEdit
        row = 0
        for tup in data:
            col = 0
            print("{} {}".format(col,row))
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                #self.tableWidget.setItem(row, col, cellinfo)
                self.tableWidget.setItem(row,col,cellinfo)
                col += 1
                #print(item)

            row += 1
    def getRequestList(self):
        Session = sessionmaker(bind=engine)
        s = Session()
        self.tableWidget.setRowCount(20)
        row = 0
        print("-----------------------------")
        Req = s.query(test_sqlAlchemy.Request).join(test_sqlAlchemy.Admin,
                                                    test_sqlAlchemy.Request.executor == test_sqlAlchemy.Admin.id)
        print(Req)
        for inst in Req:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(inst.registerTime)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(inst.decription))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(s.query(test_sqlAlchemy.Admin).get(inst.executor).name)))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(inst.status))
            print("{} | {} | {} | {} | {}".format(inst.id,inst.decription,inst.executor,inst.status, inst.registerTime))
            row += 1

    def sendRequest(self):
        textDesc = self.textDescription.toPlainText()
        userName = int(self.lineName.displayText())
        print(userName,textDesc)
        Session = sessionmaker(bind=engine)
        s = Session()
        #userID = int(s.query(test_sqlAlchemy.User).get)
        temp = test_sqlAlchemy.Request(userID=userName,description=textDesc)
        s.add(temp)
        s.commit()
        #self.getRequestList()

    def sendRequestServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        msg="111"+self.lineName.displayText()+"|"+self.textDescription.toPlainText()
        print(msg)
        s.send(msg.encode())
        #response = s.recv(1024)
        s.close()

    def getReqListServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        s.send("000".encode())
        response = s.recv(1024)
        msg = response.decode()
        self.tableWidget.setRowCount(int(msg))
        row = 0
        while response:
            response = s.recv(1024)
            msg = response.decode()
            print("Response server: " + msg)
            resp = msg.split("|")
            col = 0
            for inst in resp:
                print(inst)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(inst)))
                col += 1
            row += 1
        s.close()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


