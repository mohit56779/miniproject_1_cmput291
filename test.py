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
);   ''')
    
#    test_process_payment()    
    test_register_birth()   
#    test_process_bill_sale()
    


#    test_reg_marriage()

    
def test_reg_marriage():
    global conn,c
    
    c.execute(''' INSERT into persons values('sam','san',?,?,?,?)''',( None, None, None,None))
    c.execute(''' INSERT into persons values('john','wong',?,?,?,?)''',( None, None, None,None))
    conn.commit()
    
    c.execute(''' INSERT into users values (? ,'00000000','a','sam','san','tokyo')''', ('00000000',))
    
    conn.commit()
    
    agent = reg_agent.reg_agent('00000000','./assignment3.db')
    
    # test_1
   # agent.register_marriage('sam','san', 'john', 'wong')
    
    # test_2
    agent.register_marriage('tom','low','jam','high')
    
    conn.commit()
   # c.execute(''' INSERT into marriages values (?,?,?,'sam','san', 'john', 'wong') ''', (None, None, None))
   # conn.commit()
   
    c.execute(''' SELECT * FROM marriages''')
    
    
    rows = c.fetchall()
    print(rows)
    
    c.execute(''' SELECT * FROM persons''')
    
    
    rows = c.fetchall()    
    
    print(rows)
    
def test_process_payment():
    
    global conn,c
    c.execute(''' INSERT into vehicles values(?,?,?,?,?);''',(0,None,None,None,None))
    c.execute(''' INSERT into registrations values(?,?,?,?,?,?,?)''',(0,None, None,None,0,None,None))
    c.execute('''INSERT into tickets values (?,?,?,?,?);''', (2,0,1500,None, None))
    
    conn.commit()
    
    agent = reg_agent.reg_agent('00000000','./assignment3.db')

    agent.process_payment("",500)

  
    
    c.execute(''' SELECT * FROM payments''')
    
    print(c.fetchall())
    
    
def test_process_bill_sale():
    global conn,c
    c.execute(''' INSERT into persons values('Ron','Rin',?,?,?,?)''',( None, None, None,None))
        
    c.execute(''' INSERT into vehicles values(?,?,?,?,?);''',('0000',None,None,None,None))
    c.execute(''' INSERT into vehicles values(?,?,?,?,?);''',('1111',None,None,None,None))
    
    c.execute('''INSERT into registrations values (?, date('now'), date('now', '-1 day'),?,?,?,?);''',(98,99, '0000',"Ron","Rin"))
    c.execute('''INSERT into registrations values (?, date('now'), date('now'),?,?,?,?);''',(99,99, '0000',"Ron","Rin"))
    c.execute('''INSERT into registrations values (?,date('now'), date('now', '-1 day'),?,?,?,?);''',(100,99, '1111',"Ron","Rin"))
    
    
    conn.commit()
    
    c.execute(''' SELECT * FROM registrations WHERE vin = ?''', ('0000',))
    print(c.fetchall())
    
    agent = reg_agent.reg_agent('00000000','./assignment3.db')
 
    # agent.process_bill_sale('0000',"R","R","Aria","Smith",1000)   
    agent.process_bill_sale('0000',"Ron","Rin","Aria","Smith",1000)
    
    conn.commit()
    
    c.execute(''' SELECT * FROM registrations WHERE vin = ?''', ('0000',))
    print(c.fetchall())
    
def test_register_birth():
    global conn,c
    
    c.execute(''' INSERT into persons values('sam','san',?,?,?,?)''',( None, None, None,None))
    c.execute(''' INSERT into persons values('john','wong',?,?,?,?)''',( None, None, None,None)) 
    
    c.execute(''' INSERT into users values (? ,'00000000','a','sam','san','tokyo')''', ('00000000',))
    
    conn.commit()
    
    agent = reg_agent.reg_agent('00000000','./assignment3.db')
    
   # agent.register_birth('mal','wal','M','1925-07-13','tokyo','w','a','b','c')
    
    agent.register_birth('mal','wal','M','1925-07-13','tokyo','john','wong','sAm','sAn')
    
    c.execute(''' SELECT * FROM persons''')
    print(c.fetchall())
    
    conn.commit()
    
    c.execute(''' SELECT * FROM births''')
    print(c.fetchall())
    
    conn.commit()
    
    conn.close()
        
        
        
        
        
    

   
   
    
    
    
    
main()