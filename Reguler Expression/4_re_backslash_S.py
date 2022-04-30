import re
#program for searching all character except  space char only
#CAPITAL *S* USE
#4_re_backslash_S.py

cc = re.finditer("\S", "Au@r T&4*W@ r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50)    

