#Alter_table_2.py
#this program modified the table in oracle data base.
import cx_Oracle
con=cx_Oracle.connect("system/orcl@localhost/PROD")
print("\n connection obtained from oracle DB")
cur=con.cursor()
qry="alter table  pythemp1 add(eadd varchar2(20))"	
cur.execute(qry)
print("\nTable Modified in Oracle data base--plz verify")
