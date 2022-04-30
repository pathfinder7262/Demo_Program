#fileopn4.py
import sys
try:
    chetanp= open("file5","x")
except FileExistsError:
    print("All ready available")
    print("="*50)
sys.exit()
else:
    print("file opened succesfully ")
    print("="*50)
    print("Type of ketanp={}".format(chetanp))   #TextIOWrapper--node
    print("Mode of  ketanp={}".format(chetanp.mode)) 
    print("is the file readable?={}".format(chetanp.readable()))    #==>true
    print("is the file readable?={}".format(chetanp.writable()))    #==>false
    print("is the file closed?={}".format(chetanp.closed))
    print("="*50)
finally:
    try:
        if(chetanp!=None):
            chetanp.close()
            print("is the file closed?={}".format(chetanp.closed))
    except NameError:
        print("invalid file pointer")
     
