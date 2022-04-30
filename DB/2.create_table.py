#2.create_table.py
#conne_test.py
import cx_Oracle

try:
    db = cx_Oracle.connect("system/orcl@localhost/PROD")
    cur = db.cursor()
    print("Connected")
    qry = "update stud5 set(sname varchar(10), sno number(3), sadd varchar2(20),smarks number(6,2),sid number(3))"
    cur.execute(qry)
    print("Table Inserted-plz verify")
except cx_Oracle.DatabaseError as db:
    print(db)
    
