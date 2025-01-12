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
        # mydb.close()
        messagebox.showinfo("Success", "Data added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))


def cosmeticsTotal():
    try:
        totalc = 0
        for item, entry in cosmetics_entries.items():
            Quantites = int(entry.get() or 0)  # Default to 0 if entry is empty
            totalc += Quantites * prices1[item]
        cosmetics_price_entry.delete(0, END)
        cosmetics_price_entry.insert(0, f"{totalc:.2f}")
        cosmetics_tax_entry.delete(0, END)
        cosmetics_tax_entry.insert(0, f"{totalc * 5 / 100:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric quantities.")

def groceryTotal():

    try:
        totalg = 0
        for item, entry in grocery_entries.items():
            Quantites = int(entry.get() or 0)  # Default to 0 if entry is empty
            totalg += Quantites * prices2[item]
        grocery_price_entry.delete(0, END)
        grocery_price_entry.insert(0, f"{totalg:.2f}")
        grocery_tax_entry.delete(0, END)
        grocery_tax_entry.insert(0, f"{totalg * 5 / 100:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric quantities.")


def otherTotal():

    try:
        totalo = 0
        for item, entry in others_entries.items():
            Quantites = int(entry.get() or 0)  # Default to 0 if entry is empty
            totalo += Quantites * prices3[item]
        others_price_entry.delete(0, END)
        others_price_entry.insert(0, f"{totalo:.2f}")
        others_tax_entry.delete(0, END)
        others_tax_entry.insert(0, f"{totalo * 5 / 100:.2f}")  
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric quantities.")

def commonTotal():
    cosmeticsTotal()
    groceryTotal()
    otherTotal()

def generate_bill():
    # This function will be used to generate the bill (you can customize this)
    try:
        # Fetch customer details
        customer_name = name_entry.get()
        customer_phone = phone_entry.get()
        bill_no = bill_entry.get()

        if not customer_name or not customer_phone or not bill_no:
            messagebox.showerror("Missing Details", "Please fill in all customer details!")
            return

        # Create the bill content
        bill_content = f"\t\tWelcome to Ganesh Retail Store\n"
        bill_content += f"Bill No: {bill_no}\n"
        bill_content += f"Customer Name: {customer_name}\n"
        bill_content += f"Phone No: {customer_phone}\n"
        bill_content += f"\n============================================\n"
        bill_content += f"Items\t\tQty\tPrice\tTotal\n"
        bill_content += f"============================================\n"

        total_cost = 0
        total_tax = 0

        # Add cosmetics details
        for item, entry in cosmetics_entries.items():
            quantity = int(entry.get() or 0)
            if quantity > 0:
                price = prices1[item]
                total = quantity * price
                bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                total_cost += total

        # Add grocery details
        for item, entry in grocery_entries.items():
            quantity = int(entry.get() or 0)
            if quantity > 0:
                price = prices2[item]
                total = quantity * price
                bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                total_cost += total

        # Add others details
        for item, entry in others_entries.items():
            quantity = int(entry.get() or 0)
            if quantity > 0:
                price = prices3[item]
                total = quantity * price
                bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                total_cost += total

        # Add tax
        cosmetics_tax = float(cosmetics_tax_entry.get() or 0)
        grocery_tax = float(grocery_tax_entry.get() or 0)
        others_tax = float(others_tax_entry.get() or 0)

        total_tax = cosmetics_tax + grocery_tax + others_tax
        final_amount = total_cost + total_tax

        bill_content += f"============================================\n"
        bill_content += f"Sub Total\t\t\t\t{total_cost:.2f}\n"
        bill_content += f"Total Tax\t\t\t\t{total_tax:.2f}\n"
        bill_content += f"============================================\n"
        bill_content += f"Final Amount\t\t\t\t{final_amount:.2f}\n"
        bill_content += f"============================================\n"
        bill_content += f"Thank you for shopping with us!\n"

        # Save to file
        filename = f"Bill_{bill_no}.txt"
        with open(filename, "w") as file:
            file.write(bill_content)

        # Display in the bill area
        textarea.delete(1.0, END)
        textarea.insert(END, bill_content)

        messagebox.showinfo("Bill Generated", f"Bill has been generated and saved as {filename}!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    print("Bill Generated")

def clear_entries():
    # Clear all entry fields
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    for entry in cosmetics_entries.values():
        entry.delete(0, END)
        entry.insert(0,"0")
    for entry in grocery_entries.values():
        entry.delete(0, END)
        entry.insert(0,"0")
    for entry in others_entries.values():
        entry.delete(0, END)
        entry.insert(0,"0")
    cosmetics_price_entry.delete(0, END)
    cosmetics_price_entry.insert(0,"0.0")
    grocery_price_entry.delete(0, END)
    grocery_price_entry.insert(0,"0.0")
    others_price_entry.delete(0, END)
    others_price_entry.insert(0,"0.0")
    cosmetics_tax_entry.delete(0, END)
    cosmetics_tax_entry.insert(0,"0.0")
    grocery_tax_entry.delete(0, END)
    grocery_tax_entry.insert(0,"0.0")
    others_tax_entry.delete(0, END)
    others_tax_entry.insert(0,"0.0")

def exit_program():
    root.quit()

# Create main application window
root = Tk()
root.title("Billing Software")
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

prices1 = {"Bath Soap": 25, "Face Cream": 45, "Face Wash": 110, "Hair Spray": 150, "Body Lotion": 80}
cosmetics_items = ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"]
cosmetics_entries = {}

for i, item in enumerate(cosmetics_items):
    Label(cosmetics_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    cosmetics_entries[item] = Entry(cosmetics_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
    cosmetics_entries[item].grid(row=i, column=1, pady=9, padx=10)

# Grocery Frame
grocery_frame = LabelFrame(product_frame, text="Grocery", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
grocery_frame.grid(row=0, column=1)

prices2 = {"Rice": 25, "Food Oil": 45, "Daal": 110, "Wheat": 150, "Sugar": 80}
grocery_items = ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"]
grocery_entries = {}

for i, item in enumerate(grocery_items):
    Label(grocery_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    grocery_entries[item] = Entry(grocery_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
    grocery_entries[item].grid(row=i, column=1, pady=9, padx=10)

# Others Frame
others_frame = LabelFrame(product_frame, text="Others", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
others_frame.grid(row=0, column=2)

prices3 = {"Mazaa": 25, "Coke": 45, "Fruti": 110, "Nimkos": 150, "Biscuits": 80}
others_items = ["Mazaa", "Coke", "Fruti", "Nimkos", "Biscuits"]
others_entries = {}

for i, item in enumerate(others_items):
    Label(others_frame, text=f"{item}:", font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
    others_entries[item] = Entry(others_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
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

cosmetics_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
cosmetics_price_entry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel = Label(bill_menu_frame, text="Total Grocery",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky="w")

grocery_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
grocery_price_entry.grid(row=1, column=1, pady=6, padx=10)

otherspriceLabel = Label(bill_menu_frame, text="Total Others",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
otherspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky="w")

others_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
others_price_entry.grid(row=2, column=1, pady=6, padx=10)

cosmeticstaxLabel = Label(bill_menu_frame, text="Cosmetics Tax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
cosmeticstaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

cosmetics_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
cosmetics_tax_entry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel = Label(bill_menu_frame, text="Grocery Tax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

grocery_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
grocery_tax_entry.grid(row=1, column=3, pady=6, padx=10)

otherstaxLabel = Label(bill_menu_frame, text="OthersTax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
otherstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

others_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=StringVar(value="0.0"))
others_tax_entry.grid(row=2, column=3, pady=6, padx=10)

# Buttons
button_frame = Frame(bill_menu_frame, bd = 8, relief = GROOVE, padx=10)
button_frame.grid(row=0, column=4, rowspan=3, padx=50)

total_button = Button(button_frame, text="Total", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=commonTotal)
total_button.grid(row=1, column=4, padx=5, pady=20)

generate_bill_button = Button(button_frame, text="Generate", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=generate_bill)
generate_bill_button.grid(row=1, column=5, padx=5, pady=20)

clear_button = Button(button_frame, text="Clear", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=clear_entries)
clear_button.grid(row=1, column=6, padx=5, pady=20)

exit_button = Button(button_frame, text="Exit", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=exit_program)
exit_button.grid(row=1, column=7, padx=5, pady=20)

# Allow Bill Menu to scale
bill_menu_frame.columnconfigure(0, weight=1)
bill_menu_frame.columnconfigure(1, weight=1)
bill_menu_frame.columnconfigure(2, weight=1)
bill_menu_frame.columnconfigure(3, weight=1)


# Make fields readonly where applicable
cosmetics_price_entry.config(state='readonly')
grocery_price_entry.config(state='readonly')
others_price_entry.config(state='readonly')
cosmetics_tax_entry.config(state='readonly')
grocery_tax_entry.config(state='readonly')
others_tax_entry.config(state='readonly')

# Make bill text area non-editable
# textarea.config(state='disabled')

root.mainloop()
