#re_8_search_for_numbers(Digits)_(prog_defined)_.py
#for this u use => [0-9]
import re
match_char = re.finditer("[0-9]" ,"Ch7e1tAn3B_jfkD5jh gA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
