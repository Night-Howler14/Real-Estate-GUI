from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import sys
import os

# OFFICER -> AGENT DETAILS PAGE
root10 = Tk()
root10.title('OFFICER HOME PAGE: AGENT DETAILS')
root10.geometry('1155x718-150-80')
root10.resizable(False, False)

p1 = PhotoImage(file = 'icon.png') # ICON
root10.iconphoto(False, p1)

bg = PhotoImage(file = "BG_agent_details.png")
label1 = Label(root10, image = bg)
label1.place(x=0, y=0)

# Connect to Database
try:
    conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@')
    mycursor = conn.cursor()
except:
    messagebox.showerror('Error', 'Connection is not established! Try Again')

query = 'use realestate'
mycursor.execute(query)

#--------------------------------------------------------------------AGENT DETAILS------------------------------------------------------------------------

# QUERY for Agent Details
query = "select * from Agent where a_id = %s"
value = [sys.argv[1]]
# query = "select * from Agent where a_id = '4PA001'"
# mycursor.execute(query)
mycursor.execute(query, value)
row = mycursor.fetchone()

messagebox.showinfo('Info', 'Showing Agent Details!')

aid = Label(root10, text = row[0], fg = "#224957", bg = "#E5E5E5", font = ("yu gothic ui", 20, 'bold')).place(x=275, y=140)
name = Label(root10, text = row[2], fg = "#224957", bg = "#E5E5E5", font = ("yu gothic ui", 20, 'bold')).place(x=275, y=185)
mail = Label(root10, text = row[3], fg = "#224957", bg = "#E5E5E5", font = ("yu gothic ui", 20, 'bold')).place(x=275, y=230)
rate = Label(root10, text = row[4], fg = "#224957", bg = "#E5E5E5", font = ("yu gothic ui", 20, 'bold')).place(x=320, y=271)

#-----------------------------------------------------------------------FUNCTIONS ava_com()-------------------------------------------------------------------------------------

def ava_com():
    # Office -> Agent's Available Property
    messagebox.showinfo('Info', "Showing Agent's Available Properties!")
    
    root11 = Toplevel(root10)
    root11.title("OFFICER PAGE: AGENT'S AVAILABLE PROPERTY DETAILS")
    root11.geometry('1155x718-150-80')
    root11.resizable(False, False)
    
    p1 = PhotoImage(file = 'icon.png') # ICON
    root11.iconphoto(False, p1)

    bg = PhotoImage(file = "BG_matched_office.png")
    label1 = Label(root11, image = bg)
    label1.place(x = 0, y = 0)
    
    # Property table -> Available
    column1 = ('P_Id', 'City', 'Locality', 'Pincode', 'Area(in sq. ft.)', 'Price(in Rs.)', 'No. Of Bedroom', 'Year Of Contruc.', 'For Sale/Rent')
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight = 32)
    listbox = ttk.Treeview(root11, columns = column1, show = 'headings', height = 13)
    # listbox.place(anchor = N, relx = 0.5, y = 100)
    listbox.place(x = 40, y = 120)

    for col in column1:
        listbox.heading(col, text = col)
        listbox.column(col, anchor = CENTER, width = 100)
    
    query = "select p_id, city, locality, pincode, area, price, bedrooms, yoc, status from Property where a_id = %s and (status = 'AR' or status = 'AS')"
    mycursor.execute(query, value)
    records = mycursor.fetchall()
    
    for i, (p_id, city, locality, pincode, area, price, bedrooms, yoc, status) in enumerate(records, start = 1):
        if status == 'AS':
            s_or_r = "Sale"
        if status == 'AR':
            s_or_r = "Rent"
        listbox.insert("", "end", values = (p_id, city, locality, pincode, area, price, bedrooms, yoc, s_or_r))

    root11.mainloop()

#-----------------------------------------------------------------------FUNCTIONS sol_com()-------------------------------------------------------------------------------------

def sol_com():
    messagebox.showinfo('Info', "Showing Agent's Sold Properties!")

    # Office -> Agent's Sold Property
    root12 = Toplevel(root10)
    root12.title("OFFICER PAGE: AGENT'S SOLD PROPERTY DETAILS")
    root12.geometry('1155x718-150-80')
    root12.resizable(False, False)
    
    p1 = PhotoImage(file = 'icon.png') # ICON
    root12.iconphoto(False, p1)
    
    bg = PhotoImage(file = "BG_agent_sold.png")
    label1 = Label(root12, image = bg)
    label1.place(x = 0, y = 0)
    
    # Property table -> Sold/Rented
    column1 = ('P_Id', 'City', 'Locality', 'Pincode', 'Area(in sq. ft.)', 'Price(in Rs.)', 'No. Of Bedroom', 'Year Of Const.', 'Sold/Rented')
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight = 32)
    listbox = ttk.Treeview(root12, columns = column1, show = 'headings', height = 11)
    # listbox.place(anchor = N, relx = 0.5, y = 100)
    listbox.place(x = 250, y = 120)
    
    for col in column1:
        listbox.heading(col, text = col)
        listbox.column(col, anchor = CENTER, width = 90)
    
    query = "select p_id, city, locality, pincode, area, price, bedrooms, yoc, status from Property where a_id = %s and (status = 'R' or status = 'S')"
    mycursor.execute(query, value)
    records = mycursor.fetchall()
    
    for i, (p_id, city, locality, pincode, area, price, bedrooms, yoc, status) in enumerate(records, start = 1):
        if status == 'S':
            s_or_r = "Sold"
        if status == 'R':
            s_or_r = "Rented"
        listbox.insert("", "end", values = (p_id, city, locality, pincode, area, price, bedrooms, yoc, s_or_r))
    
    # choose selected row p_id
    def on_tree_select(event):
        # Get the selected row
        selected_row = listbox.focus()

        # Get the values from the selected row
        values = listbox.item(selected_row, 'values')

        # Update the input field
        pid.delete(0, END)
        pid.insert(0, values[0])

    # Bind the <<TreeviewSelect>> event to the on_tree_select function
    listbox.bind("<<TreeviewSelect>>", on_tree_select)

    # pid ENTRY
    pid = Entry(root12, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))
    pid.place(x = 658, y = 563)

    def topOB():
        if pid.get() == '':
            messagebox.showerror('Error', 'All fields are required!')
        else:
            value = pid.get()
            # value = pid
            # root12.withdraw()
            os.system("python office_agent_rent_sold_buyer_details.py " + str(value))
            # root12.destroy()
    
    # BUTTONS for CONFIRMATION
    buttonS = Button(root12, text = 'SUBMIT', width = 8, background= '#224957', foreground= 'white', activebackground = '#224957', activeforeground = 'black', font = ('yu gothic ui', 13, 'bold'), border = 0, command = topOB).place(x = 920, y = 558)

    root12.mainloop()

#-----------------------------------------------------------------------BUTTONS-------------------------------------------------------------------------------------

# Buttons for Available and Sold Property 
ava_button = Button(root10, text = "VIEW\nAVAILABLE\nPROPERTIES", fg = "white", bg = "#224957", activeforeground = "black", activebackground = "#224957", font = ("yu gothic ui", 12), width = 11, border = 0, command = ava_com).place(x = 370, y = 527)
sold_button = Button(root10, text = "VIEW\nSOLD/RENTED\nPROPERTIES", fg = "white", bg = "#224957", activeforeground = "black", activebackground = "#224957", font = ("yu gothic ui", 12), width = 11, border = 0, command = sol_com).place(x = 676, y = 531)

root10.mainloop()