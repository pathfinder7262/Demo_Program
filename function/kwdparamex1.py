#kwdparamex1.py

def empinfo(eno,ename,sal,dsg,cname = "IBM",ecity="nasik"):
    print("\t\t{}\t{}\t{}\t{}\t{}\t{}".format(eno,ename,sal,dsg,cname,ecity))


#main program
print("*"*50)
print("EMP INFO:===>")
print("*"*50)
empinfo(100,"pk",10000,"S.E","TSC")    
empinfo(100,"pk",dsg="T.L",sal = 12000,ecity="pune")
empinfo(100,"ok",dsg="T.L",sal = 15000,ecity="pune")  
