#ATM Application
#widrawal fun  
#deposit Fun
##show Balnace

#Main program==>

import mysql.connector
while(True):
    try:
        print("====Select the option=====")
        print("1 for Withdraw ")
        print("2 for Deposit ")
        print("3 for View Balance ")
        print("="*50)     
        ch = int(input("Enter Option==>"))
        print("="*50)  
        if(ch== 1):
            print("1")
            #return Withdraw()
        elif(ch==2):
            print("2")
            #return Deposit()
        elif(ch==3):
            print("3")
            #return Balance();
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


    
