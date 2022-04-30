import re
#program for search for all except word char(A-Za-z0-9)
#capital W
#8_re_Except_Word_char.py

cc = re.finditer("\W", "7A2u@5r T5&4*W@9 r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50) 
