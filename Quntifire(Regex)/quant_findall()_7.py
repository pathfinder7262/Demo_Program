#quant_findall()_7.py
import re
result = re.findall("python","python is lang,python is oops lang")

print("type of result=",type(result))   #==><class 'list'>
print("="*50)    
for i in result:
    print(i)
print("="*50)

if(result!=None):
    print("search is succesfull,element is found={}".format(result))
else:
    print("fail")
print("="*50)    
