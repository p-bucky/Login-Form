from tkinter import*
from PIL import ImageTk
import mysql.connector

class Register():
    
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.resizable(0,0)
        self.root.configure(bg="#424242")
        
        l1_name = Label(self.root, text = "Name:     ",bg="#424242",fg="white",font=("Helvetica", 10))
        l2_user = Label(self.root, text = "Username:",bg="#424242",fg="white",font=("Helvetica", 10))
        l3_pass = Label(self.root, text= "Password:",bg="#424242",fg="white",font=("Helvetica", 10))
        l1_name.grid(row = 1, column = 1, pady=5)
        l2_user.grid(row = 2, column = 1, pady=5)
        l3_pass.grid(row = 3, column = 1, pady=5)

        self.str_name = StringVar()
        self.str_user = StringVar()
        self.str_pass = StringVar()
        e1_name = Entry(self.root,textvariable=self.str_name)
        e2_user = Entry(self.root,textvariable=self.str_user)
        e3_pass = Entry(self.root,textvariable=self.str_pass)
        e1_name.grid(row = 1, column = 2, pady=5,padx=10)
        e2_user.grid(row = 2, column = 2, pady=5,padx=10)
        e3_pass.grid(row = 3, column = 2, pady=5,padx=10)

        btn_reg = Button(self.root, text="Register", width=10, bg="#F4511E",command= lambda : self.reg())
        btn_reg.grid(row = 4, column = 2, pady=5)


    def reg(self):
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="*Password*",database="*Database*")
        mycursor = mydb.cursor()

        sql = "INSERT INTO Register (name, username, password) VALUES (%s, %s, %s)"
        val = (self.str_name.get(), self.str_user.get(), self.str_pass.get())
        mycursor.execute(sql, val)
        mydb.commit()
        sql2 = "INSERT INTO Login (username, password) VALUES (%s, %s)"
        val2 = (self.str_user.get(), self.str_pass.get())
        mycursor.execute(sql2, val2)
        mydb.commit()
         
        print("Data is Inserted %s", self.str_name.get())
        