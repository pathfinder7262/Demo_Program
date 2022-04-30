#Delet the data in table in kvr database
#_delete_data_in_table_in_SQL_6(dynamycally)

from connector import con_package as cp
import mysql.connector
import sys

try:

    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
    print("connected")
    cur = con.cursor()
    while(True):
        print("-"*50)
        dd = int(input("Enter the number"))
        qry="delete from  student where stno=%d"
        cur.execute(qry %dd)
        con.commit()
        if(cur.rowcount>0):
            print("deleted")
        else:
            print("Sorry error")
        ch = input("Delete again y/n:=")
        if(ch == "n"):
            break
        


except mysql.connector.DatabaseError as de:
    print("problem occur",de)
