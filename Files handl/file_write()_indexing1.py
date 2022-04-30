#file_readLine().py

try:

    fp =open("file8","r")
    fdata=fp.readline()
    print(fdata)
    fp.seek(8,"/n")

    for line in fp:
        print(line,end="\t ")










except FileNotFoundError:
    print("file not exist")
    

