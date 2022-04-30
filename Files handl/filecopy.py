#41.wapp which will copy the contantent of one file into another file
#filecopy.py

sfile = input("Enter the source file:")
try:
    with open("file8","rt") as rp:
        dfile = input("Enter the dest. file")
        with open(dfile,"a") as wp:
            fdata = rp.read()
            wp.write(fdata)
            print("file copied")
except FileNotFoundError:
    print("File not Exist")
