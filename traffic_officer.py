import sqlite3
from datetime import date

class traffic_officer:
    def __init__(self,uid,db_name):
        self.ticket_tno = 0
        self.user_id = uid
        self.vehicles_vin = 0
        self.db_name = db_name
        
    def issue_ticket(self,regno):
        return 0
               
        
    def find_car_owner(self,make, model, year, color, plate):
        return 0