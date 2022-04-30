#Alter(resize_COLUMN)_table_3.py
#This program Resize the column in the oracle data base.
import cx_Oracle

try:
    con=cx_Oracle.connect("system/orcl@localhost/PROD")
    print("Connected")
    cur = con.cursor()
    qur = "alter table pythemp1 modify(eno number(3),name varchar(10),sal number(6,2),eadd varchar2(15))"
    cur.execute(qur)
    print("Size chaged")
except cx_Oracle.DatabaseError:
    print("Problem in data base ")    
    

'''
BEFORE:===>
SQL> desc pythemp1
 Name                                      Null?    Type
 -----------------------------------------------------------------------------
 ENO                                                   NUMBER(5)
 NAME                                               VARCHAR2(15)
 SAL                                                    NUMBER(6,2)
 EADD                                                VARCHAR2(20)
 
=============================SIZE CHANGED========================

 AFTER :===>
 SQL> desc pythemp1
 Name                                      Null?    Type
 -----------------------------------------------------------------------------
 ENO                                                   NUMBER(3)
 NAME                                               VARCHAR2(10)
 SAL                                                    NUMBER(6,2)
 EADD                                                VARCHAR2(15)

'''
