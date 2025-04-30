from sql_to_python_conn import conn

mycursor = conn.cursor()

mycursor.execute('create database pythondb')
