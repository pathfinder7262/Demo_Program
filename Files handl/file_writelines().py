#file_writelines().py

with open("file8.data","a") as chetanp:
    print("File created succesfullyand opend in write mode..")
    print("="*50)
    chetanp.write("This is my 3 program using write() function\n")
    chetanp.write("This is my 3 program using write() function line 2\n")
    chetanp.write("This is my 3 program using write() function line 3\n")
    chetanp.write( str(33333333333334323)+"\n")
    print("file mode:{}".format(chetanp.mode))
    print("is readable?={}".format(chetanp.readable()))
    print("is writable?={}".format(chetanp.writable()))
    print("is file closed={}".format(chetanp.closed))
print("PVM out of open() block")
print("PVM out of open() block,is closed?={}".format(chetanp.closed))
