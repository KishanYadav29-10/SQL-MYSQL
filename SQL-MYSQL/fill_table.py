import mysql.connector

conn = mysql.connector.connect(host ='localhost',user='root',password='kishan29_10',database='pythondb')
mycursor = conn.cursor()

sql = 'insert into student(name ,brach,id) values(%s,%s,%s)'

val =[('john','cse',56),('mike','IT',78),('kishan','AIML',17)]
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')