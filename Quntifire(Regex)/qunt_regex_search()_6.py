#quant_search()_6.py
import re
result = re.search("python","python is lang,python is oops lang")
if(result!=None):
    print("search is succesfull,element is found={}".format(result))
else:
    print("fail")
