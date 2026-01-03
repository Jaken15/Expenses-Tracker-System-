from tkinter import *
from tkinter import ttk
from Project import Record_system as rs
from tkinter import messagebox

class Record_SystemGui:
    def __init__(self,root):

        root.title("Record expenses system")
        root.geometry("1000x500")

        side_frame = Frame(root,bg="#1e1e1e")
        side_frame.pack(side='left',fill='y')

        self.recordsystem = rs()
        extra = Label(side_frame,bg="#1e1e1e")
        extra.pack(fill='x',padx=10,pady=10,)

        Home_button = Button(side_frame,
                             bg="#333",
                             text="Home",
                             font=("arial",10),
                             relief='raised',
                             fg='white',
                             command=self.Home)
        Home_button.pack(fill='x',padx=10,pady=10,)

        Insert_button = Button(side_frame,
                               bg="#333",
                               text="Insert Page",
                             font=("arial",10),
                             relief='raised',
                             fg='white',
                             command=self.Insert_page)
        Insert_button.pack(fill='x',padx=10,pady=10,)

        transaction = Button(side_frame,
                             bg="#333",
                             text="Transaction",
                             font=("arial",10),
                             relief='raised',
                             fg='white',
                             command=self.transaction)
        transaction.pack(fill='x',padx=10,pady=10,)

        self.main_frame = Frame(root)
        self.main_frame.pack(fill='both',expand=True,side='left')
        self.Home()

    def Insert_page(self):
        self.destroy_widget()

        Home_page = Label(self.main_frame,
                          text="Insert data page",
                          font=("arial",20,"bold"))
        Home_page.pack(pady=(5,10,))

        input_frame = Frame(self.main_frame,
                            width=500,
                            height=400,
                            relief='raised',
                            bd=4)
        input_frame.pack(pady=50)
        input_frame.pack_propagate(False)

        Item = Label(input_frame,
                     text="Enter item :",
                     font=("arial",10))
        Item.pack(pady=10)

        product_number = Entry(input_frame,font=10)
        product_number.pack()

        quantity_label = Label(input_frame,
                               text="Enter quantity :",
                               font=("arail",10))
        quantity_label.pack(pady=10)

        quantity_entry = Entry(input_frame,font=10)
        quantity_entry.pack()

        amount_label = Label(input_frame,
                             text="Enter amount :"
                             ,font=("arail",10))
        amount_label.pack(pady=10)

        amount_entry = Entry(input_frame,font=10)
        amount_entry.pack()

        buttons_frame = Frame(input_frame)
        buttons_frame.pack(side='bottom')

        Create_button = Button(buttons_frame,
                               text="Insert",font=10,width=7,
                               command=lambda:self.insert_data(product_number,quantity_entry,amount_entry))
        Create_button.pack(side='left',padx=10,pady=20)

        Delete__button = Button(buttons_frame,text="Delete",font=10,width=7,
                                command=self.delete_frame)
        Delete__button.pack(side='left',padx=10,pady=20)

        Update_button = Button(buttons_frame,text="Update",font=10,width=7,command=self.update_frame)
        Update_button.pack(side='left',padx=10,pady=20)

        exit_button = Button(buttons_frame,text="Exit",font=10,width=7,command=root.destroy)
        exit_button.pack(side='left',padx=10,pady=20)

    def Home(self):
        self.destroy_widget()
        
        Home_label = Label(self.main_frame,
                           text="Welcome to Record Expenses System",
                           font=("arial",15,"bold"),
                           bg="#1e1e1e",
                           fg="white",height=2)
        Home_label.pack(fill='x',expand=True)

        input_frame = Frame(self.main_frame,
                            width=500,height=400,
                            relief='raised',bd=4)
        input_frame.pack(pady=50)
        input_frame.pack_propagate(False)

        Label_frame = Frame(input_frame)
        Label_frame.pack()
        
        Daily_expenses = Button(Label_frame,
                               text=f"Today Expenses :\n $ ",
                               font=("arial",10),
                               bg="#1e1e1e",
                               fg= "white",
                               width=25,
                               relief='raised',command=self.Daily_frame)
        Daily_expenses.pack(pady=(30,10))

        Weekly_expenses = Button(Label_frame,
                               text="Weekly Expenses :\n $ ",
                               font=("arial",10),
                               bg="#1e1e1e",
                               fg="white",
                               width=25,
                               relief='raised',command=self.Weekly_frame)
        Weekly_expenses.pack(pady=15)

        Monthly_expenses = Button(Label_frame,
                               text="Monthly Expenses :\n $",
                               font=("arial",10),
                               bg="#1e1e1e",
                               fg="white",
                               width=25,
                               relief='raised',command=self.Monthly_frame)
        Monthly_expenses.pack(pady=15)

        Total_expenses = Button(Label_frame,
                               text=" Yearly Expenses :\n $ ",
                               font=("arial",10),
                               bg="#1e1e1e",
                               fg='white',
                               width=25,
                               relief='raised',command=self.Total_frame)
        Total_expenses.pack(pady=15)

    def transaction(self):
        self.destroy_widget()
        Transaction_page = Label(self.main_frame,
                            text="Trasaction Page",
                          font=("arial",20,"bold"))
        Transaction_page.pack(pady=(5,10,))

        row_and_columns = ttk.Treeview(self.main_frame,
        columns=("Product_number","Item","Quantity","Amount","Date","Time"),show='headings',height=18)

        row_and_columns.column("Product_number",anchor='w',width=70)
        row_and_columns.column("Item",anchor='w',width=100)
        row_and_columns.column("Quantity",anchor='w',width=70)
        row_and_columns.column("Amount",anchor='w',width=70)
        row_and_columns.column("Date",anchor='w',width=100)
        row_and_columns.column("Time",anchor='w',width=100)

        row_and_columns.heading("Product_number",anchor='w',text="Product id")
        row_and_columns.heading("Item",anchor='w',text="Items")
        row_and_columns.heading("Quantity",anchor='w',text="Quantity")
        row_and_columns.heading("Amount",anchor='w',text="Amount")
        row_and_columns.heading("Date",anchor='w',text="Date")
        row_and_columns.heading("Time",anchor='w',text="Time")

        information = self.recordsystem.transaction()
        for index,data in enumerate(information):
            row_and_columns.insert(parent='',index='end',iid=index,
                                   values=data)
        row_and_columns.pack()

    def destroy_widget(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def insert_data(self,item,amount,quantity):
        Item = item.get()
        Amount = amount.get()
        Quantity = quantity.get()

        if len(Item) and len(Amount) and len(Quantity) != 0:
            item.delete(0,END)
            amount.delete(0,END)
            quantity.delete(0,END)
            self.recordsystem.InsertToDatabase(Item,Amount,Quantity)
            print("Successfull")
        else:
            messagebox.showwarning("Empty","Pls fill enter a data ")

    def delete_frame(self):
        self.destroy_widget()

        Home_page = Label(self.main_frame,text="Insert data page",
                          font=("arial",20,"bold"))
        Home_page.pack(pady=(5,10,))

        input_frame = Frame(self.main_frame,width=500,height=400,relief='raised',bd=4)
        input_frame.pack(pady=50)
        input_frame.pack_propagate(False)

        product_number = Label(input_frame,text="Enter Product number :",font=("arial",10))
        product_number.pack(pady=10)

        product_number = Entry(input_frame,font=10)
        product_number.pack()

        buttons_frame = Frame(input_frame)
        buttons_frame.pack(side='bottom')

        
        Delete__button = Button(buttons_frame,text="Delete",font=26,width=7,
                                command=lambda:self.delete_data(product_number))
        Delete__button.pack(side='left',padx=10,pady=20)

        exit_button = Button(buttons_frame,text="Exit",font=10,width=7,command=self.Insert_page)
        exit_button.pack(side='left',padx=10,pady=20)

    def Daily_frame(self):
        self.destroy_widget()

        data_frame = Frame(self.main_frame,
                            width=500,height=400,
                            relief='raised',bd=4)
        data_frame.pack(pady=50)
        data_frame.pack_propagate(False)

        
        Data = ttk.Treeview(data_frame,
                            columns=("id","Item","quantity","amount","Date","time"),show='headings')
           
        Data.column("id",width=80,anchor='w')
        Data.column("Item",width=80,anchor='w')
        Data.column("quantity",width=80,anchor='w')
        Data.column("amount",width=80,anchor='w') 
        Data.column("Date",width=80,anchor='w')
        Data.column("time",width=80,anchor='w')

        Data.heading("id",text="Product id",anchor='w')
        Data.heading("Item",text="Item",anchor='w')
        Data.heading("quantity",text="quantity",anchor='w')
        Data.heading("amount",text="Amount",anchor='w')
        Data.heading("Date",text="Date",anchor='w')
        Data.heading("time",text="Time",anchor='w')

        total_expenses = self.recordsystem.today_expenses("total expenses")[0]
        all_data = self.recordsystem.today_expenses("all data")

        for index,data in enumerate(all_data):
            Data.insert(parent='',index='end',iid=index,values=data)

        Home_page = Label(data_frame,text=f"Today total expenses $ {total_expenses}",
                          font=("arial",13,"bold"))
        Home_page.pack(pady=(5,10,))
        Data.pack(expand=True,fill='both')
        exit_button = Button(data_frame,text="Exit",font=10,width=7,command=self.Home)
        exit_button.pack(padx=10,pady=20)

    def Weekly_frame(self):
        self.destroy_widget()

        data_frame = Frame(self.main_frame,
                            width=500,height=400,
                            relief='raised',bd=4)
        data_frame.pack(pady=50)
        data_frame.pack_propagate(False)

        Data = ttk.Treeview(data_frame,
                            columns=("id","Item","quantity","amount","Date","time"),show='headings')
           
        Data.column("id",width=80,anchor='w')
        Data.column("Item",width=80,anchor='w')
        Data.column("quantity",width=80,anchor='w')
        Data.column("amount",width=80,anchor='w') 
        Data.column("Date",width=80,anchor='w')
        Data.column("time",width=80,anchor='w')

        Data.heading("id",text="Product id",anchor='w')
        Data.heading("Item",text="Item",anchor='w')
        Data.heading("quantity",text="quantity",anchor='w')
        Data.heading("amount",text="Amount",anchor='w')
        Data.heading("Date",text="Date",anchor='w')
        Data.heading("time",text="Time",anchor='w')

        total_expenses = self.recordsystem.weekly_expenses("total expenses")[0]
        all_data = self.recordsystem.weekly_expenses("all data")

        for index,data in enumerate(all_data):
            Data.insert(parent="",index='end',iid=index,values=data)

        Home_page = Label(data_frame,text=f"Weekly total expenses $ {total_expenses}",
                          font=("arial",13,"bold"))
        Home_page.pack(pady=(5,10,))
        Data.pack(expand=True,fill='both')
        exit_button = Button(data_frame,text="Exit",font=10,width=7,command=self.Home)
        exit_button.pack(padx=10,pady=20)

    def Monthly_frame(self):
        self.destroy_widget()

        data_frame = Frame(self.main_frame,
                            width=500,height=400,
                            relief='raised',bd=4)
        data_frame.pack(pady=50)
        data_frame.pack_propagate(False)

        Data = ttk.Treeview(data_frame,
                            columns=("id","Item","quantity","Amount","Date","time"),show='headings')
        
        Data.column("id",width=80,anchor='w')
        Data.column("Item",width=80,anchor='w')
        Data.column("quantity",width=80,anchor='w')
        Data.column("Amount",width=80,anchor='w')
        Data.column("Date",width=80,anchor='w')
        Data.column("time",width=80,anchor='w')

        Data.heading("id",text="Product id",anchor='w')
        Data.heading("Item",text="Item",anchor='w')
        Data.heading("quantity",text="Amount",anchor='w')
        Data.heading("Amount",text="Amount",anchor='w')
        Data.heading("Date",text="Date",anchor='w')
        Data.heading("time",text="Time",anchor='w')

        total_expenses = self.recordsystem.monthly_expenses("total expenses")[0]
        all_data = self.recordsystem.monthly_expenses("all data")

        for index,data in enumerate(all_data):
            Data.insert(parent="",index='end',iid=index,values=data)

        Home_page = Label(data_frame,text=f"Monthly expenses {total_expenses}",
                          font=("arial",13,"bold"))
        Home_page.pack(pady=(5,10,))
        Data.pack(expand=True,fill='both')
        exit_button = Button(data_frame,text="Exit",font=10,width=7,command=self.Home)
        exit_button.pack(padx=10,pady=20)

    def Total_frame(self):
        self.destroy_widget()

        data_frame = Frame(self.main_frame,
                            width=500,height=400,
                            relief='raised',bd=4)
        data_frame.pack(pady=50)
        data_frame.pack_propagate(False)

        Data = ttk.Treeview(data_frame,
                            columns=("id","Item","quantity","Amount","Date","time"),show='headings')
        Data.column("id",width=80,anchor='w')
        Data.column("Item",width=80,anchor='w')
        Data.column("Amount",width=80,anchor='w')
        Data.column("quantity",width=80,anchor='w')
        Data.column("Date",width=80,anchor='w')
        Data.column("time",width=80,anchor='w')

        Data.heading("id",text="Product id",anchor='w')
        Data.heading("Item",text="Item",anchor='w')
        Data.heading("Amount",text="Amount",anchor='w')
        Data.heading("quantity",text="Amount",anchor='w')
        Data.heading("Date",text="Date",anchor='w')
        Data.heading("time",text="Time",anchor='w')
        
        total_expenses = self.recordsystem.yearly_expenses("total expenses")[0]
        all_data = self.recordsystem.yearly_expenses("all data")

        for index,data in enumerate(all_data):
            Data.insert(parent="",index='end',iid=index,values=data)

        Home_page = Label(data_frame,text=f"Yearly total expenses {total_expenses}",
                          font=("arial",13,"bold"))
        Home_page.pack(pady=(5,10,))
        Data.pack(expand=True,fill='both')
        exit_button = Button(data_frame,text="Exit",font=10,width=7,command=self.Home)
        exit_button.pack(padx=10,pady=20)

    def update_frame(self):
        self.destroy_widget()

        Home_page = Label(self.main_frame,text="Insert data page",
                          font=("arial",20,"bold"))
        Home_page.pack(pady=(5,10,))

        input_frame = Frame(self.main_frame,width=500,height=400,relief='raised',bd=4)
        input_frame.pack(pady=50)
        input_frame.pack_propagate(False)

        Item = Label(input_frame,text="Enter item :",font=("arial",10))
        Item.pack(pady=10)

        Item_entry = Entry(input_frame,font=10)
        Item_entry.pack()

        quantity_label = Label(input_frame,text="Enter quantity :",font=("arail",10))
        quantity_label.pack(pady=10)

        quantity_entry = Entry(input_frame,font=10)
        quantity_entry.pack()

        amount_label = Label(input_frame,text="Enter amount :",font=("arail",10))
        amount_label.pack(pady=10)

        amount_entry = Entry(input_frame,font=10)
        amount_entry.pack()

        Product_label = Label(input_frame,text="Enter product id :",font=("arail",10))
        Product_label.pack(pady=10)

        Product_entry = Entry(input_frame,font=10)
        Product_entry.pack()

        buttons_frame = Frame(input_frame)
        buttons_frame.pack(side='bottom')

        Update__button = Button(buttons_frame,text="Update",font=26,width=7,
        command=lambda:self.Update_data(Item_entry,quantity_entry,amount_entry,Product_entry))
        Update__button.pack(side='left',padx=10,pady=20)

        exit_button = Button(buttons_frame,text="Exit",font=10,width=7,command=self.Insert_page)
        exit_button.pack(side='left',padx=10,pady=20)

    def delete_data(self,Product_number):
        Product_key = Product_number.get()
        if len(Product_key) != 0:
            product_number = int(Product_key)
            self.recordsystem.delete(product_number)
            Product_number.delete(0,END)

    def Update_data(self,item,quantity,amount,product_id):
        Item = item.get()
        Quantity = quantity.get()
        Amount = amount.get()
        Product = product_id.get()

        if len(Item) and len(Quantity) and len(Amount) and len(Product) != 0:
            Quantity_int = int(Quantity)
            Amount_int = int(Amount)
            Product_int = int(Product)
            self.recordsystem.update(Item,Quantity_int,Amount_int,Product_int)

            item.delete(0,END)
            amount.delete(0,END)
            quantity.delete(0,END)
            product_id.delete(0,END)

root = Tk()
Record_SystemGui(root)
root.mainloop()
