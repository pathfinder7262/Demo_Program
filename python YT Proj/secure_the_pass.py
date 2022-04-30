#this program makes ur pass in unreadable format it replace char to given char.

rchar = (('s','$'),('a','&'),('C','@'),('o','0'),('i','1'),(' ','-'))

def changepass(pass1):
    for i,j in rchar:
        pass1 = pass1.replace(i,j)
    return pass1    

pass1 = input("Enter Ur Pass: ")
print(f"Ur Pass Is before chage:- {pass1}")
pass1 = changepass(pass1)
print("Ur Secure Pass: {}".format(pass1))

