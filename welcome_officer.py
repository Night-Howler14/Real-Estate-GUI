from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
import os

# OFFICER WELCOME PAGE
root5 = Tk()
root5.title('OFFICER HOME PAGE: WELCOME OFFICER')
root5.geometry('1155x718-150-80')
root5.resizable(False, False)

p1 = PhotoImage(file='icon.png') # ICON
root5.iconphoto(False, p1)

bg = PhotoImage(file = "BG_welcome_office_1.png")
label1 = Label(root5, image=bg)
label1.place(x = 0, y = 0)

# Connect to Database
mydb = mysql.connect(host = "localhost", user = "root", password = "Prerna@27", database = "project_realestate")
mycursor = mydb.cursor()

# Redirecting to Agent Details Page
def signin():
    global bg_wa
    
    if aid.get() == '':
        messagebox.showerror('Error', 'All fields are required!')
    else:
        value = aid.get()
        
        cmdline = "python office_agent_details.py " + value
        os.system(cmdline)



# create a treeview widget -> Agent Id and Commission Rate table
tree = ttk.Treeview(root5, columns = ("column1", "column2"), show = "headings")
tree.column("column1", width = 350, anchor = "center")
tree.column("column2", width = 350, anchor = "center")
tree.heading("column1", text = "Agent ID")
tree.heading("column2", text = "Commission Rate")
tree.pack(padx = 10, pady = 10)

style = ttk.Style()
style.theme_use("clam")
style.configure(tree, showtree = 'True')

# set the position of the treeview widget using the place() method
tree.place(x = 50, y = 100)

# Query
mycursor.execute("SELECT a_id, a_rate FROM agent")
result = mycursor.fetchall()

for row in result:
    tree.insert("", "end", values = row)

# selecting a row in the table
def on_tree_select(event):
    # Get the selected row
    selected_row = tree.focus()

    # Get the values from the selected row
    values = tree.item(selected_row, 'values')

    # Update the input field
    aid.delete(0, END)
    aid.insert(0, values[0])

# Bind the <<TreeviewSelect>> event to the on_tree_select function
tree.bind("<<TreeviewSelect>>", on_tree_select)

# aid to agent details
aid = Entry(root5, width = 29, fg = 'white', border = 0, bg = '#292F33', font = ('Microsoft YaHei UI Light', 15))
aid.place(x = 267, y = 479)    

# submit button
button = Button(root5, text = 'SUBMIT', width = 18, command = signin , cursor = 'hand2', background= 'black', foreground= 'white', activebackground = 'black', activeforeground = 'grey', font = ('yu gothic ui', 15, 'bold'), border = 0)
button.place(x = 481, y = 555)

root5.mainloop()