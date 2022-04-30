print("Welcome sir...")
bill = 0
lst = []
while(True):
    ch = int(input("Enter the Choice.."))

    if ch == 1:
        print("You Selected:Sandwich 95rs")  
        srt = 95
        bill = bill +srt
        lst.append("Sandwich = 95rs")
    elif ch == 2:
        print("You Selected:Pizza for 85rs")  
        prt = 85
        bill = bill +prt
        lst.append("Pizza = 85rs")
    elif ch == 3:
        print("You Selected:French Fries for 150rs")  
        ffrt = 150
        bill = bill +ffrt
        lst.append("French Fries = 150rs")
    elif ch == 4:
        print("You Selected:diet Coke for 50rs")  
        dcrt = 50
        bill = bill +dcrt
        lst.append("diet Coke = 50rs")
    elif ch == 5:
        print("You Selected:Coffee for 55rs")  
        crt = 55
        bill = bill +crt
        lst.append("Coffee = 55rs")
    elif ch == 6:
        print("Total Amout to pay:{}".format(bill))
        lst.append("Total Bill:{}".format(bill))
        print(lst)
        break
    else:
        print("Invalid Choice ")
    
