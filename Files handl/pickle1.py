#44wapp which will write (accepting from keyboard) student detail and save stud detail by using picking concept

import pickle as pkl
with open("stud1","ab") as wp:
    nos=int(input("Enter the number of student u have:= "))
    print("="*50)
    for i in range(1,nos+1):
        print("enter {} stud detail:".format(i))
        print("="*50)
        sno =int(input("Enter the stud no:= "))
        sname = input("Enter the name=")
        mark = float(input("eter the marks:"))
        #create lst and apend dtat
        lst=[]
        lst.append(sno)
        lst.append(sname)
        lst.append(mark)
        #save lst data in file
        pkl.dump(lst,wp)
        print("="*50)
        print("Succesfully saved")
        print("="*50)

        

