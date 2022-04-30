#Conne_demo1.py
import cx_Oracle

con = cx_Oracle.connect("system/orcl@localhost/PROD")
cur = con.cursor()
print("connected")
qur = "create table  tbl(eno number(2),name varchar2(10),sal number(6,2))"
cur.execute(qur)
print("pz varify")
    
