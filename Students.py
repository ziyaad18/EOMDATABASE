import mysql.connector
from tkinter import *
from tkinter.ttk import *
from time import strftime
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


def add_Students():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()

    sql="insert into students values(%s,%s,%s)"
    val= (str(Name.get()),str(Surname.get()),str(Time.get()))

    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,'record inserted')
    xy = mycursor.execute("select * from user")
    for i in mycursor:
        print(i)



root = tk.Tk()
root.geometry("400x400")
root.title("Registor Students")
root.configure(bg="pink")

root.title('Students registor')
#### the time

lbl = Label(root, font = ('calibri', 15, 'bold'), background = 'purple', foreground = 'white')
lbl.place(x=135, y= 200)
time()


stName = tk.Label(root, text="Full  name", )
stName.place(x=50, y=20)
Name = tk.Entry(root, width=45)
Name.place(x=250, y=20, width=100)


stSurname = tk.Label(root, text="Full surname ")
stSurname.place(x=50, y=50)
Surname = tk.Entry(root, width=35)
Surname.place(x=250, y=50, width=100)



stTime =tk.Label(root, text="Enter time")
stTime.place(x=50, y=80)

Time =tk.Entry(root,width=35)
Time.place(x=250,y=80,width=100)

btn= tk.Button(root, text="Sign in Students", bg='red',command=add_Students)
btn.place(x=135, y=300, width=150)


root.mainloop()