#45wapp which will accept emp details from keyboard and save those details in the file.
#emp no,emp name, emp salary, emp designation

import pickle 

try:
    with open("emppkl.txt","wb") as emp:
        enum = int(input("Enter the total number of emp which u want to add:= "))
        for i in range(1,enum+1):
            eno = int(input("Enter the Emp Number:="))
            enm=input("Enter the Emp Name:=")
            esal=float(input("Enter the the Emp salary:="))
            edes=input("Enter the Emp designation:=")

            lst =[]
            lst.append(eno)
            lst.append(enm)
            lst.append(esal)
            lst.append(edes)
    
            pickle.dump(lst,emp)
            print("Data insert succesfully")


except ValueError:
    print("Enter the Right Value")


    
    
