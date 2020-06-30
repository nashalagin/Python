import socket
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import design2  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design2.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.ui = design2.Ui_MainWindow()
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.tableWidget.setColumnCount(5)
        self.updateButton.clicked.connect(self.getReqListServer)
        self.addUserButton.clicked.connect(self.addUser)
        self.addAdmButton.clicked.connect(self.addAdmin)
        self.pushButton.clicked.connect(self.closeRequest)




    def getReqListServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        s.send("01".encode())
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

    def addUser(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        msg = "222" + self.lineName.displayText() + "|" + self.linePhone.displayText()
        print(msg)
        s.send(msg.encode())
        # response = s.recv(1024)
        s.close()
    def addAdmin(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        msg = "333" + self.lineName.displayText() + "|" + self.linePhone.displayText()
        print(msg)
        s.send(msg.encode())
        # response = s.recv(1024)
        s.close()
    def closeRequest(self):
        #print(self.numReqBox.value())
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1'
        port = 12346
        s.connect((host, port))

        print("Connection to {}:{}".format(host, port))
        msg = "999" + str(self.numReqBox.value())
        print(msg)
        s.send(str(msg).encode())
        # response = s.recv(1024)
        s.close()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


