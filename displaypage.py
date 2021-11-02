from tkinter import *
import tkinter as tk
from tkinter import ttk
import json

f = open("/Users/divyanshbhardwaj/Dev/Pycharmpro/my social media/database.json", "r")
s = f.read()
info = json.loads(s)

def display(naam):
    # print(info[naam])
    display = tk.Tk()
    display.geometry("320x190")
    display.title(f"{naam}'s Profile")
    display.resizable(0, 0)

    # configure the grid
    display.columnconfigure(0, weight=1)
    display.columnconfigure(1, weight=3)

    # food
    food_label = ttk.Label(display, text="favourite food:")
    food_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

    food_entry = ttk.Entry(display)
    food_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    food = info[naam].get('FavFood')
    food_entry.insert(0, food)

    # movie
    movie_label = ttk.Label(display, text="favourite movie:")
    movie_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    movie_entry = ttk.Entry(display)
    movie_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    movie = info[naam].get('FavMovie')
    movie_entry.insert(0, movie)

    # location
    location_label = ttk.Label(display, text="current location:")
    location_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

    location_entry = ttk.Entry(display)
    location_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    location = info[naam].get('Current loaction')
    location_entry.insert(0, location)

    # cricketer
    cricketer_label = ttk.Label(display, text="favourite cricketer:")
    cricketer_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

    cricketer_entry = ttk.Entry(display)
    cricketer_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    cricketer = info[naam].get('Fav cricketer')
    cricketer_entry.insert(0, cricketer)

    # age
    age_label = ttk.Label(display, text="current age:")
    age_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

    age_entry = ttk.Entry(display)
    age_entry.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
    age = info[naam].get('age')
    age_entry.insert(0, age)


