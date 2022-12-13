from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql_connection import SqlConnection
from admin_page import AdminPage
class MainPage:

    def show_admin_login(self):
        self.admin_login_page = Toplevel()
        self.admin_login_page_frame = Frame(self.admin_login_page,width=500,height=500)
        self.admin_login_page.resizable(False,False)
        self.admin_login_page.propagate(0)
        self.admin_login_page_frame.grid_propagate(False)
        self.admin_login_page_frame.grid(row=0,column=0,sticky='news',padx=20,pady=20)
        self.id_label = Label(self.admin_login_page_frame,text="Enter ID")
        self.id_label.grid(row=0,column=0,sticky="")

        self.admin_id = StringVar()
        self.admin_pass = StringVar()

        self.id_entry = Entry(self.admin_login_page_frame,textvariable=self.admin_id,borderwidth=3, relief=SUNKEN, width=23)
        self.id_entry.grid(row = 0, column=1)

        self.password_label = Label(self.admin_login_page_frame,text="Enter Password")
        self.password_label.grid(row=2,column=0)

        self.password_entry = Entry(self.admin_login_page_frame,textvariable=self.admin_pass,borderwidth=3, relief=SUNKEN, width=23,show='*')
        self.password_entry.grid(row=2,column=1)

        self.login_button = Button(self.admin_login_page_frame,text="Login",command=self.login_admin,borderwidth=3)
        self.login_button.grid(row=3,column=1)

        for widget in self.admin_login_page_frame.winfo_children():
                widget.grid(padx=20,pady=20)

    def login_admin(self):

        id = self.id_entry.get()
        password = self.password_entry.get()

        if not id or not password:
            messagebox.showerror("Error!","Please Enter ID and Password!!....",parent=self.reader_page)
        else:
            self.sql_obj = SqlConnection()

            if self.sql_obj.validate_admin(id,password):
                self.main_window.destroy()
                AdminPage.setupUI(AdminPage())
            else:
                messagebox.showerror("Error!","Invalid ID or Password!!....",parent=self.reader_page)

    def show_reader_page(self):
        self.reader_page = Toplevel()
        self.reader_page_frame = Frame(self.reader_page,width=500,height=500)
        self.reader_page.resizable(False,False)
        self.reader_page.propagate(0)
        self.reader_page_frame.grid_propagate(False)
        self.reader_page_frame.grid(row=0,column=0,sticky='news',padx=20,pady=20)
        self.reader_id_label = Label(self.reader_page_frame,text="Enter Reader Card Number")
        self.reader_id_label.grid(row=0,column=0,sticky="")

        self.reader_id = StringVar()

        self.reader_id_entry = Entry(self.reader_page_frame,textvariable=self.reader_id,borderwidth=3, relief=SUNKEN, width=23)
        self.reader_id_entry.grid(row=0, column=1)

    
        self.reader_login_button = Button(self.reader_page_frame,text="Login",command=self.login_reader,borderwidth=3)
        self.reader_login_button.grid(row=1,column=1)

        for widget in self.reader_page_frame.winfo_children():
                widget.grid(padx=20,pady=20)

    def login_reader(self):
        reader_card_no_info = self.reader_id_entry.get()
        if not reader_card_no_info or reader_card_no_info=='':
            messagebox.showerror("Error!","Please Enter a Reader ID!!....",parent=self.reader_page)
        else:
            self.sql_obj = SqlConnection()

            if self.sql_obj.validate_reader(int(reader_card_no_info)):
                self.main_window.destroy()
                AdminPage.setupUI(AdminPage())
            else:
                messagebox.showerror("Error!","Reader Doesn't Exist!!....",parent=self.reader_page) 

    def setup_UI(self):

        self.main_window = Tk()
        self.main_window.geometry("500x500")
        self.main_frame = Frame(self.main_window,width=500,height=500)
        self.main_frame.grid(row=0,column=0,sticky='news')
        self.main_window.title("Main Menu")
        self.main_window.resizable(False,False)
        self.reader_button = Button(self.main_frame, text="Reader Login",borderwidth=3,height=2,command=self.show_reader_page)

        self.reader_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.admin_button = Button(self.main_frame,text='Admin Login',borderwidth=3,height=2,command=self.show_admin_login)
        self.admin_button.place(relx=0.5, rely=0.4, anchor=CENTER)




        self.main_window.mainloop()

MainPage.setup_UI(MainPage())