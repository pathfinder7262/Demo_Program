#re_6_search_for_all_upper_case_alphabate_(prog_defined)_.py
#for this u use => [A-Z]
import re
match_char = re.finditer("[A-Z]" ,"Ch7e1tAn3B_jfkD5jh gA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
