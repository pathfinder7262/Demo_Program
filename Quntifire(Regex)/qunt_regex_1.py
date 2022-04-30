#qunt_regex_1.py
#search for exactli one 'a' 
import re
match = re.finditer('a','aadsjdkajkjwaueaaahfeuaaaahfdu')
for i in match:
    print("start={}\tend={}\tvalue={}".format(i.start(),i.end(),i.group()))
print("=="*50)
