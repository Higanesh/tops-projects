from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="cust_billing_data"
)

cursor =  mydb.cursor()


def addCustDetails(name,phone):
    try:
        qry = "insert into cust_details values(%s,%s,%s)"
        value=(name,phone,0)
        cursor.execute(qry,value)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "Data added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

def deleteCust(billNo):
    query = "DELETE FROM cust_details WHERE bill_no = %s"
    cursor.execute(query, (billNo,))
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Success", "Data delete successfully!")


# def calculate_total():
#     try:
#         price = float(price_entry.get())
#         quantity = int(quantity_entry.get())
#         total = price * quantity
#         total_label.config(text=f"Total: ${total:.2f}")
#     except ValueError:
#         total_label.config(text="Invalid input! Please enter valid numbers.")

def generate_bill():
    # This function will be used to generate the bill (you can customize this)
    print("Bill Generated")

# def clear_entries():
#     # Clear all entry fields
#     for entry in cosmetics_entries.values():
#         entry.delete(0, END)
#     for entry in grocery_entries.values():
#         entry.delete(0, END)
#     for entry in others_entries.values():
#         entry.delete(0, END)

def exit_program():
    root.quit()

# Create main application window
root = Tk()
root.title("Billing Form")
root.geometry("1270x630")  # Adjusted to make room for new frame

headingLabel = Label(root,text="Billing Software",font=('times new roman',30,'bold'), bg='gray20', fg = 'gold', bd = 12, relief = GROOVE)
headingLabel.pack(fill=X,pady=5)

# Customer Details Section
customer_frame = LabelFrame(root, text="Customer Details",font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
customer_frame.pack(fill=X)

nameLabel = Label(customer_frame,text='Name',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
nameLabel.grid(row=0, column=0, padx=20)

name_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
name_entry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_frame,text='Phone No',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phone_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
phone_entry.grid(row=0, column=3, padx=8)


billLabel = Label(customer_frame,text='Bill No',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
billLabel.grid(row=0, column=4, padx=20, pady=2)

bill_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
bill_entry.grid(row=0, column=5, padx=8)

enter_button = Button(customer_frame, text="Enter",font=('arial',12,'bold'),bd=7,width=18, command=lambda:addCustDetails(name_entry.get(),phone_entry.get()))
enter_button.grid(row=0, column=6, padx=20, pady=8)

# Product Frames Section
product_frame = Frame(root)
product_frame.pack(fill=X,pady=5) #expand=True

# Cosmetics Frame
cosmetics_frame = LabelFrame(product_frame, text="Cosmetics",font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
cosmetics_frame.grid(row=0, column=0)

cosmetics_items = ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"]
cosmetics_entries = {}

for i, item in enumerate(cosmetics_items):
    Label(cosmetics_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    cosmetics_entries[item] = Entry(cosmetics_frame, font=('times new roman',15,'bold'), width=10)
    cosmetics_entries[item].grid(row=i, column=1, pady=9, padx=10)

# Grocery Frame
grocery_frame = LabelFrame(product_frame, text="Grocery", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
grocery_frame.grid(row=0, column=1)

grocery_items = ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"]
grocery_entries = {}

for i, item in enumerate(grocery_items):
    Label(grocery_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    grocery_entries[item] = Entry(grocery_frame, font=('times new roman',15,'bold'), width=10)
    grocery_entries[item].grid(row=i, column=1, pady=9, padx=10)

# Others Frame
others_frame = LabelFrame(product_frame, text="Others", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
others_frame.grid(row=0, column=2)

others_items = ["Mazaa", "Coke", "Fruti", "Nimkos", "Biscuits"]
others_entries = {}

for i, item in enumerate(others_items):
    Label(others_frame, text=f"{item}:", font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    others_entries[item] = Entry(others_frame, font=('times new roman',15,'bold'), width=10)
    others_entries[item].grid(row=i, column=1, pady=9, padx=10)

billFrame = Frame(product_frame, bd=8, relief=GROOVE)
billFrame.grid(row=0,column=3, padx=5)

billareaLabel = Label(billFrame, text='Bill Area', font=('times new roman',15,'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea = Text(billFrame,width=55, height=13, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


# Allow components to scale
product_frame.columnconfigure(0, weight=1)
product_frame.columnconfigure(1, weight=1)
product_frame.columnconfigure(2, weight=1)
product_frame.columnconfigure(3, weight=1)
product_frame.rowconfigure(0, weight=1)

# Bill Menu Section
bill_menu_frame = LabelFrame(root, text='Bill Menu',font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
bill_menu_frame.pack(fill=X)

cosmeticspriceLabel = Label(bill_menu_frame, text="Total Cosmetics",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
cosmeticspriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky="w")

cosmetics_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
cosmetics_price_entry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel = Label(bill_menu_frame, text="Total Grocery",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky="w")

grocery_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
grocery_price_entry.grid(row=1, column=1, pady=6, padx=10)

otherspriceLabel = Label(bill_menu_frame, text="Total Others",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
otherspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky="w")

others_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
others_price_entry.grid(row=2, column=1, pady=6, padx=10)

cosmeticstaxLabel = Label(bill_menu_frame, text="Cosmetics Tax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
cosmeticstaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

cosmetics_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
cosmetics_tax_entry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel = Label(bill_menu_frame, text="Total Grocery",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

grocery_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
grocery_tax_entry.grid(row=1, column=3, pady=6, padx=10)

otherstaxLabel = Label(bill_menu_frame, text="Total Others",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
otherstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

others_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5)
others_tax_entry.grid(row=2, column=3, pady=6, padx=10)


# Buttons
button_frame = Frame(bill_menu_frame, bd = 8, relief = GROOVE, padx=10)
button_frame.grid(row=0, column=4, rowspan=3, padx=50)

total_button = Button(button_frame, text="Total", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=generate_bill)
total_button.grid(row=1, column=4, padx=5, pady=20)

generate_bill_button = Button(button_frame, text="Generate", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=generate_bill)
generate_bill_button.grid(row=1, column=5, padx=5, pady=20)

clear_button = Button(button_frame, text="Clear", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=deleteCust(bill_entry.get()))
clear_button.grid(row=1, column=6, padx=5, pady=20)

exit_button = Button(button_frame, text="Exit", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=exit_program)
exit_button.grid(row=1, column=7, padx=5, pady=20)

# Allow Bill Menu to scale
bill_menu_frame.columnconfigure(0, weight=1)
bill_menu_frame.columnconfigure(1, weight=1)
bill_menu_frame.columnconfigure(2, weight=1)
bill_menu_frame.columnconfigure(3, weight=1)

root.mainloop()
