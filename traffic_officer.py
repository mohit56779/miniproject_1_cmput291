import sqlite3
from datetime import date

class traffic_officer:
    def __init__(self,uid,db_name):
        self.ticket_tno = 0
        self.user_id = uid
        self.db_name = db_name
        
    # method for issuing a ticket under the officers name
    def issue_ticket(self,regno):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(''' SELECT fname, lname, regno, make, model, year, color
        FROM registrations JOIN vehicles USING(vin) 
        WHERE regno=? COLLATE NOCASE; ''',(regno,))
        rows = c.fetchall()
        # ticket the registration
        if rows:
            print(rows)
            vdate = input("violation date: ")
            violation = input("Brief violation description: ")
            fine = input("Fine amount:")
            c.execute(''' INSERT INTO tickets VALUES(?,?,?,?,?); ''',(self.ticket_tno,regno, fine, violation, vdate))
            self.ticket_tno += 1
        else:
            print("The registration number was not found")

    # method for finding a car owner under the officers name
    def find_car_owner(self,make, model, year, color, plate):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        return 0