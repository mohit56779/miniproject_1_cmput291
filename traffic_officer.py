import sqlite3
from datetime import date

class traffic_officer:
    def __init__(self,uid,db_name):
        self.user_id = uid
        self.db_name = db_name
        
    # method for issuing a ticket under the officers name
    def issue_ticket(self,regno):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute(''' SELECT fname, lname, regno, make, model, year, color
        FROM registrations r, vehicles v 
        WHERE r.vin = v.vin AND regno=? COLLATE NOCASE; ''',(regno,))
        rows = c.fetchall()
        # ticket the registration
        if rows == []:
            print("The registration number was not found")
            return 0
        print(rows)
        vdate = raw_input("violation date: ")
        if not vdate:
            vdate = date.today()
        violation = raw_input("Brief violation description: ")
        fine = raw_input("Fine amount:")
        # get unique ticket number based on number of tickets already in the database
        c.execute(''' SELECT count(*) from tickets; ''')
        ticket_number = c.fetchone()[0]
        c.execute(''' INSERT INTO tickets VALUES(?,?,?,?,?); ''',(ticket_number,regno, fine, violation, vdate))
        conn.commit()
        conn.close()


    # method for finding a car owner under the officers name
    def find_car_owner(self,make, model, year, color, plate):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        #incomplete
        conn.close()