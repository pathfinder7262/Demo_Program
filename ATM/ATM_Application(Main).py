#ATM Application
#widrawal fun  
#deposit Fun
##show Balnace

#Main program==>
from connection import confile as cf 
#import mysql.connect
import sys
while(True):
    try:
        print("Welcome :)")
        print("*"*60)
        ac = input("Enter the Account No.: ")
        print("*"*60)
        pn=input("Enter the Account Pin")
        print("*"*60)
        cur=cf.dcon().cursor()
        qur="select  * from cust where cacno = ' "+ac+" ' and cpin = ' "+pn+" ' "
        cur.execute(qur)
        rows = cur.fetchone()
        if cur.rowcount<=0:
            print("Sorry, Wrong Detail... ")
        else:
            Name = rows[1]
            Bal = rows[3]
            print("Welcome Mr. ",Name)
            print("====Select the option=====")
            print("1 for Withdraw ")
            print("2 for Deposit ")
            print("3 for View Balance ")
            print("="*50)     
            ch = int(input("Enter Option==>"))
            print("="*50)  
            if(ch== 1):
                wamt= float(input("Enter Enter The Amount:- "))
                if wamt > Bal:
                    print("Widrawal amount is Bigger than available Balance ")
                else:
                    qur="update cust set cbal=cbal-%f where cacno=' " +ac+ " ' "
                    cur.execute(qur %wamt)
                    cf.dcon().commit()
                    print("Plz Collect Your Cash... : )")
                    
            elif(ch==2):
                damt = float(input("Enter the Amount You Want to deposited :-"))
                if (damt<0):
                    print("Enter the Right Amount")
                else:
                    qur="update cust set cbal= %f+cbal where cacno=' "+ac+" ' "
                    cur.execute(qur %damt)
                    cf.dcon().commit()
                    print("Your Amount deposited,Thanks For Banking.. : )")
            elif(ch==3):
                print("Your Balence is",Bal)
                
            else:
                print("Enter the Valid Choice")
                print("="*50)  
    except ValueError:
        print("Enter only Valid Input")
        print("="*50)  
    ch = input("Exit Y/N==>")
    print("="*50)  
    if(ch=="y"):
        print("Thanks For Using This Application")
        print("="*50)  
        break


    
