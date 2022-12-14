from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql_connection import SqlConnection
class ReaderPage:

    choice_list = ['DOCID','TITLE','PUBNAME']
    def setup_UI(self):
        self.reader_window = Tk()
        self.reader_window.geometry()   
        self.reader_window.resizable(False,False)
 
        self.reader_window.iconbitmap("book1.ico")
        self.reader_window_frame = Frame(self.reader_window,width=1500,height=1500)
     
        self.reader_window.resizable(False,False)
        self.reader_window.propagate(0)
        self.reader_window_frame.grid_propagate(False)
        self.reader_window_frame.grid(row=0,column=0,sticky='news',padx=20,pady=20)
        #self.reader_window_frame.pack()
        self.reader_window.title("Admin Page")

        self._search_doc_label_frame= LabelFrame(self.reader_window_frame,text="Search a Document Using ID, Title, Publisher Name")
        self._search_doc_label_frame.grid(row=0,column=0,sticky="news",padx=20,pady=20)
        
        self.reader_value_entry =  Entry(self._search_doc_label_frame,textvariable=StringVar(), borderwidth=3, relief=SUNKEN, width=23)
        self.reader_value_entry.grid(row=0,column=0)

        self.search_selection_type_input = ttk.Combobox(self._search_doc_label_frame, values=self.choice_list)
        self.search_selection_type_input.grid(row=0,column=1)

        self.reader_button = Button(self._search_doc_label_frame, text="Register", command=self.display_document_data, borderwidth=3)
        self.reader_button.grid(row=1,column=1)

        for widget in self._search_doc_label_frame.winfo_children():
            widget.grid_configure(padx=20,pady=20)



        #Checkout, Reserve, Return
        sql_obj = SqlConnection()
        self.doc_res_chk_frame = LabelFrame(self.reader_window_frame,text="Show Documents",width=1500,height=1500)
        self.doc_res_chk_frame.grid(row=0,column=1,sticky='news',padx=20,pady=20)
    
        self.doc_disp_vsb = ttk.Scrollbar(self.doc_res_chk_frame, orient="vertical")
        self.doc_disp_table_show_doc = ttk.Treeview(self.doc_res_chk_frame,columns=(1,2,3,4),selectmode='browse',yscrollcommand= self.doc_disp_vsb.set)
        self.doc_disp_table_show_doc['show'] ='headings'
        self.doc_disp_vsb.pack(side='right', fill='y')
        self.doc_disp_vsb.config(command= self.doc_disp_table_show_doc.yview)
        self.doc_disp_table_show_doc.pack(side='top',expand=False,fill='none')
        self.doc_disp_table_show_doc.heading(1,text="DOCID")
        self.doc_disp_table_show_doc.heading(2,text="TITLE")
        self.doc_disp_table_show_doc.heading(3,text="PDATE")
        self.doc_disp_table_show_doc.heading(4,text="PUBLISHER NAME")

        row = sql_obj.show_all_documents()
        for data in row:
             self.doc_disp_table_show_doc.insert("","end",values=data)
        checkout_button = Button(self.doc_res_chk_frame, text="Checkout", command=self.display_document_data, borderwidth=3)
        checkout_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none')

        
        reserve_button = Button(self.doc_res_chk_frame, text="Reserve", command=self.display_document_data, borderwidth=3)
        reserve_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none',padx=25)

        
        return_button = Button(self.doc_res_chk_frame, text="Return", command=self.display_document_data, borderwidth=3)
        return_button.pack(in_=self.doc_res_chk_frame,side='left',fill='none',padx=25)
        
        
        self.doc_disp_table_show_doc.bind('<ButtonRelease-1>',self.selectItemFromTree)
        for widget in self.doc_res_chk_frame.winfo_children():
            widget.pack_configure(padx=15,pady=10)

    def selectItemFromTree(self,a):
        curItem = self.doc_disp_table_show_doc.focus()
        
        data = self.doc_disp_table_show_doc.item(curItem)['values']
        print(data[0]) #id
        print(data[1]) #title
        print(data[2]) #pubdate
        print(data[3]) #Publisher Name
        
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