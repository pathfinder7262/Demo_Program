#file_open_syn_2.py

with open("file7","w") as chetanp:
    print("File created succesfullyand opend in write mode..")
    print("="*50)
    print("file mode:{}".format(chetanp.mode))
    print("is readable?={}".format(chetanp.readable()))
    print("is writable?={}".format(chetanp.writable()))
    print("is file closed={}".format(chetanp.closed))
print("PVM out of open() block")
print("PVM out of open() block,is closed?={}".format(chetanp.closed))
