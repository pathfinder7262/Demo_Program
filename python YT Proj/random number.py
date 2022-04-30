#random number
import random as rm

while(True):
    print("*"*60)
    top_of_range = int(input("Type a  number: "))
    print("*"*60)
    while(True):
        if top_of_range <= 0:
            print("Enter the Right No.")
            print("*"*60)
            quit()
        else:
            r=rm.randrange(0,top_of_range)
            break
    gusno = int(input("Enter the Guessing No."))
    while(True):
        if(gusno>top_of_range):
            print("Enter the right no.")
            break
        else:
            print("*"*60)
            if(gusno==r):
                print("boom! u  r right")
                print("*"*60)
            else:
                print("Sorry!")
                print("*"*60)
            showno = input("Wanna see no. ? y/n: ")
            print("*"*60)
            if(showno == "y"):
                print("Random Number:{}".format(r))
                print("*"*60)
                break
    ag=input("Play again y/n:").lower()
    if(ag!="y"):
        print("Thanks to playing :) ")
        print("*"*60)
        break
    else:
        continue
    
