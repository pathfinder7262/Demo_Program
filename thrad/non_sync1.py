#non_sync1.py

import threading

def tbl(n):
    print("Mul Table For : {}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t{} X {}={}".format(n,i,n*i))
    else:
        print(" ")


#main

rt = threading.Thread(target=tbl,args=(5,))
rt1 = threading.Thread(target=tbl,args=(6,))
rt2= threading.Thread(target=tbl,args=(7,))
rt3 = threading.Thread(target=tbl,args=(25,))


rt.start()
rt1.start()
rt2.start()
rt3.start()

rt.join()
rt1.join()
rt2.join()
rt3.join()        
