#program for string reverse_pp4

def revstr(str1):
    rstr=" "
    for i in range(len(str1)-1,-1,-1):  #[start:end:step]
        rstr = rstr + str1[i]
    return rstr


rstr = revstr("Chetan")
print(rstr)
