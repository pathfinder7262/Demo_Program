#file_readLine()1.py

try:

    fp =open("file8","r")
    fdata=fp.readline()
    print(fdata)
    fp.seek(8)

    for line in fp:
        print(line,end="\t ")










except FileNotFoundError:
    print("file not exist")
    

