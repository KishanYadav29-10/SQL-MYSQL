import mysql.connector

conn = mysql.connector.connect(host ='localhost',user='root',password='kishan29_10',database='pythondb')
mycursor = conn.cursor()
mycursor.execute('create table student(name varchar(50),brach varchar(50),id int)')
mycursor.execute('show tables')
for x in mycursor:
    print(x)