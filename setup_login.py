import sqlite3
import reg_agent
import traffic_officer
import getpass
DB_NAME = input("Enter db filename: ")
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

def main():
    global conn,c

    display_login()

    
def display_login():
    global conn,c
    while True:
      username = input("Username: ")
      password = getpass.getpass("Password: ")

      c.execute(''' SELECT * FROM users WHERE uid=? AND pwd=?''',(username,password))
      rows = c.fetchall()
      if rows:
        log_on(rows)
      else:
        print("The username and password you entered were not found. Please try again.")
    
def log_on(rows):
  print(f"Welcome {rows[0][3]} {rows[0][4]}.")
  uid = rows[0][0]
  if rows[0][2] == 'a':
    agent_actions(uid)
  elif rows[0][2] == 'o':
    officer_actions(uid)

def agent_actions(uid):
  loggedIn = True
  validSelect = {"regBirth": regBirth, "regMar": regMar, "renewVR": renewVR,
  "procBill": procBill, "procPay": procPay, "getDrAb": getDrAb, "logOut": logOut}
  while loggedIn:
    print("Please enter one of the following commands:")
    print("[regBirth] - register a birth")
    print("[regMar] - register a marriage")
    print("[renewVR] - renew a vehicle registration")
    print("[procBill] - process a bill of sale")
    print("[procPay] - process a payment")
    print("[getDrAb] - get a drivers abstract")
    print("[logOut] - log out of account")
    usrSelect = input()
    func = validSelect.get(usrSelect, lambda uid:"Invalid choice")
    loggedIn = func(uid)
  
def officer_actions(uid):
  loggedIn = True
  validSelect = {"issueTick": issueTick, "FindCarOwn": findCarOwn, "logOut": logOut}
  while loggedIn:
    print("Please enter one of the following commands:")
    print("[issueTick] - issue a ticket")
    print("[FindCarOwn] - find a car owner")
    print("[logOut] - log out of account")
    usrSelect = input()
    func = validSelect.get(usrSelect, lambda uid:"Invalid choice")
    loggedIn = func(uid)

# agent options 
def regBirth(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  fname = input("first name: ")
  lname = input("last name: ")
  gender = input("gender: ")
  bdate = input("birth date: ")
  bplace = input("birth place: ")
  mother_fname = input("mother first name: ")
  mother_lname = input("mother last name: ")
  father_fname = input("father first name: ")
  father_lname = input("father last name: ")
  agent.register_birth(fname,lname,gender,bdate,bplace,mother_fname,mother_lname,father_fname,father_lname)
  return True

def regMar(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  p1_fname = input("Person 1 first name: ")
  p1_lname = input("Person 1 last name: ")
  p2_fname = input("Person 2 first name: ")
  p2_lname = input("Person 2 last name: ")
  agent.register_marriage(p1_fname,p1_lname, p2_fname, p2_lname)
  return True

def renewVR(uid):
  return True

def procBill(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  vin = input("Vehicle Id number: ")
  curr_owner_fname = input("Current Owner First Name: ")
  curr_owner_lname = input("Current Owner Last Name: ")
  new_owner_fname = input("New Owner First Name: ")
  new_owner_lname = input("New Owner Last Name: ")
  plate_no = input("Plate Number: ")
  agent.process_bill_sale(vin,curr_owner_fname,curr_owner_lname,new_owner_fname,new_owner_lname,plate_no)
  return True

def procPay(uid):
  agent = reg_agent.reg_agent(uid, DB_NAME)
  tno = input("Ticket number: ")
  amount = input("Ticket amount: ")
  agent.process_payment(tno,amount)
  return True

def getDrAb(uid):
  return True

# officer options
def issueTick(uid):
  return True

def findCarOwn(uid):
  return True

# both can use
def logOut(uid):
  return False



main()