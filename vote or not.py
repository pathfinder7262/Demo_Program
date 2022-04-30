#27.Wapp which will accept age of the citizen and decide eligible whether is to vote or not


while(True):
    age = int(input("Enter the age:=>"))
    if(age>=18 and age<=100):
        print("Elegible")
        break  
    else:
        print("Wrong age")
