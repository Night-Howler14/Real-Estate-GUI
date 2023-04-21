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
root.config(background = 'black')



image = PhotoImage(file = 'load.png')
bg_label = Label(root, image = image, bg = 'black')
bg_label.place(x = 50, y =0)

progress_label = Label(root, text = 'Please Wait...', font = ('yu gothic ui', 19, 'bold'), bg = 'black', fg = 'white')
progress_label.place(x = 160, y = 350)

progress = Progressbar(root, orient = HORIZONTAL, length = 500, mode = 'determinate')
progress.place(x = 15, y = 390)


exit_btn = Button(root, text = 'X', command = lambda: exit_window(), font = ('yu gothic ui', 11, 'bold'), fg = 'white', bg = 'black', bd = 0, activebackground = 'white')
exit_btn.place(x = 500, y = 0) 

welcome_label = Label(root, text = 'WELCOME', font = ('Lexend Deca', 30, 'bold'), fg = 'white', bg = 'black')
welcome_label.place(x = 160, y = 30)



def exit_window():
    root.destroy()
    
def top():
    root.withdraw()
    os.system("python home1.py")
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
        