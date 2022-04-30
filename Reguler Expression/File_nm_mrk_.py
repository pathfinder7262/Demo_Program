#File_nm_mrk_.py
#find out the all stude name and marks from the given text/data
import re
nmlst=[]
mrlst=[]
try:
    with open("stud.info.txt","rt") as rp:
        filedata = rp.read()
        print("Name of student:")
        print("="*50)
        nms=re.findall("[A-Z][a-z]+",filedata)
        for i in nms:
            print(i)
            nmlst.append(i)
            
        mrk = re.findall("\d{2}",filedata)
        for m in mrk:
            print()
            mrlst.append(m)
        print(nmlst)    
        print(mrlst)    
        for n,rr in nmlst,mrlst:
            print(n,"==",rr)
            
            
        


        
except FileNotFoundError:
    print("File not exist")


    
