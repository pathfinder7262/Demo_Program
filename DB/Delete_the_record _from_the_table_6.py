#Delete_the_record _from_the_table_6.py
#delete the employee whose employee number is 10

import cx_Oracle

try:
    con=cx_Oracle.connect("system/orcl@localhost/PROD")
    cur = con.cursor()
    print("connected")
    qur = 'delete from pythemp1 where eno=1'
    cur.execute(qur)
    con.commit()
    if(cur.rowcount>0):
        print("{} record deleted..('-')".format(cur.rowcount))
    else:
        print("Record does not Exists")
except cx_Oracle.DatabaseError as db:
	print("Problem in data base ", db)
