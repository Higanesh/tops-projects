
import sqlite3

conn = sqlite3.connect("demo.db")

# conn.execute("create table student (id int primary key,name varchar(20),email varchar(20))")

# conn.execute("create table products (productid int primary key, productname varchar(20), price float)")

data = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
for i in data:
    print(i)

# qry = "insert into student values (1, 'ganesh', 'ganesh@gmail.com')"
# conn.execute(qry)
# conn.commit()

data = conn.execute("select * from student")
for i in data:
    print(i)
