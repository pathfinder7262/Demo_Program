#Inser_into _table_5.py
##this program inserts the record into the table Dinamically

import cx_Oracle
try:
    con = cx_Oracle.connect('system/orcl@localhost/PROD')
    cur = con.cursor()
    while(True):
        eno =int(input("Enter the Emp no.="))
        enm = input("Enter the Name:=")
        esal = float(input("Enter the salary="))
        eadd= input("Enter the address=")
        qur =" insert into pythemp1 values(%d,'%s',%f,'%s')"
        cur.execute(qur %(eno,enm,esal,eadd))
        con.commit()
        print("Data Added")
        ch=input("again insert ? Yes/No")
        if(ch=="no"):
            break
except cx_Oracle.DatabaseError as db:
	print("Problem in data base ", db)
         
        
 
