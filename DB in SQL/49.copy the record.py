#49 wapp which will copy the record one table to another table



import mysql.connector

try:
    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="kvr")
    cur = con.cursor()
    cur.execute('create table emp select *from emp1')
    while(True):
        cur.execute('show tables')
        q1=cur.fetchall()
        for i in q1:
            print(i)
        
        tn = input("Enter the table name=>")
        q3 = 'select *from (%s)'
        cur.execute(q3 %(tn))
        q2=cur.fetchall()
        for j in q2:
            print("\t",j)
        ch = input("View gain Y/N")    
        if(ch=="n"):
             break
except mysql.connector.DatabaseError as de:
    print("Error",de)
except mysql.connector.Error1146:
    print("table not available")
