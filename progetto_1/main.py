import Tkinter as tk
import sqlite3 as sql
from generate import generate
from login import login
class main:
    def __init__(self):
        self.db=sql.connect("database.db");
        self.db.text_factory=str
        self.cursor=self.db.cursor()
        self.generate=generate(self.cursor)
        self.root=tk.Tk()
        self.main_input=tk.Frame(self.root)
        self.main_input.grid(row=1,column=1)
        self.control=tk.Frame(self.root)
        self.control.grid(row=1,column=11)
        self.login=login(self.cursor.execute("select * from login").fetchall())
        self.gui()
    def gui(self):
        tk.Label(self.main_input,text="Password:").grid(row=2,column=2,sticky=tk.W)
        tk.Label(self.main_input,text="Final:").grid(row=6,column=2,sticky=tk.W)
        tk.Label(self.main_input,text="Description:").grid(row=9,column=2,sticky=tk.W)
        #Entry
        entry_begin=tk.Entry(self.main_input)
        entry_begin.grid(row=4,column=3,sticky=tk.W)
        self.final=tk.Entry(self.main_input)
        self.final.grid(row=8,column=3,sticky=tk.W)
        self.description=tk.Entry(self.main_input)
        self.description.grid(row=10,column=3,sticky=tk.W)
        #Button
        button_save=tk.Button(self.control,text="save",command=self.save)
        button_save.grid(row=1,column=1,sticky=tk.W,padx=10)
        button_login=tk.Button(self.control,text="login",command=lambda:self.login.gui(self.root))
        button_login.grid(row=3,column=1,sticky=tk.W,padx=10)
        button_generate=tk.Button(self.control,text="generate",command=lambda:self.main_encryption(entry_begin.get()))
        button_generate.grid(row=5,column=1,sticky=tk.W,padx=10)
        self.root.protocol("WM_DELETE_WINDOW",self.close )
        self.root.mainloop()

        
        
    def main_encryption(self,password):
        if self.login.getlock()==True:
           self.final.delete(0,"end")
           self.final.insert(0, self.generate.encryption(password.lower()))
        else:
            self.log_error()
    def log_error(self):
           self.description.delete(0,"end")
           self.description.insert(0,"Error log in")
             
    def save(self):
         if self.login.getlock()==True:
           self.generate.save(self.description.get(),self.final.get())
           self.description.delete(0,"end")
           self.description.insert(0,"Save")
         else:
           self.log_error()
             
        
    def close(self):
         self.db.commit()
         self.db.close()
         self.root.destroy()
         
         
       


a=main()
