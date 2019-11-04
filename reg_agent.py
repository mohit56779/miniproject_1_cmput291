import sqlite3
from datetime import date

class reg_agent:
    def __init__(self,uid):
        self.marriage_regno = 0
        self.user_id = uid
     
    def register_marriage(self,p1_fname,p1_lname, p2_fname, p2_lname):
        conn = sqlite3.connect('./assignment3.db')
        c = conn.cursor()
        c.execute(''' SELECT * FROM persons WHERE fname = ? AND lname = ?; ''',(p1_fname,p1_lname))
        
        result_p1 = c.fetchall()
       
        if result_p1 == []:
            
            partner_name_matches = False
            all_given = False
            
            while partner_name_matches == False and all_given == False:
                inp_1 = input("The first Partner does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333: ")
                inp_1 = inp_1.split(',')
                
                if len(inp_1) == 6:
                    all_given = True
                else:
                    print("Not all values required were inputed, Please try again")
                    
                if inp_1[0] == p1_fname and inp_1[1] == p1_lname:
                    parnet_name_matches = True
                else:
                    print("That's not the name of first partner you tried to register. Please try again.")
            
            for index in range(len(inp_1)-1):
                if  inp_1[index] =="":
                    inp_1[index] == None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?)''', (inp_1[0],inp_1[1],inp_1[2],inp_1[3],inp_1[4],inp_1[5]))
            
        conn.commit()
        
        c.execute(''' SELECT * FROM persons WHERE fname = ? and lname = ? ;''',(p2_fname,p2_lname))
        result_p2 = c.fetchall()[0][0]
        print(result_p2)
        if result_p2 == None:
            inp_2 = input("The second Partner does not exist in our database. Please put this person's first name, last name, birth date, birth place, address and phone seperated by a comma. The fields except first and last names can be left empty if not known. e.g - 'Sam, Sanny,,tokyo,,+111000333")
            inp_2 = inp_1.split(',')
            
            for index in range(len(inp_2)-1):
                if  inp_2[index] =="":
                    inp_2[index] == None
                    
            c.execute('''INSERT INTO persons VALUES (?,?,?,?,?,?);''', (inp_2[0],inp_2[1],inp2[2],inp_2[3],inp_2[4],inp2[5]))
            
        conn.commit()
        
        result = c.execute(''' SELECT city FROM users WHERE uid = ?;  ''', (self.user_id,))
        
        city = c.fetchall()[0][0]
      
        
        conn.commit()
        
        c.execute('''INSERT INTO marriages VALUES (?,?,?,?,?,?,?)''', (self.marriage_regno,date.today(),city,p1_fname,p1_lname, p2_fname, p2_lname))
        
        conn.commit()
        
        self.marriage_regno += 1
        
        
        
        
        
    

    
        
        


        




