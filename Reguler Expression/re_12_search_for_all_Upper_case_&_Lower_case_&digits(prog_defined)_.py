#re_12_search_for_all_Upper_case_&_Lower_case_&digits(prog_defined)_.py
#for this u use => [a-zaA-Z0-9]
import re
match_char = re.finditer("[a-zaA-Z0-9]" ,"Ch7e1tAn3B_jfkD5jh gA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
