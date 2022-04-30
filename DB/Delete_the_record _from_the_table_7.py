#Delete_the_record _from_the_table_7.py
#delete the employee whose salary>4000

import cx_Oracle
try:
    con = cx_Oracle.connect('system/orcl@localhost/PROD')
    cur = con.cursor()
    qur='delete from pythemp1 where sal>2000 '
    cur.execute(qur)
    con.commit()
    if(cur.rowcount>0):
        print("{}Delete successfully..".format(cur.rowcount))
    else:
        print("Not found")
 
except cx_Oracle.DatabaseError as db:
	print("Problem in data base ", db)    
