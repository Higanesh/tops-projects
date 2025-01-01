import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="13nov_python"
    )

# CRUD Operations
def add_record():
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "INSERT INTO users (uname, email) VALUES (%s, %s)"
        cursor.execute(query, (uname_var.get(), email_var.get()))
        db.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        clear_fields()
        fetch_records()
    except Exception as e:
        messagebox.showerror("Error", f"Error adding record: {e}")
    finally:
        cursor.close()
        db.close()

def fetch_records():
    try:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for row in rows:
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching records: {e}")
    finally:
        cursor.close()
        db.close()

def update_record():
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "UPDATE users SET uname=%s, email=%s WHERE id=%s"
        cursor.execute(query, (uname_var.get(), email_var.get(), id_var.get()))
        db.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
        clear_fields()
        fetch_records()
    except Exception as e:
        messagebox.showerror("Error", f"Error updating record: {e}")
    finally:
        cursor.close()
        db.close()

def delete_record():
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "DELETE FROM users WHERE id=%s"
        cursor.execute(query, (id_var.get(),))
        db.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        clear_fields()
        fetch_records()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting record: {e}")
    finally:
        cursor.close()
        db.close()

def clear_fields():
    id_var.set("")
    uname_var.set("")
    email_var.set("")

def select_record(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if values:
        id_var.set(values[0])
        uname_var.set(values[1])
        email_var.set(values[2])

# GUI Setup
root = tk.Tk()
root.title("CRUD Application")
root.geometry("700x400")

# Input Frame
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(fill="x")

id_var = tk.StringVar()
uname_var = tk.StringVar()
email_var = tk.StringVar()

ttk.Label(input_frame, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky="e")
ttk.Entry(input_frame, textvariable=id_var, width=30).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Username").grid(row=1, column=0, padx=5, pady=5, sticky="e")
ttk.Entry(input_frame, textvariable=uname_var, width=30).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Email").grid(row=2, column=0, padx=5, pady=5, sticky="e")
ttk.Entry(input_frame, textvariable=email_var, width=30).grid(row=2, column=1, padx=5, pady=5)

# Buttons Frame
button_frame = ttk.Frame(root, padding=10)
button_frame.pack(fill="x")

ttk.Button(button_frame, text="Add", command=add_record).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Update", command=update_record).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Delete", command=delete_record).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(button_frame, text="Clear", command=clear_fields).grid(row=0, column=3, padx=5, pady=5)

# Treeview for Displaying Records
tree_frame = ttk.Frame(root)
tree_frame.pack(fill="both", expand=True)

columns = ("ID", "Username", "Email")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.bind("<ButtonRelease-1>", select_record)

fetch_records()

root.mainloop()
