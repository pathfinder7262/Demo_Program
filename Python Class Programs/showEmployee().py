# showEmployee().py
#Create a function showEmployee() in such a way that it should accept employee name,
#and its salary and display both. If the salary is missing in the function call
#assign default value 9000 to salary
"""
def showEmp(nm,slr=9000):
    print("Emp name:={}".format(nm))
    print("Emp Salary:={}".format(slr))

name = input("Enter the Emp name:= ")
sal = float(input("Enter the Emp sal:= "))


showEmp(name,sal) """
    
def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

showEmployee("Ben", 9000)

name = input("Enter the Emp name:= ")
sal = float(input("Enter the Emp sal:= "))

showEmployee(name,sal)
