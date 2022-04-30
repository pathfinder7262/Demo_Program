#orcl1.py
#conne_test.py
import cx_Oracle

try:
    db = cx_Oracle.connect("system/orcl@localhost/PROD")
    cur_obj = db.cursor()
    print("Connected")
    qry = "create table stud(sname varchar(10),sno number(5),sadd varchar1(20),smark number1(6,2))"
    cur_obj.execute(qry)
    print("Table Inserted-plz verify")
except cx_Oracle.DatabaseError as db:
    print("Sorry")
    
