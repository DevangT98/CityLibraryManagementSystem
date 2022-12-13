from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql_connection import SqlConnection

class AdminPage:
        
    reader_type_list = ["Student", "Staff", "Senior Citizen"]
    def go_back(self):
        self.admin_next.withdraw()
        self.admin_window.wm_deiconify()
        
    def switch_page(self):
        self.admin_window.withdraw()    
        self.admin_next = Toplevel()
        self.admin_next.resizable(False,False)  
        self.admin_next.iconbitmap("book1.ico")
        self.admin_next_frame = Frame(self.admin_next)
        self.admin_next_frame.grid(row=0,column=0,sticky="news",padx=20,pady=20)
        self.admin_next.title("Admin Page")
        self.back_button = Button(self.admin_next,text="Go to Previous Page",command=self.go_back,borderwidth=3)
        self.back_button.place(x=1,y=1)
        
        #GUI Functions Call
        self.most_freq_borrowers()    
        self.branch_most_freq_borrowers()
        self.most_borrowed_books()
        self.branch_most_borrowed_books()
        self.admin_next.mainloop()

    #GUI 

    #MOST FREQUENT BORROWERS GUI
    def most_freq_borrowers(self):
        self.most_freq_borrowers_frame = LabelFrame(self.admin_next_frame,text="Most Frequent Borrowers")
        self.most_freq_borrowers_frame.grid(row=0,column=0,sticky="news",padx=20,pady=20)

        self.n_label = Label(self.most_freq_borrowers_frame,text="Enter N: ")
        self.n_label.grid(row=0,column=0)

        n = StringVar()
        self.n_entry = Entry(self.most_freq_borrowers_frame,textvariable=n,borderwidth=3, relief=SUNKEN, width=23)
        self.n_entry.grid(row=1, column=0)

        self.most_freq_borr_button = Button(self.most_freq_borrowers_frame,text="Get Most Frequent Borrowers ",command=self.get_most_freq_borrowers,borderwidth=3)
        self.most_freq_borr_button.grid(row=2,column=0)

        for widget in self.most_freq_borrowers_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)

    #MOST FREQUENT BORROWERS IN BRANCH GUI
    def branch_most_freq_borrowers(self):
        self.branch_most_freq_borrowers_frame = LabelFrame(self.admin_next_frame,text="Most Frequent Borrowers in Branch")
        self.branch_most_freq_borrowers_frame.grid(row=0,column=1,sticky="news",padx=20,pady=20)

        self.n_branch_label = Label(self.branch_most_freq_borrowers_frame,text="Enter N: ")
        self.n_branch_label.grid(row=0,column=0)

        self.n_branch_id_label = Label(self.branch_most_freq_borrowers_frame,text="Enter Branch ID: ")
        self.n_branch_id_label.grid(row=0,column=1)

        n_branch = StringVar()
        n_branch_id = StringVar()
        self.n_branch_entry = Entry(self.branch_most_freq_borrowers_frame,textvariable=n_branch,borderwidth=3, relief=SUNKEN, width=23)
        self.n_branch_entry.grid(row=1, column=0)

        self.n_branch_id_entry = Entry(self.branch_most_freq_borrowers_frame,textvariable=n_branch_id,borderwidth=3, relief=SUNKEN, width=23)
        self.n_branch_id_entry.grid(row=1, column=1)

        self.branch_most_freq_borr_button = Button(self.branch_most_freq_borrowers_frame,text="Get Branch Most Frequent Borrowers ",command=self.get_branch_most_freq_borrowers,borderwidth=3)
        self.branch_most_freq_borr_button.grid(row=2,column=0)

        for widget in self.branch_most_freq_borrowers_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)


    #MOST BORROWED BOOKS
    def most_borrowed_books(self):
        self.most_borrowed_books_frame = LabelFrame(self.admin_next_frame,text="Most Borrowed Books")
        self.most_borrowed_books_frame.grid(row=2,column=0,sticky="news",padx=20,pady=20)

        self.n_most_borrowed_books_label = Label(self.most_borrowed_books_frame,text="Enter N: ")
        self.n_most_borrowed_books_label.grid(row=0,column=0)
    
        n_most_borrowed_books_var = StringVar()
    
        self.n_most_borrowed_books_entry = Entry(self.most_borrowed_books_frame,textvariable=n_most_borrowed_books_var,borderwidth=3, relief=SUNKEN, width=23)
        self.n_most_borrowed_books_entry.grid(row=1, column=0)

        self.n_most_borrowed_books_entry_button = Button(self.most_borrowed_books_frame,text="Get Most Borrowed Books",command=self.get_most_borrowed_books,borderwidth=3)
        self.n_most_borrowed_books_entry_button.grid(row=2,column=0)

        for widget in self.most_borrowed_books_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)

    #MOST BORROWED BOOKS IN BRANCH
    def branch_most_borrowed_books(self):
        self.branch_most_borrowed_books_frame = LabelFrame(self.admin_next_frame,text="Most Borrowed Books in Branch")
        self.branch_most_borrowed_books_frame.grid(row=2,column=1,sticky="news",padx=20,pady=20)

        self.n_branch_most_borrowed_books_label = Label(self.branch_most_borrowed_books_frame,text="Enter N: ")
        self.n_branch_most_borrowed_books_label.grid(row=0,column=0)
    
      
        self.n_branch_most_borrowed_books_id_label = Label(self.branch_most_borrowed_books_frame,text="Enter Branch ID: ")
        self.n_branch_most_borrowed_books_id_label.grid(row=0,column=1)

        n_branch_most_borrowed_books_var = StringVar()
        n_branch_most_borrowed_books_id__var = StringVar()

        self.n_branch_most_borrowed_books_entry = Entry(self.branch_most_borrowed_books_frame,textvariable=n_branch_most_borrowed_books_var,borderwidth=3, relief=SUNKEN, width=23)
        self.n_branch_most_borrowed_books_entry.grid(row=1, column=0)

        self.n_branch_most_borrowed_books_id_entry = Entry(self.branch_most_borrowed_books_frame,textvariable=n_branch_most_borrowed_books_id__var,borderwidth=3, relief=SUNKEN, width=23)
        self.n_branch_most_borrowed_books_id_entry.grid(row=1, column=1)

        self.branch_most_freq_borr_button = Button(self.branch_most_borrowed_books_frame,text="Get Branch Most Borrowed Borrowers ",command=self.get_branch_most_borrowed_books,borderwidth=3)
        self.branch_most_freq_borr_button.grid(row=2,column=0)

        for widget in self.branch_most_borrowed_books_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)



    #WRITE SQL
    
    #MOST FREQUENT BORROWERS SQL
    def get_most_freq_borrowers(self):
        self.sql_obj = SqlConnection()
        self.n_info = self.n_entry.get()
        if self.n_info == '':
             self.n_info = 1
        
        self.res_frame = Toplevel(relief=GROOVE)
        self.res_frame.resizable(False,False)
        vsb = ttk.Scrollbar(self.res_frame, orient="vertical")
        table = ttk.Treeview(self.res_frame,columns=(1,2,3),selectmode='browse',yscrollcommand=vsb.set)
        table['show'] ='headings'
        vsb.pack(side='right', fill='y')
        vsb.config(command=table.yview)
        table.pack()
        table.heading(1,text="Reader ID")
        table.heading(2,text="Reader Name")
        table.heading(3,text="Number of Books")
      

        row = self.sql_obj.show_most_frequent_borrowers(self.n_info)

        for data in row:
            table.insert("","end",values=data)
    
        self.res_frame.mainloop()


    #MOST FREQUENT BORROWERS IN BRANCH
    def get_branch_most_freq_borrowers(self):
        self.sql_obj = SqlConnection()
        self.n_branch_info = self.n_branch_entry.get() 
        self.n_branch_id_info = self.n_branch_id_entry.get()

        if self.n_branch_info == '':
             self.n_info = 1
        if self.n_branch_id_info == '':
            messagebox.showerror("Error!","Please Enter a Branch Number!....")
        else:
            self.res_frame = Toplevel(relief=GROOVE)
            self.res_frame.resizable(False,False)
            vsb = ttk.Scrollbar(self.res_frame, orient="vertical")
            table = ttk.Treeview(self.res_frame,columns=(1,2,3),selectmode='browse',yscrollcommand=vsb.set)
            table['show'] ='headings'
            vsb.pack(side='right', fill='y')
            vsb.config(command=table.yview)
            table.pack()
            table.heading(1,text="Reader ID")
            table.heading(2,text="Reader Name")
            table.heading(3,text="Number of Books")
      
            row = self.sql_obj.show_branch_most_frequenct_borrowers(self.n_info,self.n_branch_id_info)

            for data in row:
                table.insert("","end",values=data)
    
            self.res_frame.mainloop()

    
    #MOST BORROWED BOOKS
    def get_most_borrowed_books(self):
        self.sql_obj = SqlConnection()
        self.n_most_borrowed_info = self.n_branch_entry.get() 
        if self.n_most_borrowed_info == '':
            self.n_most_borrowed_info=1
        self.res_frame = Toplevel(relief=GROOVE)
        self.res_frame.resizable(False,False)
        vsb = ttk.Scrollbar(self.res_frame, orient="vertical")
        table = ttk.Treeview(self.res_frame,columns=(1,2),selectmode='browse',yscrollcommand=vsb.set)
        table['show'] ='headings'
        vsb.pack(side='right', fill='y')
        vsb.config(command=table.yview)
        table.pack()
        table.heading(1,text="Book ID")
        table.heading(2,text="Book Name")
      
        row = self.sql_obj.show_most_borrowed_books(self.n_most_borrowed_info)

        for data in row:
            table.insert("","end",values=data)
    
        self.res_frame.mainloop()

    #MOST BORROWED BOOKS IN BRANCH
    def get_branch_most_borrowed_books(self):

        self.sql_obj = SqlConnection()
        self.n_branch_most_borrowed_info = self.n_branch_most_borrowed_books_entry.get() 
        self.n_branch_most_borrowed_books_id = self.n_branch_most_borrowed_books_id_entry.get()
        if self.n_branch_most_borrowed_info == '':
            self.n_branch_most_borrowed_info=1
        
        if self.n_branch_most_borrowed_books_id == '':
            messagebox.showerror("Error!","Please Enter a Branch Number!....")
        else:
            self.res_frame = Toplevel(relief=GROOVE)
            self.res_frame.resizable(False,False)
            vsb = ttk.Scrollbar(self.res_frame, orient="vertical")
            table = ttk.Treeview(self.res_frame,columns=(1,2),selectmode='browse',yscrollcommand=vsb.set)
            table['show'] ='headings'
            vsb.pack(side='right', fill='y')
            vsb.config(command=table.yview)
            table.pack()
            table.heading(1,text="Book ID")
            table.heading(2,text="Book Name")
        
            row = self.sql_obj.show_branch_most_borrowed_books(self.n_branch_most_borrowed_info,self.n_branch_most_borrowed_books_id)

            for data in row:
                table.insert("","end",values=data)
        
            self.res_frame.mainloop()
 


    def insert_doc(self):
        pass


    def search_doc(self):
        pass

    #PRINT BRANCH
    def get_branch(self):
        self.sql_obj = SqlConnection()

        
    
        self.res_frame = Toplevel(relief=GROOVE)
        self.res_frame.resizable(False,False)
        vsb = ttk.Scrollbar(self.res_frame, orient="vertical")
        table = ttk.Treeview(self.res_frame,columns=(1,2),selectmode='browse',yscrollcommand=vsb.set)
        table['show'] ='headings'
        vsb.pack(side='right', fill='y')
        vsb.config(command=table.yview)
        table.pack()
        table.heading(1,text="Branch Name")
        table.heading(2,text="Branch Location")
      

        row = self.sql_obj.show_branch_details()

        for data in row:
            table.insert("","end",values=data)
    
        self.res_frame.mainloop()
        
        
    def store_data(self):
        self.sql_obj = SqlConnection()
        self.reader_card_no_info = self.reader_card_no_input.get()
        self.reader_type_info = self.reader_type_input.get()
        self.reader_name_info = self.reader_name_input.get()
        self.reader_addr_info = self.reader_addr_input.get()
        self.reader_phone_info = int(self.reader_phone_input.get())

        if not self.reader_card_no_info:
            messagebox.showerror("Error!","Please enter a card number!!....")
            
        else:
            self.sql_obj.insert_reader(
                self.reader_card_no_info,
                self.reader_type_info,
                self.reader_name_info,
                self.reader_addr_info,
                self.reader_phone_info,
            )
            messagebox.showinfo("Success!","Reader Registered!!....")

        self.reader_card_no_input.delete(0, END)
        self.reader_type_input.delete(0, END)
        self.reader_name_input.delete(0, END)
        self.reader_addr_input.delete(0, END)
        self.reader_phone_input.delete(0, END)

    def setupUI(self):
        self.admin_window = Tk()
        self.admin_window.geometry()   
        self.admin_window.resizable(False,False)
        #self.bg_image = PhotoImage(file='G:\\My Drive\\MS - NJIT\\Data Mgmt System Design (CS 631)\\Project\\DMSD_Project\\library.png')
        #self.bg_label_admin = Label(self.admin_window,image=self.bg_image)
        #self.bg_label_admin.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.admin_window.iconbitmap("book1.ico")
        self.admin_frame = Frame(self.admin_window,width=1500,height=1100)
        #self.bg_label = Label(self.admin_frame,image=self.bg_image)
        #self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        self.admin_frame.pack()
        self.admin_window.title("Admin Page")

        #ADD DOCUMENT FRAME
        self.add_doc_label_frame= LabelFrame(self.admin_frame,text="Add a Document Copy")
        self.add_doc_label_frame.grid(row=0,column=0,sticky="news",padx=20,pady=20)

        #docid, copyno,bid,position labels
        self.doc_id_label = Label(self.add_doc_label_frame,text="DocumentID (DocID)")
        self.doc_id_label.grid(row=0,column=0)

        self.copy_no_label = Label(self.add_doc_label_frame,text="No of Copies (CopyNO)")
        self.copy_no_label.grid(row=0,column=1)


        self.bid_label = Label(self.add_doc_label_frame,text="Branch ID (BID)")
        self.bid_label.grid(row=2,column=0)


        self.position_label = Label(self.add_doc_label_frame,text="Copy Position (Position)")
        self.position_label.grid(row=2,column=1)

        #Variables to store input
        self.doc_id = StringVar()
        self.bid = StringVar()
        self.copy_no = StringVar()
        self.position = StringVar()

        #inputs
        add_doc_entry = Entry(self.add_doc_label_frame,textvariable=self.doc_id, borderwidth=3, relief=SUNKEN, width=23)
        add_doc_entry.grid(row=1,column=0)


        copy_no_entry = Entry(self.add_doc_label_frame,textvariable=self.copy_no, borderwidth=3, relief=SUNKEN, width=23)
        copy_no_entry.grid(row=1,column=1)

        bid_entry = Entry(self.add_doc_label_frame,textvariable=self.bid, borderwidth=3, relief=SUNKEN, width=23)
        bid_entry.grid(row=3,column=0)

        position_entry = Entry(self.add_doc_label_frame,textvariable=self.position, borderwidth=3, relief=SUNKEN, width=23)
        position_entry.grid(row=3,column=1)


        add_copy_button = Button(self.add_doc_label_frame,text="Add Copy",command=self.insert_doc,borderwidth=3)
        add_copy_button.grid(row=4,column=0)

        for widget in self.add_doc_label_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)



        #SEARCH DOCUMENT FRAME
        search_doc_label_frame= LabelFrame(self.admin_frame,text="Search Document")
        search_doc_label_frame.grid(row=0,column=1,sticky="news",padx=20,pady=20)

        #Label
        search_doc_id_label = Label(search_doc_label_frame,text="Enter DocID")
        search_doc_id_label.grid(row=0,column=0)

        #variables to store input
        search_doc_id = StringVar()

        #input
        search_doc_id_input = Entry(search_doc_label_frame,textvariable=search_doc_id, borderwidth=3, relief=SUNKEN, width=23)
        search_doc_id_input.grid(row=0,column=1)


        search_doc_id_button = Button(search_doc_label_frame,text="Search Document",command=self.search_doc,borderwidth=3)
        search_doc_id_button.grid(row=1,column=0)


        for widget in search_doc_label_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)



        #Add Reader Frame

        add_new_reader_frame = LabelFrame(self.admin_frame,text='Add new Reader')
        add_new_reader_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

        reader_card_no_label = Label(add_new_reader_frame,text="Reader Card Number", fg="black")
        reader_card_no_label.grid(row=0,column=0)

        reader_type_label = Label(add_new_reader_frame,text="Reader Type", fg="black")
        reader_type_label.grid(row=0,column=1)

        reader_name_label = Label(add_new_reader_frame,text="Reader Name", fg="black")
        reader_name_label.grid(row=2, column=0)

        reader_addr_label = Label(add_new_reader_frame,text="Reader Address", fg="black")
        reader_addr_label.grid(row=2, column=1)

        reader_phone_label = Label(add_new_reader_frame,text="Reader Phone", fg="black")
        reader_phone_label.grid(row=2, column=2)


        self.reader_card_no = StringVar()
        self.reader_name = StringVar()
        self.reader_addr = StringVar()
        self.reader_phone = StringVar()
        self.reader_type = StringVar()

        # inputs
        self.reader_card_no_input = Entry(add_new_reader_frame,textvariable=self.reader_card_no, borderwidth=3, relief=SUNKEN, width=23)
        self.reader_card_no_input.grid(row= 1,column=0)


        self.reader_type.set("Student")  # default value
        self.reader_type_input = ttk.Combobox(add_new_reader_frame, values=self.reader_type_list)
        self.reader_type_input.grid(row=1,column=1)


        self.reader_name_input = Entry(add_new_reader_frame,textvariable=self.reader_name, borderwidth=3, relief=SUNKEN, width=23)
        self.reader_name_input.grid(row=3,column=0)

        self.reader_addr_input = Entry(add_new_reader_frame,textvariable=self.reader_addr, borderwidth=3, relief=SUNKEN, width=23)
        self.reader_addr_input.grid(row=3,column=1)

        self.reader_phone_input = Entry(add_new_reader_frame,textvariable=self.reader_phone, borderwidth=3, relief=SUNKEN, width=23)
        self.reader_phone_input.grid(row=3,column=2)


        self.register_button = Button(add_new_reader_frame, text="Register", command=self.store_data, borderwidth=3)
        self.register_button.grid(row=4,column=0)



        for widget in add_new_reader_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)






        #Print Branch Frame

        branch_det_label_frame = LabelFrame(self.admin_frame,text="Print Branch Info")
        branch_det_label_frame.grid(row=1,column=1,sticky="news",padx=20,pady=20)

        branch_det_button = Button(branch_det_label_frame,text="Get Branch Details",command=self.get_branch,borderwidth=3)
        branch_det_button.grid(row=3,column=3)


        for widget in branch_det_label_frame.winfo_children():
            widget.grid_configure(padx=15,pady=10)



        next_button = Button(self.admin_window,text="Next Page",command=self.switch_page,borderwidth=3,width=15)
        next_button.place(x=813,y=522)

        self.admin_window.mainloop()


#AdminPage.setupUI(AdminPage())