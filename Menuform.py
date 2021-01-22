import mysql.connector
from tkinter import *
from tkinter import messagebox
from time import strftime
from tkinter import *
import tkinter as tk

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)



def students():
    import Students
    Students.mainloop()


def regdetails():
    pass
    import employees

def SIGNIN():
    pass
    import employees
    employees.mainloop()
def SIGNOUT():
    pass
#Design the login form
root = tk.Tk()
root.geometry("500x400")
root.title("Registor")
root.configure(bg="pink")

lbl = Label(root, font = ('calibri', 15, 'bold'), background = 'purple', foreground = 'white')
lbl.place(x=150, y= 25)
time()





btn_adduser=tk.Button(root, text="Sign in students",bg="red",command=students)
btn_adduser.place(x=150,y=100)
btn_signin=tk.Button(root, text="Sign in employees",bg="red", command=SIGNIN)
btn_signin.place(x=150,y=200)

root.mainloop()