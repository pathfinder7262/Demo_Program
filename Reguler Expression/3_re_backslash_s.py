import re
#program for searching space char only
#3_re_backslash_s.py

cc = re.finditer("\s", "Au@r T&4*W@ r")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50)    
