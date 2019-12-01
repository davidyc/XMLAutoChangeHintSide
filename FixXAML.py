import FuncFixXAML as FFX
from tkinter import *
from tkinter import messagebox
import os


def CallFunc():
    if new.get() == "":
        messagebox.showinfo("Info", "New is empty!")
    elif old.get() == "":
        messagebox.showinfo("Info", "Old is empty!")
    elif os.path.isfile(new.get()) == False:
        messagebox.showinfo("Info", "New file was not found!")
    elif os.path.isfile(old.get()) == False:
        messagebox.showinfo("Info", "Old file was not found!")
    elif old.get() == new.get():
        messagebox.showinfo("Info", "New and old is one and the same file!")    
    else:
        if new.get().split('.')[-1] != "xaml":
            messagebox.showinfo("Info", "New is not xaml file!")    
        elif old.get().split('.')[-1] != "xaml":
            messagebox.showinfo("Info", "Old is not xaml file!")
        else:  
            FFX.FixXAML(new.get(), old.get())
            messagebox.showinfo("Info", "Done!")
    
    

root = Tk()
root.title("Fix XAML")
root.geometry('600x130')

new = StringVar()
old = StringVar()


Label(text="New:").grid(row=0, column=0, sticky=W, padx=10, pady=10) 
Entry(width="86", name="newFile", textvariable=new ).grid(row=0, column=1) 
Label(text="Old:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Entry(width="86", name="oldFile", textvariable=old).grid(row=1, column=1) 

Button(text="Fix", command=CallFunc, width=20, height=1).grid(row=2, column=1)
root.mainloop()