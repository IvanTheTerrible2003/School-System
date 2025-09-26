import tkinter as tk
from tkinter import *
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

r = tk.Tk()
r.geometry("1280x720")
r.title("Blackthorn Primary School")

tk_username = tk.StringVar()
tk_password = tk.StringVar()

#Initializing parent frame and centering it
grid_frame = tk.Frame(r)
grid_frame.place(relx=0.5, rely=0.42, anchor="center")

image = PhotoImage(file="blackthorn.png")
image_label = tk.Label(grid_frame, image=image)
image_label.grid(row=0, column=1, pady=50)

#Authentication form
Label(grid_frame, text='Username', font=("Helvetica", 10)).grid(row=1, column=0, pady=5)
Label(grid_frame, text='Password', font=("Helvetica", 10)).grid(row=2, column=0, pady=5)
username_entry = Entry(grid_frame, textvariable=tk_username, width=20, font=("Helvetica", 10))
password_entry = Entry(grid_frame, textvariable=tk_password, width=20, font=("Helvetica", 10))
username_entry.grid(row=1, column=2)
password_entry.grid(row=2, column=2)
auth_btn = Button(grid_frame, text="Submit", width=16, font=("Helvetica", 10), command=submit)
auth_btn.grid(row=3, column=2, padx=5, pady=5)

def submit():
    username = tk_username.get()
    password = tk_password.get()

    tk_username.set("")
    tk_password.set("")

    cursor.execute("SELECT username, password_hash FROM users;")
    rows = cursor.fetchall()
    for element in rows:
        if (element[0]==username and element[1]==password):
            print("User authenticated")
        else:
            print("Could not authenticate user, please try again")

r.mainloop()
connection.close()