import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="emp_data"
)

cursor = db.cursor()

sql = "insert into emp(name,age) values (%s,%d)"
values = ("ganesh",25)
cursor.execute(sql,values)
db.commit()
print(cursor.rowcount,"record inserted.")

  