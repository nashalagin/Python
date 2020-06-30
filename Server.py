from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
#from base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime
import socket
from sqlalchemy import update

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/tsrm', echo = True)
print(engine)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column('name', String(99))
    phone = Column('phone', Integer)
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key = True)
    name = Column('name', String(99))
    phone = Column('phone', Integer)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key = True)
    initiato = Column(Integer, ForeignKey('users.id'))
    executor = Column(Integer, ForeignKey('admins.id'))
    decription = Column('decription', String(255))# ИСПРАВИТЬ АРФОГРАФИЧЕСКУЮ ОШИБКУ!!!!
    status = Column('status', String(99))
    registerTime = Column('registerTime', String(10))


    def __init__(self, userID, description):
        self.initiato = userID
        self.decription = description
        self.registerTime = str(datetime.datetime.now())[0:19]
        self.status = "На исполнении"
        self.executor = 3

def sendReqList(flag):
    Session = sessionmaker(bind=engine)
    ss = Session()
    Req1 = ss.query(Request)  # .join(Admin,Request.executor == Admin.id)
    # for inst in Req1:
    #    inst.executor = str(ss.query(Admin).get(inst.executor).name)
    # s.close()
    count = 0
    for counter in Req1:
        count += 1
    conn.send(str(count).encode())
    for inst in Req1:
        # print("\n\t№{}|{}|{}|{}|{}\n".format(inst.id, inst.decription, inst.registerTime,
        # str(ss.query(Admin).get(inst.executor).name),inst.status))
        if flag == "0":
            conn.send("{}|{}|{}|{}|{}".format(inst.id, inst.registerTime, inst.decription,
                                              str(ss.query(Admin).get(inst.executor).name), inst.status).encode())
        else:
            conn.send("{}|{}|{}|{}|{}".format(inst.id, inst.registerTime, inst.decription,
                                              str(ss.query(User).get(inst.initiato).name), inst.status).encode())
        # conn.send("{}|{}|{}|{}".format(inst.id, inst.decription, inst.registerTime,
        #                                 str(ss.query(Admin).get(inst.executor).name)).encode())

    # conn.send(Req1)
def sendRequest(msg):
    msg = msg.split("|")
    print("User:{} \n{}".format(msg[0], msg[1]))
    Session = sessionmaker(bind=engine)
    ss = Session()
    # userID = int(s.query(test_sqlAlchemy.User).get)
    temp = Request(userID=msg[0], description=msg[1])
    ss.add(temp)
    ss.commit()
def addUser(msg):
    msg = msg.split("|")
    Session = sessionmaker(bind=engine)
    ss = Session()
    temp = User(name=msg[0], phone=msg[1])
    ss.add(temp)
    ss.commit()
def addAdmin(msg):
    msg = msg.split("|")
    Session = sessionmaker(bind=engine)
    ss = Session()
    temp = Admin(name=msg[0], phone=msg[1])
    ss.add(temp)
    ss.commit()
def closeRequest(msg):
    Session = sessionmaker(bind=engine)
    ss = Session()
    print(msg)
    temp = ss.query(Request).filter(Request.id == int(msg)).update({Request.status: "Исполнено"})
    ss.commit()
    print("DATABASE UPDATE!")
    ss.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET-IPv4 SOCK_STREAM-TCP
host = '127.0.0.1'
port = 12346
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Server got connection from {}'.format(addr))
    req = conn.recv(1024)
    msg = req.decode()
    print(msg)
    if msg[0] == "0":
        sendReqList(msg[1])
    if msg[0:3] == "111":
        msg = msg[3:]
        sendRequest(msg)
    if msg[0:3] == "222":
        msg = msg[3:]
        addUser(msg)
    if msg[0:3] == "333":
        msg = msg[3:]
        addAdmin(msg)
    if msg[0:3] == "999":
        msg = msg[3:]
        closeRequest(msg)
    conn.close()
s.close()