#Alter(ADD_COLUMN)_table_2.py
#This program Add the column in the oracle data base.
import cx_Oracle
try:
    con=cx_Oracle.connect("system/orcl@localhost/PROD")
    print("\n connection obtained from oracle DB")
    cur=con.cursor()
    qry="alter table  pythemp1 add(eadd varchar2(20))"	
    cur.execute(qry)
    print("\nTable Modified in Oracle data base--plz verify")
except cx_Oracle.DatabaseError as db:
	print("Problem in data base ", db)
