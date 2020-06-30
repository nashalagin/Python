from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
#from base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime
from sqlalchemy import func

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/tsrm', echo = True)
print(engine)
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    name = Column('name', String(99))
    phone = Column('phone', Integer)
    departament = Column('departament', String(99))
    def __init__(self, name, phone, departament):
        self.name = name
        self.phone = phone
        self.departament = departament

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.phone, self.departament)

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
    chat = Column('chat', String(255))
    ip = Column('ip', Integer)
    status = Column('status', String(99))
    registerTime = Column('registerTime', String(10))
    #user_ = relationship("User")
    #admin_ = relationship("Admin")

    def __init__(self, userID, description):
        self.initiato = userID
        self.decription = description
        self.registerTime = str(datetime.datetime.now())[0:19]
        self.status = "Не назначено"


#Session = sessionmaker(bind = engine)
#s = Session()
#test = Admin("Vasya",123)
#s.add(test)
#s.commit()
#print(test.id)

#for inst in s.query(Admin).filter(Admin.phone == 123):
#    print(inst.id, inst.name)
#for instance in s.query(Admin).order_by(Admin.id):
#    print(instance.name, instance.phone)


#temp = Request(9,"lalala")
#print(temp.id)
#s.add(temp)
#s.commit()

#for instance in s.query(Request).join(Admin, Request.executor == Admin.id):#.order_by(Request.id):
#    print("{} | {} | {} | {}".format(str(s.query(Admin).get(instance.executor).name),instance.decription, str(instance.executor) ,instance.status))
