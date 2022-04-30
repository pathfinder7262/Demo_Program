#sqlQRY

import mysql.connector

con = mysql.connector.connect(host="3306",use="root",passwd=" " )
print("Connected")
cur = con.cursor()

'''
show databases;

use db_name;

show tables;

select *from tbl_nm;
'''
https://stackoverflow.com/questions/51633002/how-to-use-mysql-from-xampp-for-python-3/51633382
