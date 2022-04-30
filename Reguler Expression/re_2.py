#re_2_search_prog_defined_(search for either C,h,e,t,a or n).py
import re
match_char = re.finditer("[Chetan]" ,"Ch7e1tan3Bjfkd5jhgA")
for i in match_char:
    print("start={} \tend={} \tvalue={}".format(i.start(),(i.end()),(i.group())))
