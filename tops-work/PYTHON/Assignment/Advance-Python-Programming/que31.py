"""
Que31. Write a Python program to create a database and a table using SQLite3.
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create_table_query = "create table student(id int primary key,name varchar(20),email varchar(20))"
create_table_query = "create table products(id int primary key, pname varchar(20),price int)"
cursor.execute(create_table_query)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table = cursor.fetchall()
print(f"Table: {table}")

connection.commit()
connection.close()

print("Database and table created successfully.")



