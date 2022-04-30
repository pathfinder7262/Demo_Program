#ATM Application
#widrawal fun  
#deposit Fun
##show Balnace

#DataBase==>

import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',user='root',passwd='',database='kvr')
    cur=con.cursor()
    qur= "create table cust(cname varchar(20),cacno int(10) primary key,cbal float (10))"
    cur.execute(qur)
    print("Table Created")
except  mysql.connector.DatabaseError as de:
    print("error",de)
