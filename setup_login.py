import sqlite3
import reg_agent
import traffic_officer
conn = sqlite3.connect('./assignment3.db')
c = conn.cursor()

def main():
    global conn,c
    

    c.executescript('''drop table if exists demeritNotices;
drop table if exists tickets;
drop table if exists registrations;
drop table if exists vehicles;
drop table if exists marriages;
drop table if exists births;
drop table if exists persons;
drop table if exists payments;
drop table if exists users;

PRAGMA foreign_keys = ON;

create table persons (
  fname		char(12),
  lname		char(12),
  bdate		date,
  bplace	char(20), 
  address	char(30),
  phone		char(12),
  primary key (fname, lname)
);
create table births (
  regno		int,
  fname		char(12),
  lname		char(12),
  regdate	date,
  regplace	char(20),
  gender	char(1),
  f_fname	char(12),
  f_lname	char(12),
  m_fname	char(12),
  m_lname	char(12),
  primary key (regno),
  foreign key (fname,lname) references persons,
  foreign key (f_fname,f_lname) references persons,
  foreign key (m_fname,m_lname) references persons
);
create table marriages (
  regno		int,
  regdate	date,
  regplace	char(20),
  p1_fname	char(12),
  p1_lname	char(12),
  p2_fname	char(12),
  p2_lname	char(12),
  primary key (regno),
  foreign key (p1_fname,p1_lname) references persons,
  foreign key (p2_fname,p2_lname) references persons
);
create table vehicles (
  vin		char(5),
  make		char(10),
  model		char(10),
  year		int,
  color		char(10),
  primary key (vin)
);
create table registrations (
  regno		int,
  regdate	date,
  expiry	date,
  plate		char(7),
  vin		char(5), 
  fname		char(12),
  lname		char(12),
  primary key (regno),
  foreign key (vin) references vehicles,
  foreign key (fname,lname) references persons
);
create table tickets (
  tno		int,
  regno		int,
  fine		int,
  violation	text,
  vdate		date,
  primary key (tno),
  foreign key (regno) references registrations
);
create table demeritNotices (
  ddate		date, 
  fname		char(12), 
  lname		char(12), 
  points	int, 
  desc		text,
  primary key (ddate,fname,lname),
  foreign key (fname,lname) references persons
);
create table payments (
  tno		int,
  pdate		date,
  amount	int,
  primary key (tno, pdate),
  foreign key (tno) references tickets
);
create table users (
  uid		char(8),
  pwd		char(8),
  utype		char(1),	-- 'a' for agents, 'o' for officers
  fname		char(12),
  lname		char(12), 
  city		char(15),
  primary key(uid),
  foreign key (fname,lname) references persons
);   
INSERT into persons VALUES('John', 'Wick','09-09-2000','Edmonton','why','care');
INSERT into persons VALUES('Viggo', 'Tarasov','09-09-2000','Russia','why','care');
INSERT into users VALUES('officer1', 'password1', 'o', 'Viggo', 'Tarasov', 'Russia');
INSERT into users VALUES('agent1', 'password1', 'a', 'John', 'Wick', 'Edmonton'); ''')

    display_login()

    
def display_login():
    global conn,c
    while True:
      username = input("Username: ")
      password = input("Password: ")

      c.execute(''' SELECT * FROM users WHERE uid=? AND pwd=?''',(username,password))
      rows = c.fetchall()
      if rows:
        log_on(rows)
      else:
        print("The username and password you entered were not found. Please try again.")
    
def log_on(rows):
  print(f"Welcome {rows[0][3]} {rows[0][4]}.")
  if rows[0][2] == 'a':
    agent_actions(rows)
  elif rows[0][2] == 'o':
    officer_actions(rows)

def agent_actions(rows):
  loggedOut = False
  validSelect = {"regBirth": regBirth, "regMar": regMar, "renewVR": renewVR,
  "procBill": procBill, "procPay": procPay, "getDrAb": getDrAb, "logOut": logOut}
  while not loggedOut:
    print("Please enter one of the following options:")
    print("[regBirth] - register a birth")
    print("[regMar] - register a marriage")
    print("[renewVR] - renew a vehicle registration")
    print("[procBill] - process a bill of sale")
    print("[procPay] - process a payment")
    print("[getDrAb] - get a drivers abstract")
    print("[logOut] - log out of account")
    usrSelect = input()
    func = validSelect.get(usrSelect, lambda:"Invalid choice")
    loggedOut = func()
  
def officer_actions(rows):
  loggedOut = False
  validSelect = {"issueTick": issueTick, "FindCarOwn": findCarOwn, "logOut": logOut}
  while not loggedOut:
    print("Please enter one of the following options:")
    print("[issueTick] - issue a ticket")
    print("[FindCarOwn] - find a car owner")
    print("[logOut] - log out of account")
    usrSelect = input()
    func = validSelect.get(usrSelect, lambda:"Invalid choice")
    loggedOut = func()

# agent options 
def regBirth():
  # to use these functions prompt input from user and 
  # use values to pass to actual class methods
  return False

def regMar():
  return False

def renewVR():
  return False

def procBill():
  return False

def procPay():
  return False

def getDrAb():
  return False

# officer options
def issueTick():
  return False

def findCarOwn():
  return False

# both can use
def logOut():
  return True



main()