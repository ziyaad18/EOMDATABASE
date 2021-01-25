import mysql.connector
from tkinter import *
from tkinter import messagebox
from time import strftime
from tkinter import *
import tkinter as tk


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')