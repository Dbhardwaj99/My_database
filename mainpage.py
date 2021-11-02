import json
from tkinter import *

f = open("/Users/divyanshbhardwaj/Dev/Pycharmpro/my social media/database.json", "r")
s = f.read()
info = json.loads(s)

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("270x110")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

def login():
    name = username_entry.get()
    password = password_entry.get()
    if name in info.keys():
        if password == info[name]["Password"]:
            print("something")
        else:
            root.geometry("270x150")
            wrong_password = ttk.Label(root, text="You're not that guy pal!")
            wrong_password.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
    else:
        root.geometry("270x150")
        not_authorised = ttk.Label(root, text="Who are you nigga?")
        not_authorised.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()