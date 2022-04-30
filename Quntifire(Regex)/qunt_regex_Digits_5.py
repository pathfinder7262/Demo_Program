#qunt_regex_Digits_4.py
#search for one digit or more digit at a time
import re
match = re.finditer('\d+','aadsjd322kajkjwa65ueaaahf4euaaaahfdu')
for i in match:
    print("start={}\tend={}\tvalue={}".format(i.start(),i.end(),i.group()))
print("="*50)
