from email.errors import MessageError
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")


        #__________________IMAGES_____________________

        self.bg_icon=ImageTk.PhotoImage(file="bg_image.jpg") # Bc it is a jpg image
        self.user_icon=PhotoImage(file="user_icon.png")
        self.pass_icon=PhotoImage(file="padlock.png")
        self.logo_icon=PhotoImage(file="logo_icon.png")

        #________________VARIABLE____________________

        self.uname=StringVar()
        self.pass_=StringVar() 

        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="blue", fg="red", bd=10,relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="blue",fg="red").grid(row=3,column=1,pady=10)


    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error!","All field are required!!!")
        elif self.uname.get()=="Vikas" or self.pass_.get()=="12345":
            messagebox.showinfo("Successful",f"welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error!","Invalid Username or Passname")

root = Tk()
obj = Login_System(root)

root.mainloop()