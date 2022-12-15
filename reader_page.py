from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql_connection import SqlConnection
import datetime
import random
class ReaderPage:
    choice_list = ['DOCID','TITLE','PUBNAME']
    def __init__(self,reader_no):
        self.reader_no = reader_no
        #self.setup_UI()

    def setup_UI(self):
        self.reader_window = Tk()
        self.reader_window.configure(background='#E0E0FF')
        self.reader_window.geometry()   
        self.reader_window.resizable(False,False)

        self.reader_window.iconbitmap("book1.ico")
        self.reader_window_frame = Frame(self.reader_window,width=1800,height=1800,bg='#E0E0FF')
     
        self.reader_window.resizable(False,False)
        self.reader_window.propagate(0)
        self.reader_window_frame.grid_propagate(False)
        self.reader_window_frame.grid(row=0,column=0,sticky='news',padx=20,pady=20)
        #self.reader_window_frame.pack()
        self.reader_window.title("Reader Page")

        self.reader_welcome_label = Label(self.reader_window,font=("Trajan Pro", 16, "bold"),text="Welcome, "+str(self.reader_no),bg='#E0E0EE')
        self.reader_welcome_label.place(x=10,y=10)
        self._search_doc_label_frame= LabelFrame(self.reader_window_frame,text="Search a Document Using ID, Title, Publisher Name",bg='#ffffeb')
        self._search_doc_label_frame.grid(row=0,column=0,sticky="news",padx=20,pady=20)
        
        self.reader_value_entry =  Entry(self._search_doc_label_frame,textvariable=StringVar(), borderwidth=3, relief=SUNKEN, width=23)
        self.reader_value_entry.grid(row=0,column=0)

        self.search_selection_type_input = ttk.Combobox(self._search_doc_label_frame, values=self.choice_list)
        self.search_selection_type_input.grid(row=0,column=1)

        self.reader_button = Button(self._search_doc_label_frame, text="Search Document", command=self.display_document_data, borderwidth=3)
        self.reader_button.grid(row=1,column=1)

        for widget in self._search_doc_label_frame.winfo_children():
            widget.grid_configure(padx=20,pady=20)



        #Checkout, Reserve, Return
        sql_obj = SqlConnection()
        self.doc_res_chk_frame = LabelFrame(self.reader_window_frame,text="Show Documents",width=1500,height=1500,bg='#ffffeb')
        self.doc_res_chk_frame.grid(row=0,column=1,sticky='news',padx=20,pady=20)
    
        self.doc_disp_vsb = ttk.Scrollbar(self.doc_res_chk_frame, orient="vertical")
        self.doc_disp_hsb = ttk.Scrollbar(self.doc_res_chk_frame, orient="horizontal")

        self.doc_disp_table_show_doc = ttk.Treeview(self.doc_res_chk_frame,columns=(1,2,3,4,5,6,7),selectmode='browse',yscrollcommand= self.doc_disp_vsb.set,xscrollcommand=self.doc_disp_hsb.set)
        self.doc_disp_table_show_doc['show'] ='headings'
        self.doc_disp_vsb.pack(side='right', fill='y')
        self.doc_disp_hsb.pack(side='bottom', fill='x')
        self.doc_disp_vsb.config(command= self.doc_disp_table_show_doc.yview)
        self.doc_disp_hsb.config(command= self.doc_disp_table_show_doc.xview)
        self.doc_disp_table_show_doc.pack(side='top',expand=True,fill='x')
        self.doc_disp_table_show_doc.column(1,width=60,minwidth=60,stretch=NO)
        self.doc_disp_table_show_doc.heading(1,text="DOCID")
        self.doc_disp_table_show_doc.column(2,width=110,minwidth=110,stretch=NO)
        self.doc_disp_table_show_doc.heading(2,text="TITLE")
        self.doc_disp_table_show_doc.column(3,width=60,minwidth=60,stretch=NO)
        self.doc_disp_table_show_doc.heading(3,text="COPY Number")
        self.doc_disp_table_show_doc.column(4,width=110,minwidth=110,stretch=NO)
        self.doc_disp_table_show_doc.heading(4,text="COPY POSITION")
        self.doc_disp_table_show_doc.column(5,width=60,minwidth=60,stretch=NO)
        self.doc_disp_table_show_doc.heading(5,text="Branch ID")
        self.doc_disp_table_show_doc.column(6,width=100,minwidth=100,stretch=NO)
        self.doc_disp_table_show_doc.heading(6,text="PDATE")
        self.doc_disp_table_show_doc.column(7,width=170,minwidth=170,stretch=YES)
        self.doc_disp_table_show_doc.heading(7,text="PUBLISHER NAME")


        row = sql_obj.show_all_documents()
        for data in row:
             self.doc_disp_table_show_doc.insert("","end",values=data)

        checkout_button = Button(self.doc_res_chk_frame, text="Checkout", command=self.borrow_book, borderwidth=3)
        checkout_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none')

        
        reserve_button = Button(self.doc_res_chk_frame, text="Reserve", command=self.reserve_book, borderwidth=3)
        reserve_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none',padx=25)

        
        return_button = Button(self.doc_res_chk_frame, text="Return", command=self.return_book, borderwidth=3)
        return_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none',padx=25)
        

        self.doc_disp_table_show_doc.bind('<ButtonRelease-1>',self.selectItemFromTree)

        for widget in self.doc_res_chk_frame.winfo_children():
            widget.pack_configure(padx=15,pady=10)

    def return_book(self):
        sql_obj = SqlConnection()
        
        now = datetime.datetime.now()
    
        formatted_date = now.utcnow().replace(microsecond=0)
    
        #sql_obj.return_book_sql(bor_no,formatted_date)

        self.return_display_frame = Toplevel(relief=GROOVE)
        self.return_display_frame.resizable(False,False)
        bor_disp_vsb = ttk.Scrollbar(self.return_display_frame, orient="vertical")
        self.bor_disp_table = ttk.Treeview(self.return_display_frame,columns=(1,2,3,4,5,6),selectmode='browse',yscrollcommand=bor_disp_vsb.set)
        self.bor_disp_table['show'] ='headings'
        bor_disp_vsb.pack(side='right', fill='y')
        bor_disp_vsb.config(command=self.bor_disp_table.yview)
        self.bor_disp_table.pack()
        self.bor_disp_table.heading(1,text="Borrow Number")
        self.bor_disp_table.heading(2,text="Borrow Date")
        self.bor_disp_table.heading(3,text="TITLE")
        self.bor_disp_table.heading(4,text="COPY NO")
        self.bor_disp_table.heading(5,text="DOC ID")
        self.bor_disp_table.heading(6,text="BRANCH ID")
      
       # if search_selection_type == 'DOCID':
            #row = self.sql_obj.get_doc_details(int(reader_value),search_selection_type)
        #else:
            #row = self.sql_obj.get_doc_details(reader_value,search_selection_type)

        button_return_doc  = Button(self.return_display_frame, text="Return Document", command=self.return_item, borderwidth=3)
        button_return_doc.pack(side='bottom',expand=False,anchor='center',padx=20,pady=20)
        row = sql_obj.show_borrowed_docs()

        for data in row:
            self.bor_disp_table.insert("","end",values=data)

       # self.bor_disp_table.bind('<ButtonRelease-1>',self.selectReturnItemFromTree)

        #curItem = bor_disp_table.focus()
        
        #data = bor_disp_table.item(curItem)['values']
        self.return_display_frame.mainloop()

    def reserve_book(self):
        self.selected_item = self.doc_disp_table_show_doc.focus()
        self.item_det = self.doc_disp_table_show_doc.item(self.selected_item) # dictionary
        
        res_no =random.randint(10000,99999)
        
        doc_id =self.item_det['values'][0]
        copy_no = self.item_det['values'][2]
        branch_id = self.item_det['values'][4]
        reader_id = self.reader_no
        now = datetime.datetime.now()
        formatted_date = now.utcnow().replace(microsecond=0)
        sql_obj = SqlConnection()
        sql_obj.insert_in_reserves(res_no,doc_id,copy_no,branch_id,reader_id,formatted_date)
        messagebox.showinfo("Success!","Document Copy Reserved!!.... ")

    def borrow_book(self):

        self.selected_item = self.doc_disp_table_show_doc.focus()
        self.item_det = self.doc_disp_table_show_doc.item(self.selected_item) # dictionary
        
        bor_no =random.randint(10000,99999)
        
        doc_id =self.item_det['values'][0]
        copy_no = self.item_det['values'][2]
        branch_id = self.item_det['values'][4]
        reader_id = self.reader_no
        
        now = datetime.datetime.now()
        formatted_date = now.utcnow().replace(microsecond=0)
        sql_obj = SqlConnection()
        sql_obj.insert_in_borrowings(bor_no,doc_id,copy_no,branch_id,reader_id,formatted_date)
        messagebox.showinfo("Success!","Document Copy Borrowed!!.... ")


    def return_item(self):

        self.selected_item = self.bor_disp_table.focus()
        self.item_det = self.bor_disp_table.item(self.selected_item)
        bor_no = self.item_det['values'][0]

        sql_obj = SqlConnection()

        return_time = datetime.datetime.now()
    
        return_date_time = return_time.utcnow().replace(microsecond=0)
        print(bor_no,return_date_time)
        sql_obj.return_book_sql(bor_no,return_date_time)
    
    # def selectReturnItemFromTree(self,a):
    #     curItem = self.bor_disp_table.focus()
        
    #     data = self.bor_disp_table.item(curItem)['values']
    #     bor_no = data[0]
    #     sql_obj = SqlConnection
    #     now = datetime.datetime.now()
    #     formatted_date = now.utcnow().replace(microsecond=0)
    #     sql_obj.return_book(bor_no,formatted_date)


    def selectItemFromTree(self,a):
        curItem = self.doc_disp_table_show_doc.focus()
        
        data = self.doc_disp_table_show_doc.item(curItem)['values']
        print(data)
        

    def display_document_data(self):

        reader_value = self.reader_value_entry.get()
        search_selection_type = self.search_selection_type_input.get()


        self.sql_obj = SqlConnection()
        
    
        self.reader_display_frame = Toplevel(relief=GROOVE)
        self.reader_display_frame.resizable(False,False)
        doc_disp_vsb = ttk.Scrollbar(self.reader_display_frame, orient="vertical")
        doc_disp_table = ttk.Treeview(self.reader_display_frame,columns=(1,2,3,4),selectmode='browse',yscrollcommand=doc_disp_vsb.set)
        doc_disp_table['show'] ='headings'
        doc_disp_vsb.pack(side='right', fill='y')
        doc_disp_vsb.config(command=doc_disp_table.yview)
        doc_disp_table.pack()
        doc_disp_table.heading(1,text="DOCID")
        doc_disp_table.heading(2,text="TITLE")
        doc_disp_table.heading(3,text="PDATE")
        doc_disp_table.heading(4,text="PUBLISHER NAME")
      
        if search_selection_type == 'DOCID':
            row = self.sql_obj.get_doc_details(int(reader_value),search_selection_type)
        else:
            row = self.sql_obj.get_doc_details(reader_value,search_selection_type)

        for data in row:
            doc_disp_table.insert("","end",values=data)
    
        self.reader_display_frame.mainloop()