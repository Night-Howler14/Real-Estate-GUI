import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import sys
import os

# AGENT-> SOLD/RENT DETAIL
root8 = Tk()
root8.title('AGENT PAGE: SOLD/RENT DETAILS')
root8.geometry('1155x718-150-80')
root8.resizable(False, False)

# ICON
p1 = PhotoImage(file = 'icon.png')
root8.iconphoto(False, p1)


#  CONNECTION TO DATABASE
try:
    conn = mysql.connect(host = 'localhost', user = 'root', password = 'Prerna@27', database = "project_realestate")
    mycursor = conn.cursor()
    
    query = 'use project_realestate'
    mycursor.execute(query)
    
except:
    messagebox.showerror('Error', 'Connection is not established! Try Again')
    
    
# def delete():
#    for item in listbox.get_children():
#       listbox.delete(item)   
                                    
        
bg_br = PhotoImage(file = "BG_agent_sold_1.png") # BACKGROUND_AGENT_SOLD
label_br = Label(root8, image = bg_br)
label_br.place(x = 0, y = 0)

# Table of PROPERTY details
column_list = ('P_Id', 'Status', 'City', 'Locality', 'Pincode', 'Area(in Sq. ft.)', 'Price(in Rs.)', 'No. Of Bedrooms', 'Year Of Construction')
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview', rowheight = 32)
listbox = ttk.Treeview(root8, columns = column_list, show = 'headings')

listbox.column('#1', anchor = CENTER, width = 80)
listbox.column('#2', anchor = CENTER, width = 104)
listbox.column('#3', anchor = CENTER, width = 104)
listbox.column('#4', anchor = CENTER, width = 104)
listbox.column('#5', anchor = CENTER, width = 104)
listbox.column('#6', anchor = CENTER, width = 104)
listbox.column('#7', anchor = CENTER, width = 104)   
listbox.column('#8', anchor = CENTER, width = 104)   
listbox.column('#9', anchor = CENTER, width = 120)   

for col in column_list:
    listbox.heading(col, text = col)
    listbox.grid(row = 1, column = 0, columnspan = 2)
    listbox.place(x = 180, y = 120)
    

# SHOW TABLE DATA   
messagebox.showinfo('Success', 'Welcome to Sold/Rent Page')

query = 'select p_id, status, city, locality, pincode, area, price, bedrooms, yoc from Property where a_id = %s and (status = "R" or status = "S")'
mycursor.execute(query, [sys.argv[1]])
# query = 'select p_id, status, city, locality, pincode, area, price, bedrooms, yoc from Property where a_id = "4PA001" and (status = "R" or status = "S")'
# mycursor.execute(query)
records = mycursor.fetchall()
print(records)

for i, (p_id, status, city, locality, pincode, area, price, bedrooms, yoc) in enumerate(records, start = 1):
    if status == 'S':
        s_or_r = "Sold"
    if status == 'R':
        s_or_r = "Rented"
    listbox.insert("", "end", values = (p_id, s_or_r, city, locality, pincode, area, price, bedrooms, yoc))

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
pid = Entry(root8, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))
pid.place(x = 658, y = 563)

def topB():
    if pid.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        value = pid.get()
        # value = pid
        # root8.withdraw()
        os.system("python agent_rent_sold_buyer_details.py " + str(value))
        # root8.destroy()
    
# BUTTONS for CONFIRMATION
buttonS = Button(root8, text = 'SUBMIT', width = 8, background= '#E5E5E5', foreground= 'black', activebackground = '#E5E5E5', activeforeground = 'grey', font = ('yu gothic ui', 13, 'bold'), border = 0, command = topB).place(x = 920, y = 558)


root8.mainloop()