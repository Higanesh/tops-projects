from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="13nov_python"
)

cursor =  mydb.cursor()

def addData(id,uname,email):
    qry = "insert into users values(%s,%s,%s)"
    val = (id,uname,email)
    cursor.execute(qry,val)
    mydb.commit()
    print("Data added successfully")

root = Tk()
root.geometry("500x500")

idl = Label(root,text="Id")
unamel = Label(root,text="Username")
emaill = Label(root,text="Email")


idt = Entry(root)
unamet = Entry(root)
emailt = Entry(root)

idl.place(x=100,y=50)
unamel.place(x=100,y=100)
emaill.place(x=100,y=150)

idt.place(x=200,y=50)
unamet.place(x=200,y=100)
emailt.place(x=200,y=150)

submit = Button(root,text="submit",command=lambda:addData(idt.get(),unamet.get(),emailt.get()))
submit.place(x=200,y=250)



root.mainloop()