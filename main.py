from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql_connection import SqlConnection


reader_type_list = ["Student", "Staff", "Senior Citizen"]


def store_data():
    sql_obj = SqlConnection()
    reader_card_no_info = reader_card_no_input.get()
    reader_type_info = reader_type_input.get()
    reader_name_info = reader_name_input.get()
    reader_addr_info = reader_addr_input.get()
    reader_phone_info = int(reader_phone_input.get())

    if not reader_card_no_info:
        messagebox.showerror("Error!","Please enter a card number!!..")
        
    else:
        sql_obj.insert_reader(
            reader_card_no_info,
            reader_type_info,
            reader_name_info,
            reader_addr_info,
            reader_phone_info,
        )
        

    reader_card_no_input.delete(0, END)
    reader_type_input.delete(0, END)
    reader_name_input.delete(0, END)
    reader_addr_input.delete(0, END)
    reader_phone_input.delete(0, END)


user_window = Tk()
user_window.geometry("640x400")
frame = Frame(user_window,width=640,height=400)
frame.pack()
user_window.title("Register Reader")

#Labels
reader_card_no_label = Label(frame,text="Reader Card Number", fg="black")
reader_card_no_label.place(x=150, y=100)

reader_type_label = Label(frame,text="Reader Type", fg="black")
reader_type_label.place(x=150, y=150)

reader_name_label = Label(frame,text="Reader Name", fg="black")
reader_name_label.place(x=150, y=200)

reader_addr_label = Label(frame,text="Reader Address", fg="black")
reader_addr_label.place(x=150, y=250)

reader_phone_label = Label(frame,text="Reader Phone", fg="black")
reader_phone_label.place(x=150, y=300)

# Variables to Store input
reader_card_no = StringVar()
reader_name = StringVar()
reader_addr = StringVar()
reader_phone = StringVar()
reader_type = StringVar()

# inputs
reader_card_no_input = Entry(frame,textvariable=reader_card_no, borderwidth=3, relief=SUNKEN, width=23)
reader_card_no_input.place(x=350, y=100)


reader_type.set("Student")  # default value
# reader_type_input = OptionMenu(user_window, reader_type, *reader_type_list)
reader_type_input = ttk.Combobox(frame, values=reader_type_list)
reader_type_input.place(x=350, y=150)


reader_name_input = Entry(frame,textvariable=reader_name, borderwidth=3, relief=SUNKEN, width=23)
reader_name_input.place(x=350, y=200)

reader_addr_input = Entry(frame,textvariable=reader_addr, borderwidth=3, relief=SUNKEN, width=23)
reader_addr_input.place(x=350, y=250)

reader_phone_input = Entry(frame,textvariable=reader_phone, borderwidth=3, relief=SUNKEN, width=23)
reader_phone_input.place(x=350, y=300)


# Button

register_button = Button(frame, text="Register", command=store_data, borderwidth=3)
register_button.place(x=250, y=350)


user_window.mainloop()
