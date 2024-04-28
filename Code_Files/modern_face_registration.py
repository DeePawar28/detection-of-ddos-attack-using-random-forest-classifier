import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os

import customtkinter

app = customtkinter.CTk()
app.geometry("500x750")
app.title("Registration form ")
# app.config(bg ='#290514')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

font1 = ('Arial',18,'bold')
font2 = ('Arial',15)

db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()

Fullname = customtkinter.StringVar()
Address = customtkinter.StringVar()
Username = customtkinter.StringVar()
Email = customtkinter.StringVar()
Phone = customtkinter.IntVar()
var = customtkinter.IntVar()
Age = customtkinter.IntVar()
Password = customtkinter.StringVar()
Confirm_password = customtkinter.StringVar()
policeno = customtkinter.IntVar()
value = random.randint(1, 1000)



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = Address.get()
    un = Username.get()
    email = Email.get()
    mobile = Phone.get()
    gender = var.get()
    time = Age.get()
    pwd = Password.get()
    cnpwd = Confirm_password.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(Username.get())])

    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            app.destroy()
           # window.destroy()

#####################################################################################################################################################
def login():
     from subprocess import call
     call(["python", "modern_face_login.py"])
     app.destroy()

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady =0, padx=20, fill="both", expand=True)


label = customtkinter.CTkLabel(frame, text ="Register", font = ("Roboto",40,'bold') )
label.pack(pady =20, padx = 5)

fullname = customtkinter.CTkLabel(frame,text="Fullname: ",font = font2, width =10)
fullname.place(x =90, y=150)

address= customtkinter.CTkLabel(frame,text="Address: ",font = font2, width =10)
address.place(x =90, y=210)

email = customtkinter.CTkLabel(frame,text="Email: ",font = font2, width =10)
email.place(x =90, y=270)

phone= customtkinter.CTkLabel(frame,text="Phone: ",font = font2, width =10)
phone.place(x =90, y=330)

age= customtkinter.CTkLabel(frame,text="Age: ",font = font2, width =10)
age.place(x =90, y=390)

gender= customtkinter.CTkLabel(frame,text="Gender: ",font = font2, width =10)
gender.place(x =90, y=450)

username = customtkinter.CTkLabel(frame,text="Username: ",font = font2, width =10)
username.place(x =90, y=510)

password= customtkinter.CTkLabel(frame,text="Password: ",font = font2, width =10)
password.place(x =90, y=570)

confirm_password= customtkinter.CTkLabel(frame,text="F.Password: ",font = font2, width =10)
confirm_password.place(x =90, y=630)


################################################################################

entry1 = customtkinter.CTkEntry(app,textvariable=Fullname, width =150)
entry1.place(x =230, y=152)

entry2 = customtkinter.CTkEntry(app,textvariable= Address, width =150)
entry2.place(x =230, y=212)

entry3 = customtkinter.CTkEntry(app,textvariable=Email, width =150)
entry3.place(x =230, y=272)

entry4 = customtkinter.CTkEntry(app, font= font2,textvariable=Phone, width =150)
entry4.place(x =230, y=332)

entry5 = customtkinter.CTkEntry(app,textvariable=Age, width =150)
entry5.place(x =230, y=392)

entry5 = customtkinter.CTkComboBox(app,dropdown_hover_color ="#145e15",values=["Male","Female"],width =150)
entry5.place(x =230, y=452)

entry6 = customtkinter.CTkEntry(app,textvariable=Username, width =150)
entry6.place(x =230, y=510)

entry7 = customtkinter.CTkEntry(app,textvariable=Password, width =150)
entry7.place(x =230, y=570)

entry8 = customtkinter.CTkEntry(app,textvariable=Confirm_password, width =150)
entry8.place(x =230, y=628)

button1 = customtkinter.CTkButton(app, text="Register",font = ("Roboto",13,'bold'), command = insert)
button1.place(x =70, y=690)

button1 = customtkinter.CTkButton(app, text="Login",font = ("Roboto",13,'bold'), command = login)
button1.place(x =260, y=690)


app.mainloop()

