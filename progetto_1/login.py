import Tkinter as tk
class login :
    def __init__(self,credentials):
        self.credentials=(str(credentials[0][0]),str(credentials[0][1]))
        print(self.credentials[0])
        self.lock=False
    def unlock(self,username,password):
        if (username,password)==self.credentials:
            self.lock=True
            self.check.configure(text="Correct",fg="green")
        else:
            self.check.configure(text="Wrong",fg="red")
    def getlock(self):
        return self.lock
    def gui(self,root):
        self.root=tk.Toplevel(root)
        self.lock=False
        self.check=tk.Label(self.root,text="")
        self.check.grid(row=9,column=2,sticky=tk.W)
        tk.Label(self.root,text="Usename: ").grid(row=2,column=1,sticky=tk.W)
        entry_username=tk.Entry(self.root)
        entry_username.grid(row=4,column=2,sticky=tk.W)
        
        tk.Label(self.root,text="Password: ").grid(row=6,column=1,sticky=tk.W)
        entry_password=tk.Entry(self.root)
        entry_password.grid(row=8,column=2,sticky=tk.W)
        
        button_login=tk.Button(self.root,text="login",command=lambda:self.unlock(entry_username.get(),entry_password.get()))
        button_login.grid(row=9,column=1,sticky=tk.W,padx=10)
        self.root.protocol("WM_DELETE_WINDOW",self.close )
        
    def close(self):
        self.root.destroy()