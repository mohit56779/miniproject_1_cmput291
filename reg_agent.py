import sqlite3
from datetime import date
from datetime import datetime

class reg_agent:
    def __init__(self,uid,db_name):
        self.marriage_regno = 0
        self.registration_regno = 0
        self.user_id = uid
        self.birth_regno = 0
        self.db_name = db_name
        
    def register_birth(self,fname,lname,gender,bdate,bplace,mother_fname,mother_lname,father_fname,father_lname):
        
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute('''SELECT * FROM persons WHERE fname = ? COLLATE NOCASE AND lname = ? COLLATE NOCASE; ''',(father_fname,father_lname))
        
        result = c.fetchall()
        
        if result == []:
            name_matches = False
            all_given = False
            
            while name_matches == False or all_given == False:
                inp_1 = input("The child's Father does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333: ")
                inp_1 = inp_1.split(',')
                
                if len(inp_1) == 6:
                    all_given = True
                else:
                    print("Not all values required were inputed, Please try again")
                    
                if inp_1[0] == father_fname and inp_1[1] == father_lname:
                    name_matches = True
                else:
                    print("That's not the name of father you tried to register for the child. Please try again.")
            
            for index in range(len(inp_1)):
                if  inp_1[index] =="":
                    inp_1[index] = None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?)''', (inp_1[0],inp_1[1],inp_1[2],inp_1[3],inp_1[4],inp_1[5]))
            
        conn.commit()
        
        c.execute('''SELECT address,phone FROM persons WHERE fname = ? COLLATE NOCASE AND lname = ? COLLATE NOCASE; ''',(mother_fname,mother_lname))
        
        result = c.fetchall()

        
        if result == []:
            name_matches = False
            all_given = False
            
            while name_matches == False or all_given == False:
                inp_1 = input("The child's Mother does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333: ")
                inp_1 = inp_1.split(',')
                
                if len(inp_1) == 6:
                    all_given = True
                else:
                    print("Not all values required were inputed, Please try again")
                    
                if inp_1[0] == mother_fname and inp_1[1] == mother_lname:
                    name_matches = True
                else:
                    print("That's not the name of Mother you tried to register for the the child. Please try again.")
            
            for index in range(len(inp_1)):
                if  inp_1[index] =="":
                    inp_1[index] = None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?)''', (inp_1[0],inp_1[1],inp_1[2],inp_1[3],inp_1[4],inp_1[5]))
            
            mother_address = inp_1[4]
            mother_phone = inp_1[5]              
            
            conn.commit()  
        else:
            mother_address = result[0][0]
            mother_phone = result[0][1]            
            
        c.execute(''' SELECT city FROM users WHERE uid = ? COLLATE NOCASE;  ''', (self.user_id,))
     
        city = c.fetchall()[0][0]
      
        
        conn.commit()
        
        c.execute('''INSERT INTO births VALUES (?,?,?,date('now'),?,?,?,?,?,?)''', (self.birth_regno,fname,lname,city,gender,father_fname,father_lname,mother_fname,mother_lname))
        
        conn.commit()
        
        c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?)''', (fname,lname,bdate,bplace,mother_address,mother_phone))
        
        conn.commit()
        
        self.birth_regno += 1
        
        conn.close()         
        
    def register_marriage(self,p1_fname,p1_lname, p2_fname, p2_lname):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(''' SELECT * FROM persons WHERE fname = ? COLLATE NOCASE AND lname = ? COLLATE NOCASE; ''',(p1_fname,p1_lname))
        
        result_p1 = c.fetchall()
       
        if result_p1 == []:
            
            partner_name_matches = False
            all_given = False
            
            while partner_name_matches == False or all_given == False:
                inp_1 = input("The first Partner does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333: ")
                inp_1 = inp_1.split(',')
                
                if len(inp_1) == 6:
                    all_given = True
                else:
                    print("Not all values required were inputed, Please try again")
                    
                if inp_1[0] == p1_fname and inp_1[1] == p1_lname:
                    partner_name_matches = True
                else:
                    print("That's not the name of first partner you tried to register. Please try again.")
            
            for index in range(len(inp_1)):
                if  inp_1[index] =="":
                    inp_1[index] = None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?)''', (inp_1[0],inp_1[1],inp_1[2],inp_1[3],inp_1[4],inp_1[5]))
            
        conn.commit()
        
        c.execute(''' SELECT * FROM persons WHERE fname = ? COLLATE NOCASE and lname = ? COLLATE NOCASE ;''',(p2_fname,p2_lname))
        result_p2 = c.fetchall()
       
        if result_p2 == []:
            
            partner_name_matches = False
            all_given = False
            
            while partner_name_matches == False or all_given == False:
                inp_2 = input("The second Partner does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333: ")
                inp_2 = inp_2.split(',')
                
                if len(inp_2) == 6:
                    all_given = True
                else:
                    print("Not all values required were inputed, Please try again")
                    
                if inp_2[0] == p2_fname and inp_2[1] == p2_lname:
                    partner_name_matches = True
                else:
                    print("That's not the name of second partner you tried to register. Please try again.")
                    
            
            for index in range(len(inp_2)):
                if  inp_2[index] =="":
                    inp_2[index] = None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?);''', (inp_2[0],inp_2[1],inp_2[2],inp_2[3],inp_2[4],inp_2[5]))
            
        conn.commit()
        
        c.execute(''' SELECT city FROM users WHERE uid = ? COLLATE NOCASE;  ''', (self.user_id,))
        
        city = c.fetchall()[0][0]
      
        
        conn.commit()
        
        c.execute('''INSERT INTO marriages VALUES (?,?,?,?,?,?,?)''', (self.marriage_regno,date.today(),city,p1_fname,p1_lname, p2_fname, p2_lname))
        
        conn.commit()
        
        self.marriage_regno += 1
        
        conn.close()
        
    def process_payment(self, tno,amount):
        int(tno)
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        
        c.execute(''' SELECT * FROM tickets WHERE tno = ? ;''', (tno,))
        
        result = c.fetchone()
       
        assert result!= None, "Ticket number does not exist"
        
        conn.commit()
        
        c.execute(''' SELECT fine FROM tickets WHERE tno = ? ;''', (tno,))
        
        fine = c.fetchone()[0]
        
        conn.commit()
        
        c.execute(''' SELECT amount FROM payments where tno = ?;''', (tno,))
        
        result = c.fetchall()
        
        total_paid = 0
        
        for item in result:
            total_paid += item[0]
            
        new_total = total_paid + int(amount)
        
        assert new_total <= fine, "The total payment for this ticket exceeds the fine amount"
        
        conn.commit()
        
        c.execute(''' INSERT into payments values (?,?,?);''',(tno,date.today(),amount))
        
        conn.commit()
        conn.close()
        
    def process_bill_sale(self,vin,curr_owner_fname,curr_owner_lname,new_owner_fname,new_owner_lname,plate_no):
        
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()       
        c.execute(''' SELECT * FROM persons WHERE fname = ? COLLATE NOCASE and lname = ? COLLATE NOCASE ''', (new_owner_fname, new_owner_lname))
        
        result = c.fetchall()
        
        assert result != [], "New owner does not exist"
        
        conn.commit()
        c.execute(''' SELECT fname,lname,regno FROM registrations WHERE vin = ? COLLATE NOCASE AND julianday(expiry) >= julianday(CURRENT_DATE); ''', (vin,))
        
       
        result = c.fetchall()
        result_fname = result [0][0]
        result_lname = result [0][1]
        result_regno = result [0][2]
        
        assert result_fname == curr_owner_fname and result_lname == curr_owner_lname, "The current owner for this car in our database is different from what was mentioned"
        
        conn.commit()
        
        today = date.today()
        
        c.execute(''' UPDATE registrations SET expiry = ? WHERE regno = ? ''', (today,result_regno))     
        
        
        c.execute(''' INSERT into registrations values (?,?,date('now','+1 year'),?,?,?,?);''',(self.registration_regno, today,plate_no,vin,new_owner_fname,new_owner_lname))
        
        self.registration_regno += 1
        
        conn.commit()
        conn.close()
        
    def renew_reg(self,Num_Reg):
    
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(''' SELECT expiry FROM registrations WHERE regno= ? COLLATE NOCASE; ''',(Num_Reg,))
       
        result = c.fetchall() 
        Actual_date = date.today()
        
        assert result != None, "Wrong Registration Number"
  
        C_expiry = result[0][0]
    
        C_expiry = C_expiry.split('-')
        C_expiry_datetime = datetime(int(C_expiry[0]),int(C_expiry[1]),int(C_expiry[2]))
        
        Actual_date = str(Actual_date).split('-')
        Actual_date_datetime = datetime(int(Actual_date[0]),int(Actual_date[1]),int(Actual_date[2]))
      
        if C_expiry_datetime <= Actual_date_datetime: 
            c.execute("UPDATE registrations SET expiry=date('now', '+1 year') WHERE regno=?", (Num_Reg,))
            conn.commit()
            
        elif C_expiry_datetime > Actual_date_datetime:
            c.execute("UPDATE registrations SET expiry=date(expiry, '+1 year') WHERE regno=?", (Num_Reg,))
            conn.commit()   
            

    
        
        
        
        
        
        
        
        
        
        
        
    

    
        
        


        




