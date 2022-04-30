#Delet the data in table in kvr database
#_delete_data_in_table_in_SQL_5

from connector import con_package as cp
import mysql.connector
import sys

try:

    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
    print("connected")
    cur = con.cursor()
    qry="delete from  student where stno=10"
    cur.execute(qry)
    con.commit()
    print("record inserted")


except mysql.connector.DatabaseError as de:
    print("problem occur",de)
