import re
#program for searching all Digit only in string
#5_re_digit_searching.py

cc = re.finditer("\d", "7A2u@5r T5&4*W@9 r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50)    
