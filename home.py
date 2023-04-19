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
                conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established! Try Again')
                return
            
            # DATABASE selected
            query = 'use realestate'
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
                    
                bg_wa = PhotoImage(file = "BG_welcome_agent.png") # BACKGROUND_WELCOME_AGENT
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
                
                def avai():
                    value2=user.get()
                    os.system("python agent_available.py " + value2)
                
                # BUTTONS available in AGENT_HOME_PAGE for selecting AVAILABLE and SOLD
                button_available = Button(root4, text = 'AVAILABLE PROPERTIES', width = 20, background = '#224957', foreground = 'white', activebackground = '#224957', font = ('yu gothic ui', 15, 'bold'), border = 0, command = topA).place(x = 200, y = 480)
                all= Button(root4, text = 'VIEW ALL \n PROPERTIES',command=avai, width = 10, background = '#539D96', foreground = 'white', activebackground = '#539D96', font = ('Antonio Bold', 10, 'bold'), border = 0).place(x = 1060, y = 30)
                button_sold = Button(root4, text = 'SOLD PROPERTIES', width = 20, background = '#224957', foreground = 'white', activebackground = '#224957', font = ('yu gothic ui', 15, 'bold'), border = 0, command = topS).place(x = 795, y = 480)
        
                root4.mainloop()
    
    
    bg_al = PhotoImage(file = "BG_agent_login.png")  # BACKGROUND_AGENT_LOGIN_CRED
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
    label_user_icon = Label(root2, image = user_icon, bg = '#224957')
    label_user_icon.place(x = 685, y = 300)

    user = Entry(root2, width = 31, fg = 'white', border = 0, bg = '#224957', font = ('Microsoft YaHei UI Light', 13))   # USERNAME BUTTON
    user.place(x = 712, y = 300)
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
    label_pass_icon = Label(root2, image = pass_icon, bg = '#224957')
    label_pass_icon.place(x = 685, y = 385)
            
    code = Entry(root2, width = 31, fg = 'white', border = 0, bg = '#224957', font = ('Microsoft YaHei UI Light', 13))   # PASSWORD BUTTON
    code.place(x = 712, y = 385)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    # SHOW/HIDE PASSWORD
    def show():
        show_image.config(file = 'show.png')
        code.config(show = '')
        show_button.config(command = hide) 

    def hide():
        show_image.config(file = 'hide.png')
        code.config(show = '*')
        show_button.config(command = show)

    show_image = PhotoImage(file = 'show.png')  # SHOW_IMAGE

    show_button = Button(root2, image = show_image , command = hide, relief = FLAT , activebackground = '#224957', bd = 0, background = '#224957', cursor = 'hand2')    # SHOW_BUTTON
    show_button.place(x = 975, y = 390)

    frame = Frame(root2, width = 320, height = 20, bg = '#E5E5E5')
    frame.place(x = 680, y = 445)
    
    # AGENT_SIGNIN_BUTTON
    button_a = Button(root2, text = 'Sign In', width = 30, background= '#20DF7F', foreground= '#224957', activebackground = '#20DF7F', activeforeground = 'white', font = ('yu gothic ui', 13, 'bold'), border = 0, command = signin).place(x = 690, y = 497)

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
                conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established! Try Again')
                return
            
            # DATABASE selected
            query = 'use realestate'
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
                    root3.destroy
                    
                topO()
                
            
    bg_ol = PhotoImage(file = "BG_office.png")  # BACKGROUND_OFFICE_LOGIN_CRED
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
    label_user_icon = Label(root3, image = user_icon, bg = '#224957')
    label_user_icon.place(x = 685, y = 300)
        
    user = Entry(root3, width = 31, fg = 'white', border = 0, bg = '#224957', font = ('Microsoft YaHei UI Light', 13))  # USERNAME BUTTON
    user.place(x = 712, y = 300)
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
    label_pass_icon = Label(root3, image = pass_icon, bg = '#224957')
    label_pass_icon.place(x = 685, y = 385)
            
    code =Entry(root3, width = 31, fg = 'white', border = 0, bg = '#224957', font = ('Microsoft YaHei UI Light', 13))   # PASSWORD BUTTON
    code.place(x = 712, y = 385)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    
    # SHOW/HIDE PASSWORD
    def show():
        show_image.config(file = 'show.png')
        code.config(show = '')
        show_button.config(command = hide) 

    def hide():
        show_image.config(file = 'hide.png')
        code.config(show = '*')
        show_button.config(command = show)

    show_image = PhotoImage(file = 'show.png')  #SHOW_IMAGE

    show_button = Button(root3, image = show_image , command = hide, relief = FLAT , activebackground = '#224957', bd = 0, background = '#224957', cursor = 'hand2')  # SHOW BUTTON
    show_button.place(x = 975, y = 390)

    frame = Frame(root3, width = 320, height = 20, bg = '#E5E5E5')
    frame.place(x = 680, y = 445)

    button_o = Button(root3, text = 'Sign In', width = 30, background= '#20DF7F', foreground= '#224957', activebackground = '#20DF7F', activeforeground = 'white', font = ('yu gothic ui', 13, 'bold'), border = 0, command = signin).place(x = 690, y = 497)

    root3.mainloop()




# -----------------------------------------------HOME--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




root1 = Tk()  #HOME_PAGE
root1.title('LOGIN AS')
root1.geometry('1155x718-150-80')
root1.resizable(False, False)

p1 = PhotoImage(file = 'icon.png') # ICON
root1.iconphoto(False, p1)

bg = PhotoImage(file = "BG_home.png")  # BACKGROUND_HOME
label1 = Label(root1, image = bg)
label1.place(x = 0, y = 0)

# BUTTONS for selecting AGENT and OFFICE
buttonA = Button(root1, text = 'Agent', width = 20, background= '#224957', foreground= 'white', activebackground = '#224957', activeforeground = '#48E094', font = ('yu gothic ui', 13, 'bold'), border = 0, command = agent_login).place(x =124 , y = 495)
buttonR = Button(root1, text = 'Real Estate Office', width = 23, background= '#224957', foreground= 'white', activebackground = '#224957', activeforeground = '#48E094', font = ('yu gothic ui', 13, 'bold'), border = 0, command = office_login).place(x =760 , y = 495)  

root1.mainloop()