import re
#program for search for all (print all)
#dot (.)
#9_re_search_for_all.py

cc = re.finditer(".", "7A2u,@5.r T5&4*W@9 r.")
print("="*50)  
for match in cc:
    print("Start Index:{} \t value={}".format(match.start(),match.group()))
print("="*50) 
