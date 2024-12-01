from tkinter import *
from tkinter import messagebox
import sqlite3
import os

class Admin:

    #This function defines the tkinter window alongside its labels and buttons
    def __init__(self,root):
        self.root = root
        self.root.geometry("245x120")

        self.myLabel = Label(root, text="Username: ")
        self.myLabel.place(relx= 0.25, rely = 0.25, anchor = CENTER)

        self.myLabel2 = Label(root, text="Password: ")
        self.myLabel2.place(relx= 0.25, rely = 0.45, anchor = CENTER)

        self.myLabel3 = Label(root, text="Admin login")
        self.myLabel3.pack()

        self.username = Entry(root)
        self.username.place(relx= 0.62, rely = 0.25, anchor = CENTER)

        self.password = Entry(root, show='*')
        self.password.place(relx= 0.62, rely = 0.45, anchor = CENTER)

        self.login = Button(root, text="Login", command=self.admin_login)
        self.login.place(relx=0.5, rely=0.65, anchor=CENTER)
