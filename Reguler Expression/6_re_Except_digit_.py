import re
#program for search for all except Digit only in string
#6_re_Except_digit_.py

cc = re.finditer("\D", "7A2u@5r T5&4*W@9 r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50)    
