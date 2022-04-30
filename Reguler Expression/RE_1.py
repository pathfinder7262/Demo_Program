#RE_1_program to find word/char in program .py
#gd = given_data
#sd = search_data
import re
sd = "Python"   #it is case_sensitive
gd= "Python is a programming language Python follows oops as well as pop lang"
found_data=re.finditer(sd,gd)
#print(found_data):=it gives memory address
noc = 0 #no. of occurences
print("="*50)
for data in found_data:
    print("start index:{} \t End index:{} \t value:{}".format(data.start(),data.end(),data.group()))
    noc= noc+1
print("="*50)    
print(noc)
print("="*50) 
