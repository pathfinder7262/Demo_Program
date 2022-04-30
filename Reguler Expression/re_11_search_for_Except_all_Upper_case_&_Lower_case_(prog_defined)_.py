#re_11_search_for_Except_all_Upper_case_&_Lower_case_(prog_defined)_.py
#for this u use => [^a-zaA-Z]
import re
match_char = re.finditer("[^a-zaA-Z]" ,"Ch7e1tAn3B_jfkD5jh gA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
