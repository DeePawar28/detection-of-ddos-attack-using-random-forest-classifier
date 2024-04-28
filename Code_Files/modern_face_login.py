import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import customtkinter

root = customtkinter.CTk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x450")
root.title("Login Form")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

username = customtkinter.StringVar()
password = customtkinter.StringVar()

def registration():
    from subprocess import call
    call(["python","modern_face_registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            print(msg)
            ms.showinfo("message", "LogIn sucessfully")
            # ===========================================
            root.destroy()
            from subprocess import call
            call(['python','real_test.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady =40, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master= frame, text ="Login Here", font = ("Roboto",40,'bold') )
label.pack(pady =12, padx = 10)
        
label2 = customtkinter.CTkLabel(master= frame, text ="Username :", font = ("Roboto",11,'bold') )
label2.place(x =70, y= 102)

username = customtkinter.CTkEntry(master= frame,placeholder_text_color="white" ,placeholder_text = "Username",textvariable=username, width = 200,justify="left")
username.pack(pady= 12, padx =10)

label3 = customtkinter.CTkLabel(master= frame, text ="Password :", font = ("Roboto",11,'bold') )
label3.place(x =70, y= 154)

password = customtkinter.CTkEntry(master= frame,placeholder_text_color="white" , placeholder_text = "Password", textvariable= password, show ="*", width =200)
password.pack(pady= 12, padx =10)

button1 = customtkinter.CTkButton(master= frame, text="Login",font = ("Roboto",13,'bold'), command=login)
button1.pack(pady= 12, padx =40)
    
root.mainloop()