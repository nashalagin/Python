import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='tsrm',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#ADD USER (A)
def addUser(name, phone, departament):
    sqlAddUser = 'INSERT INTO `users` (`name`, `phone`, `departament`) ' \
                 'VALUES ("'+ name +'","'+ phone +'","'+ departament+ '");'
    print(sqlAddUser)
    with connection.cursor() as cursor:
        cursor.execute(sqlAddUser)
        connection.commit()
    print("User add {} ({}) {}".format(name, phone, departament))

#ADD ADMIN (A)
def addAdmin(name, phone):
    sqlAddAdmin = 'INSERT INTO `admins` (`name`, `phone`) ' \
                 'VALUES ("'+ name +'","'+ phone +'");'
    print(sqlAddAdmin)
    with connection.cursor() as cursor:
        cursor.execute(sqlAddAdmin)
        connection.commit()
    print("Admin add {} ({})".format(name, phone))

#USER LIST (A)
def userList():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        for row in cursor:
             print(row)

#ADMIN LIST (A)
def adminList():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM admins"
        cursor.execute(sql)
        for row in cursor:
             print(row)

#REQUESTS LIST (AU)
def requestList():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM requests"
        cursor.execute(sql)
        for row in cursor:
             print(row)
#ADD COMMENT (AU)
#CHANGE STATUS (AU)
#SUMBIT REQUEST (U)
def sumbitRequest(userID,description):
    pass
#STATISTICS (A)

# Get User ID
def getUserID(name):
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM `users` WHERE `name`="' + name + '";'
        cursor.execute(sql)
        test = cursor.fetchall()
        for p in test:
            print(p.type)
            print(test.type)

getUserID("Иванов Иван Иванович")
connection.close()