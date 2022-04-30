#insert data in table in kvr database
#_insert_data_in_table_in_SQL_3

from connector import con_package as cp
import mysql.connector
import sys

try:

    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
    print("connected")
    cur = con.cursor()
    qry="insert into student values(10,'nehal',67.54)"
    cur.execute(qry)
    con.commit()
    print("record inserted")


except mysql.connector.DatabaseError as de:
    print("problem occur",de)
