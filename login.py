import sqlite3
import reg_agent
import traffic_officer
import getpass
DB_NAME = raw_input("Enter db filename: ")
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

def main():
    global conn,c
    display_login()

    
# prompt user for username and password and check if they are in database
def display_login():
    global conn,c
    while True:
      username = raw_input("Username: ").lower()
      password = getpass.getpass("Password: ")

      c.execute(''' SELECT * FROM users WHERE uid=? AND pwd=?''',(username,password))
      rows = c.fetchall()
      if rows:
        log_on(rows)
      else:
        print("The username and password you entered were not found. Please try again.")
    
# Welcome user and move them to appropriate options based on position
def log_on(rows):
  print("Welcome.")
  uid = rows[0][0]
  if rows[0][2] == 'a':
    agent_actions(uid)
  elif rows[0][2] == 'o':
    officer_actions(uid)

# list possible agent actions and prompt user to choose one
def agent_actions(uid):
  loggedIn = True
  validSelect = {"regbirth": regBirth, "regmar": regMar, "renewvr": renewVR,
  "procbill": procBill, "procpay": procPay, "getdrab": getDrAb, "logout": logOut}
  while loggedIn:
    print("Please enter one of the following commands:")
    print("[regBirth] - register a birth")
    print("[regMar] - register a marriage")
    print("[renewVR] - renew a vehicle registration")
    print("[procBill] - process a bill of sale")
    print("[procPay] - process a payment")
    print("[getDrAb] - get a drivers abstract")
    print("[logOut] - log out of account")
    usrSelect = raw_input().lower()
    func = validSelect.get(usrSelect, lambda uid:"Invalid choice")
    loggedIn = func(uid)
  
# list possible officer actions and prompt user to choose one
def officer_actions(uid):
  loggedIn = True
  validSelect = {"issuetick": issueTick, "findcarown": findCarOwn, "logout": logOut}
  while loggedIn:
    print("Please enter one of the following commands:")
    print("[issueTick] - issue a ticket")
    print("[findCarOwn] - find a car owner")
    print("[logOut] - log out of account")
    usrSelect = raw_input().lower()
    func = validSelect.get(usrSelect, lambda uid:"Invalid choice")
    loggedIn = func(uid)

# agent options 
# register a birth
def regBirth(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  fname = raw_input("first name: ")
  lname = raw_input("last name: ")
  gender = raw_input("gender: ")
  bdate = raw_input("birth date: ")
  bplace = raw_input("birth place: ")
  mother_fname = raw_input("mother first name: ")
  mother_lname = raw_input("mother last name: ")
  father_fname = raw_input("father first name: ")
  father_lname = raw_input("father last name: ")
  agent.register_birth(fname,lname,gender,bdate,bplace,mother_fname,mother_lname,father_fname,father_lname)
  return True

# register marriage
def regMar(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  p1_fname = raw_input("Person 1 first name: ")
  p1_lname = raw_input("Person 1 last name: ")
  p2_fname = raw_input("Person 2 first name: ")
  p2_lname = raw_input("Person 2 last name: ")
  agent.register_marriage(p1_fname,p1_lname, p2_fname, p2_lname)
  return True

# renew vehicle registration
def renewVR(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  num_Reg = int(raw_input("Registration number: "))
  agent.renew_reg(num_Reg)
  return True

# process bill of sale
def procBill(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  vin = int(raw_input("Vehicle Id number: "))
  curr_owner_fname = raw_input("Current Owner First Name: ")
  curr_owner_lname = raw_input("Current Owner Last Name: ")
  new_owner_fname = raw_input("New Owner First Name: ")
  new_owner_lname = raw_input("New Owner Last Name: ")
  plate_no = raw_input("Plate Number: ")
  agent.process_bill_sale(vin,curr_owner_fname,curr_owner_lname,new_owner_fname,new_owner_lname,plate_no)
  return True

# process payment
def procPay(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  tno = raw_input("Ticket number: ")
  amount = raw_input("Ticket amount: ")
  agent.process_payment(tno,amount)
  return True

# get a drivers abstract
def getDrAb(uid):
  # incomplete
  return True

# officer options
# issue a ticket
def issueTick(uid):
  officer = traffic_officer.traffic_officer(uid, DB_NAME)
  regno = raw_input("Vehicle registration number: ")
  officer.issue_ticket(regno)
  return True

# find a cars owner 
def findCarOwn(uid):
  officer = traffic_officer.traffic_officer(uid, DB_NAME)
  make = raw_input("Make of car: ")
  model = raw_input("Model of car: ")
  year = raw_input("Year of car: ")
  color = raw_input("Color of car: ")
  plate = raw_input("Plate of car: ")
  officer.find_car_owner(make, model, year, color, plate)
  return True

# both can use
def logOut(uid):
  return False



main()