import mysql.connector
from tkinter import messagebox


# Base Application Class (Demonstrating Inheritance and Encapsulation)
class BaseApp:
    def __init__(self):
        self._connection = None  # Encapsulation: Protected attribute for database connection

    def connect_to_database(self):
        try:
            self._connection = mysql.connector.connect()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def close_database_connection(self):
        if self._connection:
            self._connection.close()
