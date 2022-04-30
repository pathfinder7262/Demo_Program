#sync1.py

import threading
l=threading.Lock()
def tbl(n):
    l.acquire()   #lock the obj
    print("Mul Table For : {}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t{} X {}={}".format(n,i,n*i))
    else:
        print(" ")
    l.release()

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
