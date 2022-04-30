if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    list1 = []
    for i in arr:
        list1.append(i)
        if n >= 2 and n <= 10:
            for i in list1:
                if i >= -100 and i <= 100:
                    print("Valid")
                else:
                    print("Invalid Input")
        else:
            print("Invalid Input")
        











          
