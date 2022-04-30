#create table in kvr database
#table_create_in_SQL_2
import mysql.connector
from connector import con_package as cp
import sys
try:
    print("connected")
    cur = cp.dcon().cursor()
    tqry='create table emp1(ename varchar(10) not null,eno int primary key not null)'
    cur.execute(tqry)
    print(" created--pizz verify...")
except mysql.connector.DatabaseError as de:
    print("error",de)
