from tkinter import *
from tkinter import messagebox
import mysql.connector
from baseApp import *
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="cust_billing_data"
)

cursor =  mydb.cursor()

class BillingApp(BaseApp):

    def __init__(self,root):
        super().__init__()  # Call the parent class constructor
        self.root = root
        root.title("Billing Software")
        root.geometry("1270x630")

        headingLabel = Label(root,text="Billing Software",font=('times new roman',30,'bold'), bg='gray20', fg = 'gold', bd = 12, relief = GROOVE)
        headingLabel.pack(fill=X,pady=5)

        # Customer Details Section
        customer_frame = LabelFrame(root, text="Customer Details",font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
        customer_frame.pack(fill=X)

        nameLabel = Label(customer_frame,text='Name',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        nameLabel.grid(row=0, column=0, padx=20)

        self.name_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
        self.name_entry.grid(row=0, column=1, padx=8)

        phoneLabel = Label(customer_frame,text='Phone No',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        phoneLabel.grid(row=0, column=2, padx=20, pady=2)

        self.phone_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
        self.phone_entry.grid(row=0, column=3, padx=8)


        billLabel = Label(customer_frame,text='Bill No',font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        billLabel.grid(row=0, column=4, padx=20, pady=2)

        self.bill_entry = Entry(customer_frame, font=('arial',15), bd=7, width=18)
        self.bill_entry.grid(row=0, column=5, padx=8)

        enter_button = Button(customer_frame, text="Enter",font=('arial',12,'bold'),bd=7,width=18, command=lambda:self.addCustDetails(self.name_entry.get(),self.phone_entry.get()))
        enter_button.grid(row=0, column=6, padx=20, pady=8)

        # Product Frames Section
        product_frame = Frame(root)
        product_frame.pack(fill=X,pady=5) #expand=True

        # Cosmetics Frame
        cosmetics_frame = LabelFrame(product_frame, text="Cosmetics",font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
        cosmetics_frame.grid(row=0, column=0)

        self.prices1 = {"Bath Soap": 25, "Face Cream": 45, "Face Wash": 110, "Hair Spray": 150, "Body Lotion": 80}
        self.cosmetics_items = ["Bath Soap", "Face Cream", "Face Wash", "Hair Spray", "Body Lotion"]
        self.cosmetics_entries = {}

        for i, item in enumerate(self.cosmetics_items):
            Label(cosmetics_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
            self.cosmetics_entries[item] = Entry(cosmetics_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
            self.cosmetics_entries[item].grid(row=i, column=1, pady=9, padx=10)

        # Grocery Frame
        grocery_frame = LabelFrame(product_frame, text="Grocery", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
        grocery_frame.grid(row=0, column=1)

        self.prices2 = {"Rice": 25, "Food Oil": 45, "Daal": 110, "Wheat": 150, "Sugar": 80}
        self.grocery_items = ["Rice", "Food Oil", "Daal", "Wheat", "Sugar"]
        self.grocery_entries = {}

        for i, item in enumerate(self.grocery_items):
            Label(grocery_frame, text=f"{item}:",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
            self.grocery_entries[item] = Entry(grocery_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
            self.grocery_entries[item].grid(row=i, column=1, pady=9, padx=10)

        # Others Frame
        others_frame = LabelFrame(product_frame, text="Others", font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
        others_frame.grid(row=0, column=2)

        self.prices3 = {"Mazaa": 25, "Coke": 45, "Fruti": 110, "Nimkos": 150, "Biscuits": 80}
        self.others_items = ["Mazaa", "Coke", "Fruti", "Nimkos", "Biscuits"]
        self.others_entries = {}

        for i, item in enumerate(self.others_items):
            Label(others_frame, text=f"{item}:", font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white').grid(row=i, column=0, pady=9, padx=10, sticky="w")
            self.others_entries[item] = Entry(others_frame, font=('times new roman',15,'bold'), width=10, textvariable=StringVar(value="0"))
            self.others_entries[item].grid(row=i, column=1, pady=9, padx=10)

        billFrame = Frame(product_frame, bd=8, relief=GROOVE)
        billFrame.grid(row=0,column=3, padx=5)

        billareaLabel = Label(billFrame, text='Bill Area', font=('times new roman',15,'bold'), bd=7, relief=GROOVE)
        billareaLabel.pack(fill=X)

        scrollbar = Scrollbar(billFrame,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.textarea = Text(billFrame,width=55, height=13, yscrollcommand=scrollbar.set)
        self.textarea.pack()
        scrollbar.config(command=self.textarea.yview)


        # Allow components to scale
        product_frame.columnconfigure(0, weight=1)
        product_frame.columnconfigure(1, weight=1)
        product_frame.columnconfigure(2, weight=1)
        product_frame.columnconfigure(3, weight=1)
        product_frame.rowconfigure(0, weight=1)

        # Bill Menu Section
        bill_menu_frame = LabelFrame(root, text='Bill Menu',font=('times new roman',15,'bold'), bg='gray20', fg = 'gold', bd = 8, relief = GROOVE)
        bill_menu_frame.pack(fill=X)

        cosmetics_total = StringVar(value="0.0")
        grocery_total = StringVar(value="0.0")
        others_total = StringVar(value="0.0")
        cosmetics_tax = StringVar(value="0.0")
        grocery_tax = StringVar(value="0.0")
        others_tax = StringVar(value="0.0")

        cosmeticspriceLabel = Label(bill_menu_frame, text="Total Cosmetics",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        cosmeticspriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky="w")

        self.cosmetics_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=cosmetics_total,state='readonly')
        self.cosmetics_price_entry.grid(row=0, column=1, pady=6, padx=10)

        grocerypriceLabel = Label(bill_menu_frame, text="Total Grocery",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky="w")

        self.grocery_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=grocery_total,state='readonly')
        self.grocery_price_entry.grid(row=1, column=1, pady=6, padx=10)

        otherspriceLabel = Label(bill_menu_frame, text="Total Others",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        otherspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky="w")

        self.others_price_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=others_total,state='readonly')
        self.others_price_entry.grid(row=2, column=1, pady=6, padx=10)

        cosmeticstaxLabel = Label(bill_menu_frame, text="Cosmetics Tax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        cosmeticstaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

        self.cosmetics_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=cosmetics_tax,state='readonly')
        self.cosmetics_tax_entry.grid(row=0, column=3, pady=6, padx=10)

        grocerytaxLabel = Label(bill_menu_frame, text="Grocery Tax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

        self.grocery_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=grocery_tax,state='readonly')
        self.grocery_tax_entry.grid(row=1, column=3, pady=6, padx=10)

        otherstaxLabel = Label(bill_menu_frame, text="OthersTax",font=('times new roman',15,'bold'),bg = 'gray20', fg = 'white')
        otherstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

        self.others_tax_entry = Entry(bill_menu_frame, font=('times new roman',15,'bold'), width=10, bd=5, textvariable=others_tax,state='readonly')
        self.others_tax_entry.grid(row=2, column=3, pady=6, padx=10)

        # Buttons
        button_frame = Frame(bill_menu_frame, bd = 8, relief = GROOVE, padx=10)
        button_frame.grid(row=0, column=4, rowspan=3, padx=50)

        total_button = Button(button_frame, text="Total", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=self.commonTotal)
        total_button.grid(row=1, column=4, padx=5, pady=20)

        generate_bill_button = Button(button_frame, text="Generate", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=self.generate_bill)
        generate_bill_button.grid(row=1, column=5, padx=5, pady=20)

        clear_button = Button(button_frame, text="Clear", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=self.clear_entries)
        clear_button.grid(row=1, column=6, padx=5, pady=20)

        exit_button = Button(button_frame, text="Exit", font=('arial',16,'bold'), bg='gray20', fg='white', bd=5, width=8, pady=10, command=self.exit_program)
        exit_button.grid(row=1, column=7, padx=5, pady=20)

    def addCustDetails(self,name,phone):
        try:
            if(name.isalpha() and re.fullmatch(r"\d{10}",phone) is not None):
                qry = "insert into cust_details values(%s,%s,%s)"
                value=(name,phone,0)
                cursor.execute(qry,value)
                mydb.commit()
                # mydb.close()
                messagebox.showinfo("Success", "Data added successfully!")
            else: raise ValueError("Enter valid data")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        except ValueError as err:
            messagebox.showerror("Value Error", str(err))
        
    def cosmeticsTotal(self,cosmetics_entries,cosmetics_price_entry,cosmetics_tax_entry,prices1):
        try:
            totalc = 0
            for item, entry in self.cosmetics_entries.items():
                Quantites = int(entry.get() or 0)  # Default to 0 if entry is empty
                totalc += Quantites * prices1[item]
            self.cosmetics_price_entry = cosmetics_price_entry.delete(0, END)
            self.cosmetics_price_entry.insert(0, f"{totalc:.2f}")
            self.cosmetics_tax_entry.delete(0, END)
            self.cosmetics_tax_entry.insert(0, f"{totalc * 5 / 100:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric quantities.")

    def groceryTotal(self,grocery_entries,grocery_price_entry,grocery_tax_entry,prices2):

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


    def otherTotal(self,others_entries,others_price_entry,others_tax_entry,prices3):

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

    def commonTotal(self):
        self.cosmeticsTotal(self.cosmetics_entries,self.cosmetics_price_entry,self.cosmetics_tax_entry,self.prices1)
        self.groceryTotal(self.grocery_entries,self.grocery_price_entry,self.grocery_tax_entry,self.prices2)
        self.otherTotal(self.others_entries,self.others_price_entry,self.others_tax_entry,self.prices3)

    def generate_bill(self):
        # This function will be used to generate the bill (you can customize this)
        try:
            # Fetch customer details
            customer_name = self.name_entry.get()
            customer_phone = self.phone_entry.get()
            bill_no = cursor.lastrowid
            # bill_no = self.bill_entry.get()

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
            for item, entry in self.cosmetics_entries.items():
                quantity = int(entry.get() or 0)
                if quantity > 0:
                    price = self.prices1[item]
                    total = quantity * price
                    bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                    total_cost += total

            # Add grocery details
            for item, entry in self.grocery_entries.items():
                quantity = int(entry.get() or 0)
                if quantity > 0:
                    price = self.prices2[item]
                    total = quantity * price
                    bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                    total_cost += total

            # Add others details
            for item, entry in self.others_entries.items():
                quantity = int(entry.get() or 0)
                if quantity > 0:
                    price = self.prices3[item]
                    total = quantity * price
                    bill_content += f"{item}\t\t{quantity}\t{price}\t{total}\n"
                    total_cost += total

            # Add tax
            cosmetics_tax = float(self.cosmetics_tax_entry.get() or 0)
            grocery_tax = float(self.grocery_tax_entry.get() or 0)
            others_tax = float(self.others_tax_entry.get() or 0)

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
            self.textarea.delete(1.0, END)
            self.textarea.insert(END, bill_content)

            messagebox.showinfo("Bill Generated", f"Bill has been generated and saved as {filename}!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        print("Bill Generated")

    def clear_entries(self):
        # Clear all entry fields
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        for entry in self.cosmetics_entries.values():
            entry.delete(0, END)
            entry.insert(0,"0")
        for entry in self.grocery_entries.values():
            entry.delete(0, END)
            entry.insert(0,"0")
        for entry in self.others_entries.values():
            entry.delete(0, END)
            entry.insert(0,"0")
        self.cosmetics_price_entry.delete(0, END)
        self.cosmetics_price_entry.insert(0,"0.0")
        self.grocery_price_entry.delete(0, END)
        self.grocery_price_entry.insert(0,"0.0")
        self.others_price_entry.delete(0, END)
        self.others_price_entry.insert(0,"0.0")
        self.cosmetics_tax_entry.delete(0, END)
        self.cosmetics_tax_entry.insert(0,"0.0")
        self.grocery_tax_entry.delete(0, END)
        self.grocery_tax_entry.insert(0,"0.0")
        self.others_tax_entry.delete(0, END)
        self.others_tax_entry.insert(0,"0.0")

    def exit_program(self):
        self.root.quit()


        # Allow Bill Menu to scale
        self.bill_menu_frame.columnconfigure(1, weight=1)
        self.bill_menu_frame.columnconfigure(2, weight=1)
        self.bill_menu_frame.columnconfigure(3, weight=1)
        self.bill_menu_frame.columnconfigure(0, weight=1)

        # Make bill text area non-editable
        # textarea.config(state='disabled')

# Main Function

def main():
     root = Tk()
     app = BillingApp(root)
     print(type(app))
     root.mainloop()

if __name__ == "__main__":
    main()
