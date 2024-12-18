import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="13nov_python"
)

cursor =  mydb.cursor()

# qry = "insert into users values(0,'kb','kb@gmail.com','8596857485')"
# qry = "insert into users values(%s,%s,%s)"
# val = (0,'Ganesh','ganesh@gmail.com')
# cursor.execute(qry,val)
# mydb.commit()

# cursor.execute("select * from users")
# # Fetch all rows from the result of the query
# data = cursor.fetchall()

# # Print the fetched data
# for row in data:
#     print(row)

# cursor.execute("UPDATE users SET email = 'rupesh@gmail.com' WHERE id = 3")
# cursor.execute("select * from users where id = 3")
# data = cursor.fetchone()
# print(data)

cursor.execute("delete from users where uname = 'ganesh'")
cursor.execute("select * from users")
# Fetch all rows from the result of the query
data = cursor.fetchall()

# Print the fetched data
for row in data:
    print(row)

mydb.commit()