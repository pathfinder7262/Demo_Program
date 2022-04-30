#qunt_regex_2.py
#search for one 'a' or more 'a' at a time
import re
match = re.finditer('a+','aadsjdkajkjwaueaaahfeuaaaahfdu')
for i in match:
    print("start={}\tend={}\tvalue={}".format(i.start(),i.end(),i.group()))
print("="*50)
