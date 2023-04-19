from tkinter import *
from tkinter.ttk import Progressbar
import os  
import mysql.connector as mysql

 
root = Tk()
root.resizable(0, 0)

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.overrideredirect(1) 
root.config(background = '#224957')

welcome_label = Label(root, text = 'WELCOME TO OUR REAL ESTATE GUI', font = ('Lexend Deca', 20, 'bold'), fg = 'white', bg = '#224957')
welcome_label.place(x = 8, y = 30)

exit_btn = Button(root, text = 'X', command = lambda: exit_window(), font = ('yu gothic ui', 11, 'bold'), fg = '#47DF94', bg = '#224957', bd = 0, activebackground = 'white')
exit_btn.place(x = 500, y = 0) 

image = PhotoImage(file = 'load.png')
bg_label = Label(root, image = image, bg = '#224957')
bg_label.place(x = 130, y = 120)

progress_label = Label(root, text = 'Please Wait...', font = ('yu gothic ui', 19, 'bold'), bg = '#224957', fg = 'white')
progress_label.place(x = 190, y = 350)

progress = Progressbar(root, orient = HORIZONTAL, length = 500, mode = 'determinate')
progress.place(x = 15, y = 390)

def exit_window():
    os.exit(root.destroy())
    
def top():
    root.withdraw()
    os.system("python home.py")
    root.destroy()
    
i = 0
    
def load():
    global i
    
    if i <= 10:
        txt = 'Please Wait...' + (str(10*i)+'%')
        progress_label.config(text = txt)
        progress_label.after(200, load)
        progress['value'] = 10*i
        i += 1
        
    else:
        top()
        
load()      
root.mainloop()
        