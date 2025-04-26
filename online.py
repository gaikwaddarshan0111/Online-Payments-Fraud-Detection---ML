import numpy as np
import tkinter as kt
from tkinter import messagebox

valid_username = "Darshan"
valid_password = "Darshan@#4553"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == valid_password and password == valid_password:
        messagebox.showinfo("Login","Loggein Successfully")
    else:
        messagebox.showerror("Login","Invalid Credentials")
     


root = kt.Kt()
root.title("Login Form")
root.geometry("300x200")


label_username = kt.Label(root , text="Username")
label_username.pack(pady=(20,5))
entry_username = kt.Entry(root)
entry_username.pack()

label_password = kt.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = kt.Entry(root, show="*")
entry_password.pack()

login_button = kt.Button(root, text="Login", command=login)
login_button.pack(pady=20)

root.mainloop()