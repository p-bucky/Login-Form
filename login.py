from tkinter import*
from PIL import ImageTk
from register import Register
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="*Password*",database="*Database*")
mycursor = mydb.cursor()

class Login_System:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.resizable(0,0)
        self.root.configure(bg="#558B2F")
        
        l1_Login = Label(self.root, text = "USERNAME: ",bg="#558B2F",fg="white",font=("Helvetica", 15))
        l2_pass = Label(self.root, text= "PASSWORD:",bg="#558B2F",fg="white",font=("Helvetica", 15))
        l1_Login.grid(row = 1, column = 1, pady=5,padx=0)
        l2_pass.grid(row = 2, column = 1, pady=5,padx=0)

        self.str_id = StringVar()
        self.str_pass = StringVar()
        e1_Id = Entry(self.root, textvariable=self.str_id)
        e2_pass = Entry(self.root, textvariable=self.str_pass)
        e1_Id.grid(row = 1, column = 2, pady=5,padx=5)
        e2_pass.grid(row = 2, column = 2, pady=5,padx=5)

        btn_login = Button(self.root, text="Login", width=10, bg="#00695C", command= lambda : self.Login())
        btn_reg = Button(self.root, text="Register", width=10, bg="#00695C", command= lambda : self.open_reg())
        btn_login.grid(row = 3, column = 1,pady=5,padx=30)
        btn_reg.grid(row = 3, column = 2)

    def open_reg(self):
        self.root.withdraw()
        self.open_reg = Toplevel(self.root)
        bb = Register(self.open_reg)

    def Login(self):
        usr= self.str_id.get()
        pss = self.str_pass.get()
        q = "SELECT username,password FROM login"
        mycursor.execute(q)
        for (username,password) in mycursor:
            if username == usr and password == pss :
                login = True
                break
            else:
                login = False
        
        if login == True:
            print("##### Logged In Successfully as", usr)
        elif login==False:
            print("===Please check your username and password===")
      
root = Tk()
obj = Login_System(root)
root.mainloop()