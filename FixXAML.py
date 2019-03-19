import FuncFixXAML as FFX
from tkinter import *
from tkinter import messagebox


def CallFunc():
    messagebox.showinfo("Info", "Done!")

root = Tk()
root.title("Fix XAML")
root.geometry('600x130')

Label(text="New:").grid(row=0, column=0, sticky=W, padx=10, pady=10) 
Entry(width="86", name="newFile").grid(row=0, column=1) 
Label(text="Old:").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Entry(width="86", name="oldFile").grid(row=1, column=1) 


Button(text="Fix", command=CallFunc, width=20, height=1).grid(row=2, column=1)






root.mainloop()