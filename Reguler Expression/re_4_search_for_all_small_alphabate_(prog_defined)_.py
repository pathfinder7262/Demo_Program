#re_4_search_for_all_small_alphabate_(prog_defined)_.py
#for this u use => [a-z]
import re
match_char = re.finditer("[a-z]" ,"Ch7e1tan3Bjfkd5jhgA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
