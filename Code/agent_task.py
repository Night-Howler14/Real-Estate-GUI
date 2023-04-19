from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql
from tkcalendar import *
import sys
import os

# AGENT TASK PAGE
root15 = Tk()
root15.title('AGENT PAGE: SELLER/BUYER PAGE')
root15.geometry('1155x718-150-80')
root15.resizable(False, False)

#  CONNECTION TO DATABASE
try:
    conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@', database = "realestate")
    mycursor = conn.cursor()
    
    query = 'use realestate'
    mycursor.execute(query)
    
except:
    messagebox.showerror('Error', 'Connection is not established! Try Again')
    
    
p1 = PhotoImage(file = 'icon.png')  # ICON
root15.iconphoto(False, p1)
           
bg_wa = PhotoImage(file = "BG_agent_task.png")
label_wa = Label(root15, image = bg_wa)
label_wa.place(x = 0, y = 0)
 

#------------------------------------------------------------------functions for SELLER page--------------------------------------------------------------------------------------------------------

def seller_page():
    root10 = Toplevel(root15)  #HOME_PAGE
    root10.title('AGENT PAGE: SELLER DETAILS')
    root10.geometry('1155x718-150-80')
    root10.resizable(False, False)
    
    #  CONNECTION TO DATABASE
    try:
        conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@', database = "realestate")
        mycursor = conn.cursor()
        query = 'use realestate'
        mycursor.execute(query)
    except:
        messagebox.showerror('Error', 'Connection is not established! Try Again')
    
    
    p1 = PhotoImage(file = 'icon.png') # ICON
    root10.iconphoto(False, p1)
    
    bg = PhotoImage(file = "BG_agent_seller.png")  # BACKGROUND_SELLER
    label1 = Label(root10, image = bg)
    label1.place(x = 0, y = 0)
    
    
    # Property details
    global city, locality, area, pincode, price, n_o_b, stat, yoc, yos, sname, smail
    
    city = Entry(root10, width = 30, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    city.place(x = 205, y = 85)
        
    locality = Entry(root10, width = 30, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    locality.place(x = 205, y = 131)
        
    
    area = Entry(root10, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    area.place(x = 205, y = 170)
        
    pincode = Entry(root10, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    pincode.place(x = 205, y = 218)
        
    price = Entry(root10, width = 21, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 15))  
    price.place(x = 205, y = 267)
            
    values1 = values = list(range(0,7,1))
    n_o_b = ttk.Combobox(root10, values = values1 , justify = 'center' )
    n_o_b.current(0)
    n_o_b.bind("<<ComboboxSelected>>")
    n_o_b.place(x = 630, y = 270, width = 100)
    n_o_b.config(font = ("yu gothic ui", 11))
    
    stat = ttk.Combobox(root10, state = "readonly") 
    stat['values'] = ('Rent', 'Sell')
    stat.current(1)
    stat.bind("<<ComboboxSelected>>")
    stat.place(x = 635, y = 308, width = 75)
    stat.config(font = ("yu gothic ui", 11))
        
    # yoc
    values = list(range(2023, 1970, -1))
    yoc = ttk.Combobox(root10, values = values , justify = 'center')
    yoc.current(0)
    yoc.bind("<<ComboboxSelected>>")
    yoc.place(x = 340, y = 314, width=100)
    yoc.config(font=("yu gothic ui", 11))
    
    # seller details   
    sname = Entry(root10, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    sname.place(x = 262, y = 490)
        
    smail = Entry(root10, width = 21, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
    smail.place(x = 262, y = 540)
    
    # YEAR OF selling
    values = list(range(2023, 1970, -1))
    yos = ttk.Combobox(root10, values = values , justify = 'center')
    yos.current(0)
    yos.bind("<<ComboboxSelected>>")
    yos.place(x = 807, y = 528)
    yos.config(font=("yu gothic ui", 11))
    
    
    
    def submit_seller_det():
            global city, locality, yoc, area, sname, smail
            
            if city.get() == '' or locality.get() == '' or area.get() == '' or pincode.get() == '' or price.get() == '' or n_o_b.get() == 0 or sname.get() == '' or smail.get() == '':
                messagebox.showerror("Error", "All fields are required!")
            
            else:    
                # messagebox.showinfo("Info", "Welcome to seller page!")
                e1 = city.get()
                e2 = locality.get()
                e3 = int(area.get())
                e4 = int(pincode.get())
                e5 = int(price.get())
                e6 = int(n_o_b.get())
                e7 = int(yoc.get())
                e8 = stat.get()
                e9 = sname.get()
                e10 = smail.get()
                e11 = int(yos.get())
                
                if stat.get() == 'Sell':         
                    query = "insert into Property(status, a_id, city, locality, pincode, area, price, bedrooms, yoc, yos, s_name, s_mail) values('AS',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    value = (str(sys.argv[1]), e1, e2, e4, e3, e5, e6, e7, e11,e9, e10)
                    mycursor.execute(query, value)
                    conn.commit()
                    
                    messagebox.showinfo('Info', 'Property for selling has been added successfully!') 
    
                else:
                    query = "insert into Property(status, a_id, city, locality, pincode, area, price, bedrooms, yoc, yos, s_name, s_mail) values('AR',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    value = (str(sys.argv[1]), e1, e2, e4, e3, e5, e6, e7, e11,e9, e10)
                    mycursor.execute(query, value)
                    conn.commit()
                
                    messagebox.showinfo("Info", "Property for renting has been added successfully!")
    
    
    # SUBMIT button
    button_submit = Button(root10, text = 'SUBMIT', width = 20, background = '#224957', foreground = 'white', activebackground = '#224957', font = ('yu gothic ui', 15, 'bold'), border = 0, command = submit_seller_det).place(x = 250, y = 600)
    
    root10.mainloop()

#------------------------------------------------------------------functions for BUYER page--------------------------------------------------------------------------------------------------------
  
def buyer_page():
    root7 = Toplevel(root15)
    root7.title('AGENT PAGE: BUYER REQUIREMENTS')
    root7.geometry('1155x718-150-80')
    root7.resizable(False, False)

    #  CONNECTION TO DATABASE
    try:
        conn = mysql.connect(host = 'localhost', user = 'root', password = 'Pr@141003@', database = "realestate")
        mycursor = conn.cursor()

        query = 'use realestate'
        mycursor.execute(query)

    except:
        messagebox.showerror('Error', 'Connection is not established! Try Again')


    p1 = PhotoImage(file = 'icon.png') # ICON
    root7.iconphoto(False, p1)

    bg_br = PhotoImage(file = "BG_buyer_req.png") # BACKGROUND_BUYER_REQ
    label_br = Label(root7, image = bg_br)
    label_br.place(x = 0, y = 0)

    # CITY, LOCALITY, AREA
    global city, locality, area, yoc, var3, var4
    city = Entry(root7, width = 42, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  # CITY SPACE
    city.place(x = 287, y = 183)
    
    locality = Entry(root7, width = 42, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))   # LOCALITY SPACE
    locality.place(x = 287, y = 223)

    area = Entry(root7, width = 42, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  # AREA SPACE
    area.place(x = 287, y = 266)

    # PROPERTY TYPE -> CHECK BOX
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = 0
    var4 = 0

    def s_clicked():
        global var3
        
        if var3 == 0:
            ptype_r.deselect()
            var3 = 1
        else:
            var3 = 0
            ptype_s.deselect()
    

    def r_clicked():
        global var4
        
        if var4 == 0:
            var4 = 1
            ptype_s.deselect()
        else:
            var4 = 0
            ptype_r.deselect()
        
    ptype_s = tk.Checkbutton(root7, variable = var1, onvalue = 1, offvalue = 0, text = "Sell", bg = "#E5E5E5" , command = s_clicked)  # SELL CHECK BOX
    ptype_s.place(x = 317, y = 313)
    ptype_s.config(font = ("yu gothic ui", 13))

    ptype_r = tk.Checkbutton(root7, variable = var2, onvalue = 1, offvalue = 0, text = "Rent", bg = "#E5E5E5" , command = r_clicked)  # RENT CHECK BOX
    ptype_r.place(x = 379, y = 313)
    ptype_r.config(font = ("yu gothic ui", 13))

    # BEDROOMS
    values1 = values = list(range(0,7,1))
    no_bed = ttk.Combobox(root7, values = values1 , justify = 'center' )
    no_bed.current(0)
    no_bed.bind("<<ComboboxSelected>>", lambda e: frame.focus())
    no_bed.place(x = 338, y = 366)
    no_bed.config(font = ("yu gothic ui", 11))

    # PARKING
    var1 = tk.IntVar()
    var2 = tk.IntVar()

    def p2_clicked():
        park_1.deselect()

    def p1_clicked():
        park_2.deselect()

    park_1 = tk.Checkbutton(root7, text = "Yes", variable = var1 , bg = "#E5E5E5" , command = p1_clicked) # PARKING -> YES
    park_1.place(x = 699, y = 361)
    park_1.config(font = ("yu gothic ui", 13))

    park_2 = tk.Checkbutton(root7, text = "No", variable = var2 , bg = "#E5E5E5" , command = p2_clicked)  # PARKING -> NO
    park_2.place(x = 761, y = 361)
    park_2.config(font = ("yu gothic ui", 13))

    # PRICE RANGE
    varpr0 = IntVar()

    pr_ini = Entry(root7 , width = 12, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 15) , justify='center')
    pr_ini.insert(0, "0")
    pr_ini.get()
    pr_ini.place(x = 286, y = 412)

    pr_last = Entry(root7, width = 12, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 15) , justify='center')
    pr_last.insert(0, "0")
    pr_last.place(x = 451, y = 412)

    # YEAR OF CONSTRUCTION
    values = list(range(2023, 1970, -1))
    yoc = ttk.Combobox(root7, values = values , justify = 'center')
    yoc.current(0)
    yoc.bind("<<ComboboxSelected>>",lambda e: frame.focus())
    yoc.place(x = 416, y = 464)
    yoc.config(font=("yu gothic ui", 11))
    
    frame = Frame(root7, width = 120, height = 30, bg = '#224957')
    frame.place(x = 481, y = 566)


    
    # BUYER_DETAILS_PAGE 
    def submit_buyer_req():
        global city, locality, yoc, area, bg_bd
        
        if city.get() == '' or locality.get() == '' or area.get() == '' or pr_last.get() == '0' or no_bed.get() == '0':
            messagebox.showerror("Error", "All fields are required!")
        
        else:    
            messagebox.showinfo("Info", "Welcome to Buyer details page!\nSelect a property and proceed further.")

            root8 = Toplevel(root7)
            root8.title('AGENT HOME PAGE: BUYER DETAILS')
            root8.geometry('1155x718-150-80')
            root8.resizable(False, False)
            p1 = PhotoImage(file = 'icon.png')  #ICON
            root8.iconphoto(False, p1)


            # BACKGROUND_BUYER_DETAILS
            bg_bd = PhotoImage(file = "BG_buyer_details.png")
            label_bd = Label(root8, image = bg_bd)
            label_bd.place(x = 0, y = 0)


            column1 = ('P_Id', 'City', 'Locality', 'Area', 'No. of Bedrooms', 'Price', 'Year of construc.')
            listbox = ttk.Treeview(root8, columns = column1, show = 'headings')
            listbox.column("#1", anchor = CENTER, width = 120)
            listbox.column("#2", anchor = CENTER, width = 120)
            listbox.column("#3", anchor = CENTER, width = 120)
            listbox.column("#4", anchor = CENTER, width = 120)
            listbox.column("#5", anchor = CENTER, width = 120)
            listbox.column("#6", anchor = CENTER, width = 120)
            listbox.column("#7", anchor = CENTER, width = 120)  

            for col in column1:
                listbox.heading(col, text = col)
                listbox.grid(row = 1, column = 0, columnspan = 1)
                listbox.place(x = 100, y = 100)

            e1 = city.get()
            e2 = locality.get()
            e4 = int(no_bed.get())
            e5 = int(pr_ini.get())
            e6 = int(pr_last.get())
            e7 = int(yoc.get())
            e3 = area.get()
            # print(var3)
            # print(var4)

            print(e7)

            if var3 == 1 and var4 == 0:
                sql = "select p_id, city, locality, area, bedrooms, price, yoc from Property where status = 'AS' and a_id = %s and (city = %s or locality = %s) and (area >= %s and bedrooms > %s and price > %s and price < %s and yoc > %s)"
                # sql = "select p_id, city, locality, area, bedrooms, price, yoc from Property where status = 'AS' and a_id = '4PA002' and (city = %s or locality = %s) and (area >= %s and bedrooms >= %s and price >= %s and price <= %s and yoc > %s)"
                value = [str(sys.argv[1]), e1, e2, e3, e4, e5, e6, e7]
                # value = [e1, e2, e3, e4, e5, e6, e7]
                mycursor.execute(sql, value)
                records = mycursor.fetchall()
                print(records)

                for i, (p_id, city, locality, area, bedrooms, price, yoc) in enumerate(records, start = 1):
                 listbox.insert("", "end", values = (p_id, city, locality, area, bedrooms, price, yoc))

            else:
                sql = "select p_id, city, locality, area, bedrooms, price, yoc from Property where status ='AR'and a_id = %s and (city = %s or locality = %s) and (area >= %s and bedrooms > %s and price > %s and price < %s and yoc > %s)"
                # sql = "select p_id, city, locality, area, bedrooms, price, yoc from Property where status = 'AR' and a_id = '4PA002' and city = %s or locality = %s and area >= %s and bedrooms > %s and price > %s and price < %s and yoc > %s"
                value= [str(sys.argv[1]), e1, e2, e3, e4, e5, e6, e7]
                # value= [e1, e2, e3, e4, e5, e6, e7]
                mycursor.execute(sql, value)
                records = mycursor.fetchall()
                print(records)

                for i, (p_id, city, locality, area, bedrooms, price, yoc) in enumerate(records, start = 1):
                 listbox.insert("", "end", values = (p_id, city, locality, area, bedrooms, price, yoc))


            def on_tree_select(e):
                selected_row = listbox.focus()
                values = listbox.item(selected_row, 'values')

                prop_id.delete(0, END)
                prop_id.insert(0, values[0])

            listbox.bind("<<TreeviewSelect>>", on_tree_select)


            # DATE CALENDER
            def pick_date(e):
                global cal, date_window 
                date_window = Toplevel()
                date_window.grab_set()
                date_window.title('Select date of buying: ')
                date_window.geometry('250x220+590+370')
                cal = Calendar(date_window, selectmode = "day", date_pattern = "y-mm-dd")
                cal.place(x = 0, y = 0)

                submit_btn = Button(date_window, text = "Submit", command = grab_date)
                submit_btn.place(x = 80, y = 190)

            def grab_date():
                dob.delete(0, END)
                dob.insert(0, cal.get_date())
                date_window.destroy()


            # BUYER_DETAILS
            prop_id = Entry(root8, width = 11, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
            prop_id.place(x = 247, y = 459)

            durat = Entry(root8, width = 11, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
            durat.place(x = 773, y = 459)
            
            if var3 == 1 and var4 == 0:
                durat.insert(0, "-------")
                durat.config(state='disabled')
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

            buyer_name = Entry(root8, width = 30, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
            buyer_name.place(x = 247, y = 495)

            buyer_id = Label(root8, width = 20, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 20))  
            buyer_id.place(x = 600, y = 495)

            buyer_mail = Entry(root8, width = 30, fg = 'black', border = 0, bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
            buyer_mail.place(x = 250, y = 535)

            dob = Entry(root8, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
            dob.place(x = 815, y = 542)
            dob.insert(0, "yyyy-mm-dd")
            dob.bind("<1>", pick_date)


            # SUBMIT BUTTON
            def submitl():
                if prop_id == '' or buyer_name == '' or buyer_mail == '' or durat == '':
                    messagebox.showerror("Error", "All fields are required!")
                else:
                    a = prop_id.get()
                    b = buyer_name.get()
                    c = buyer_mail.get()
                    d = dob.get()
                    e = durat.get()
                    print(a, b, c, d, e, var3, var4)

                    if var3 == 1 and var4 == 0:         
                        query = "update Property set status = 'S' where p_id = %s"
                        value = (a,)
                        mycursor.execute(query, value)
                        conn.commit()


                        query = "insert into Sales(p_id, a_id, b_name, b_mail, status, dob) values(%s,%s,%s,%s,%s,%s)"
                        value = (a, str(sys.argv[1]), b, c, 'S', d)
                        mycursor.execute(query, value)
                        conn.commit()

                        messagebox.showinfo('Info', 'Property has been sold successfully!') 

                    else:
                        query="update Property set status='R' where p_id=%s"
                        value=(a,)
                        mycursor.execute(query,value)
                        conn.commit()
                        
                        
                        
                        query = "insert into Sales(p_id, a_id, b_name, b_mail, status, dob) values(%s,%s,%s,%s,'R',%s)"
                        value = [a, str(sys.argv[1]), b, c, d]
                        mycursor.execute(query, value)
                        conn.commit()
                        
                        # mycursor.execute(query)
                        query = "insert into Rent (p_id, status, duration, dob) values (%s,'R', %s, %s)"
                        value = [a,e,d]
                        mycursor.execute(query, value)
                        conn.commit()
                        
                        
                   
                        
                        messagebox.showinfo('Info', 'Property has been given on rent successfully!') 


            button = Button(root8, text = 'SUBMIT', command = submitl, width = 15, cursor = 'hand2', background= '#224957', foreground= 'white', activebackground = '#224957', activeforeground = '#E5E5E5', font = ('yu gothic ui', 15, 'bold'), border = 0)
            button.place(x = 295, y = 600)      
            root8.mainloop()


    # SUBMIT BUTTON
    button = Button(root7, text = 'SUBMIT', width = 18, cursor = 'hand2', background = '#224957', foreground= 'white', activebackground = '#224957', activeforeground = '#E5E5E5', font = ('yu gothic ui', 15, 'bold'), border = 0, command = submit_buyer_req)
    button.place(x = 481, y = 566) 


    root7.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BUTTONS FOR BUYER/SELLER PAGE
button_seller = Button(root15, text = 'SELLER PAGE', width = 20, background = '#224957', foreground = 'white', activebackground = '#224957', font = ('yu gothic ui', 15, 'bold'), border = 0, command = seller_page).place(x = 200, y = 480)
button_buyer = Button(root15, text = 'BUYER PAGE', width = 20, background = '#224957', foreground = 'white', activebackground = '#224957', font = ('yu gothic ui', 15, 'bold'), border = 0, command = buyer_page).place(x = 820, y = 480)

root15.mainloop()