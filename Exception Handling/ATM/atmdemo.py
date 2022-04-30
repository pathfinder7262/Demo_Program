#atmdemo
import sys
from bankexcep import DepositError
from bankexcep import ValueError
from bankexcep import WithdrawError
from bankexcep import ValueError
from bankingop import *
from atmmenu import menu
while(True):
    try:
        
        menu()
        ch = int(input("Enter ur choice:"))
        if (ch==1):
            try:
                deposit()
            except DepositError:
                print("dont try to deposit 0 or -ve")
              except ValueError:
                print("dont try to deposit star or 0 or -ve")    
        elif (ch ==2):
            try:
                withdraw()
            except WithdrawError:
                print("dont try to withdraw 0 or -ve")
            except InSuffFundError:
                print("in suff fund")
             except ValueError:
                print("dont try to withdraw star or 0 or -ve")    
        elif (ch ==3):pass
        elif (ch ==4):
            print("thanks...")
            sys.exit()
        else:
            print("Wrong choice")
    except(ValueError):
        print("wrong choice Entered")
