import sqlite3 as sql
class generate :
    def __init__(self,cursor):
        self.cursor=cursor
       
    def encryption(self,password):
           result=""
           for i in password[:]:
               a=("select * from alphabet where letters= (?)")
               result+=str(self.cursor.execute(a,i).fetchall()[0][1])
           return result
       
    def save(self,word,password):
           execute=('insert into passwords values (?, ?) ')
           self.cursor.execute(execute,(word, password))
          
        
        
        