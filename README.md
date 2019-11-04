# miniproject_1_cmput291

MOHIT COMMENTS FOR COLLABORATION -

Hi guys, Just putting some info here so you guys can work with the methods I wrote easily -

-> test.py

(1) This file contains 2 global vars (conn and c) for the DB connections.
(2) Main function contains the script to create tables for testing and it calls the test functions one by one. (commented, uncomment the one you would like to test)
(3) There are seperate functions to test each methods I have written. 

-> reg_agent.py

I have finished following methods in this class till now, Information for each is below -

(1) register_marriages (Test function included in the test file)
(2) process_payment ( Test function included in the test file)
(3) process_bill_sale ( Test functin included in the test file)
(4) register_births ( Test function still on work)

I have put some info about these methods in the whatsapp group. In case of errors specified in the method question, assertion errors are raised in call stack by the methods. 

The User inputs will need to be tested for correctness in the main function.

~ The bugs currently that need to be fixed in this class are following -
HIGH PRIORITY -
(1) The SQlite codes are not case insenstive as per requirements

LOW PRIORITY -

(2) In registed_marriages and register_births methods, I am not sure if "NULL" is getting inserted for the blank fields when the new person is created or an empty string is inserted. This needs to be "NULL".
(3) For each of regno ( registration numbers), it would be good to do a validity check to make sure the regnos are really unique, I am using an instance variable and incrementing it for each method call for uniqueness. This is very low priority tho.

-> SQL injection attacks

To prevent from SQL injection attacks, Please check the wahtsapp group or the lab slides for lab class 2 python inside applications. Basically, use tuples to insert the variables instead of without them in each "execute" command. e.g -

SQL injection proof execute -
c.execute(''' SELECT id FROM users where pass = ?''', (password))

DONT DO THIS -

c.execute(''' SELECT id FROM users where pass = %s''', password)



