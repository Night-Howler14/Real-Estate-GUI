from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import sys
import os

# OFFICER -> AGENT DETAILS PAGE
root10 = Tk()
root10.title('Agent PAGE: ALL PROPERTY DETAILS')
root10.geometry('1155x718-150-80')
root10.resizable(False, False)

p1 = PhotoImage(file = 'icon.png') # ICON
root10.iconphoto(False, p1)

bg = PhotoImage(file = "agent_available_1.png")
label1 = Label(root10, image = bg)
label1.place(x=0, y=0)

# Connect to Database
try:
    conn = mysql.connect(host = 'localhost', user = 'root', password = 'Prerna@27')
    mycursor = conn.cursor()
except:
    messagebox.showerror('Error', 'Connection is not established! Try Again')

query = 'use project_realestate'
mycursor.execute(query)

#--------------------------------------------------------------------AGENT DETAILS------------------------------------------------------------------------


# Property table -> Available
column1 = ('P_Id', 'seller Name', 'Seller Mail','For Sale/Rent')
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview', rowheight = 25)
listbox = ttk.Treeview(root10, columns = column1, show = 'headings', height = 13)
# listbox.place(anchor = N, relx = 0.5, y = 100)
listbox.place(x = 150, y = 130)
listbox.config(height=15)

for col in column1:
    listbox.heading(col, text = col)
    listbox.column(col, anchor = CENTER, width = 200)

query = "select p_id, s_name, s_mail, status from Property where a_id = %s and (status = 'AR' or status = 'AS' or status='R' or status='S')"
value = [sys.argv[1]]
# value = ["4PA001"]
mycursor.execute(query, value)
records = mycursor.fetchall()

for i, (p_id, s_name, s_mail, status) in enumerate(records, start = 1):
    if status == 'AS':
        s_or_r = "For Sale"
    if status == 'AR':
        s_or_r = "For Rent"
    if status == 'S':
        s_or_r = "Sold"
    if status == 'R':
        s_or_r = "Rented"
    listbox.insert("", "end", values = (p_id, s_name, s_mail, s_or_r))

root10.mainloop()