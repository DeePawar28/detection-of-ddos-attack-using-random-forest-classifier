import customtkinter 

global fn
fn = ""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady =60, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master= frame, text ="DDoS Detection", font = ("Roboto",24,'bold'), )
label.pack(pady =12, padx = 10)

def reg():
    from subprocess import call
    call(["python","modern_face_registration.py"])

def log():
    from subprocess import call
    call(["python","modern_face_login.py"])
    
def window():
  root.destroy()

button1 = customtkinter.CTkButton(master= frame, text="Login", command=log)
button1.pack(pady= 12, padx =10)

button2 = customtkinter.CTkButton(master= frame, text="Register",command=reg)
button2.pack(pady= 12, padx =10)

button3 = customtkinter.CTkButton(master= frame, text="Exit",command=window)
button3.pack(pady= 12, padx =10)

root.mainloop()