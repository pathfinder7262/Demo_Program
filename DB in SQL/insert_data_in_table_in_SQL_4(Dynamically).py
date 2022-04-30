#insert data in table in kvr database(dynamically)
#_insert_data_in_table_in_SQL_4(Dynamically)

from connector import con_package as cp
import mysql.connector
import sys

try:
    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
    print("connected")
    cur = con.cursor()
    while(True):
        print('-----------------------------------------------------------------------')
        snm = input("Enter the student name")
        sno = int(input("Enter the stud no."))
        smr = float(input("Enter marks"))
        qry="insert into student values(%s,%d,%f)"
    cur.execute(qry %(snm,sno,smr))
    con.commit()
    print("record inserted")


except mysql.connector.DatabaseError as de:
    print("problem occur",de)
