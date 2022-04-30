#ATM Application
#widrawal fun  
#deposit Fun
##show Balnace

#Withdraw==>
import mysql.connector


try:
    con = mysql.connector.connect(host='localhost',user='root',passwd='',database='kvr')
    cur=con.cursor()
    sq="select *from cust"
    cur.execute(sq)
    records=cur.fetchall()
    pin=int(input("Enter the pin==>"))
    if(records[0] == pin):
        print("valid")
except mysql.connector.DatabaseError as ab:
    print("Problem in My Sql Data Base",ab)



'''
        
        while(count==3):
            cp=int(input("Enter The Pin")) 
            print("Enter The Amount You Want To Withdraw==>")
        

        if(amount<cbal):
            print("Take ur Money And Enjoy")
            qur = update cust set cbal=cbal
        else:
            print("Unsufficient balance")
        
'''
    
