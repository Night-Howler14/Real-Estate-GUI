import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import sys

# AGENT -> BUYER (SOLD/RENT) DETAILS
root9 = Tk()
root9.title('AGENT PAGE: BUYER (SOLD/RENT) DETAILS')
root9.geometry('1155x718-150-80')
root9.resizable(False, False)

# ICON
p1 = PhotoImage(file = 'icon.png')
root9.iconphoto(False, p1)


#  CONNECTION TO DATABASE
try:
    conn = mysql.connect(host = 'localhost', user = 'root', password = 'Prerna@27', database = "project_realestate")
    mycursor = conn.cursor()
    
    query = 'use project_realestate'
    mycursor.execute(query)
    
except:
    messagebox.showerror('Error', 'Connection is not established! Try Again')
                                        
        
bg_br = PhotoImage(file = "BG_buyer_details_sold_1.png") # BACKGROUND_AGENT_SOLD
label_br = Label(root9, image = bg_br)
label_br.place(x = 0, y = 0)


# SHOW TABLE DATA   
messagebox.showinfo('Success', 'Welcome to Buyer Details Page')

query = 'select b_name, b_mail, status, dob from Sales where p_id = %s and (status = "S" or status = "R")'
mycursor.execute(query, [sys.argv[1]])
# query = 'select b_id, b_name, b_mail, status, dob from Sales where p_id = 201 and (status = "S" or status = "R")'
# mycursor.execute(query)
records = mycursor.fetchone()
print(records)

    
# BUYER details
bname = Label(root9, text = records[0], fg = "#D4D4D4", bg = "#292F33", font = ("yu gothic ui", 20, 'bold')).place(x = 275, y = 187)
bmail = Label(root9, text = records[1], fg = "#D4D4D4", bg = "#292F33", font = ("yu gothic ui", 20, 'bold')).place(x = 275, y = 232)
dob = Label(root9, text = records[3], fg = "#D4D4D4", bg = "#292F33", font = ("yu gothic ui", 20, 'bold')).place(x = 320, y = 280)

if(records[2] == "R"):
    # create another treeview widget
    tree1 = ttk.Treeview(root9, columns = ("column1"))
    
    query = 'select duration from Rent where p_id = %s'
    mycursor.execute(query, [sys.argv[1]])
    # query = 'select duration from Rent where p_id = 201'
    # mycursor.execute(query)
    
    records1 = mycursor.fetchall()
    print(records1)

    for row1 in records1:
        tree1.insert("", "end", values = row1)
        
    time = Label(root9, text = row1[0], fg = "#D4D4D4", bg = "#292F33", font = ("yu gothic ui", 20, 'bold')).place(x = 570, y = 325)

elif(records[2] == "S"):
    time = Label(root9, text = "--NIL--", fg = "#D4D4D4", bg = "#292F33", font = ("yu gothic ui", 20, 'bold')).place(x = 570, y = 325)


root9.mainloop()