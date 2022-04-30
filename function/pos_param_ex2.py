#pos_param_ex2
#positional parameter/argument

def studdata(sname,sno,smarks,city = "jalgaon",comp=" TCS"):
    print("Name of student={}".format(sname))
    print("Roll no. of student={}".format(sno))
    print("Marks of student={}".format(smarks))
    print("City of student={}".format(city))
    print("Compeny of student={}".format(comp))
    print("*"*50)

studdata("chetan",10,87.89)
studdata("akshay",11,97.89)
studdata("pk",13,77.89)
studdata("sk",14,87.89)
studdata("nk",15,37.89,"pune")
studdata("tk",16,67.89,"pune","IBM")
