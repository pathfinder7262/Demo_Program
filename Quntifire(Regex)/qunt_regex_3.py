#qunt_regex_3.py
#search forzero 'a' or one 'a' or more 'a' at a time
import re
match = re.finditer('a*','aadsjd322kajkjwa65ueaaahf4euaaaahfdu')
for i in match:
    print("start={}\tend={}\tvalue={}".format(i.start(),i.end(),i.group()))
print("="*50)

'''
OUPUT

start=0	end=2	value=aa
start=2	end=2	value=
start=3	end=3	value=
start=4	end=4	value=
start=5	end=5	value=
start=6	end=6	value=
start=7	end=8	value=a
start=8	end=8	value=
start=9	end=9	value=
start=10	end=10	value=
start=11	end=11	value=
start=12	end=13	value=a
start=13	end=13	value=
start=14	end=14	value=
start=15	end=18	value=aaa
start=18	end=18	value=
start=19	end=19	value=
start=20	end=20	value=
start=21	end=21	value=
start=22	end=26	value=aaaa
start=26	end=26	value=
start=27	end=27	value=
start=28	end=28	value=
start=29	end=29	value=
start=30	end=30	value=


'''
