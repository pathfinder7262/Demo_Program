#Inser_into _table_4.py
##this program inserts the record into the table Manually

import cx_Oracle
try:
    con = cx_Oracle.connect('system/orcl@localhost/PROD')
    print("connected")
    cur = con.cursor()
    qur = "insert into pythemp1 values(4,'rohit',3000,'jalna')"
    qur2 = "insert into pythemp1 values(5,'manoj',3500,'mumbai')"
    cur.execute(qur)
    cur.execute(qur2)
    con.commit()
    print("Data inserted -plz varify")
except cx_Oracle.DatabaseError as db:
    print("Problem in data base ", db)    
 
