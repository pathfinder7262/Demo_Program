#createtable_1.py
#this program create a table in oracle data base.
import cx_Oracle
try:
	con=cx_Oracle.connect("system/orcl@localhost/PROD")
	print("\n connection obtained from oracle DB")
	cur=con.cursor()
	qry="create table  pythemp1(eno number(2),name varchar2(10),sal number(6,2))"	
	cur.execute(qry)
	print("\nTable Created in Oracle data base--plz verify")
except cx_Oracle.DatabaseError as db:
	print("Problem in data base ", db)
