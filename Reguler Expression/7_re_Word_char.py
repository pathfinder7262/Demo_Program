import re
#program for search for any word character, digit except spacial character (similer to A-Za-z0-9)
#print only (alpha + digit)
#7_re_Word_char.py

cc = re.finditer("\w", "7A2u@5r T5&4*W@9 r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50) 
