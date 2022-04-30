#DB_create_in_SQL_1
#database creation program in mysql
import mysql.connector


try:
    #obtained the connection  
    db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '')
    print("connected")
    cur = db.cursor()
    print("connected")
    #quiry for database creation
    dbc ="create database kvr" #sysntax=crete database db_nm
    cur.execute(dbc)
    print("/nDATABASE Created in my sql db--plz verify")

except mysql.connector.DatabaseError as db:
    print("problem...('-')")

