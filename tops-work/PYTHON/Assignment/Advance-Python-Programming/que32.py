"""
Que32. Write a Python program to insert data into an SQLite3 database and fetch it. 
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
print(f"Table: {table}")

qry = "insert into student values(2,'Sagar','sagar@gmail.com')"
connection.execute(qry)
connection.commit()

data =  connection.execute("select * from student")
for i in data:
    for k in i:
        print(k,end=" ")
    print(end='\n')

connection.close()