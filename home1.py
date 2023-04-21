from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk
import os 


# root -> loading
# root1 -> home_page
# root2 -> agent_login_cred
# root3 -> office_login_cred
# root4 -> agent_login_page
# root5 -> office_login_page
# root6 -> buyer_req(Agent)
# root7 -> buyer_matched/buyer_details (Agent)
# root8 -> rent_sold_details (Agent)
# root9 -> rent_sold_buyer_details (Agent)
# root10 -> agent_details (Office)
# root11 -> agent_matched (Office)
# root12 -> agent_sold_matched (Office)



# ---------------------------------------------AGENT LOGIN-----------------------------------------------------------------------------------------------



# AGENT_LOGIN_CRED_PAGE
def agent_login():  # root2
    root2 = Toplevel(root1)
    root2.title('AGENT LOGIN PORTAL')
    root2.geometry('1155x718-150-80')
    root2.resizable(False, False)

    # ICON
    p1 = PhotoImage(file = 'icon.png')
    root2.iconphoto(False, p1)
    
    # AGENT_VALIDATION function
    def signin():
        username = user.get()
        password = code.get()
    
        if username == '' or password == '':
            messagebox.showerror('Error', 'All fields are required!')
        
        else:
            try:
                conn = mysql.connect(host = 'localhost', user = 'root', password = 'Prerna@27')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established! Try Again')
                return
            
            # DATABASE selected
            query = 'use project_realestate'
            mycursor.execute(query)
            
            # QUERY for agent validation
            query = 'select a_id, a_pass from Agent where a_id = %s and a_pass = %s'
            mycursor.execute(query, (username, password))
        
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username or password!')
            else:
                messagebox.showinfo('Success', 'Login is Successful')
            
                # redirecting to AGENT_HOME_PAGE if credentials are valid
                root4 = Toplevel(root2)  
                root4.title('AGENT HOME PAGE') # AGENT_HOME_PAGE
                root4.geometry('1155x718-150-80')
                root4.resizable(False, False)

                p1 = PhotoImage(file = 'icon.png') # ICON
                root4.iconphoto(False, p1)
                    
                bg_wa = PhotoImage(file = "BG_welcome_agent_1.png") # BACKGROUND_WELCOME_AGENT
                label_wa = Label(root4, image = bg_wa)
                label_wa.place(x = 0, y = 0)
                
                # defining function TOPA to redirect to BUYER_REQ page when selected AVAILABLE
                def topA():
                    value = user.get()
                    # root2.withdraw()
                    os.system("python agent_task.py " + value)
                    # root2.destroy()
                    
                # defining function TOPS to redirect to SOLD_RENTED_PROPERTIES page when selected SOLD
                def topS():
                    value1 = user.get()
                    # root2.withdraw()
                    os.system("python agent_sold_rent.py " + value1)
                    # root2.destroy()
                   
                # list of ALL properties   
                def avai():
                    value2=user.get()
                    os.system("python agent_available.py " + value2)
                
                # BUTTONS available in AGENT_HOME_PAGE for selecting AVAILABLE and SOLD
                button_available = Button(root4, text = 'AVAILABLE \n PROPERTIES', command = topA, width = 20, background = 'black', foreground = 'white', activebackground = 'black', activeforeground = 'grey',font = ('Canva Sans', 15, 'bold'), border = 0).place(x = 200, y = 538)
                all= Button(root4, text = 'VIEW ALL \nPROPERTIES',command=avai, width = 10, background = 'white', foreground = 'black', activebackground = 'white', activeforeground = 'grey', font = ('Antonio Bold', 11, 'bold'), border = 0).place(x = 1055, y = 26)
                button_sold = Button(root4, text = 'SOLD \n PROPERTIES', command = topS, width = 22, background = 'black', foreground = 'white', activebackground = 'black', activeforeground = 'grey',font = ('Canva Sans', 15, 'bold'), border = 0).place(x = 735, y = 538)
        
                root4.mainloop()
    
    
    bg_al = PhotoImage(file = "BG_agent_login_1.png")  # BACKGROUND_AGENT_LOGIN_CRED
    label_al = Label(root2, image = bg_al)
    label_al.place(x = 0, y = 0)
    
    # USERNAME ICON & BUTTONS
    def on_enter(e):
        user.delete(0, 'end')
        
    def on_leave(e):
        name = user.get()
        
        if name == '':
            user.insert(0, 'Username')
        
    user_icon = PhotoImage(file = "username_icon.png")   # USER ICON
    label_user_icon = Label(root2, image = user_icon, bg = '#454545')
    label_user_icon.place(x = 362, y = 366)

    user = Entry(root2, width = 25, fg = 'white', border = 0, bg = '#454545', font = ('Microsoft YaHei UI Light', 18))   # USERNAME BUTTON
    user.place(x = 389, y = 362)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    
    # PASSWORD ICON & BUTTONS
    def on_enter(e):
        code.delete(0, 'end')
        
    def on_leave(e):
        name = code.get()
        
        if name == '':
            code.insert(0, 'Password')
            
    pass_icon = PhotoImage(file = "password_icon.png")   # PASSWORD ICON
    label_pass_icon = Label(root2, image = pass_icon, bg = '#454545')
    label_pass_icon.place(x = 362, y = 459)
            
    code = Entry(root2, width = 25, fg = 'white', border = 0, show = '*', bg = '#454545', font = ('Microsoft YaHei UI Light', 18))   # PASSWORD BUTTON
    code.place(x = 389, y = 458)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    # SHOW/HIDE PASSWORD
    def show():
        show_image.config(file = 'show_1.png')
        code.config(show = '')
        show_button.config(command = hide) 

    def hide():
        show_image.config(file = 'hide_1.png')
        code.config(show = '*')
        show_button.config(command = show)

    show_image = PhotoImage(file = 'show_1.png')  # SHOW_IMAGE

    show_button = Button(root2, image = show_image , command = show, relief = FLAT , activebackground = '#454545', bd = 0, background = '#454545', cursor = 'hand2')    # SHOW_BUTTON
    show_button.place(x = 680, y = 450)
    
    # AGENT_SIGNIN_BUTTON
    button_a = Button(root2, text = 'Sign In', width = 32, background= '#A6AAB0', foreground= 'black', activebackground = '#A6AAB0', activeforeground = 'white', font = ('yu gothic ui', 15, 'bold'), border = 0, command = signin).place(x = 365, y = 543)

    root2.mainloop()



# ------------------------------------------------OFFICE LOGIN---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# OFFICE_VALIDATION function
def office_login():  # root3
    root3 = Toplevel(root1)
    root3.title('OFFICE LOGIN PORTAL')
    root3.geometry('1155x718-150-80')
    root3.resizable(False, False)
    
    # ICON
    p1 = PhotoImage(file = 'icon.png')
    root3.iconphoto(False, p1)
    
    # OFFICE_VALIDATION function
    def signin():
        username = user.get()
        password = code.get()
    
        if username == '' or password == '':
            messagebox.showerror('Error', 'All fields are required!')
        
        else:
            try:
                conn = mysql.connect(host = 'localhost', user = 'root', password = 'Prerna@27')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established! Try Again')
                return
            
            # DATABASE selected
            query = 'use project_realestate'
            mycursor.execute(query)
            
            # QUERY for office validation
            query = 'select o_id, o_pass from Office where o_id = %s and o_pass = %s'
            mycursor.execute(query, (username, password))
        
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username or password!')
            else:
                messagebox.showinfo('Success', 'Login is Successful')
            
                # redirecting to OFFICE_HOME_PAGE if credentials are valid
                def topO():
                    root3.withdraw()
                    os.system("python welcome_officer.py")
                    root3.destroy()
                    
                topO()
                
            
    bg_ol = PhotoImage(file = "BG_office_1.png")  # BACKGROUND_OFFICE_LOGIN_CRED
    label_ol = Label(root3, image = bg_ol)
    label_ol.place(x = 0, y = 0)
    
    # USERNAME ICON & BUTTONS
    def on_enter(e):
        user.delete(0, 'end')
        
    def on_leave(e):
        name = user.get()
        
        if name == '':
            user.insert(0, 'Username')

    user_icon = PhotoImage(file = "username_icon.png")  # USER ICON
    label_user_icon = Label(root3, image = user_icon, bg = '#454545')
    label_user_icon.place(x = 362, y = 366)
        
    user = Entry(root3, width = 25, fg = 'white', border = 0, bg = '#454545', font = ('Microsoft YaHei UI Light', 18))  # USERNAME BUTTON
    user.place(x = 389, y = 362)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    
    # PASSWORD ICON & BUTTONS
    def on_enter(e):
        code.delete(0, 'end')
        
    def on_leave(e):
        name = code.get()
        
        if name == '':
            code.insert(0, 'Password')
            
    pass_icon = PhotoImage(file = "password_icon.png")  # PASSWORD ICON
    label_pass_icon = Label(root3, image = pass_icon, bg = '#454545')
    label_pass_icon.place(x = 362, y = 459)
            
    code =Entry(root3, width = 25, fg = 'white', border = 0, bg = '#454545', show = '*', font = ('Microsoft YaHei UI Light', 18))   # PASSWORD BUTTON
    code.place(x = 389, y = 458)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    # SHOW/HIDE PASSWORD
    def show():
        show_image.config(file = 'show_1.png')
        code.config(show = '')
        show_button.config(command = hide) 

    def hide():
        show_image.config(file = 'hide_1.png')
        code.config(show = '*')
        show_button.config(command = show)

    show_image = PhotoImage(file = 'show_1.png')  #SHOW_IMAGE

    show_button = Button(root3, image = show_image , command = show, relief = FLAT , activebackground = '#454545', bd = 0, background = '#454545', cursor = 'hand2')  # SHOW BUTTON
    show_button.place(x = 680, y = 450)

    button_o = Button(root3, text = 'Sign In', width = 32, background= '#A6AAB0', foreground= 'black', activebackground = '#A6AAB0', activeforeground = 'white', font = ('yu gothic ui', 15, 'bold'), border = 0, command = signin).place(x = 365, y = 543)

    root3.mainloop()




# -----------------------------------------------HOME--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




root1 = Tk()  #HOME_PAGE
root1.title('LOGIN AS')
root1.geometry('1155x718-150-80')
root1.resizable(False, False)

p1 = PhotoImage(file = 'icon.png') # ICON
root1.iconphoto(False, p1)

bg = PhotoImage(file = "BG_home_1.png")  # BACKGROUND_HOME
label1 = Label(root1, image = bg)
label1.place(x = 0, y = 0)

# BUTTONS for selecting AGENT and OFFICE
buttonA = Button(root1, text = 'AGENT', width = 20, background= '#000000', foreground= 'white', activebackground = '#000000', activeforeground = 'grey', font = ('Archivo Black', 16, 'bold'), border = 0, command = agent_login).place(x =135 , y = 595)
buttonR = Button(root1, text = 'REAL ESTATE OFFICE', width = 27, background= '#000000', foreground= 'white', activebackground = '#000000', activeforeground = 'grey', font = ('Archivo Black', 16, 'bold'), border = 0, command = office_login).place(x =730 , y = 595)  

root1.mainloop()

