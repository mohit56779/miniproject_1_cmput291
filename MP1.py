'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")


def renew_reg(self,Num_Reg):

   conn = sqlite3.connect(self.db_name)
   c = conn.cursor()
   c.execute(''' SELECT regno,expiry FROM regstrations WHERE regno= ? COLLATE NOCASE; ''',(Num_reg))
   
   result = c.fetchall() 
   Actual_date = date.today()
    
   assert result != None, "Wrong Registration Number"
            
    if C_expiry <= Actual_date: 
        cursor.execute("UPDATE registrations SET expiry=date('now', '+1 year') WHERE Num_reg=?", (reg_no,))
        conn.commit()
        
    elif C_expiry > Actual_date()::
        cursor.execute("UPDATE registrations SET expiry=date(expiry, '+1 year') WHERE Num_reg=?", (reg_no,))
        conn.commit() 
      
    
       

  
