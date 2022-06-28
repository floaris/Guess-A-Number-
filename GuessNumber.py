from cgi import test
import tkinter as tk

from tkinter import *
import random
from tkinter import ttk

root = tk.Tk()

root.title("Calcul de Nombres!")

root.geometry("600x400")
i=random.randint(1, 10)

def devine():
    global b
    string= b.get()
    texto='BRAVO'
    
    value = str(i)
    if string == value:
        test.configure(text=texto)
    elif string != value:
        test.configure(text="FAUX!")


label = Label(root, text="Insérer un chiffre !", font=("Arial", 24, "bold") )
label.pack()

b=tk.Entry(root)
b.pack()
test=Label(root, text="", font=("Courier 22 bold"))
test.pack()
b.place(x=250, y=200)
ttk.Button(root, text= "Okay",width= 20, command= devine).pack(pady=20)
root.mainloop()